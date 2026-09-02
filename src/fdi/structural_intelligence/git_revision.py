from __future__ import annotations
from pathlib import Path
import re, subprocess

FULL_SHA = re.compile(r"^(?:[0-9a-fA-F]{40}|[0-9a-fA-F]{64})$")

def require_full_git_revision(value: str) -> str:
    if not FULL_SHA.fullmatch(value):
        raise ValueError("canonical revision must be a full 40- or 64-hex Git object id")
    return value.lower()

def resolve_git_revision(repo: str | Path, value: str) -> str:
    repo = Path(repo)
    resolved = subprocess.check_output(["git", "-C", str(repo), "rev-parse", f"{value}^{{commit}}"], text=True).strip()
    return require_full_git_revision(resolved)

def require_equal_revision(repo: str | Path, provider_value: str, canonical_value: str) -> str:
    canonical = require_full_git_revision(canonical_value)
    resolved = resolve_git_revision(repo, provider_value)
    if resolved != canonical:
        raise ValueError(f"provider revision {resolved} != canonical revision {canonical}")
    return resolved
