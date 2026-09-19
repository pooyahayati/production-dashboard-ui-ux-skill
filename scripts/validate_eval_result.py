#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
cases_manifest = json.loads((ROOT / "evals" / "cases.json").read_text(encoding="utf-8"))
expected = {case["id"]: case for case in cases_manifest["cases"]}
VALID = {"pass", "partial", "fail", "not-testable"}

def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a recorded behavioral-eval result.")
    parser.add_argument("result")
    parser.add_argument("--require-all", action="store_true")
    args = parser.parse_args()

    result = json.loads(Path(args.result).read_text(encoding="utf-8"))
    errors: list[str] = []

    if result.get("skillVersion") != cases_manifest.get("version"):
        errors.append("skillVersion does not match eval manifest")
    for field in ["host", "model", "date", "cases"]:
        if not result.get(field):
            errors.append(f"Missing result field: {field}")

    seen: set[str] = set()
    for item in result.get("cases", []):
        case_id = item.get("id")
        if case_id not in expected:
            errors.append(f"Unknown case id: {case_id}")
            continue
        if case_id in seen:
            errors.append(f"Duplicate result case: {case_id}")
        seen.add(case_id)
        if item.get("triggerMode") not in {"explicit", "implicit"}:
            errors.append(f"{case_id}: invalid triggerMode")
        if item.get("result") not in VALID:
            errors.append(f"{case_id}: invalid result")

        expected_invariants = expected[case_id]["invariants"]
        recorded = item.get("invariants", [])
        recorded_text = {x.get("text") for x in recorded}
        for inv in expected_invariants:
            if inv not in recorded_text:
                errors.append(f"{case_id}: missing invariant result: {inv}")
        for inv in recorded:
            if inv.get("result") not in VALID:
                errors.append(f"{case_id}: invalid invariant result")

    if args.require_all:
        missing = sorted(set(expected) - seen)
        if missing:
            errors.append(f"Missing case results: {', '.join(missing)}")

    if errors:
        print("Behavioral eval result validation failed:")
        for item in errors:
            print(f"- {item}")
        sys.exit(1)

    failures = [x["id"] for x in result["cases"] if x.get("result") == "fail"]
    partials = [x["id"] for x in result["cases"] if x.get("result") == "partial"]
    print(f"Behavioral eval result is structurally valid. Fail={len(failures)} Partial={len(partials)}")
    if failures:
        print("Failed cases:", ", ".join(failures))

if __name__ == "__main__":
    main()
