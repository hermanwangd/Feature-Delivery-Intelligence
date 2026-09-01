import copy
import pytest

from runtime.product_knowledge_maintenance import (
    MaintenanceError,
    create_semantic_draft,
    mark_product_knowledge_stale,
    onboarding_request_maintenance,
    publish_semantic_revision,
    supersede_semantic_revision,
)
from runtime.product_semantics import ContractError, resolve_layer1_product_semantics_ref


def semantic_candidate(revision=1):
    return {
        "fdi_asset_version": "0.1",
        "asset_id": "pa01:spc",
        "asset_family": "PRODUCT",
        "asset_type": "PA-01_MINIMAL_PRODUCT_SEMANTICS",
        "asset_revision": revision,
        "descriptor_ref": f"descriptor:pa01:spc@{revision}",
        "content_ref": f"content:pa01:spc@{revision}",
        "publication_state": "PUBLISHED",
        "validity_state": "ACTIVE",
        "owner": "SPC Product Owner",
        "maintenance_mode": "CURATED",
        "publication_policy": "HUMAN_APPROVAL",
        "scope": {
            "products": ["SPC"],
            "systems": [],
            "repositories": [],
            "environments": [],
        },
        "authority_dimensions": ["DURABLE_CONSTRAINT"],
        "trust_profile": {
            "provenance": "DIRECT",
            "review": "UNREVIEWED",
            "verification": "VERIFIED",
            "authorization": "NONE",
        },
        "as_of": f"catalog:spc@r{revision}",
        "source_refs": [f"catalog:spc@r{revision}"],
        "dependency_refs": [],
        "freshness_policy": {"mode": "SOURCE_CHANGE", "ttl": None},
        "supersedes": None,
        "invalidation_triggers": [
            {
                "trigger_type": "SCOPE_CHANGED",
                "source_scope": "capability:CLR",
                "effect": "SCOPED_RECORD",
            }
        ],
        "selection_metadata": {"terms": ["SPC", "control limit"], "applicability": ["product:SPC"]},
        "reviewed_by": [],
        "product": {"product_id": "SPC", "name": "SPC Platform"},
        "sub_products": [],
        "capabilities": [
            {
                "capability_id": "CLR",
                "parent_id": "SPC",
                "name": "Control Limit Resolution",
                "scope_statement": "Resolve applicable control limits.",
                "semantic_refs": ["domain:spc/chamber-match@12"],
            }
        ],
    }


def test_agent_semantic_proposal_is_forced_to_draft():
    draft = create_semantic_draft(
        semantic_candidate(), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    assert (draft["publication_state"], draft["validity_state"]) == ("DRAFT", "NOT_APPLICABLE")
    assert draft["publication_policy"] == "HUMAN_APPROVAL"
    assert draft["proposed_by"] == "agent:product-intelligence"
    assert draft["source_refs"] == ["catalog:spc@r1"]
    assert draft["trust_profile"]["review"] == "UNREVIEWED"
    assert draft["trust_profile"]["authorization"] == "NONE"


def test_agent_cannot_publish_pa01_semantics():
    draft = create_semantic_draft(
        semantic_candidate(), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    with pytest.raises(MaintenanceError, match="accountable publication authority"):
        publish_semantic_revision(
            draft,
            actor="agent:product-intelligence",
            authorized_publishers={"SPC Product Owner"},
        )


def test_draft_cannot_satisfy_normal_layer1_resolution():
    draft = create_semantic_draft(
        semantic_candidate(), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    with pytest.raises(ContractError, match=r"PUBLISHED \+ ACTIVE"):
        resolve_layer1_product_semantics_ref(draft)


def test_accountable_human_publication_creates_published_active_revision():
    draft = create_semantic_draft(
        semantic_candidate(), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    published = publish_semantic_revision(
        draft,
        actor="SPC Product Owner",
        authorized_publishers={"SPC Product Owner"},
    )
    assert (published["publication_state"], published["validity_state"]) == ("PUBLISHED", "ACTIVE")
    assert published["trust_profile"]["review"] == "REVIEWED"
    assert published["trust_profile"]["authorization"] == "EXPLICIT"
    assert "SPC Product Owner" in published["reviewed_by"]
    assert resolve_layer1_product_semantics_ref(published)["asset_revision"] == 1


def test_staleness_changes_only_lifecycle_and_invalidates_resolution():
    draft = create_semantic_draft(
        semantic_candidate(), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    published = publish_semantic_revision(
        draft, actor="SPC Product Owner", authorized_publishers={"SPC Product Owner"}
    )
    before_content = copy.deepcopy({k: v for k, v in published.items() if k not in {"validity_state", "lifecycle_events"}})
    stale = mark_product_knowledge_stale(published, trigger="SCOPE_CHANGED")
    after_content = {k: v for k, v in stale.items() if k not in {"validity_state", "lifecycle_events"}}
    assert stale["validity_state"] == "STALE"
    assert after_content == before_content
    with pytest.raises(ContractError, match=r"PUBLISHED \+ ACTIVE"):
        resolve_layer1_product_semantics_ref(stale)


def test_undeclared_invalidation_trigger_fails_closed():
    draft = create_semantic_draft(
        semantic_candidate(), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    published = publish_semantic_revision(
        draft, actor="SPC Product Owner", authorized_publishers={"SPC Product Owner"}
    )
    with pytest.raises(MaintenanceError, match="not declared"):
        mark_product_knowledge_stale(published, trigger="SOURCE_CHANGED")


def test_supersession_preserves_old_revision_and_activates_successor():
    current_draft = create_semantic_draft(
        semantic_candidate(1), proposer="agent:product-intelligence", source_snapshot_refs=["catalog:spc@r1"]
    )
    current = publish_semantic_revision(
        current_draft, actor="SPC Product Owner", authorized_publishers={"SPC Product Owner"}
    )
    replacement_candidate = semantic_candidate(2)
    replacement_candidate["capabilities"][0]["scope_statement"] = "Resolve applicable control limits including recipe context."
    replacement_draft = create_semantic_draft(
        replacement_candidate,
        proposer="agent:product-intelligence",
        source_snapshot_refs=["catalog:spc@r2"],
    )
    old, new = supersede_semantic_revision(
        current,
        replacement_draft,
        actor="SPC Product Owner",
        authorized_publishers={"SPC Product Owner"},
    )
    assert old["asset_revision"] == 1
    assert old["validity_state"] == "SUPERSEDED"
    assert new["asset_revision"] == 2
    assert new["validity_state"] == "ACTIVE"
    assert new["supersedes"] == {"asset_id": "pa01:spc", "asset_revision": 1}
    with pytest.raises(ContractError):
        resolve_layer1_product_semantics_ref(old)
    assert resolve_layer1_product_semantics_ref(new)["asset_revision"] == 2


def test_onboarding_only_requests_maintenance_and_has_no_publication_side_effect():
    request = onboarding_request_maintenance(
        {
            "gap_id": "gap:missing-pa01",
            "target_profile": "PA-01",
            "reason": "Required Product Semantics missing for capability CLR",
        },
        requested_by="Product Team Onboarding",
    )
    assert request["status"] == "REQUESTED"
    assert request["requested_by"] == "Product Team Onboarding"
    assert request["target_profile"] == "PA-01"
    assert request["may_publish"] is False
    assert "publication_state" not in request
