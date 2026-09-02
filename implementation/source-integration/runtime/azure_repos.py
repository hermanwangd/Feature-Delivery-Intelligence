from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
import subprocess, shutil

@dataclass(frozen=True)
class RepositorySpec:
    id: str
    remote: str
    branch_or_ref: str = "main"

class AzureReposSourceProvider:
    """Git-level Azure Repos acquisition.

    Credentials are supplied by the environment/credential helper and are never
    persisted by this class.
    """
    def __init__(self, workspace: str | Path):
        self.workspace = Path(workspace)
        self.clones = self.workspace / "clones"
        self.worktrees = self.workspace / "worktrees"
        self.clones.mkdir(parents=True, exist_ok=True)
        self.worktrees.mkdir(parents=True, exist_ok=True)

    def sync(self, spec: RepositorySpec) -> Path:
        clone = self.clones / spec.id
        if not clone.exists():
            subprocess.check_call(["git", "clone", "--no-checkout", spec.remote, str(clone)])
        else:
            subprocess.check_call(["git", "-C", str(clone), "fetch", "--all", "--prune"])
        return clone

    def resolve(self, clone: str | Path, ref: str) -> str:
        return subprocess.check_output(["git", "-C", str(clone), "rev-parse", f"{ref}^{{commit}}"], text=True).strip()

    def materialize(self, spec: RepositorySpec, revision: str) -> Path:
        clone = self.sync(spec)
        wt = self.worktrees / spec.id
        if wt.exists():
            subprocess.check_call(["git", "-C", str(clone), "worktree", "remove", "--force", str(wt)])
        subprocess.check_call(["git", "-C", str(clone), "worktree", "add", "--detach", str(wt), revision])
        return wt
