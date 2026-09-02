#!/usr/bin/env python3
from pathlib import Path
import json
from jsonschema import Draft202012Validator
import sys

def main(root: str) -> int:
    root = Path(root)
    schemas = sorted(root.glob("**/*.schema.json"))
    failures = []
    for p in schemas:
        try:
            schema = json.loads(p.read_text(encoding="utf-8"))
            Draft202012Validator.check_schema(schema)
            print(f"PASS {p.relative_to(root)}")
        except Exception as e:
            failures.append((p, e))
            print(f"FAIL {p.relative_to(root)}: {e}")
    print(f"schemas={len(schemas)} failures={len(failures)}")
    return 1 if failures else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv) > 1 else "."))
