from __future__ import annotations
from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Iterable
import json

@dataclass(frozen=True)
class ProductAssetRef:
    asset_id: str
    asset_revision: int

class ProductIntelligenceStore(Protocol):
    def get_asset(self, ref: ProductAssetRef) -> dict: ...
    def list_assets(self) -> Iterable[dict]: ...
    def write_draft(self, proposal: dict) -> Path: ...

class GitStoreAdapter:
    """Recovery scaffold for a Git-backed Product Intelligence repo.

    Git operations/PR approval are intentionally outside this class. This adapter
    manages deterministic files; publication authority remains in Layer 2 policy.
    """
    def __init__(self, root: str | Path):
        self.root = Path(root)

    def _asset_file(self, ref: ProductAssetRef) -> Path:
        return self.root / "assets" / "by-id" / ref.asset_id / "revisions" / f"r{ref.asset_revision:04d}.json"

    def get_asset(self, ref: ProductAssetRef) -> dict:
        return json.loads(self._asset_file(ref).read_text(encoding="utf-8"))

    def list_assets(self):
        base = self.root / "assets" / "by-id"
        if not base.exists():
            return []
        out = []
        for path in sorted(base.glob("*/revisions/r*.json")):
            out.append(json.loads(path.read_text(encoding="utf-8")))
        return out

    def write_draft(self, proposal: dict) -> Path:
        pid = proposal["proposal_id"]
        p = self.root / "proposals" / f"{pid}.json"
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(json.dumps(proposal, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        return p
