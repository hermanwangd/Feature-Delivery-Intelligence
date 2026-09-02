from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOC = ROOT / "01-layer2" / "PA-01-MINIMAL-PRODUCT-SEMANTICS-PROFILE-v0.1-approval-candidate.md"


def test_pa01_spec_uses_common_descriptor_and_rejects_legacy_shortcuts():
    text = DOC.read_text()
    required = [
        'asset_family: "PRODUCT"',
        'publication_state: "DRAFT|PUBLISHED|RETIRED"',
        'validity_state: "NOT_APPLICABLE|ACTIVE|STALE|SUPERSEDED"',
        "trust_profile:",
        "freshness_policy:",
        "Product → Repository` is not a PA-01 shortcut",
        "current feature-specific pinned Evidence",
    ]
    assert all(item in text for item in required)
    assert 'lifecycle: "DRAFT|PUBLISHED|ACTIVE|STALE|SUPERSEDED"' not in text
