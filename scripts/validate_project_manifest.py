#!/usr/bin/env python3
"""Validate the Project AVI machine-readable status manifest using only Python's standard library."""
import argparse
import json
import sys
from pathlib import Path

REQUIRED = {
    "schema_version", "project", "full_name", "repository", "status", "maturity",
    "design_pillars", "implemented_capabilities", "planned_capabilities",
    "runtime_required", "license_status", "limitations",
}
ALLOWED_STATUS = {"announcement", "prototype", "beta", "released", "archived"}

def validate(data):
    errors = []
    if not isinstance(data, dict):
        return ["manifest must be a JSON object"]
    missing = sorted(REQUIRED - data.keys())
    extra = sorted(data.keys() - REQUIRED)
    if missing:
        errors.append("missing fields: " + ", ".join(missing))
    if extra:
        errors.append("unexpected fields: " + ", ".join(extra))
    if data.get("schema_version") != "1.0.0":
        errors.append("schema_version must be 1.0.0")
    if data.get("project") != "Project AVI":
        errors.append("project must be Project AVI")
    if data.get("status") not in ALLOWED_STATUS:
        errors.append("status is not a supported lifecycle value")
    for field in ("design_pillars", "implemented_capabilities", "planned_capabilities", "limitations"):
        if field in data and (not isinstance(data[field], list) or any(not isinstance(item, str) for item in data[field])):
            errors.append(f"{field} must be an array of strings")
    if not isinstance(data.get("runtime_required"), bool):
        errors.append("runtime_required must be a boolean")
    if not isinstance(data.get("license_status"), str):
        errors.append("license_status must be a string")
    if data.get("status") == "announcement" and data.get("implemented_capabilities") != []:
        errors.append("announcement status requires an empty implemented_capabilities list")
    return errors

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("manifest", nargs="?", default="project.json")
    args = parser.parse_args()
    try:
        data = json.loads(Path(args.manifest).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        print(f"Manifest could not be read: {type(error).__name__}", file=sys.stderr)
        return 2
    errors = validate(data)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print("Project AVI manifest is structurally valid.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
