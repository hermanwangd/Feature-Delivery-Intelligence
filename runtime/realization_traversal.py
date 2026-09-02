"""Bounded Product Realization traversal conformance runtime.

This produces repository *candidates with provenance*, never current-feature
Change Surface truth.
"""

from __future__ import annotations

from collections import defaultdict, deque


class TraversalError(ValueError):
    """Raised for fail-closed realization contract violations."""


_TYPED_EDGES = {
    "REALIZED_BY": {("CAPABILITY", "COMPONENT")},
    "PROVIDES": {("COMPONENT", "INTERFACE")},
    "CONSUMED_BY": {("INTERFACE", "COMPONENT")},
    "IMPLEMENTED_IN": {("COMPONENT", "REPOSITORY"), ("INTERFACE", "REPOSITORY")},
    "CONTAINS": {("REPOSITORY", "MODULE")},
    "DEPENDS_ON": {("COMPONENT", "COMPONENT")},
}


def _validate_policy(policy: dict) -> None:
    for key in ("max_depth", "max_edges_examined", "max_paths_per_repository"):
        value = policy.get(key)
        if not isinstance(value, int) or value <= 0:
            raise TraversalError(f"{key} must be a positive integer")
    if not policy.get("allowed_relation_types"):
        raise TraversalError("allowed_relation_types must be non-empty")
    if not policy.get("allowed_product_scope"):
        raise TraversalError("allowed_product_scope must be non-empty")
    if policy.get("lifecycle_required") != "PUBLISHED_ACTIVE":
        raise TraversalError("overlay requires lifecycle_required=PUBLISHED_ACTIVE")


def _validate_relation(relation: dict) -> None:
    if relation.get("declared_by_profile") is not True:
        raise TraversalError("realization relation must be profile-declared; caller injection is prohibited")
    relation_type = relation.get("relation_type")
    src = relation.get("from", {})
    dst = relation.get("to", {})
    pair = (src.get("type"), dst.get("type"))
    if relation_type not in _TYPED_EDGES or pair not in _TYPED_EDGES[relation_type]:
        raise TraversalError(
            f"invalid typed realization edge: {pair[0]} --{relation_type}--> {pair[1]}"
        )
    if not relation.get("relation_id") or not src.get("id") or not dst.get("id"):
        raise TraversalError("relation and node ids must be non-empty")


def derive_repository_candidates(start_nodes: list[dict], relations: list[dict], policy: dict) -> dict:
    """Derive bounded repository candidates from exact active realization relations.

    The result deliberately contains no CONFIRMED/EXCLUDED/SPEC_READY fields.
    """
    _validate_policy(policy)
    allowed_types = set(policy["allowed_relation_types"])
    allowed_scope = set(policy["allowed_product_scope"])

    adjacency = defaultdict(list)
    for relation in relations:
        _validate_relation(relation)
        adjacency[relation["from"]["id"]].append(relation)
    for outgoing in adjacency.values():
        outgoing.sort(key=lambda r: r["relation_id"])

    diagnostics = []
    diagnostic_keys = set()

    def add_diag(code: str, **details):
        key = (code, tuple(sorted(details.items())))
        if key not in diagnostic_keys:
            diagnostic_keys.add(key)
            diagnostics.append({"code": code, **details})

    repository_paths = defaultdict(list)
    repository_truncated = defaultdict(bool)
    edges_examined = 0
    incomplete = False
    budget_exhausted = False

    queue = deque()
    for start in sorted(start_nodes, key=lambda n: n.get("id", "")):
        if not start.get("id") or not start.get("type"):
            raise TraversalError("start node id/type must be non-empty")
        if start.get("product_scope") not in allowed_scope:
            add_diag("OUT_OF_SCOPE", node_id=start.get("id"), scope=start.get("product_scope"))
            continue
        queue.append(
            {
                "start": start,
                "node": start,
                "depth": 0,
                "relation_ids": [],
                "node_ids": [start["id"]],
                "seen": frozenset({start["id"]}),
            }
        )

    while queue and not budget_exhausted:
        state = queue.popleft()
        node = state["node"]

        if node.get("type") == "REPOSITORY":
            repo_id = node["id"]
            path = {
                "start_node_id": state["start"]["id"],
                "relation_ids": list(state["relation_ids"]),
                "node_ids": list(state["node_ids"]),
            }
            existing = repository_paths[repo_id]
            if path not in existing:
                if len(existing) < policy["max_paths_per_repository"]:
                    existing.append(path)
                else:
                    repository_truncated[repo_id] = True
                    incomplete = True
                    add_diag("MAX_PATHS_PER_REPOSITORY", repository_id=repo_id)
            continue

        outgoing = adjacency.get(node["id"], [])
        if outgoing and state["depth"] >= policy["max_depth"]:
            incomplete = True
            add_diag("MAX_DEPTH", node_id=node["id"], max_depth=policy["max_depth"])
            continue

        for relation in outgoing:
            if edges_examined >= policy["max_edges_examined"]:
                incomplete = True
                budget_exhausted = True
                add_diag("MAX_EDGES", max_edges_examined=policy["max_edges_examined"])
                break
            edges_examined += 1

            relation_type = relation["relation_type"]
            if relation_type not in allowed_types:
                add_diag("RELATION_NOT_ALLOWED", relation_id=relation["relation_id"], relation_type=relation_type)
                continue

            if (
                relation.get("publication_state") != "PUBLISHED"
                or relation.get("validity_state") != "ACTIVE"
            ):
                add_diag(
                    "INELIGIBLE_LIFECYCLE",
                    relation_id=relation["relation_id"],
                    publication_state=relation.get("publication_state"),
                    validity_state=relation.get("validity_state"),
                )
                continue

            src = relation["from"]
            dst = relation["to"]
            if src.get("product_scope") not in allowed_scope or dst.get("product_scope") not in allowed_scope:
                add_diag(
                    "OUT_OF_SCOPE",
                    relation_id=relation["relation_id"],
                    from_scope=src.get("product_scope"),
                    to_scope=dst.get("product_scope"),
                )
                continue

            next_id = dst["id"]
            if next_id in state["seen"]:
                add_diag("CYCLE", relation_id=relation["relation_id"], node_id=next_id)
                continue

            queue.append(
                {
                    "start": state["start"],
                    "node": dst,
                    "depth": state["depth"] + 1,
                    "relation_ids": [*state["relation_ids"], relation["relation_id"]],
                    "node_ids": [*state["node_ids"], next_id],
                    "seen": state["seen"] | {next_id},
                }
            )

    repositories = []
    for repo_id in sorted(repository_paths):
        paths = sorted(
            repository_paths[repo_id],
            key=lambda p: (p["relation_ids"], p["start_node_id"], p["node_ids"]),
        )
        repositories.append(
            {
                "repository_id": repo_id,
                "paths": paths,
                "paths_truncated": repository_truncated[repo_id],
                "basis": "LAYER2_PA03",
            }
        )

    diagnostics.sort(key=lambda d: (d["code"], repr(sorted(d.items()))))
    return {
        "repositories": repositories,
        "diagnostics": diagnostics,
        "incomplete": incomplete,
        "edges_examined": edges_examined,
    }
