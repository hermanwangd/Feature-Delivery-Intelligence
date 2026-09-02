from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_required_overlay_modules_and_frozen_docs_exist():
    required = [
        ROOT / "00-product" / "MVP-HYPOTHESIS-FREEZE-v0.4.6.2.md",
        ROOT / "06-validation" / "OPTION-B-PAIRED-REPLAY-PROTOCOL-v0.1.md",
        ROOT / "runtime" / "product_semantics.py",
        ROOT / "runtime" / "feature_knowledge_plan.py",
        ROOT / "runtime" / "realization_traversal.py",
        ROOT / "runtime" / "product_knowledge_maintenance.py",
        ROOT / "runtime" / "verification_accounting.py",
    ]
    missing = [str(p.relative_to(ROOT)) for p in required if not p.exists()]
    assert missing == []
