"""Provider-independent Structural Intelligence runtime support for FDI.

Structural outputs are deliberately non-authoritative. They may guide bounded
investigation and Product Intelligence maintenance, but they never establish
current Feature truth.
"""
from __future__ import annotations

from copy import deepcopy
import hashlib
import json


class StructuralIntelligenceError(ValueError):
    """Raised when Structural Intelligence input violates FDI runtime bounds."""


SUPPORTED_RELATION_TYPES = {
    "HTTP_CALL",
    "MESSAGE_PUBLISH",
    "MESSAGE_CONSUME",
    "SCHEMA_DEPENDENCY",
    "COMPONENT_DEPENDENCY",
    "INFRA_BINDING",
    "CONFIG_DEPENDENCY",
}

_REQUIRED_BUDGETS = ("max_depth", "max_nodes", "max_edges", "max_paths", "max_result_bytes")


def _fail(message: str) -> None:
    raise StructuralIntelligenceError(message)


def validate_snapshot_ref(ref: dict) -> dict:
    if not isinstance(ref, dict):
        _fail("StructuralSnapshotRef must be an object")
    if not ref.get("snapshot_id"):
        _fail("snapshot_id is required")
    provider = ref.get("provider")
    if not isinstance(provider, dict) or not provider.get("name") or not provider.get("version"):
        _fail("provider name/version are required")
    if not ref.get("adapter_version"):
        _fail("adapter_version is required")
    if not ref.get("created_at"):
        _fail("created_at is required")
    sources = ref.get("source_snapshots")
    if not isinstance(sources, list) or not sources:
        _fail("source_snapshots must be non-empty")
    seen_repositories = set()
    for source in sources:
        if not isinstance(source, dict) or not source.get("repository") or not source.get("revision"):
            _fail("every source snapshot requires repository and revision")
        repository = source["repository"]
        if repository in seen_repositories:
            _fail(f"duplicate repository snapshot: {repository}")
        seen_repositories.add(repository)
    result = deepcopy(ref)
    result["source_snapshots"] = sorted(
        result["source_snapshots"], key=lambda item: (item["repository"], item["revision"])
    )
    return result


def validate_snapshot_binding(snapshot_ref: dict, provider_binding_state: dict) -> dict:
    """Prove exact, queryable provider routing for a StructuralSnapshotRef.

    FDI requires equivalence between the canonical repository revisions pinned
    by ``StructuralSnapshotRef`` and the provider graph that will actually be
    queried.  The provider graph may be the live/current ref or a historical
    indexed ref; scheduler freshness is a facet, not an authority requirement.

    Provider-specific discovery of this state is deliberately outside this
    provider-neutral validator.  Adapters receive it from a binding attestor.
    """
    snapshot = validate_snapshot_ref(snapshot_ref)
    state = provider_binding_state
    if not isinstance(state, dict):
        _fail("provider snapshot binding state must be an object")

    scope_id = state.get("provider_scope_id")
    provider_ref = state.get("provider_ref")
    if not isinstance(scope_id, str) or not scope_id:
        _fail("provider_scope_id is required")
    if not isinstance(provider_ref, str) or not provider_ref:
        _fail("provider_ref is required")
    if state.get("queryability") != "QUERYABLE":
        _fail("provider snapshot must be QUERYABLE")
    freshness = state.get("freshness")
    if freshness not in {"LIVE_CURRENT", "FROZEN_INDEXED"}:
        _fail("freshness must be LIVE_CURRENT or FROZEN_INDEXED")

    repository_state = state.get("repositories")
    if not isinstance(repository_state, list) or not repository_state:
        _fail("provider snapshot binding repositories must be non-empty")
    by_repo: dict[str, dict] = {}
    for item in repository_state:
        if not isinstance(item, dict) or not item.get("repository"):
            _fail("provider snapshot binding entry requires repository")
        repo = item["repository"]
        if repo in by_repo:
            _fail(f"duplicate provider binding repository: {repo}")
        by_repo[repo] = item

    expected = {item["repository"]: item["revision"] for item in snapshot["source_snapshots"]}
    if set(by_repo) != set(expected):
        _fail("provider snapshot binding repository set does not match StructuralSnapshotRef")

    normalized = []
    provider_repositories = set()
    for repo in sorted(expected):
        item = by_repo[repo]
        indexed = item.get("indexed_revision")
        if item.get("queryable") is not True:
            _fail(f"provider repository snapshot is not queryable: {repo}")
        if indexed != expected[repo]:
            _fail(f"provider indexed revision does not match StructuralSnapshotRef: {repo}")
        normalized_item = {
            "repository": repo,
            "indexed_revision": indexed,
            "queryable": True,
            "head_revision": item.get("head_revision"),
        }
        if "provider_repository" in item:
            provider_repository = item.get("provider_repository")
            if not isinstance(provider_repository, str) or not provider_repository:
                _fail(f"provider repository mapping is invalid: {repo}")
            if provider_repository in provider_repositories:
                _fail(f"provider repository mapping is ambiguous: {provider_repository}")
            provider_repositories.add(provider_repository)
            normalized_item["provider_repository"] = provider_repository
        normalized.append(normalized_item)

    provider_route = {"scope_id": scope_id, "ref": provider_ref}
    payload = json.dumps(
        {
            "snapshot_id": snapshot["snapshot_id"],
            "provider_route": provider_route,
            "freshness": freshness,
            "repositories": normalized,
        },
        sort_keys=True,
        separators=(",", ":"),
    )
    return {
        "snapshot_id": snapshot["snapshot_id"],
        "binding_state": "VERIFIED",
        "provider_route": provider_route,
        "freshness": freshness,
        "repositories": normalized,
        "attestation_id": "sba:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24],
    }


def _validate_binding_attestation(snapshot: dict, attestation: dict | None) -> dict:
    if not isinstance(attestation, dict):
        _fail("verified snapshot binding attestation is required")
    if attestation.get("snapshot_id") != snapshot["snapshot_id"] or attestation.get("binding_state") != "VERIFIED":
        _fail("snapshot binding attestation does not match StructuralSnapshotRef")
    if not attestation.get("attestation_id"):
        _fail("snapshot binding attestation id is required")
    route = attestation.get("provider_route")
    if not isinstance(route, dict) or not route.get("scope_id") or not route.get("ref"):
        _fail("snapshot binding attestation requires exact provider route")
    if attestation.get("freshness") not in {"LIVE_CURRENT", "FROZEN_INDEXED"}:
        _fail("snapshot binding attestation freshness is invalid")
    expected = {item["repository"]: item["revision"] for item in snapshot["source_snapshots"]}
    state = attestation.get("repositories")
    if not isinstance(state, list) or {x.get("repository") for x in state} != set(expected):
        _fail("snapshot binding attestation repository set does not match StructuralSnapshotRef")
    for item in state:
        repo = item.get("repository")
        if item.get("queryable") is not True or item.get("indexed_revision") != expected[repo]:
            _fail("snapshot binding attestation no longer proves exact queryable repository revisions")
    return deepcopy(attestation)


def validate_structural_query(query: dict, snapshot_ref: dict) -> dict:
    snapshot = validate_snapshot_ref(snapshot_ref)
    if not isinstance(query, dict):
        _fail("StructuralQuery must be an object")
    if not query.get("query_id"):
        _fail("query_id is required")
    if query.get("snapshot_id") != snapshot["snapshot_id"]:
        _fail("query snapshot_id must match StructuralSnapshotRef")
    scope = query.get("scope")
    if not isinstance(scope, dict) or not scope.get("products"):
        _fail("query scope.products must be non-empty")
    if not isinstance(scope.get("repositories"), list) or not scope.get("repositories"):
        _fail("query scope.repositories must be non-empty")
    source_repositories = {item["repository"] for item in snapshot["source_snapshots"]}
    requested_repositories = set(scope["repositories"])
    if not requested_repositories.issubset(source_repositories):
        _fail("query repository scope must be pinned by StructuralSnapshotRef")
    seed = query.get("seed")
    if not isinstance(seed, dict) or not seed.get("type") or not seed.get("id"):
        _fail("query seed type/id are required")
    relation_types = query.get("allowed_relation_types")
    if not isinstance(relation_types, list) or not relation_types:
        _fail("allowed_relation_types must be non-empty")
    unsupported = set(relation_types) - SUPPORTED_RELATION_TYPES
    if unsupported:
        _fail(f"unsupported relation types: {sorted(unsupported)}")
    for field in _REQUIRED_BUDGETS:
        value = query.get(field)
        if not isinstance(value, int) or isinstance(value, bool) or value <= 0:
            _fail(f"{field} must be a positive integer")
    result = deepcopy(query)
    result["scope"]["products"] = sorted(set(result["scope"]["products"]))
    result["scope"]["repositories"] = sorted(set(result["scope"]["repositories"]))
    result["allowed_relation_types"] = sorted(set(result["allowed_relation_types"]))
    return result


def _canonical_edge(record: dict) -> dict:
    src = record.get("from")
    dst = record.get("to")
    if not isinstance(src, dict) or not isinstance(dst, dict):
        _fail("provider observation requires from/to objects")
    for label, node in (("from", src), ("to", dst)):
        if not node.get("type") or not node.get("id"):
            _fail(f"provider observation {label} requires type/id")
        if not node.get("repository_id"):
            _fail(f"provider observation {label} requires repository_id for source-scope verification")
    relation_type = record.get("relation_type")
    if not relation_type:
        _fail("provider observation relation_type is required")
    evidence_refs = record.get("evidence_refs", [])
    if not isinstance(evidence_refs, list):
        _fail("provider observation evidence_refs must be a list")
    path_id = record.get("path_id")
    if path_id is not None and not isinstance(path_id, str):
        _fail("provider observation path_id must be a string when present")
    return {
        "from": {"type": src["type"], "id": src["id"], "repository_id": src["repository_id"]},
        "relation_type": relation_type,
        "to": {"type": dst["type"], "id": dst["id"], "repository_id": dst["repository_id"]},
        "evidence_refs": sorted(set(evidence_refs)),
        "path_ids": [path_id] if path_id else [],
    }


def _edge_signature(edge: dict) -> tuple:
    return (
        edge["from"]["type"], edge["from"]["id"], edge["from"]["repository_id"],
        edge["relation_type"],
        edge["to"]["type"], edge["to"]["id"], edge["to"]["repository_id"],
    )


def _observation_id(snapshot_id: str, edge: dict) -> str:
    payload = json.dumps([snapshot_id, *_edge_signature(edge)], separators=(",", ":"), sort_keys=False)
    return "so:" + hashlib.sha256(payload.encode("utf-8")).hexdigest()[:24]


def normalize_observations(
    provider_records: list[dict],
    snapshot_ref: dict,
    query: dict,
    *,
    binding_attestation: dict | None = None,
    require_path_ids: bool = False,
) -> dict:
    snapshot = validate_snapshot_ref(snapshot_ref)
    attestation = _validate_binding_attestation(snapshot, binding_attestation)
    validated_query = validate_structural_query(query, snapshot)
    if not isinstance(provider_records, list):
        _fail("provider_records must be a list")
    allowed_relations = set(validated_query["allowed_relation_types"])
    scoped_repositories = set(validated_query["scope"]["repositories"])
    observations_by_signature: dict[tuple, dict] = {}
    for record in provider_records:
        if not isinstance(record, dict):
            _fail("provider observation must be an object")
        if require_path_ids and not record.get("path_id"):
            _fail("trace provider observation requires path_id for max_paths enforcement")
        edge = _canonical_edge(record)
        if edge["relation_type"] not in allowed_relations:
            _fail(f"provider relation outside query allowlist: {edge['relation_type']}")
        endpoint_repositories = {edge["from"]["repository_id"], edge["to"]["repository_id"]}
        if not endpoint_repositories.issubset(scoped_repositories):
            _fail("provider observation endpoint is outside bounded repository scope")
        signature = _edge_signature(edge)
        provider_metadata = {
            "name": snapshot["provider"]["name"],
            "version": snapshot["provider"]["version"],
            "adapter_version": snapshot["adapter_version"],
            "provider_observation_id": record.get("provider_observation_id"),
        }
        if record.get("provider_assessment") is not None:
            provider_metadata["provider_assessment"] = deepcopy(record["provider_assessment"])
        observation = {
            "observation_id": _observation_id(snapshot["snapshot_id"], edge),
            "structural_snapshot_id": snapshot["snapshot_id"],
            **edge,
            "provider": provider_metadata,
            "observed_at": snapshot["created_at"],
            "non_authoritative": True,
        }
        existing = observations_by_signature.get(signature)
        if existing is None:
            observations_by_signature[signature] = observation
        else:
            existing["evidence_refs"] = sorted(set(existing["evidence_refs"]) | set(observation["evidence_refs"]))
            existing["path_ids"] = sorted(set(existing["path_ids"]) | set(observation["path_ids"]))

    observations = [observations_by_signature[key] for key in sorted(observations_by_signature, key=repr)]
    if len(observations) > validated_query["max_edges"]:
        _fail("normalized observations exceed max_edges budget")
    nodes = {
        (node["type"], node["id"], node["repository_id"])
        for observation in observations
        for node in (observation["from"], observation["to"])
    }
    if len(nodes) > validated_query["max_nodes"]:
        _fail("normalized observations exceed max_nodes budget")
    path_ids = {path_id for observation in observations for path_id in observation.get("path_ids", [])}
    if len(path_ids) > validated_query["max_paths"]:
        _fail("normalized observations exceed max_paths budget")
    encoded_size = len(json.dumps(observations, sort_keys=True).encode("utf-8"))
    if encoded_size > validated_query["max_result_bytes"]:
        _fail("normalized observations exceed max_result_bytes budget")
    return {
        "query_id": validated_query["query_id"],
        "structural_snapshot_id": snapshot["snapshot_id"],
        "binding_attestation_id": attestation["attestation_id"],
        "observations": observations,
        "non_authoritative": True,
    }


def derive_discovery_hints(observation_set: dict, *, max_hints: int) -> dict:
    if not isinstance(max_hints, int) or isinstance(max_hints, bool) or max_hints <= 0:
        _fail("max_hints must be a positive integer")
    if not isinstance(observation_set, dict) or observation_set.get("non_authoritative") is not True:
        _fail("StructuralObservationSet must be explicitly non_authoritative")
    if not isinstance(observation_set.get("observations"), list):
        _fail("StructuralObservationSet is required")
    by_repository: dict[str, dict] = {}
    for observation in observation_set["observations"]:
        if not isinstance(observation, dict) or observation.get("non_authoritative") is not True:
            _fail("every StructuralObservation must remain non_authoritative")
        for node in (observation.get("from", {}), observation.get("to", {})):
            repository_id = node.get("repository_id")
            if not repository_id:
                _fail("StructuralObservation node repository_id is required")
            hint = by_repository.setdefault(
                repository_id,
                {"repository_id": repository_id, "observation_ids": [], "relation_types": [], "evidence_refs": [], "non_authoritative": True},
            )
            hint["observation_ids"].append(observation["observation_id"])
            hint["relation_types"].append(observation["relation_type"])
            hint["evidence_refs"].extend(observation.get("evidence_refs", []))
    hints = []
    for repository_id in sorted(by_repository):
        hint = by_repository[repository_id]
        hint["observation_ids"] = sorted(set(hint["observation_ids"]))
        hint["relation_types"] = sorted(set(hint["relation_types"]))
        hint["evidence_refs"] = sorted(set(hint["evidence_refs"]))
        hints.append(hint)
    truncated = len(hints) > max_hints
    hints = hints[:max_hints]
    return {
        "structural_snapshot_id": observation_set.get("structural_snapshot_id"),
        "binding_attestation_id": observation_set.get("binding_attestation_id"),
        "hints": hints,
        "truncated": truncated,
        "non_authoritative": True,
    }


def _structural_signature(observation: dict) -> tuple:
    return _edge_signature(observation)


def diff_observations(before: dict, after: dict) -> dict:
    if not isinstance(before, dict) or not isinstance(after, dict):
        _fail("before/after StructuralObservationSet objects are required")
    if before.get("non_authoritative") is not True or after.get("non_authoritative") is not True:
        _fail("before/after StructuralObservationSet must remain non_authoritative")
    before_items = before.get("observations")
    after_items = after.get("observations")
    if not isinstance(before_items, list) or not isinstance(after_items, list):
        _fail("before/after observations must be lists")
    if not before.get("structural_snapshot_id") or not after.get("structural_snapshot_id"):
        _fail("before/after structural_snapshot_id are required")
    if not before.get("binding_attestation_id") or not after.get("binding_attestation_id"):
        _fail("before/after binding_attestation_id are required")
    if before["structural_snapshot_id"] == after["structural_snapshot_id"]:
        _fail("StructuralDelta requires distinct before/after snapshots")
    before_map = {_structural_signature(item): item for item in before_items}
    after_map = {_structural_signature(item): item for item in after_items}
    added_keys = sorted(set(after_map) - set(before_map), key=repr)
    removed_keys = sorted(set(before_map) - set(after_map), key=repr)
    unchanged_keys = sorted(set(before_map) & set(after_map), key=repr)
    return {
        "before_snapshot_id": before["structural_snapshot_id"],
        "after_snapshot_id": after["structural_snapshot_id"],
        "before_binding_attestation_id": before["binding_attestation_id"],
        "after_binding_attestation_id": after["binding_attestation_id"],
        "added": [deepcopy(after_map[key]) for key in added_keys],
        "removed": [deepcopy(before_map[key]) for key in removed_keys],
        "unchanged": [deepcopy(after_map[key]) for key in unchanged_keys],
        "non_authoritative": True,
    }


def normalize_structural_delta(
    provider_delta: dict,
    before_snapshot_ref: dict,
    after_snapshot_ref: dict,
    request: dict,
    *,
    before_binding_attestation: dict | None = None,
    after_binding_attestation: dict | None = None,
) -> dict:
    """Normalize an explicit provider ref-to-ref diff into FDI StructuralDelta.

    Both ends must be proven against the live provider index. Merely carrying
    before/after revision metadata is not sufficient for replay-safe source
    pinning.
    """
    before = validate_snapshot_ref(before_snapshot_ref)
    after = validate_snapshot_ref(after_snapshot_ref)
    before_attestation = _validate_binding_attestation(before, before_binding_attestation)
    after_attestation = _validate_binding_attestation(after, after_binding_attestation)
    if before["snapshot_id"] == after["snapshot_id"]:
        _fail("StructuralDelta requires distinct before/after snapshots")
    if before["provider"] != after["provider"] or before["adapter_version"] != after["adapter_version"]:
        _fail("StructuralDelta snapshots must use the same provider and adapter revision")
    if not isinstance(request, dict) or not request.get("query_id"):
        _fail("StructuralDiffQuery query_id is required")
    repo = request.get("repository")
    before_revs = {x["repository"]: x["revision"] for x in before["source_snapshots"]}
    after_revs = {x["repository"]: x["revision"] for x in after["source_snapshots"]}
    if not repo or repo not in before_revs or repo not in after_revs:
        _fail("StructuralDiffQuery repository must be pinned by both snapshots")
    if before_revs[repo] == after_revs[repo]:
        _fail("StructuralDiffQuery before/after revisions must differ")
    allowed = request.get("allowed_relation_types")
    if not isinstance(allowed, list) or not allowed:
        _fail("StructuralDiffQuery allowed_relation_types must be non-empty")
    unsupported = set(allowed) - SUPPORTED_RELATION_TYPES
    if unsupported:
        _fail(f"unsupported relation types: {sorted(unsupported)}")
    max_edges = request.get("max_edges")
    max_result_bytes = request.get("max_result_bytes")
    if not isinstance(max_edges, int) or isinstance(max_edges, bool) or max_edges <= 0:
        _fail("StructuralDiffQuery max_edges must be positive")
    if not isinstance(max_result_bytes, int) or isinstance(max_result_bytes, bool) or max_result_bytes <= 0:
        _fail("StructuralDiffQuery max_result_bytes must be positive")
    if not isinstance(provider_delta, dict):
        _fail("provider diff mapper must return an object")

    source_scope = set(before_revs) | set(after_revs)

    def normalize_records(records, snapshot, expected_snapshot_id):
        if not isinstance(records, list):
            _fail("provider diff added/removed/unchanged must be lists")
        result = []
        for record in records:
            edge = _canonical_edge(record)
            if edge["relation_type"] not in set(allowed):
                _fail("provider diff relation outside allowlist")
            if {edge["from"]["repository_id"], edge["to"]["repository_id"]} - source_scope:
                _fail("provider diff observation endpoint is outside pinned snapshot scope")
            result.append(
                {
                    "observation_id": _observation_id(expected_snapshot_id, edge),
                    "structural_snapshot_id": expected_snapshot_id,
                    **edge,
                    "provider": {
                        "name": snapshot["provider"]["name"],
                        "version": snapshot["provider"]["version"],
                        "adapter_version": snapshot["adapter_version"],
                        "provider_observation_id": record.get("provider_observation_id"),
                    },
                    "observed_at": snapshot["created_at"],
                    "non_authoritative": True,
                }
            )
        return sorted(result, key=lambda x: repr(_edge_signature(x)))

    added = normalize_records(provider_delta.get("added"), after, after["snapshot_id"])
    removed = normalize_records(provider_delta.get("removed"), before, before["snapshot_id"])
    unchanged = normalize_records(provider_delta.get("unchanged"), after, after["snapshot_id"])
    if len(added) + len(removed) + len(unchanged) > max_edges:
        _fail("normalized StructuralDelta exceeds max_edges budget")
    result = {
        "query_id": request["query_id"],
        "before_snapshot_id": before["snapshot_id"],
        "after_snapshot_id": after["snapshot_id"],
        "before_binding_attestation_id": before_attestation["attestation_id"],
        "after_binding_attestation_id": after_attestation["attestation_id"],
        "repository": repo,
        "added": added,
        "removed": removed,
        "unchanged": unchanged,
        "non_authoritative": True,
    }
    if len(json.dumps(result, sort_keys=True).encode("utf-8")) > max_result_bytes:
        _fail("normalized StructuralDelta exceeds max_result_bytes budget")
    return result
