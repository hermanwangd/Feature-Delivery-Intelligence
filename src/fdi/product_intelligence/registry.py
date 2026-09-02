from __future__ import annotations
from pathlib import Path
import json
from jsonschema import Draft202012Validator


def _bundle_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "VERSION").exists() and (parent / "governance").exists():
            return parent
    raise RuntimeError("FDI bundle root not found")

def _schema(root: Path) -> dict:
    bundle = _bundle_root()
    return json.loads((bundle / "contracts" / "layer2" / "ProductAssetDescriptor.schema.json").read_text(encoding="utf-8"))


def _scope_partition(scope: dict) -> str:
    return json.dumps(scope, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def rebuild_registry(product_store_root: str | Path) -> dict:
    root = Path(product_store_root)
    records = []
    active_keys = set()
    validator = Draft202012Validator(_schema(root))
    for path in sorted((root / "assets" / "by-id").glob("*/revisions/r*.json")):
        asset = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(asset), key=lambda e: list(e.path))
        if errors:
            raise ValueError(f"invalid ProductAssetDescriptor {path}: {errors[0].message}")
        if asset["publication_state"] != "PUBLISHED" or asset["validity_state"] != "ACTIVE":
            continue
        key = (asset["asset_id"], _scope_partition(asset["scope"]))
        if key in active_keys:
            raise ValueError(f"multiple PUBLISHED+ACTIVE revisions for asset/scope: {asset['asset_id']}")
        active_keys.add(key)
        descriptor_ref = str(path.relative_to(root))
        records.append({
            "asset_id": asset["asset_id"],
            "asset_revision": asset["asset_revision"],
            "asset_family": asset["asset_family"],
            "asset_type": asset["asset_type"],
            "descriptor_ref": descriptor_ref,
            "content_ref": asset["content_ref"],
            "publication_state": asset["publication_state"],
            "validity_state": asset["validity_state"],
            "as_of": asset.get("as_of"),
            "authority_dimensions": asset.get("authority_dimensions", []),
            "trust_profile": asset["trust_profile"],
            "scope_match": asset["scope"],
            "scope": asset["scope"],
            "selection_metadata": asset.get("selection_metadata", {}),
        })
    return {"schema_version": "0.1", "assets": records}


def write_registry(product_store_root: str | Path) -> Path:
    root = Path(product_store_root)
    out = root / "registry" / "active.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(json.dumps(rebuild_registry(root), indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    return out
