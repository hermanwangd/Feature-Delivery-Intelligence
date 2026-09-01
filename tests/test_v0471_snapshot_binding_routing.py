import pytest

from runtime.structural_intelligence import (
    StructuralIntelligenceError,
    validate_snapshot_binding,
)
from runtime.grafel_adapter import GrafelAdapter, GrafelAdapterError
from runtime.code_intelligence_provider import SnapshotBindingAttestor


def snapshot(snapshot_id='struct:cutoff', revision='aaa111'):
    return {
        'snapshot_id': snapshot_id,
        'provider': {'name': 'GRAFEL', 'version': '0.1.x'},
        'adapter_version': 'fdi-grafel-adapter@0.3',
        'source_snapshots': [{'repository': 'repo:a', 'revision': revision}],
        'created_at': '2026-09-01T00:00:00Z',
    }


def query(snapshot_id='struct:cutoff'):
    return {
        'query_id': 'sq:frozen',
        'snapshot_id': snapshot_id,
        'scope': {'products': ['SPC'], 'repositories': ['repo:a']},
        'seed': {'type': 'COMPONENT', 'id': 'component:a'},
        'allowed_relation_types': ['HTTP_CALL'],
        'max_depth': 2,
        'max_nodes': 20,
        'max_edges': 30,
        'max_paths': 5,
        'max_result_bytes': 32768,
    }


def provider_binding(*, revision='aaa111', provider_ref='fdi/f001-cutoff', freshness='FROZEN_INDEXED'):
    return {
        'provider_scope_id': 'grafel-group:spc-replay',
        'provider_ref': provider_ref,
        'queryability': 'QUERYABLE',
        'freshness': freshness,
        'repositories': [
            {
                'repository': 'repo:a',
                'provider_repository': 'repo-a',
                'indexed_revision': revision,
                'queryable': True,
                # A historical frozen ref may coexist with a newer HEAD.
                'head_revision': 'future999',
            }
        ],
    }


def test_binding_accepts_exact_queryable_historical_ref_even_when_head_has_advanced():
    attestation = validate_snapshot_binding(snapshot(), provider_binding())
    assert attestation['binding_state'] == 'VERIFIED'
    assert attestation['provider_route'] == {
        'scope_id': 'grafel-group:spc-replay',
        'ref': 'fdi/f001-cutoff',
    }
    assert attestation['freshness'] == 'FROZEN_INDEXED'
    assert attestation['repositories'][0]['indexed_revision'] == 'aaa111'
    assert attestation['repositories'][0]['head_revision'] == 'future999'


def test_binding_fails_closed_without_exact_queryable_route_or_revision_equivalence():
    base = provider_binding()
    bad_cases = []

    no_scope = dict(base)
    no_scope.pop('provider_scope_id')
    bad_cases.append(no_scope)

    not_queryable = dict(base)
    not_queryable['queryability'] = 'NOT_QUERYABLE'
    bad_cases.append(not_queryable)

    wrong_revision = provider_binding(revision='wrong999')
    bad_cases.append(wrong_revision)

    repo_not_queryable = provider_binding()
    repo_not_queryable['repositories'] = [dict(repo_not_queryable['repositories'][0], queryable=False)]
    bad_cases.append(repo_not_queryable)

    for state in bad_cases:
        with pytest.raises(StructuralIntelligenceError):
            validate_snapshot_binding(snapshot(), state)


class FakeTransport:
    def __init__(self):
        self.calls = []

    def invoke(self, tool_name, payload):
        self.calls.append((tool_name, payload))
        return {'tool': tool_name, 'payload': payload}


def mapper(raw, *, operation, snapshot_ref, structural_query):
    if operation in {'find', 'expand'}:
        return [{
            'from': {'type': 'COMPONENT', 'id': 'component:a', 'repository_id': 'repo:a'},
            'relation_type': 'HTTP_CALL',
            'to': {'type': 'COMPONENT', 'id': 'component:b', 'repository_id': 'repo:a'},
            'evidence_refs': [f"repo:a@{snapshot_ref['source_snapshots'][0]['revision']}:a.py:10"],
        }]
    if operation == 'trace':
        return [{
            'from': {'type': 'COMPONENT', 'id': 'component:a', 'repository_id': 'repo:a'},
            'relation_type': 'HTTP_CALL',
            'to': {'type': 'COMPONENT', 'id': 'component:b', 'repository_id': 'repo:a'},
            'evidence_refs': [f"repo:a@{snapshot_ref['source_snapshots'][0]['revision']}:a.py:10"],
            'path_id': 'path:1',
        }]
    if operation == 'diff':
        return {'added': [], 'removed': [], 'unchanged': []}
    if operation == 'orient':
        return {'overview': True}
    raise AssertionError(operation)


class BindingAttestor:
    def __init__(self, by_snapshot):
        self.by_snapshot = by_snapshot
        self.calls = []

    def __call__(self, snapshot_ref):
        self.calls.append(snapshot_ref['snapshot_id'])
        return self.by_snapshot[snapshot_ref['snapshot_id']]


def test_adapter_routes_query_through_the_exact_provider_scope_and_ref_that_were_attested():
    transport = FakeTransport()
    attestor = BindingAttestor({'struct:cutoff': provider_binding()})
    assert isinstance(attestor, SnapshotBindingAttestor)
    adapter = GrafelAdapter(
        transport,
        response_mapper=mapper,
        binding_attestor=attestor,
    )

    result = adapter.find(query(), snapshot())

    assert attestor.calls == ['struct:cutoff']
    assert [tool for tool, _ in transport.calls] == ['grafel_find']
    assert transport.calls[0][1]['group'] == 'grafel-group:spc-replay'
    assert transport.calls[0][1]['ref'] == 'fdi/f001-cutoff'
    assert result['binding_attestation_id'].startswith('sba:')


def test_adapter_diff_uses_two_exact_indexed_provider_refs_without_requiring_both_to_be_current():
    transport = FakeTransport()
    before = snapshot('struct:before', 'aaa111')
    after = snapshot('struct:after', 'bbb222')
    attestor = BindingAttestor({
        'struct:before': provider_binding(
            revision='aaa111',
            provider_ref='fdi/before',
            freshness='FROZEN_INDEXED',
        ),
        'struct:after': provider_binding(
            revision='bbb222',
            provider_ref='fdi/after',
            freshness='LIVE_CURRENT',
        ),
    })
    adapter = GrafelAdapter(
        transport,
        response_mapper=mapper,
        binding_attestor=attestor,
    )

    result = adapter.diff(
        {
            'query_id': 'sdq:refs',
            'repository': 'repo:a',
            'allowed_relation_types': ['HTTP_CALL'],
            'max_edges': 20,
            'max_result_bytes': 32768,
        },
        before,
        after,
    )

    assert attestor.calls == ['struct:before', 'struct:after']
    assert [tool for tool, _ in transport.calls] == ['grafel_diff']
    assert transport.calls[0][1] == {
        'group': 'grafel-group:spc-replay',
        'repo': 'repo-a',
        'ref_a': 'fdi/before',
        'ref_b': 'fdi/after',
        'aspect': 'refs',
    }
    assert result['before_binding_attestation_id'].startswith('sba:')
    assert result['after_binding_attestation_id'].startswith('sba:')


def test_adapter_requires_a_binding_attestor_instead_of_treating_provider_metadata_as_proof():
    with pytest.raises(GrafelAdapterError, match='binding_attestor'):
        GrafelAdapter(FakeTransport(), response_mapper=mapper)
