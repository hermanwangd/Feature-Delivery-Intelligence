import hashlib
import json
from pathlib import Path

import pytest

from runtime.dev204_validation import (
    ValidationError,
    build_execution_packet,
    evaluate_dev204_gate,
    validate_execution_record,
    validate_plan,
)


ROOT = Path(__file__).resolve().parents[1]
PLAN = ROOT / '06-validation' / 'skill-behavior' / 'VALIDATION-PLAN-v0.4.6.2.json'


def _sha(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def _record(*, arm: str, context_id: str, reviewer_context_id: str, scenario_sha: str, loaded: bool, overall: str):
    return {
        'schema_version': '0.1',
        'release': 'fdi-mvp-v0.4.6.2',
        'scenario_id': 'DEV204-RD-01',
        'target': 'repo-discovery',
        'arm': arm,
        'fresh_context': True,
        'context_id': context_id,
        'reviewer_context_id': reviewer_context_id,
        'scenario_sha256': scenario_sha,
        'target_skill_loaded': loaded,
        'ground_truth_mounted': False,
        'agent_output_ref': f'evidence/{arm.lower()}-output.md',
        'review_ref': f'evidence/{arm.lower()}-review.json',
        'scores': {
            'authority': 'PASS',
            'decision': overall,
            'physical_shape': 'PASS',
            'provenance': 'PASS',
            'lifecycle': 'PASS',
            'reentry': 'PASS',
        },
        'overall': overall,
    }


def test_validation_plan_preserves_original_ten_and_adds_option_b_system_behavior():
    plan = json.loads(PLAN.read_text())
    validate_plan(plan)
    targets = [s['skill_or_behavior'] for s in plan['scenarios']]
    assert targets[:10] == [
        'PA-Codebase-Inventory',
        'PA-Historical-Delivery',
        'feature-intent-analysis',
        'repo-discovery',
        'changesurface-investigation',
        'dependency-closure',
        'closure-review',
        'ft-t1-intention',
        'ft-t2-delivery-spec',
        'product-team-onboarding-leader',
    ]
    assert targets[10] == 'product-knowledge-feature-discovery-closed-loop'
    assert plan['claim_boundary'] == 'EXECUTION_READY_NOT_BEHAVIORALLY_VALIDATED'
    assert plan['execution_requirements']['independent_fresh_contexts'] is True
    assert plan['execution_requirements']['same_frozen_scenario_per_red_green_pair'] is True
    assert plan['execution_requirements']['independent_review_required'] is True


def test_build_execution_packet_freezes_same_prompt_and_sha_for_red_green(tmp_path):
    prompt = 'Feature X may affect checkout and ledger. Determine candidate repositories.'
    red = build_execution_packet(
        release='fdi-mvp-v0.4.6.2', scenario_id='DEV204-RD-01', target='repo-discovery',
        arm='RED', prompt=prompt, output_dir=tmp_path,
    )
    green = build_execution_packet(
        release='fdi-mvp-v0.4.6.2', scenario_id='DEV204-RD-01', target='repo-discovery',
        arm='GREEN', prompt=prompt, output_dir=tmp_path,
    )
    assert red['scenario_sha256'] == green['scenario_sha256'] == _sha(prompt)
    assert red['target_skill_loaded'] is False
    assert green['target_skill_loaded'] is True
    assert red['ground_truth_mounted'] is False
    assert green['ground_truth_mounted'] is False


def test_execution_record_rejects_non_fresh_or_ground_truth_or_wrong_skill_loading():
    sha = _sha('same')
    red = _record(arm='RED', context_id='ctx-r', reviewer_context_id='rev-r', scenario_sha=sha, loaded=False, overall='FAIL')
    validate_execution_record(red)

    bad = dict(red, fresh_context=False)
    with pytest.raises(ValidationError):
        validate_execution_record(bad)

    bad = dict(red, ground_truth_mounted=True)
    with pytest.raises(ValidationError):
        validate_execution_record(bad)

    bad = dict(red, target_skill_loaded=True)
    with pytest.raises(ValidationError):
        validate_execution_record(bad)


def test_gate_requires_meaningful_red_failure_then_green_pass_in_distinct_contexts():
    sha = _sha('same')
    red = _record(arm='RED', context_id='ctx-r', reviewer_context_id='rev-r', scenario_sha=sha, loaded=False, overall='FAIL')
    green = _record(arm='GREEN', context_id='ctx-g', reviewer_context_id='rev-g', scenario_sha=sha, loaded=True, overall='PASS')
    assert evaluate_dev204_gate(red, green)['status'] == 'GREEN_PASS'

    with pytest.raises(ValidationError):
        evaluate_dev204_gate(red, dict(green, context_id='ctx-r'))
    with pytest.raises(ValidationError):
        evaluate_dev204_gate(red, dict(green, reviewer_context_id='rev-r'))
    with pytest.raises(ValidationError):
        evaluate_dev204_gate(red, dict(green, scenario_sha256=_sha('changed')))


def test_gate_does_not_validate_skill_when_red_has_no_failure():
    sha = _sha('same')
    red = _record(arm='RED', context_id='ctx-r', reviewer_context_id='rev-r', scenario_sha=sha, loaded=False, overall='PASS')
    green = _record(arm='GREEN', context_id='ctx-g', reviewer_context_id='rev-g', scenario_sha=sha, loaded=True, overall='PASS')
    result = evaluate_dev204_gate(red, green)
    assert result['status'] == 'RED_NO_SKILL_GAP_OBSERVED'
    assert result['behaviorally_validated'] is False


def test_option_b_closed_loop_behavior_cannot_be_declared_green_from_product_knowledge_only():
    from runtime.dev204_validation import evaluate_closed_loop_behavior

    result = evaluate_closed_loop_behavior({
        'semantics_used': True,
        'realization_used': True,
        'delivery_prior_used': True,
        'candidate_repo_set_produced': True,
        'current_feature_evidence_refs': [],
        'confirmed_surface_claims': ['repo-a:path-x'],
        'spec_ready': True,
    })
    assert result['status'] == 'FAIL'
    assert 'CURRENT_EVIDENCE_REQUIRED' in result['violations']
    assert 'FALSE_SPEC_READY' in result['violations']


def test_execution_record_schema_rejects_ground_truth_and_wrong_red_skill_loading():
    from jsonschema import Draft202012Validator
    schema = json.loads((ROOT / '06-validation' / 'skill-behavior' / 'execution-record.schema.json').read_text())
    sha = _sha('same')
    red = _record(arm='RED', context_id='ctx-r', reviewer_context_id='rev-r', scenario_sha=sha, loaded=False, overall='FAIL')
    assert list(Draft202012Validator(schema).iter_errors(red)) == []
    bad = dict(red, ground_truth_mounted=True)
    assert list(Draft202012Validator(schema).iter_errors(bad))
    bad = dict(red, target_skill_loaded=True)
    assert list(Draft202012Validator(schema).iter_errors(bad))


def test_evaluate_dev204_pair_cli_emits_green_pass(tmp_path):
    import subprocess, sys
    sha = _sha('same')
    red = _record(arm='RED', context_id='ctx-r', reviewer_context_id='rev-r', scenario_sha=sha, loaded=False, overall='FAIL')
    green = _record(arm='GREEN', context_id='ctx-g', reviewer_context_id='rev-g', scenario_sha=sha, loaded=True, overall='PASS')
    red_path = tmp_path / 'red.json'; red_path.write_text(json.dumps(red))
    green_path = tmp_path / 'green.json'; green_path.write_text(json.dumps(green))
    script = ROOT / 'scripts' / 'evaluate_dev204_pair.py'
    proc = subprocess.run([
        sys.executable, str(script), '--red', str(red_path), '--green', str(green_path)
    ], check=True, capture_output=True, text=True, cwd=ROOT)
    result = json.loads(proc.stdout)
    assert result['status'] == 'GREEN_PASS'
    assert result['behaviorally_validated'] is True
