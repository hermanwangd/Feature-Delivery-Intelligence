from __future__ import annotations

import json
import os
from pathlib import Path
import re
import tempfile

from jsonschema import Draft202012Validator


class RegistryConflictError(ValueError):
    """Stored descriptors cannot produce one deterministic Registry."""


_REVISION_FILE = re.compile(r"^r([0-9]+)\.json$")


def _bundle_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "VERSION").exists() and (parent / "governance").exists():
            return parent
    raise RuntimeError("FDI bundle root not found")


def _schema() -> dict:
    bundle = _bundle_root()
    return json.loads(
        (bundle / "contracts" / "layer2" / "ProductAssetDescriptor.schema.json").read_text(
            encoding="utf-8"
        )
    )


def _scope_partition(scope: dict) -> str:
    return json.dumps(scope, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def _descriptor_records(root: Path) -> list[tuple[Path, dict]]:
    validator = Draft202012Validator(_schema())
    records: list[tuple[Path, dict]] = []
    for path in sorted((root / "assets" / "by-id").glob("*/revisions/r*.json")):
        asset = json.loads(path.read_text(encoding="utf-8"))
        errors = sorted(validator.iter_errors(asset), key=lambda error: list(error.path))
        if errors:
            raise ValueError(f"invalid ProductAssetDescriptor {path}: {errors[0].message}")
        match = _REVISION_FILE.fullmatch(path.name)
        path_asset_id = path.parent.parent.name
        if (
            match is None
            or asset["asset_id"] != path_asset_id
            or asset["asset_revision"] != int(match.group(1))
        ):
            raise ValueError(f"descriptor path does not match asset identity: {path}")
        records.append((path, asset))
    return records


def _current_records(root: Path) -> list[tuple[Path, dict]]:
    records = _descriptor_records(root)
    by_ref: dict[tuple[str, int], tuple[Path, dict]] = {}
    successors: dict[tuple[str, int], list[tuple[str, int]]] = {}
    for path, asset in records:
        ref = (asset["asset_id"], asset["asset_revision"])
        if ref in by_ref:
            raise RegistryConflictError(f"duplicate Product Asset revision: {ref}")
        by_ref[ref] = (path, asset)

    for _, asset in records:
        ref = (asset["asset_id"], asset["asset_revision"])
        if asset["publication_state"] == "DRAFT":
            continue
        supersedes = asset["supersedes"]
        if supersedes is None:
            continue
        predecessor = (supersedes["asset_id"], supersedes["asset_revision"])
        if predecessor not in by_ref:
            raise RegistryConflictError(f"supersedes ref does not exist: {predecessor}")
        if by_ref[predecessor][1]["publication_state"] == "DRAFT":
            raise RegistryConflictError(f"published revision supersedes a DRAFT: {predecessor}")
        if predecessor == ref:
            raise RegistryConflictError(f"revision cannot supersede itself: {ref}")
        successors.setdefault(predecessor, []).append(ref)

    forks = {ref: values for ref, values in successors.items() if len(values) > 1}
    if forks:
        predecessor = sorted(forks)[0]
        raise RegistryConflictError(f"multiple successors for Product Asset revision: {predecessor}")

    for start in by_ref:
        visited: set[tuple[str, int]] = set()
        cursor = start
        while cursor in successors:
            if cursor in visited:
                raise RegistryConflictError(f"supersession cycle contains: {cursor}")
            visited.add(cursor)
            cursor = successors[cursor][0]

    superseded = set(successors)
    current = [
        record
        for ref, record in by_ref.items()
        if ref not in superseded and record[1]["publication_state"] != "DRAFT"
    ]
    current.sort(key=lambda record: (record[1]["asset_id"], record[1]["asset_revision"]))
    current_asset_ids: set[str] = set()
    for _, asset in current:
        if asset["asset_id"] in current_asset_ids:
            raise RegistryConflictError(
                f"multiple current revisions for Product Asset: {asset['asset_id']}"
            )
        current_asset_ids.add(asset["asset_id"])
    return current


def current_asset_refs(product_store_root: str | Path) -> list[tuple[str, int]]:
    return [
        (asset["asset_id"], asset["asset_revision"])
        for _, asset in _current_records(Path(product_store_root))
    ]


def rebuild_registry(product_store_root: str | Path) -> dict:
    root = Path(product_store_root)
    records = []
    active_keys = set()
    for path, asset in _current_records(root):
        if asset["publication_state"] != "PUBLISHED" or asset["validity_state"] != "ACTIVE":
            continue
        key = (asset["asset_id"], _scope_partition(asset["scope"]))
        if key in active_keys:
            raise RegistryConflictError(
                f"multiple PUBLISHED+ACTIVE revisions for asset/scope: {asset['asset_id']}"
            )
        active_keys.add(key)
        descriptor_ref = str(path.relative_to(root))
        records.append(
            {
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
            }
        )
    return {"schema_version": "0.1", "assets": records}


def write_registry(product_store_root: str | Path) -> Path:
    root = Path(product_store_root)
    out = root / "registry" / "active.json"
    out.parent.mkdir(parents=True, exist_ok=True)
    content = (
        json.dumps(rebuild_registry(root), indent=2, sort_keys=True, ensure_ascii=False) + "\n"
    ).encode("utf-8")
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{out.name}.", suffix=".tmp", dir=out.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as output:
            output.write(content)
            output.flush()
            os.fsync(output.fileno())
        os.replace(temporary, out)
    finally:
        temporary.unlink(missing_ok=True)
    return out
