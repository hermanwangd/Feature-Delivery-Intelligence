from __future__ import annotations

from dataclasses import dataclass
import json
import os
from pathlib import Path
import re
import tempfile
from typing import Iterable, Protocol

from jsonschema import Draft202012Validator


class ProductStoreError(ValueError):
    """Base error for a rejected Product Intelligence Store operation."""


class StoreConflictError(ProductStoreError):
    """The caller's view conflicts with durable store state."""


class PublicationGateError(ProductStoreError):
    """The external publication decision does not authorize the operation."""


class InvalidLifecycleTransition(ProductStoreError):
    """A proposal does not describe a legal append-only lifecycle step."""


@dataclass(frozen=True)
class ProductAssetRef:
    asset_id: str
    asset_revision: int


@dataclass(frozen=True)
class PublicationAuthorization:
    """Evidence-bearing result from the Layer 2 publication gate.

    The store validates and consumes this result; it does not decide whether a
    Human, rule, or source was authoritative enough to produce it.
    """

    policy: str
    approved: bool
    evidence_refs: tuple[str, ...]


class ProductIntelligenceStore(Protocol):
    def get_asset(self, ref: ProductAssetRef) -> dict: ...

    def get_current_ref(self, asset_id: str) -> ProductAssetRef | None: ...

    def list_assets(self) -> Iterable[dict]: ...

    def write_draft(self, proposal: dict) -> Path: ...

    def publish_proposal(
        self,
        proposal_id: str,
        authorization: PublicationAuthorization,
        expected_current: ProductAssetRef | None,
    ) -> ProductAssetRef: ...


_SAFE_SEGMENT = re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]*$")
_OUTCOMES = {
    "CREATE": ("PUBLISHED", "ACTIVE"),
    "REVISE": ("PUBLISHED", "ACTIVE"),
    "MARK_STALE": ("PUBLISHED", "STALE"),
    "SUPERSEDE": ("PUBLISHED", "ACTIVE"),
    "RETIRE": ("RETIRED", "NOT_APPLICABLE"),
}


def _bundle_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "VERSION").exists() and (parent / "governance").exists():
            return parent
    raise RuntimeError("FDI bundle root not found")


def _validator(schema_name: str) -> Draft202012Validator:
    schema_path = _bundle_root() / "contracts" / "layer2" / schema_name
    return Draft202012Validator(json.loads(schema_path.read_text(encoding="utf-8")))


def _validate(instance: dict, schema_name: str, label: str) -> None:
    errors = sorted(_validator(schema_name).iter_errors(instance), key=lambda error: list(error.path))
    if errors:
        location = ".".join(str(part) for part in errors[0].path) or "<root>"
        raise ProductStoreError(f"invalid {label} at {location}: {errors[0].message}")


def _json_bytes(value: dict) -> bytes:
    return (json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n").encode("utf-8")


def _safe_segment(value: str, label: str) -> str:
    if not isinstance(value, str) or not _SAFE_SEGMENT.fullmatch(value) or value in {".", ".."}:
        raise ProductStoreError(f"unsafe {label}: {value!r}")
    return value


def _write_once(path: Path, content: bytes) -> None:
    """Atomically create path, rejecting a different existing value."""

    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary_name = tempfile.mkstemp(
        prefix=f".{path.name}.", suffix=".tmp", dir=path.parent
    )
    temporary = Path(temporary_name)
    try:
        with os.fdopen(descriptor, "wb") as output:
            output.write(content)
            output.flush()
            os.fsync(output.fileno())
        try:
            os.link(temporary, path)
        except FileExistsError:
            if path.read_bytes() == content:
                return
            raise StoreConflictError(f"path already contains different immutable bytes: {path}")
    finally:
        temporary.unlink(missing_ok=True)


class GitStoreAdapter:
    """Deterministic, append-only files for a Product-owned Git repository.

    Git merge and approval remain outside the adapter. A successful publication
    consumes an explicit Layer 2 gate result, creates a revision without
    overwriting history, and refreshes the rebuildable Registry projection.
    """

    def __init__(self, root: str | Path):
        self.root = Path(root)

    def _asset_file(self, ref: ProductAssetRef) -> Path:
        asset_id = _safe_segment(ref.asset_id, "asset_id")
        if ref.asset_revision < 1:
            raise ProductStoreError("asset_revision must be positive")
        return self.root / "assets" / "by-id" / asset_id / "revisions" / f"r{ref.asset_revision:04d}.json"

    def _proposal_file(self, proposal_id: str) -> Path:
        return self.root / "proposals" / f"{_safe_segment(proposal_id, 'proposal_id')}.json"

    def get_asset(self, ref: ProductAssetRef) -> dict:
        return json.loads(self._asset_file(ref).read_text(encoding="utf-8"))

    def get_current_ref(self, asset_id: str) -> ProductAssetRef | None:
        from .registry import current_asset_refs

        _safe_segment(asset_id, "asset_id")
        matching = [ref for ref in current_asset_refs(self.root) if ref[0] == asset_id]
        if not matching:
            return None
        if len(matching) > 1:
            raise StoreConflictError(f"multiple current revisions for asset: {asset_id}")
        return ProductAssetRef(*matching[0])

    def list_assets(self) -> Iterable[dict]:
        base = self.root / "assets" / "by-id"
        if not base.exists():
            return []
        return [
            json.loads(path.read_text(encoding="utf-8"))
            for path in sorted(base.glob("*/revisions/r*.json"))
        ]

    def write_draft(self, proposal: dict) -> Path:
        _validate(proposal, "ProductAssetProposal.schema.json", "ProductAssetProposal")
        proposal_id = proposal["proposal_id"]
        path = self._proposal_file(proposal_id)
        _write_once(path, _json_bytes(proposal))
        return path

    def _authorize(self, proposal: dict, authorization: PublicationAuthorization) -> None:
        required_policy = proposal["review_requirement"]
        asset_policy = proposal["proposed_asset"].get("publication_policy")
        if required_policy != asset_policy:
            raise PublicationGateError("proposal review requirement does not match asset publication policy")
        if authorization.policy != required_policy:
            raise PublicationGateError("authorization policy does not match proposal review requirement")
        if not authorization.approved:
            raise PublicationGateError("publication gate denied the proposal")
        if not authorization.evidence_refs or any(not ref for ref in authorization.evidence_refs):
            raise PublicationGateError("publication authorization requires evidence refs")

    def _validate_transition(
        self,
        proposal: dict,
        expected_current: ProductAssetRef | None,
    ) -> ProductAssetRef:
        kind = proposal["proposal_kind"]
        asset = proposal["proposed_asset"]
        target_asset_id = proposal["target_asset_id"]
        new_ref = ProductAssetRef(asset["asset_id"], asset["asset_revision"])
        _safe_segment(new_ref.asset_id, "asset_id")

        required_outcome = _OUTCOMES[kind]
        actual_outcome = (asset["publication_state"], asset["validity_state"])
        if actual_outcome != required_outcome:
            raise InvalidLifecycleTransition(
                f"{kind} requires state {required_outcome[0]}+{required_outcome[1]}"
            )

        if kind == "CREATE":
            if target_asset_id is not None or expected_current is not None:
                raise InvalidLifecycleTransition("CREATE requires no target or expected current revision")
            if asset["asset_revision"] != 1 or asset["supersedes"] is not None:
                raise InvalidLifecycleTransition("CREATE requires revision 1 and no supersedes ref")
            if any(existing["asset_id"] == new_ref.asset_id for existing in self.list_assets()):
                raise StoreConflictError(f"asset already exists: {new_ref.asset_id}")
            return new_ref

        if not isinstance(target_asset_id, str):
            raise InvalidLifecycleTransition(f"{kind} requires target_asset_id")
        current = self.get_current_ref(target_asset_id)
        if current != expected_current:
            raise StoreConflictError(
                f"expected current {expected_current!r}, found {current!r} for {target_asset_id}"
            )
        if current is None:
            raise StoreConflictError(f"target asset has no current revision: {target_asset_id}")
        current_asset = self.get_asset(current)
        if current_asset["publication_state"] == "RETIRED":
            raise InvalidLifecycleTransition("RETIRED is terminal")
        if kind == "MARK_STALE" and current_asset["validity_state"] != "ACTIVE":
            raise InvalidLifecycleTransition("MARK_STALE requires a PUBLISHED+ACTIVE current revision")
        if current_asset["validity_state"] not in {"ACTIVE", "STALE"}:
            raise InvalidLifecycleTransition(f"cannot {kind} from the current lifecycle state")

        expected_supersedes = {
            "asset_id": current.asset_id,
            "asset_revision": current.asset_revision,
        }
        if asset["supersedes"] != expected_supersedes:
            raise InvalidLifecycleTransition(f"{kind} must supersede the expected current revision")

        if kind != "SUPERSEDE" or new_ref.asset_id == target_asset_id:
            if new_ref.asset_id != target_asset_id:
                raise InvalidLifecycleTransition(f"{kind} cannot change asset_id")
            if new_ref.asset_revision != current.asset_revision + 1:
                raise InvalidLifecycleTransition(f"{kind} must increment asset_revision by one")
        else:
            if new_ref.asset_revision != 1:
                raise InvalidLifecycleTransition("cross-asset SUPERSEDE must create revision 1")
            if any(existing["asset_id"] == new_ref.asset_id for existing in self.list_assets()):
                raise StoreConflictError(f"replacement asset already exists: {new_ref.asset_id}")
        return new_ref

    def publish_proposal(
        self,
        proposal_id: str,
        authorization: PublicationAuthorization,
        expected_current: ProductAssetRef | None,
    ) -> ProductAssetRef:
        proposal_path = self._proposal_file(proposal_id)
        if not proposal_path.exists():
            raise ProductStoreError(f"proposal not found: {proposal_id}")
        proposal = json.loads(proposal_path.read_text(encoding="utf-8"))
        _validate(proposal, "ProductAssetProposal.schema.json", "ProductAssetProposal")
        asset = proposal["proposed_asset"]
        _validate(asset, "ProductAssetDescriptor.schema.json", "ProductAssetDescriptor")
        self._authorize(proposal, authorization)
        new_ref = self._validate_transition(proposal, expected_current)
        _write_once(self._asset_file(new_ref), _json_bytes(asset))

        from .registry import write_registry

        write_registry(self.root)
        return new_ref
