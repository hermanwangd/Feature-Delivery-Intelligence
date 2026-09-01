from runtime.feature_knowledge_plan import compile_feature_knowledge_plan
from runtime.product_knowledge_maintenance import create_semantic_draft, publish_semantic_revision
from runtime.product_semantics import resolve_layer1_product_semantics_ref
from runtime.realization_traversal import derive_repository_candidates


def pa01_candidate():
    return {
        "fdi_asset_version": "0.1",
        "asset_id": "pa01:spc",
        "asset_family": "PRODUCT",
        "asset_type": "PA-01_MINIMAL_PRODUCT_SEMANTICS",
        "asset_revision": 1,
        "descriptor_ref": "descriptor:pa01:spc@1",
        "content_ref": "content:pa01:spc@1",
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
        "owner": "SPC Product Owner",
        "maintenance_mode": "CURATED",
        "publication_policy": "HUMAN_APPROVAL",
        "scope": {"products": ["SPC"], "systems": [], "repositories": [], "environments": []},
        "authority_dimensions": ["DURABLE_CONSTRAINT"],
        "trust_profile": {
            "provenance": "DIRECT",
            "review": "UNREVIEWED",
            "verification": "VERIFIED",
            "authorization": "NONE",
        },
        "as_of": "catalog:spc@r1",
        "source_refs": ["catalog:spc@r1"],
        "dependency_refs": [],
        "freshness_policy": {"mode": "SOURCE_CHANGE", "ttl": None},
        "supersedes": None,
        "invalidation_triggers": [
            {"trigger_type": "SCOPE_CHANGED", "source_scope": "capability:CLR", "effect": "SCOPED_RECORD"}
        ],
        "selection_metadata": {"terms": ["SPC", "control limit"], "applicability": ["product:SPC"]},
        "product": {"product_id": "SPC", "name": "SPC Platform"},
        "sub_products": [{"sub_product_id": "LIMITS", "parent_id": "SPC", "name": "Chart & Limit Management"}],
        "capabilities": [
            {
                "capability_id": "CLR",
                "parent_id": "LIMITS",
                "name": "Control Limit Resolution",
                "scope_statement": "Resolve applicable control limits for measurement context.",
                "semantic_refs": ["domain:spc/chamber-match@12"],
            }
        ],
    }


def root_skill():
    return {
        "skill_id": "ft-t2-delivery-spec",
        "skill_revision": "0.4.2",
        "context_requirement_templates": [
            {
                "template_id": "product-semantics-required",
                "knowledge_role": "SEMANTICS",
                "allowed_modes": ["REQUIRED"],
                "allowed_authority_dimensions": ["DURABLE_CONSTRAINT"],
                "selector_bounds": {"max_assets": 1},
                "minimum_trust": {
                    "review": "REVIEWED",
                    "verification": "VERIFIED",
                    "authorization": "EXPLICIT",
                },
                "freshness_requirement": "SOURCE_CHANGE",
                "may_promote_to_required": False,
            }
        ],
    }


def relation(rel_id, src, relation_type, dst):
    return {
        "relation_id": rel_id,
        "from": src,
        "relation_type": relation_type,
        "to": dst,
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
        "declared_by_profile": True,
    }


def test_product_semantics_to_realization_guides_repo_candidate_without_creating_current_truth():
    draft = create_semantic_draft(
        pa01_candidate(),
        proposer="agent:product-intelligence",
        source_snapshot_refs=["catalog:spc@r1"],
    )
    published = publish_semantic_revision(
        draft,
        actor="SPC Product Owner",
        authorized_publishers={"SPC Product Owner"},
    )
    semantic_ref = resolve_layer1_product_semantics_ref(published)

    plan = {
        "plan_id": "fkp:SPC-123",
        "revision": 1,
        "items": [
            {
                "template_id": "product-semantics-required",
                "knowledge_role": "SEMANTICS",
                "mode": "REQUIRED",
                "authority_dimension": "DURABLE_CONSTRAINT",
                "selector": {"max_assets": 1},
                "trust_requirements": {
                    "review": "REVIEWED",
                    "verification": "VERIFIED",
                    "authorization": "EXPLICIT",
                },
                "freshness_requirement": "SOURCE_CHANGE",
                "product_asset_ref": semantic_ref,
                "dependent_claims": ["intent:capability:CLR"],
            }
        ],
    }
    compiled = compile_feature_knowledge_plan(plan, root_skill())
    assert compiled[0]["product_asset_ref"] == semantic_ref

    cap = {"id": "capability:CLR", "type": "CAPABILITY", "product_scope": "product:spc"}
    component = {"id": "component:limit-service", "type": "COMPONENT", "product_scope": "product:spc"}
    repo = {"id": "repo:spc-limit-service", "type": "REPOSITORY", "product_scope": "product:spc"}
    result = derive_repository_candidates(
        [cap],
        [
            relation("realization:1", cap, "REALIZED_BY", component),
            relation("realization:2", component, "IMPLEMENTED_IN", repo),
        ],
        {
            "allowed_relation_types": ["REALIZED_BY", "IMPLEMENTED_IN"],
            "max_depth": 4,
            "max_edges_examined": 10,
            "max_paths_per_repository": 3,
            "allowed_product_scope": ["product:spc"],
            "lifecycle_required": "PUBLISHED_ACTIVE",
        },
    )

    assert result["repositories"][0]["repository_id"] == "repo:spc-limit-service"
    assert result["repositories"][0]["basis"] == "LAYER2_PA03"
    serialized = repr(result)
    assert "CONFIRMED" not in serialized
    assert "EXCLUDED" not in serialized
    assert "SPEC_READY" not in serialized
    assert "ChangeSurfaceSet" not in serialized
