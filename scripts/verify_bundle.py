#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, sys

IGNORED_PREFIXES=(".fdi-work/", ".git/", ".pytest_cache/", "__pycache__/", "runtime-logs/")
IGNORED_NAMES={".DS_Store"}

def sha256(path: Path) -> str:
    h=hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024*1024), b""):
            h.update(chunk)
    return h.hexdigest()

def ignored(rel: str) -> bool:
    return any(rel.startswith(p) for p in IGNORED_PREFIXES) or Path(rel).name in IGNORED_NAMES or "__pycache__" in Path(rel).parts

def main(root: str) -> int:
    root=Path(root)
    manifest_path=root/"BUNDLE-MANIFEST.json"
    if not manifest_path.exists():
        print("FAIL missing BUNDLE-MANIFEST.json")
        return 1
    manifest=json.loads(manifest_path.read_text(encoding="utf-8"))
    failures=[]
    for item in manifest["files"]:
        p=root/item["path"]
        if not p.exists():
            failures.append(f"missing {item['path']}")
            continue
        actual=sha256(p)
        if actual != item["sha256"]:
            failures.append(f"digest {item['path']}: {actual} != {item['sha256']}")
    expected={x["path"] for x in manifest["files"]} | {"BUNDLE-MANIFEST.json"}
    extra=[]
    for p in root.rglob("*"):
        if p.is_file():
            rel=str(p.relative_to(root))
            if rel not in expected and not ignored(rel):
                extra.append(rel)
    for f in failures: print("FAIL", f)
    for e in extra: print("FAIL unexpected active file", e)
    print(f"verified={len(manifest['files'])} failures={len(failures)} extras={len(extra)}")
    return 1 if failures or extra else 0

if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1] if len(sys.argv)>1 else "."))
