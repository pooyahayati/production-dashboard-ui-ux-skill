# Production Dashboard UI/UX Skill

[![Validate](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml/badge.svg)](https://github.com/pooyahayati/production-dashboard-ui-ux-skill/actions/workflows/validate-skill.yml)
![Version](https://img.shields.io/badge/version-1.2.0-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A production-oriented Agent Skill for designing, auditing, improving, and redesigning dashboards, admin panels, CRM, analytics, and operational product interfaces.

Supports OpenAI Codex, Claude Code, Claude.ai / Claude Desktop, Persian RTL, English LTR, bilingual products, responsive UI, Light/Dark themes, branding, accessibility, performance, and existing-product regression-aware improvement.

## Quick start

### OpenAI Codex

Install from the canonical skill path:

```text
Use $skill-installer to install this skill from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill
```

Then use it explicitly:

```text
Use $production-dashboard-ui-ux-skill to audit and improve this dashboard.
```

Or:

```text
Use $production-dashboard-ui-ux-skill to redesign this dashboard.
```

Codex can also select the skill automatically when the request clearly matches its description.

### Claude.ai / Claude Desktop

1. Open the latest GitHub Release.
2. Download `production-dashboard-ui-ux-skill-claude-v1.2.0.zip`.
3. In Claude, enable **Code execution and file creation** if required.
4. Open **Customize → Skills**.
5. Choose **Upload a skill** and upload the ZIP.
6. Enable it.

Example:

```text
Use the Production Dashboard UI/UX Skill to audit and improve this dashboard.
```

### Claude Code

Download the same Claude-ready ZIP from the latest Release and extract the contained `production-dashboard-ui-ux-skill` folder into:

```text
~/.claude/skills/
```

Project-local installation can use:

```text
<project>/.claude/skills/
```

Then invoke:

```text
/production-dashboard-ui-ux-skill
```

## Existing projects

The skill is explicitly designed for completed or live products.

It can:

- establish an Observed Baseline
- audit current UI/UX
- report audit coverage instead of claiming unverified full coverage
- classify findings by severity, impact, scope, confidence, and fix type
- implement safe UI/UX improvements
- preserve business logic, permissions, validation, routing, API/data meaning, and user changes
- improve palette, typography, logo treatment, themes, responsive behavior, RTL/LTR, tables, forms, navigation, accessibility, and performance
- perform before/after and regression-aware QA
- separate local treatment fixes from strategic redesign or identity changes

Example:

```text
Use $production-dashboard-ui-ux-skill to audit and improve this existing product.

Inspect the rendered UI and source code. Review UX, visual hierarchy,
responsive behavior, RTL/LTR, localization, accessibility, performance,
palette, typography, logo treatment, themes, tables, forms, navigation,
and design-system consistency.

Fix safe issues, preserve working product behavior and my existing changes,
and report audit coverage plus any remaining strategic decisions.
```

## Brand and visual refresh

The skill distinguishes:

- **Treatment fix** — logo placement, sizing, spacing, contrast, variants
- **Brand refresh** — palette, typography, iconography, surfaces, personality
- **Identity redesign** — actual logo/mark replacement

It may improve weak existing visual design. It does not preserve poor design merely because it already exists.

Actual identity replacement requires explicit user intent.

## Installation details

### Codex via skill-installer

The official Codex skill installer requires a path inside a GitHub repository. Use:

```text
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill
```

The installer currently installs into `$CODEX_HOME/skills` (default `~/.codex/skills`).

### Codex manual discovery locations

Current Codex documentation also supports user-level skills at:

```text
~/.agents/skills/
```

and repository skills at:

```text
<repo>/.agents/skills/
```

If installing manually, copy the canonical folder:

```text
skills/production-dashboard-ui-ux-skill/
```

into one of those locations.

## Updating

### Codex installed with $skill-installer

The installer intentionally does not overwrite an existing destination.

Ask Codex:

```text
Update $production-dashboard-ui-ux-skill to the latest version from:
https://github.com/pooyahayati/production-dashboard-ui-ux-skill/tree/main/skills/production-dashboard-ui-ux-skill

Remove the currently installed copy if necessary, then reinstall it with $skill-installer.
```

If doing it manually on macOS/Linux and using the installer's default destination:

```bash
rm -rf "${CODEX_HOME:-$HOME/.codex}/skills/production-dashboard-ui-ux-skill"
```

Then reinstall from the canonical GitHub path above.

If you maintain a manual Git checkout elsewhere, update that checkout with `git pull --ff-only` and copy or symlink the canonical skill folder into the supported Codex/Claude skills directory.

Restart Codex or start a new session if the updated skill is not immediately detected.

### Claude.ai / Claude Desktop

Download the newest Claude-ready ZIP from Releases and replace the older uploaded custom skill.

### Claude Code

Replace the installed skill folder with the folder from the newest Claude-ready ZIP.

## Usage examples

### New dashboard

```text
Use $production-dashboard-ui-ux-skill to design this new dashboard.
Recommend a design direction, establish a Design Profile, then implement it.
```

### Existing product — audit only

```text
Use $production-dashboard-ui-ux-skill to audit this existing product.
Do not modify code. Report coverage, prioritized findings, evidence, and recommendations.
```

### Existing product — delegated improvement

```text
Use $production-dashboard-ui-ux-skill to audit and improve this existing product.
Make reasonable design decisions without stopping for every approval.
Preserve business logic and report important decisions at the end.
```

### Persian RTL

```text
Use $production-dashboard-ui-ux-skill to improve this Persian RTL dashboard.
Audit mixed-direction technical values, tables, forms, navigation, typography,
localization, mobile behavior, and accessibility.
```

## Project structure

```text
production-dashboard-ui-ux-skill/
├── plugin.json
├── assets/
│   ├── logo.svg
│   └── composer-icon.svg
├── skills/
│   └── production-dashboard-ui-ux-skill/
│       ├── SKILL.md
│       ├── agents/
│       │   └── openai.yaml
│       └── references/
├── scripts/
│   ├── validate_release.py
│   └── package_release.py
├── evals/
├── submission/
├── .github/workflows/
├── README.md
├── CHANGELOG.md
├── VERSION
└── LICENSE
```

The canonical Skill source exists only under `skills/production-dashboard-ui-ux-skill/`. Release packages are generated from that source.

## Validation

Local release checks:

```bash
python3 scripts/validate_release.py
python3 scripts/package_release.py --output dist
```

CI additionally runs OpenAI's current `quick_validate.py` and a Codex installer smoke test on pushes to `main`.

Behavioral eval cases live in `evals/`. They are intentionally separate from structural validation because model behavior cannot be proven by regex or file checks.

## Releases

Latest release: **v1.2.0**

Release assets include:

- Claude-ready Skill ZIP
- OpenAI portable Plugin ZIP
- SHA-256 checksums

## Community and security

- [CONTRIBUTING.md](CONTRIBUTING.md)
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)
- [SECURITY.md](SECURITY.md)
- [PRIVACY.md](PRIVACY.md)
- [TERMS.md](TERMS.md)
- [SUPPORT.md](SUPPORT.md)

## Author

**Pooya Hayati | پویا حیاتی**

[Pooyahayati.com](https://pooyahayati.com)

## License

MIT
