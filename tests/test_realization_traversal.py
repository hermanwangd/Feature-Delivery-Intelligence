import copy
import pytest

from runtime.realization_traversal import TraversalError, derive_repository_candidates


def node(node_id, node_type, scope="product:spc"):
    return {"id": node_id, "type": node_type, "product_scope": scope}


def rel(rel_id, src, relation_type, dst, *, publication="PUBLISHED", validity="ACTIVE", declared=True):
    return {
        "relation_id": rel_id,
        "from": src,
        "relation_type": relation_type,
        "to": dst,
        "publication_state": publication,
        "validity_state": validity,
        "declared_by_profile": declared,
    }


def policy(**overrides):
    p = {
        "allowed_relation_types": [
            "REALIZED_BY",
            "PROVIDES",
            "CONSUMED_BY",
            "IMPLEMENTED_IN",
            "CONTAINS",
            "DEPENDS_ON",
        ],
        "max_depth": 6,
        "max_edges_examined": 50,
        "max_paths_per_repository": 3,
        "allowed_product_scope": ["product:spc"],
        "lifecycle_required": "PUBLISHED_ACTIVE",
    }
    p.update(overrides)
    return p


def repository_ids(result):
    return [entry["repository_id"] for entry in result["repositories"]]


def diagnostic_codes(result):
    return [d["code"] for d in result["diagnostics"]]


def test_self_cycle_terminates_with_diagnostic():
    c = node("component:A", "COMPONENT")
    result = derive_repository_candidates([c], [rel("r1", c, "DEPENDS_ON", c)], policy())
    assert result["repositories"] == []
    assert "CYCLE" in diagnostic_codes(result)


def test_two_node_cycle_terminates_with_diagnostic():
    a = node("component:A", "COMPONENT")
    b = node("component:B", "COMPONENT")
    relations = [
        rel("r1", a, "DEPENDS_ON", b),
        rel("r2", b, "DEPENDS_ON", a),
    ]
    result = derive_repository_candidates([a], relations, policy())
    assert result["repositories"] == []
    assert "CYCLE" in diagnostic_codes(result)


def test_depth_budget_stops_expansion_and_marks_incomplete():
    cap = node("cap:A", "CAPABILITY")
    c1 = node("component:1", "COMPONENT")
    c2 = node("component:2", "COMPONENT")
    repo = node("repo:R", "REPOSITORY")
    relations = [
        rel("r1", cap, "REALIZED_BY", c1),
        rel("r2", c1, "DEPENDS_ON", c2),
        rel("r3", c2, "IMPLEMENTED_IN", repo),
    ]
    result = derive_repository_candidates([cap], relations, policy(max_depth=2))
    assert repository_ids(result) == []
    assert result["incomplete"] is True
    assert "MAX_DEPTH" in diagnostic_codes(result)


def test_edge_budget_stops_fanout_and_marks_incomplete():
    cap = node("cap:A", "CAPABILITY")
    relations = [
        rel(f"r{i}", cap, "REALIZED_BY", node(f"component:{i}", "COMPONENT"))
        for i in range(5)
    ]
    result = derive_repository_candidates([cap], relations, policy(max_edges_examined=2))
    assert result["edges_examined"] == 2
    assert result["incomplete"] is True
    assert "MAX_EDGES" in diagnostic_codes(result)


def test_repo_path_budget_preserves_bounded_provenance_and_truncation():
    cap = node("cap:A", "CAPABILITY")
    a = node("component:A", "COMPONENT")
    b = node("component:B", "COMPONENT")
    repo = node("repo:R", "REPOSITORY")
    relations = [
        rel("r1", cap, "REALIZED_BY", a),
        rel("r2", cap, "REALIZED_BY", b),
        rel("r3", a, "IMPLEMENTED_IN", repo),
        rel("r4", b, "IMPLEMENTED_IN", repo),
    ]
    result = derive_repository_candidates([cap], relations, policy(max_paths_per_repository=1))
    assert repository_ids(result) == ["repo:R"]
    assert len(result["repositories"][0]["paths"]) == 1
    assert result["repositories"][0]["paths_truncated"] is True
    assert "MAX_PATHS_PER_REPOSITORY" in diagnostic_codes(result)


def test_shared_repo_across_two_allowed_capabilities_preserves_both_paths():
    cap_a = node("cap:A", "CAPABILITY")
    cap_b = node("cap:B", "CAPABILITY")
    a = node("component:A", "COMPONENT")
    b = node("component:B", "COMPONENT")
    repo = node("repo:shared", "REPOSITORY")
    relations = [
        rel("r1", cap_a, "REALIZED_BY", a),
        rel("r2", cap_b, "REALIZED_BY", b),
        rel("r3", a, "IMPLEMENTED_IN", repo),
        rel("r4", b, "IMPLEMENTED_IN", repo),
    ]
    result = derive_repository_candidates([cap_b, cap_a], relations, policy())
    assert repository_ids(result) == ["repo:shared"]
    paths = result["repositories"][0]["paths"]
    assert len(paths) == 2
    assert {p["start_node_id"] for p in paths} == {"cap:A", "cap:B"}


def test_unauthorized_cross_product_scope_is_excluded():
    cap = node("cap:A", "CAPABILITY")
    other_component = node("component:APC", "COMPONENT", "product:apc")
    repo = node("repo:shared", "REPOSITORY", "product:apc")
    relations = [
        rel("r1", cap, "REALIZED_BY", other_component),
        rel("r2", other_component, "IMPLEMENTED_IN", repo),
    ]
    result = derive_repository_candidates([cap], relations, policy())
    assert repository_ids(result) == []
    assert "OUT_OF_SCOPE" in diagnostic_codes(result)


@pytest.mark.parametrize("validity", ["STALE", "SUPERSEDED"])
def test_ineligible_relation_lifecycle_is_excluded(validity):
    cap = node("cap:A", "CAPABILITY")
    component = node("component:A", "COMPONENT")
    repo = node("repo:R", "REPOSITORY")
    relations = [
        rel("r1", cap, "REALIZED_BY", component, validity=validity),
        rel("r2", component, "IMPLEMENTED_IN", repo),
    ]
    result = derive_repository_candidates([cap], relations, policy())
    assert repository_ids(result) == []
    assert "INELIGIBLE_LIFECYCLE" in diagnostic_codes(result)


def test_caller_injected_undeclared_relation_is_rejected():
    cap = node("cap:A", "CAPABILITY")
    component = node("component:A", "COMPONENT")
    with pytest.raises(TraversalError, match="profile-declared"):
        derive_repository_candidates(
            [cap], [rel("r1", cap, "REALIZED_BY", component, declared=False)], policy()
        )


def test_lifecycle_change_recomputes_view_without_stale_repo():
    cap = node("cap:A", "CAPABILITY")
    component = node("component:A", "COMPONENT")
    repo = node("repo:R", "REPOSITORY")
    relations = [
        rel("r1", cap, "REALIZED_BY", component),
        rel("r2", component, "IMPLEMENTED_IN", repo),
    ]
    active = derive_repository_candidates([cap], relations, policy())
    assert repository_ids(active) == ["repo:R"]
    changed = copy.deepcopy(relations)
    changed[1]["validity_state"] = "STALE"
    stale = derive_repository_candidates([cap], changed, policy())
    assert repository_ids(stale) == []


def test_output_order_is_deterministic_for_identical_semantics():
    cap = node("cap:A", "CAPABILITY")
    a = node("component:A", "COMPONENT")
    b = node("component:B", "COMPONENT")
    repo_a = node("repo:A", "REPOSITORY")
    repo_b = node("repo:B", "REPOSITORY")
    relations = [
        rel("z1", cap, "REALIZED_BY", b),
        rel("z2", b, "IMPLEMENTED_IN", repo_b),
        rel("a1", cap, "REALIZED_BY", a),
        rel("a2", a, "IMPLEMENTED_IN", repo_a),
    ]
    forward = derive_repository_candidates([cap], relations, policy())
    reverse = derive_repository_candidates([cap], list(reversed(relations)), policy())
    assert forward == reverse
    assert repository_ids(forward) == ["repo:A", "repo:B"]


def test_invalid_typed_edge_fails_closed():
    test = node("test:X", "TEST")
    cap = node("cap:A", "CAPABILITY")
    bad = rel("r1", test, "REALIZED_BY", cap)
    with pytest.raises(TraversalError, match="invalid typed realization edge"):
        derive_repository_candidates([test], [bad], policy())
