import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

from runtime.dev204_validation import (
    ValidationError,
    build_execution_packet,
    evaluate_dev204_gate,
    validate_execution_record,
)

ROOT = Path(__file__).resolve().parents[1]


def scorecard(overall):
    return {
        'authority': 'PASS',
        'decision': overall,
        'physical_shape': 'PASS',
        'provenance': 'PASS',
        'lifecycle': 'PASS',
        'reentry': 'PASS',
    }


def record(*, arm, kind, loaded, overall, context, reviewer):
    return {
        'schema_version': '0.2',
        'release': 'fdi-mvp-v0.4.7.1',
        'scenario_id': 'DEV204-FDI-SI-01',
        'target': 'structural-intelligence-feature-discovery-integration',
        'target_kind': kind,
        'arm': arm,
        'fresh_context': True,
        'context_id': context,
        'reviewer_context_id': reviewer,
        'scenario_sha256': 'a' * 64,
        'target_loaded': loaded,
        'ground_truth_mounted': False,
        'agent_output_ref': f'evidence/{arm.lower()}-output.md',
        'review_ref': f'evidence/{arm.lower()}-review.json',
        'scores': scorecard(overall),
        'overall': overall,
    }


def test_v0471_system_behavior_packet_uses_neutral_target_loaded_not_skill_field(tmp_path):
    packet = build_execution_packet(
        release='fdi-mvp-v0.4.7.1',
        scenario_id='DEV204-FDI-SI-01',
        target='structural-intelligence-feature-discovery-integration',
        target_kind='SYSTEM_BEHAVIOR',
        arm='GREEN',
        prompt='same frozen scenario',
        output_dir=tmp_path,
    )
    assert packet['schema_version'] == '0.2'
    assert packet['target_kind'] == 'SYSTEM_BEHAVIOR'
    assert packet['target_loaded'] is True
    assert 'target_skill_loaded' not in packet


def test_v0471_execution_record_schema_matches_release_and_system_behavior_semantics():
    schema_path = ROOT / '06-validation' / 'skill-behavior' / 'execution-record-v0.2.schema.json'
    schema = json.loads(schema_path.read_text())
    assert schema['properties']['release']['const'] == 'fdi-mvp-v0.4.7.1'
    green = record(arm='GREEN', kind='SYSTEM_BEHAVIOR', loaded=True, overall='PASS', context='ctx-g', reviewer='rev-g')
    assert list(Draft202012Validator(schema).iter_errors(green)) == []
    bad = dict(green, target_loaded=False)
    assert list(Draft202012Validator(schema).iter_errors(bad))


def test_v0471_gate_uses_generic_red_no_target_gap_for_system_behavior():
    red = record(arm='RED', kind='SYSTEM_BEHAVIOR', loaded=False, overall='PASS', context='ctx-r', reviewer='rev-r')
    green = record(arm='GREEN', kind='SYSTEM_BEHAVIOR', loaded=True, overall='PASS', context='ctx-g', reviewer='rev-g')
    result = evaluate_dev204_gate(red, green)
    assert result['status'] == 'RED_NO_TARGET_GAP_OBSERVED'
    assert result['behaviorally_validated'] is False


def test_v0471_rejects_skill_named_loading_field_for_system_behavior_record():
    rec = record(arm='GREEN', kind='SYSTEM_BEHAVIOR', loaded=True, overall='PASS', context='ctx-g', reviewer='rev-g')
    rec['target_skill_loaded'] = True
    with pytest.raises(ValidationError):
        validate_execution_record(rec)


def test_f001_v0471_freeze_declares_shared_identity_only_substrate_for_all_arms():
    text = (ROOT / '00-product' / 'MVP-HYPOTHESIS-FREEZE-v0.4.7.1.md').read_text()
    assert 'Shared Repository Identity Substrate' in text
    assert 'PA-03 CB-01' in text
    assert 'all four arms' in text.lower()
    assert 'must not include capability terms' in text.lower()
    assert 'B Structural only' in text


def test_f001_v0471_ablation_does_not_call_structural_arm_product_intelligence_free_without_qualification():
    text = (ROOT / '06-validation' / 'FDI-v0.4.7.1-ABLATION-PROTOCOL.md').read_text()
    assert 'identity-only substrate' in text.lower()
    assert 'PA-03 CB-01' in text
    assert 'semantic Product Intelligence: NO' in text
    assert 'structural Intelligence: YES' in text
