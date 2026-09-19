#!/usr/bin/env python3
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from xml.etree import ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "production-dashboard-ui-ux-skill"
SKILL = ROOT / "skills" / SKILL_NAME
VERSION = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
ERRORS: list[str] = []

def error(msg: str) -> None:
    ERRORS.append(msg)

def require(path: str) -> Path:
    p = ROOT / path
    if not p.exists():
        error(f"Missing required path: {path}")
    return p

for path in [
    "README.md", "CHANGELOG.md", "LICENSE", "VERSION", "plugin.json",
    "assets/logo.svg", "assets/composer-icon.svg",
    f"skills/{SKILL_NAME}/SKILL.md",
    f"skills/{SKILL_NAME}/agents/openai.yaml",
    f"skills/{SKILL_NAME}/references/discovery-and-profile.md",
    f"skills/{SKILL_NAME}/references/existing-product-audit.md",
    f"skills/{SKILL_NAME}/references/execution-safety.md",
    f"skills/{SKILL_NAME}/references/accessibility.md",
    f"skills/{SKILL_NAME}/references/performance.md",
    f"skills/{SKILL_NAME}/references/qa-checklist.md",
    "submission/TEST_CASES.md",
    "submission/SUBMISSION_CHECKLIST.md",
    "evals/cases.json",
]:
    require(path)

for old in ["SKILL.md", "agents", "references"]:
    if (ROOT / old).exists():
        error(f"Duplicate root Skill source still exists: {old}")

skill_text = (SKILL / "SKILL.md").read_text(encoding="utf-8")
if not skill_text.startswith("---\n"):
    error("SKILL.md must start with YAML frontmatter")
else:
    parts = skill_text.split("---", 2)
    if len(parts) != 3:
        error("SKILL.md frontmatter is not closed")
    else:
        fm = parts[1].strip().splitlines()
        keys = [line.split(":", 1)[0].strip() for line in fm if ":" in line]
        if keys != ["name", "description"]:
            error(f"SKILL.md frontmatter must contain only name and description; got {keys}")
        name = next((line.split(":", 1)[1].strip() for line in fm if line.startswith("name:")), "")
        description = next((line.split(":", 1)[1].strip() for line in fm if line.startswith("description:")), "")
        if name != SKILL_NAME:
            error(f"Unexpected Skill name: {name}")
        if not description or len(description) > 1024:
            error("Skill description must be 1..1024 characters")
        if "Use " not in description or "Do not use" not in description:
            error("Skill description must say when to use and when not to use it")

body_lines = skill_text.split("---", 2)[-1].splitlines()
if len(body_lines) >= 500:
    error(f"SKILL.md body should stay under 500 lines; got {len(body_lines)}")

for ref in re.findall(r"references/[a-z0-9-]+\.md", skill_text):
    if not (SKILL / ref).exists():
        error(f"Referenced file missing: {ref}")

manifest = json.loads((ROOT / "plugin.json").read_text(encoding="utf-8"))
if manifest.get("version") != VERSION:
    error("plugin.json version does not match VERSION")

plugin_name = manifest.get("name", "")
if len(f"{plugin_name}:{SKILL_NAME}") > 64:
    error("plugin-name:skill-name identity exceeds 64 characters")

interface = manifest.get("extensions", {}).get("com.openai", {}).get("interface", {})
display_name = interface.get("displayName", "")
short = interface.get("shortDescription", "")
long_desc = interface.get("longDescription", "")
developer = interface.get("developerName", "")

if not display_name or len(display_name) > 30:
    error("Plugin displayName must be 1..30 characters")
if not short or len(short) > 30 or "\n" in short:
    error("Plugin shortDescription must be one line and <=30 characters")
if not long_desc or len(long_desc) > 4000:
    error("Plugin longDescription must be 1..4000 characters")
if not developer or len(developer) > 80 or "\n" in developer:
    error("Plugin developerName must be one line and <=80 characters")

author_name = manifest.get("author", {}).get("name", "")
if author_name and developer and author_name != developer:
    error("plugin author.name and interface.developerName should match")

allowed_categories = {
    "Productivity", "Creativity", "Developer Tools", "Business & Operations",
    "Data & Analytics", "Communication", "Education & Research", "Security",
    "Finance", "Healthcare", "Travel", "Entertainment", "Other",
}
if interface.get("category") not in allowed_categories:
    error("Plugin category is missing or unsupported")

caps = interface.get("capabilities", [])
if len(caps) > 20 or any(not isinstance(x, str) or not x.strip() or len(x) > 120 or "\n" in x for x in caps):
    error("Plugin capabilities violate directory limits")

prompts = interface.get("defaultPrompt", [])
if not isinstance(prompts, list) or len(prompts) > 3:
    error("Plugin defaultPrompt must be a list of at most 3 prompts")
else:
    normalized = set()
    for prompt in prompts:
        if not isinstance(prompt, str) or not prompt.strip() or len(prompt) > 128 or "\n" in prompt or "@" in prompt:
            error(f"Invalid starter prompt: {prompt!r}")
        key = " ".join(prompt.split()).casefold()
        if key in normalized:
            error("Duplicate starter prompt")
        normalized.add(key)

for field in ["websiteURL", "supportURL", "privacyPolicyURL", "termsOfServiceURL"]:
    value = interface.get(field, "")
    if value and not value.startswith("https://"):
        error(f"{field} must use HTTPS")

def validate_svg(field: str) -> None:
    rel = interface.get(field)
    if not rel or not rel.startswith("./"):
        error(f"{field} must be a ./ relative asset path")
        return
    path = ROOT / rel[2:]
    if not path.is_file():
        error(f"{field} asset missing: {rel}")
        return
    try:
        root = ET.fromstring(path.read_text(encoding="utf-8"))
    except Exception as exc:
        error(f"{field} SVG cannot be parsed: {exc}")
        return
    if not root.tag.endswith("svg"):
        error(f"{field} root must be svg")
    viewbox = root.attrib.get("viewBox")
    width = root.attrib.get("width")
    height = root.attrib.get("height")
    if viewbox:
        vals = [float(x) for x in viewbox.split()]
        if len(vals) != 4 or vals[2] != vals[3] or vals[2] < 48:
            error(f"{field} viewBox must be square and >=48")
    elif width and height:
        try:
            w, h = float(width), float(height)
            if w != h or w < 48:
                error(f"{field} dimensions must be square and >=48")
        except ValueError:
            error(f"{field} dimensions must be numeric")
    else:
        error(f"{field} SVG needs numeric viewBox or dimensions")

validate_svg("logo")
validate_svg("composerIcon")

readme = (ROOT / "README.md").read_text(encoding="utf-8")
canonical_url = "https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill"
if canonical_url not in readme:
    error("README is missing the canonical Codex installer URL")

tests = (ROOT / "submission/TEST_CASES.md").read_text(encoding="utf-8")
positive_section, _, negative_section = tests.partition("## Negative test cases")
positive_count = len(re.findall(r"^### \d+\.", positive_section, re.M))
negative_count = len(re.findall(r"^### \d+\.", negative_section, re.M))
if positive_count != 5 or negative_count != 3:
    error(f"Submission tests must be exactly 5 positive and 3 negative; got {positive_count}+{negative_count}")
if tests.count("**Expected result format**") != 8:
    error("Every submission test needs Expected result format")
if tests.count("**Fixtures / test data**") != 8:
    error("Every submission test needs Fixtures / test data")

profile = (SKILL / "references/discovery-and-profile.md").read_text(encoding="utf-8")
for term in ["profile_version", "skill_version", "status:", "source:", "locked_constraints"]:
    if term not in profile:
        error(f"Design Profile provenance field missing: {term}")

evals = json.loads((ROOT / "evals/cases.json").read_text(encoding="utf-8"))
if evals.get("version") != VERSION or not evals.get("cases"):
    error("Behavioral eval manifest version or cases are invalid")

if ERRORS:
    print("Release validation failed:")
    for item in ERRORS:
        print(f"- {item}")
    sys.exit(1)

print(f"Release validation passed for v{VERSION}.")
