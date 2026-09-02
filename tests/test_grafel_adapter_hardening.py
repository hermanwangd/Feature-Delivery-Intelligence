import pytest

from runtime.grafel_adapter import GrafelAdapter, GrafelAdapterError
from runtime.code_intelligence_provider import CodeIntelligenceProvider


def snapshot(snapshot_id='struct:r1', revision='aaa111'):
    return {
        'snapshot_id': snapshot_id,
        'provider': {'name': 'GRAFEL', 'version': '0.1.x'},
        'adapter_version': 'fdi-grafel-adapter@0.2',
        'source_snapshots': [{'repository': 'repo:a', 'revision': revision}],
        'created_at': '2026-09-01T00:00:00Z',
    }


def query(query_id='sq:1'):
    return {
        'query_id': query_id,
        'snapshot_id': 'struct:r1',
        'scope': {'products': ['SPC'], 'repositories': ['repo:a']},
        'seed': {'type': 'COMPONENT', 'id': 'component:a'},
        'allowed_relation_types': ['HTTP_CALL'],
        'max_depth': 2,
        'max_nodes': 20,
        'max_edges': 30,
        'max_paths': 5,
        'max_result_bytes': 32768,
    }


class FakeTransport:
    def __init__(self, *, indexed_revision='aaa111'):
        self.calls = []
        self.indexed_revision = indexed_revision

    def invoke(self, tool_name, payload):
        self.calls.append((tool_name, payload))
        return {'tool': tool_name, 'payload': payload}


def mapper(raw, *, operation, snapshot_ref, structural_query):
    if operation in {'find', 'expand'}:
        return [{
            'from': {'type': 'COMPONENT', 'id': 'component:a', 'repository_id': 'repo:a'},
            'relation_type': 'HTTP_CALL',
            'to': {'type': 'COMPONENT', 'id': 'component:b', 'repository_id': 'repo:a'},
            'evidence_refs': ['repo:a@aaa111:a.py:10'],
        }]
    if operation == 'trace':
        return [{
            'from': {'type': 'COMPONENT', 'id': 'component:a', 'repository_id': 'repo:a'},
            'relation_type': 'HTTP_CALL',
            'to': {'type': 'COMPONENT', 'id': 'component:b', 'repository_id': 'repo:a'},
            'evidence_refs': ['repo:a@aaa111:a.py:10'],
            'path_id': 'path:1',
        }]
    if operation == 'diff':
        return {
            'added': [{
                'from': {'type': 'COMPONENT', 'id': 'component:a', 'repository_id': 'repo:a'},
                'relation_type': 'HTTP_CALL',
                'to': {'type': 'COMPONENT', 'id': 'component:c', 'repository_id': 'repo:a'},
                'evidence_refs': ['repo:a@bbb222:a.py:20'],
            }],
            'removed': [{
                'from': {'type': 'COMPONENT', 'id': 'component:a', 'repository_id': 'repo:a'},
                'relation_type': 'HTTP_CALL',
                'to': {'type': 'COMPONENT', 'id': 'component:b', 'repository_id': 'repo:a'},
                'evidence_refs': ['repo:a@aaa111:a.py:10'],
            }],
            'unchanged': [],
        }
    if operation == 'orient':
        return {'overview': True}
    raise AssertionError(operation)


def binding_state(snapshot_ref, *, revision_override=None, freshness='FROZEN_INDEXED'):
    return {
        'provider_scope_id': 'grafel-group:test',
        'provider_ref': snapshot_ref['snapshot_id'],
        'queryability': 'QUERYABLE',
        'freshness': freshness,
        'repositories': [
            {
                'repository': item['repository'],
                'provider_repository': 'repo-a',
                'indexed_revision': revision_override or item['revision'],
                'queryable': True,
                'head_revision': 'future-head',
            }
            for item in snapshot_ref['source_snapshots']
        ],
    }


def binding_attestor(snapshot_ref):
    return binding_state(snapshot_ref)


def test_adapter_implements_provider_contract_and_verifies_snapshot_before_live_query():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)
    assert isinstance(adapter, CodeIntelligenceProvider)
    result = adapter.find(query(), snapshot())
    assert transport.calls[0][0] == 'grafel_find'
    assert transport.calls[0][1]['group'] == 'grafel-group:test'
    assert transport.calls[0][1]['ref'] == 'struct:r1'
    assert result['binding_attestation_id'].startswith('sba:')


def test_adapter_fails_closed_when_attested_provider_revision_does_not_match_snapshot_revision():
    def bad_attestor(snapshot_ref):
        return binding_state(snapshot_ref, revision_override='future999')

    adapter = GrafelAdapter(FakeTransport(), response_mapper=mapper, binding_attestor=bad_attestor)
    with pytest.raises(GrafelAdapterError, match='snapshot binding'):
        adapter.find(query(), snapshot())


def test_trace_requires_path_provenance_to_enforce_max_paths():
    def no_path_mapper(raw, *, operation, snapshot_ref, structural_query):
        result = mapper(raw, operation=operation, snapshot_ref=snapshot_ref, structural_query=structural_query)
        if operation == 'trace':
            result[0].pop('path_id')
        return result
    adapter = GrafelAdapter(FakeTransport(), response_mapper=no_path_mapper, binding_attestor=binding_attestor)
    q = query('sq:trace'); q['target'] = {'type': 'COMPONENT', 'id': 'component:b'}
    with pytest.raises(GrafelAdapterError, match='path_id'):
        adapter.trace(q, snapshot())


def test_diff_derives_exact_refs_from_two_pinned_snapshots_and_returns_normalized_delta():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)
    before = snapshot('struct:before', 'aaa111')
    after = snapshot('struct:after', 'bbb222')
    result = adapter.diff({
        'query_id': 'sdq:1',
        'repository': 'repo:a',
        'allowed_relation_types': ['HTTP_CALL'],
        'max_edges': 20,
        'max_result_bytes': 32768,
    }, before, after)
    tool, payload = transport.calls[-1]
    assert tool == 'grafel_diff'
    assert payload == {
        'group': 'grafel-group:test',
        'repo': 'repo-a',
        'ref_a': 'struct:before',
        'ref_b': 'struct:after',
        'aspect': 'refs',
    }
    assert result['before_snapshot_id'] == 'struct:before'
    assert result['after_snapshot_id'] == 'struct:after'
    assert result['non_authoritative'] is True
    assert result['added'][0]['structural_snapshot_id'] == 'struct:after'
    assert result['removed'][0]['structural_snapshot_id'] == 'struct:before'


def test_diff_rejects_same_or_unpinned_snapshot_pair():
    adapter = GrafelAdapter(FakeTransport(), response_mapper=mapper, binding_attestor=binding_attestor)
    request = {'query_id': 'sdq:1', 'repository': 'repo:a', 'allowed_relation_types': ['HTTP_CALL'], 'max_edges': 20, 'max_result_bytes': 32768}
    with pytest.raises(GrafelAdapterError):
        adapter.diff(request, snapshot('same', 'aaa111'), snapshot('same', 'aaa111'))


def test_diff_verifies_both_queryable_snapshot_bindings_and_preserves_attestation_provenance():
    transport = FakeTransport()
    adapter = GrafelAdapter(transport, response_mapper=mapper, binding_attestor=binding_attestor)
    before = snapshot('struct:before-bound', 'aaa111')
    after = snapshot('struct:after-bound', 'bbb222')
    result = adapter.diff({
        'query_id': 'sdq:bound',
        'repository': 'repo:a',
        'allowed_relation_types': ['HTTP_CALL'],
        'max_edges': 20,
        'max_result_bytes': 32768,
    }, before, after)

    assert [tool for tool, _ in transport.calls] == ['grafel_diff']
    assert transport.calls[0][1]['ref_a'] == 'struct:before-bound'
    assert transport.calls[0][1]['ref_b'] == 'struct:after-bound'
    assert result['before_binding_attestation_id'].startswith('sba:')
    assert result['after_binding_attestation_id'].startswith('sba:')
    assert result['before_binding_attestation_id'] != result['after_binding_attestation_id']
