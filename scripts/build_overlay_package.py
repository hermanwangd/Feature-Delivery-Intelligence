#!/usr/bin/env python3
"""Build a deterministic, manifest-backed FDI v0.4.7.2 live Grafel binding overlay ZIP."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import zipfile


FIXED_ZIP_TIME = (2026, 9, 2, 0, 0, 0)
EXCLUDED_DIRS = {".git", ".pytest_cache", ".venv", "__pycache__"}
EXCLUDED_SUFFIXES = {".pyc", ".pyo", ".zip"}


def include_file(path: Path, source: Path, output: Path) -> bool:
    rel = path.relative_to(source)
    if any(part in EXCLUDED_DIRS for part in rel.parts):
        return False
    if path.suffix in EXCLUDED_SUFFIXES:
        return False
    try:
        if path.resolve() == output.resolve():
            return False
    except FileNotFoundError:
        pass
    return path.is_file()


def collect(source: Path, output: Path) -> list[tuple[str, bytes]]:
    files = []
    for path in sorted(source.rglob("*"), key=lambda p: p.as_posix()):
        if include_file(path, source, output):
            rel = path.relative_to(source).as_posix()
            if rel == "MANIFEST.json":
                continue
            files.append((rel, path.read_bytes()))
    return files


def build(source: Path, output: Path) -> dict:
    source = source.resolve()
    output = output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    files = collect(source, output)
    manifest = {
        "format": "FDI_IMPLEMENTATION_OVERLAY_MANIFEST_V1",
        "release": "fdi-mvp-v0.4.7.2-live-grafel-binding-overlay",
        "entries": [
            {"path": rel, "size": len(data), "sha256": hashlib.sha256(data).hexdigest()}
            for rel, data in files
        ],
    }
    manifest_bytes = (json.dumps(manifest, sort_keys=True, indent=2) + "\n").encode("utf-8")

    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=9) as zf:
        for rel, data in [*files, ("MANIFEST.json", manifest_bytes)]:
            info = zipfile.ZipInfo(rel, FIXED_ZIP_TIME)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            info.create_system = 3
            zf.writestr(info, data, compress_type=zipfile.ZIP_DEFLATED, compresslevel=9)

    return {
        "output": str(output),
        "entries": len(files) + 1,
        "sha256": hashlib.sha256(output.read_bytes()).hexdigest(),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", required=True)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    result = build(Path(args.source), Path(args.output))
    print(json.dumps(result, sort_keys=True))


if __name__ == "__main__":
    main()
