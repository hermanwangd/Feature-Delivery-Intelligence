"""Grafel reference adapter for the FDI Structural Intelligence Runtime.

Only this adapter knows Grafel MCP tool names. Governing FDI contracts depend on
provider-independent operations and normalized structural artifacts.
"""
from __future__ import annotations

from copy import deepcopy

from runtime.structural_intelligence import (
    StructuralIntelligenceError,
    normalize_observations,
    normalize_structural_delta,
    validate_snapshot_binding,
    validate_snapshot_ref,
    validate_structural_query,
)


class GrafelAdapterError(ValueError):
    """Raised when the Grafel binding cannot satisfy the FDI adapter contract."""


DEFAULT_TOOL_MAPPING = {
    "orient": "grafel_orient",
    "find": "grafel_find",
    "expand": "grafel_subgraph",
    "trace": "grafel_find_paths",
    "diff": "grafel_diff",
}


class GrafelAdapter:
    """Reference adapter over an injected MCP-like transport.

    Graph queries are eligible for FDI normalization only after an injected
    binding attestor proves that an explicit provider scope/ref is queryable at
    the exact repository revisions in StructuralSnapshotRef. Historical indexed
    refs are valid; scheduler-current HEAD is a freshness facet, not authority.
    """

    def __init__(self, transport, *, response_mapper, binding_attestor=None, tool_mapping: dict | None = None):
        if transport is None or not callable(getattr(transport, "invoke", None)):
            raise GrafelAdapterError("transport must provide invoke(tool_name, payload)")
        if not callable(response_mapper):
            raise GrafelAdapterError("response_mapper is required")
        if not callable(binding_attestor):
            raise GrafelAdapterError("binding_attestor is required")
        mapping = deepcopy(tool_mapping or DEFAULT_TOOL_MAPPING)
        if set(mapping) != set(DEFAULT_TOOL_MAPPING) or not all(mapping.values()):
            raise GrafelAdapterError("tool_mapping must define orient/find/expand/trace/diff")
        self._transport = transport
        self._response_mapper = response_mapper
        self._binding_attestor = binding_attestor
        self.tool_mapping = mapping

    @staticmethod
    def _snapshot(snapshot_ref: dict) -> dict:
        try:
            snapshot = validate_snapshot_ref(snapshot_ref)
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc
        if snapshot["provider"]["name"] != "GRAFEL":
            raise GrafelAdapterError("GrafelAdapter requires provider.name=GRAFEL")
        return snapshot

    def _mapped(self, operation: str, raw, snapshot: dict, structural_query: dict | None):
        return self._response_mapper(
            raw,
            operation=operation,
            snapshot_ref=deepcopy(snapshot),
            structural_query=deepcopy(structural_query) if structural_query is not None else None,
        )

    def _verify_snapshot_binding(self, snapshot: dict) -> dict:
        try:
            provider_state = self._binding_attestor(deepcopy(snapshot))
        except Exception as exc:  # provider/version-specific provenance stays outside FDI core
            raise GrafelAdapterError(f"snapshot binding attestor failed: {exc}") from exc
        try:
            return validate_snapshot_binding(snapshot, provider_state)
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(f"snapshot binding failed: {exc}") from exc

    @staticmethod
    def _route_payload(attestation: dict) -> dict:
        route = attestation["provider_route"]
        return {"group": route["scope_id"], "ref": route["ref"]}

    @staticmethod
    def _repository_map(attestation: dict) -> dict:
        mapping = {
            item["repository"]: item.get("provider_repository")
            for item in attestation["repositories"]
        }
        if any(not isinstance(provider_repository, str) or not provider_repository for provider_repository in mapping.values()):
            raise GrafelAdapterError("verified binding attestation requires provider repository mapping")
        if len(set(mapping.values())) != len(mapping):
            raise GrafelAdapterError("verified binding attestation provider repository mapping must be unique")
        return mapping

    def orient(self, request: dict, snapshot_ref: dict):
        snapshot = self._snapshot(snapshot_ref)
        if not isinstance(request, dict) or request.get("view") not in {"overview", "me", "clusters", "topology", "modules"}:
            raise GrafelAdapterError("orient view is invalid")
        repositories = request.get("repositories") or [x["repository"] for x in snapshot["source_snapshots"]]
        pinned = {x["repository"] for x in snapshot["source_snapshots"]}
        if not isinstance(repositories, list) or not set(repositories).issubset(pinned):
            raise GrafelAdapterError("orient repository scope must be pinned by StructuralSnapshotRef")
        attestation = self._verify_snapshot_binding(snapshot)
        repository_map = self._repository_map(attestation)
        payload = {
            **self._route_payload(attestation),
            "view": request["view"],
            "repo_filter": sorted({repository_map[repository] for repository in repositories}),
        }
        raw = self._transport.invoke(self.tool_mapping["orient"], payload)
        return {
            "structural_snapshot_id": snapshot["snapshot_id"],
            "binding_attestation_id": attestation["attestation_id"],
            "provider_result": self._mapped("orient", raw, snapshot, None),
            "non_authoritative": True,
        }

    def _live_query(self, operation: str, structural_query: dict, snapshot_ref: dict, payload: dict, *, require_path_ids=False):
        snapshot = self._snapshot(snapshot_ref)
        try:
            query = validate_structural_query(structural_query, snapshot)
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc
        attestation = self._verify_snapshot_binding(snapshot)
        repository_map = self._repository_map(attestation)
        if "repo_filter" in payload:
            payload = {
                **payload,
                "repo_filter": [repository_map[repository] for repository in payload["repo_filter"]],
            }
        routed_payload = {**self._route_payload(attestation), **payload}
        raw = self._transport.invoke(self.tool_mapping[operation], routed_payload)
        provider_records = self._mapped(operation, raw, snapshot, query)
        try:
            return normalize_observations(
                provider_records,
                snapshot,
                query,
                binding_attestation=attestation,
                require_path_ids=require_path_ids,
            )
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc

    def find(self, structural_query: dict, snapshot_ref: dict) -> dict:
        snapshot = self._snapshot(snapshot_ref)
        try:
            query = validate_structural_query(structural_query, snapshot)
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc
        payload = {
            "query": query.get("text_query") or query["seed"]["id"],
            "depth": query["max_depth"],
            "token_budget": max(1, query["max_result_bytes"] // 16),
            "repo_filter": list(query["scope"]["repositories"]),
            "cross_repo": len(query["scope"]["repositories"]) > 1,
        }
        return self._live_query("find", query, snapshot, payload)

    def expand(self, structural_query: dict, snapshot_ref: dict) -> dict:
        snapshot = self._snapshot(snapshot_ref)
        try:
            query = validate_structural_query(structural_query, snapshot)
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc
        payload = {
            "entity_id": query["seed"]["id"],
            "depth": query["max_depth"],
            "max_nodes": query["max_nodes"],
            "format": "raw",
        }
        return self._live_query("expand", query, snapshot, payload)

    def trace(self, structural_query: dict, snapshot_ref: dict) -> dict:
        snapshot = self._snapshot(snapshot_ref)
        try:
            query = validate_structural_query(structural_query, snapshot)
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc
        target = query.get("target")
        if not isinstance(target, dict) or not target.get("id") or not target.get("type"):
            raise GrafelAdapterError("trace requires target type/id")
        payload = {"from": query["seed"]["id"], "to": target["id"], "max_hops": query["max_depth"]}
        return self._live_query("trace", query, snapshot, payload, require_path_ids=True)

    def diff(self, request: dict, before_snapshot_ref: dict, after_snapshot_ref: dict) -> dict:
        before = self._snapshot(before_snapshot_ref)
        after = self._snapshot(after_snapshot_ref)
        if before["snapshot_id"] == after["snapshot_id"]:
            raise GrafelAdapterError("diff requires distinct before/after StructuralSnapshotRef values")
        if not isinstance(request, dict):
            raise GrafelAdapterError("diff request must be an object")
        repository = request.get("repository")
        before_revs = {x["repository"]: x["revision"] for x in before["source_snapshots"]}
        after_revs = {x["repository"]: x["revision"] for x in after["source_snapshots"]}
        if repository not in before_revs or repository not in after_revs:
            raise GrafelAdapterError("diff repository must be pinned by both StructuralSnapshotRef values")
        left = before_revs[repository]
        right = after_revs[repository]
        if left == right:
            raise GrafelAdapterError("diff requires distinct pinned repository revisions")
        before_attestation = self._verify_snapshot_binding(before)
        after_attestation = self._verify_snapshot_binding(after)
        before_route = before_attestation["provider_route"]
        after_route = after_attestation["provider_route"]
        if before_route["scope_id"] != after_route["scope_id"]:
            raise GrafelAdapterError("diff requires before/after provider refs in the same provider scope")
        if before_route["ref"] == after_route["ref"]:
            raise GrafelAdapterError("diff requires distinct provider refs")
        before_repository = self._repository_map(before_attestation)[repository]
        after_repository = self._repository_map(after_attestation)[repository]
        if before_repository != after_repository:
            raise GrafelAdapterError("diff requires the same provider repository mapping in both attestations")
        payload = {
            "group": before_route["scope_id"],
            "repo": before_repository,
            "ref_a": before_route["ref"],
            "ref_b": after_route["ref"],
            "aspect": "refs",
        }
        raw = self._transport.invoke(self.tool_mapping["diff"], payload)
        provider_delta = self._mapped("diff", raw, after, request)
        try:
            return normalize_structural_delta(
                provider_delta,
                before,
                after,
                request,
                before_binding_attestation=before_attestation,
                after_binding_attestation=after_attestation,
            )
        except StructuralIntelligenceError as exc:
            raise GrafelAdapterError(str(exc)) from exc
