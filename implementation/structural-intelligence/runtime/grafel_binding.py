from __future__ import annotations
from dataclasses import dataclass
from datetime import datetime, timezone
import json
from pathlib import Path
from jsonschema import Draft202012Validator
from .git_revision import require_equal_revision


def _bundle_root() -> Path:
    here = Path(__file__).resolve()
    for parent in here.parents:
        if (parent / "VERSION").exists() and (parent / "governance").exists():
            return parent
    raise RuntimeError("FDI bundle root not found")


def _validate(schema_name: str, value: dict) -> None:
    schema = json.loads((_bundle_root() / "implementation" / "structural-intelligence" / "contracts" / schema_name).read_text(encoding="utf-8"))
    errors = sorted(Draft202012Validator(schema).iter_errors(value), key=lambda e: list(e.path))
    if errors:
        raise ValueError(f"{schema_name}: {errors[0].message}")


def validate_binding_evidence(evidence: dict) -> None:
    _validate("GrafelBindingEvidenceRecord.schema.json", evidence)
    snapshot = evidence["snapshot"]
    att = evidence["attestation"]
    if evidence["runtime_version"] != att["runtime_version"]:
        raise ValueError("runtime_version mismatch")
    if evidence["wire_version"] != att["wire_version"]:
        raise ValueError("wire_version mismatch")
    if evidence["adapter_version"] != att["adapter_version"]:
        raise ValueError("adapter_version mismatch")
    if evidence["compatibility"] != att["compatibility"] or evidence["result"] != att["result"]:
        raise ValueError("attestation result mismatch")
    if snapshot["snapshot_id"] != att["snapshot_id"]:
        raise ValueError("snapshot_id mismatch")
    if snapshot["provider_scope_id"] != att["provider_scope_id"] or snapshot["provider_ref"] != att["provider_ref"]:
        raise ValueError("provider route mismatch")
    if evidence["provider_route"] != {"group": snapshot["provider_scope_id"], "ref": snapshot["provider_ref"]}:
        raise ValueError("provider_route mismatch")
    expected = {r["repository_id"]: r["canonical_revision"].lower() for r in snapshot["repositories"]}
    got = {r["repository_id"]: r for r in att["repository_bindings"]}
    if set(expected) != set(got):
        raise ValueError("repository binding set mismatch")
    for repo_id, canonical in expected.items():
        row = got[repo_id]
        if row["canonical_revision"].lower() != canonical or row["indexed_revision"].lower() != canonical:
            raise ValueError(f"repository revision mismatch: {repo_id}")
        if row["indexed_ref"] != snapshot["provider_ref"]:
            raise ValueError(f"indexed_ref mismatch: {repo_id}")


@dataclass
class GrafelSnapshotBindingAttestor:
    metadata_provider: object
    route_probe: object
    runtime_metadata_provider: object
    compatibility_policy: object
    adapter_version: str = "recovery-0.2"

    def attest(self, snapshot: dict) -> dict:
        repo_rows = []
        for repo in snapshot["repositories"]:
            meta = self.metadata_provider.get(
                group=snapshot["provider_scope_id"],
                ref=snapshot["provider_ref"],
                repository_id=repo["repository_id"],
                local_path=repo["local_path"],
            )
            if meta.get("state") != "current":
                raise ValueError("Grafel repository graph state is not current")
            if meta.get("indexed_ref") != snapshot["provider_ref"]:
                raise ValueError("Grafel indexed_ref mismatch")
            resolved = require_equal_revision(repo["local_path"], meta["indexed_commit"], repo["canonical_revision"])
            repo_rows.append({
                "repository_id": repo["repository_id"],
                "canonical_revision": repo["canonical_revision"].lower(),
                "indexed_revision": resolved.lower(),
                "indexed_ref": meta["indexed_ref"],
            })
        probe = self.route_probe.probe(snapshot["provider_scope_id"], snapshot["provider_ref"])
        if not probe.get("queryable"):
            raise ValueError("Grafel route is not queryable")
        runtime = self.runtime_metadata_provider.get()
        self.compatibility_policy.verify(snapshot, runtime, probe)
        runtime_version = str(runtime.get("runtime_version") or "")
        wire_version = str(runtime.get("wire_version") or "")
        if not runtime_version or not wire_version:
            raise ValueError("runtime/wire version unavailable")
        att = {
            "attestation_id": f"attest:{snapshot['snapshot_id']}",
            "snapshot_id": snapshot["snapshot_id"],
            "provider_scope_id": snapshot["provider_scope_id"],
            "provider_ref": snapshot["provider_ref"],
            "repository_bindings": repo_rows,
            "queryable": True,
            "runtime_version": runtime_version,
            "wire_version": wire_version,
            "adapter_version": self.adapter_version,
            "compatibility": "VERIFIED",
            "result": "EXACTLY_BOUND",
            "captured_at": datetime.now(timezone.utc).isoformat(),
        }
        _validate("SnapshotBindingAttestation.schema.json", att)
        return att
