from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HYPOTHESIS = ROOT / "00-product" / "MVP-HYPOTHESIS-FREEZE-v0.4.7.0.md"
ABLATION = ROOT / "06-validation" / "FDI-v0.4.7.0-ABLATION-PROTOCOL.md"


def test_v047_h01_h05_are_refrozen_before_f001_with_full_fdi_hypothesis():
    text = HYPOTHESIS.read_text()
    for gate in ["MVP-H01", "MVP-H02", "MVP-H03", "MVP-H04", "MVP-H05"]:
        assert gate in text
    assert text.count("Status: `FROZEN`") == 5
    assert "Feature Delivery Intelligence" in text
    assert "governed Product Intelligence" in text
    assert "bounded live Structural Intelligence" in text
    assert "current feature-specific pinned Evidence" in text
    assert "F001 MUST NOT execute until this v0.4.7.0 H01–H05 freeze is active" in text


def test_f001_has_four_exact_ablation_arms_and_primary_blind_holdout_remains_baseline_vs_full_fdi():
    text = ABLATION.read_text()
    required = [
        "A — Baseline",
        "B — Structural only",
        "C — Product Intelligence only",
        "D — Full FDI",
        "F002–F005",
        "A vs D",
    ]
    assert all(item in text for item in required)
    assert "Product Intelligence: NO" in text
    assert "Structural Intelligence: YES" in text


def test_v047_ablation_freezes_fair_controls_and_temporal_isolation():
    text = ABLATION.read_text()
    required = [
        "same frozen Feature signal",
        "same exact pre-feature source cutoff",
        "same model/configuration",
        "same execution/tool/time budget",
        "same evaluation rubric",
        "target Feature implementation",
        "target PR/commit",
        "post-cutoff Structural Intelligence",
        "future Product Asset",
        "future Registry",
    ]
    assert all(item in text for item in required)
    assert "MUST NOT" in text


def test_v047_authority_boundary_keeps_structural_and_product_intelligence_out_of_current_truth():
    text = HYPOTHESIS.read_text() + "\n" + ABLATION.read_text()
    for forbidden_shortcut in [
        "Product Intelligence cannot establish current `CONFIRMED`",
        "Structural Intelligence cannot establish current `CONFIRMED`",
        "current feature-specific pinned Evidence remains authoritative",
        "SPEC_READY",
    ]:
        assert forbidden_shortcut in text


def test_f001_decision_vocabulary_remains_continue_revise_stop():
    text = ABLATION.read_text()
    assert "CONTINUE | REVISE | STOP" in text
    assert "CONTINUE | REVISE | REJECT" not in text
