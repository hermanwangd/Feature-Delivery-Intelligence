# HERM-220 v0.4.7.2 integration evidence

## Source identity

- Canonical repository: `https://github.com/hermanwangd/Feature-Delivery-Intelligence`
- Canonical continuation base: `e29cc31ec1f7480f624ffc33aa83fc9eb5db27a9` (`agent/mika/herm-213-phase1-package`, PR #4)
- Isolated integration branch: `agent/mika/herm-220-live-grafel-binding`
- Corrected integration implementation commit: `24b9e65c97e5db09d9f850231c1d6ea003fc3a89`
- Validated remediation commit: `d195f52ce8aba360d9398d9cd1456882f45a0187`
- Source bundle: `fdi-mvp-v0.4.7.2-multica-handoff-bundle.zip`
- Source bundle SHA-256: `7c35ea4872c74549efb50f1251ffa9af4eed6e24027f44f9055af769ca9517b0`
- Successor handoff SHA-256: `2d2cf4e3a72e29d492921303f74bd3de48d8061041bf86655203185a8a2cb441`
- Extracted source manifest: 285 entries, 0 missing, 0 size mismatches, 0 digest mismatches, 0 unlisted files

The HERM-213 branch is the required continuation base because `main` at `54db6e2879abd5ac8e7319efe8ef06a5b7ae5482` does not contain the Phase 1 runtime and HERM-213 PR #4 remains open. The integration PR is therefore stacked on PR #4 rather than duplicating or bypassing its contracts.

## Environment contract

- Platform: macOS arm64
- Python: `3.9.6`, pinned by `.python-version`
- `jsonschema[format]`: `4.25.1`, pinned by `requirements-dev.txt`
- `pytest`: `8.4.2`, pinned by `requirements-dev.txt`
- Fresh environment creation: `python3 -m venv ../herm-220-work/fresh-venv`
- Fresh dependency install: `../herm-220-work/fresh-venv/bin/python -m pip install --disable-pip-version-check -r requirements-dev.txt`

The fresh install completed successfully and reported Python `3.9.6`, jsonschema `4.25.1`, and pytest `8.4.2`.

## Pre-integration evidence

Executed at base commit `e29cc31ec1f7480f624ffc33aa83fc9eb5db27a9` before applying the overlay:

| Command | Result |
|---|---|
| `make bootstrap` | PASS |
| `make validate` | PASS — 19 passed, 0 failed, 0 skipped |
| `make score` | PASS — exit 0 |

No pre-existing canonical regression failure required diagnosis.

The immutable extracted overlay was also independently verified before integration:

| Command | Result |
|---|---|
| `PYTHONPATH=. PYTHONDONTWRITEBYTECODE=1 <venv-python> -m pytest -q --ignore=tests/test_release_guards.py` | PASS — 157 passed |
| `PYTHONPATH=. PYTHONDONTWRITEBYTECODE=1 <venv-python> -m pytest -q tests/test_release_guards.py` | PASS — 12 passed |

## Corrected integration behavior

- `GrafelSnapshotBindingAttestor` rejects empty orient results; absent or mismatched scope/ref; missing or false queryability; missing, true, or incomplete warming/indexing state; absent or mismatched group metadata identity; ambiguous mappings; and extra/missing metadata repositories.
- The concrete binding state records each FDI repository identity with its `provider_repository` Grafel slug. `validate_snapshot_binding` retains that mapping and includes it in the attestation digest.
- `GrafelAdapter` uses only the attested Grafel slug for `orient.repo_filter`, `find.repo_filter`, and `diff.repo`. `diff` rejects a mapping that changes between its two independently attested snapshots.
- Response mapping and normalized observations/deltas continue to expose FDI repository identities and remain non-authoritative.
- The deterministic package builder excludes `.venv`, caches, compiled files, and ZIP inputs.

TDD defect reproduction: the initial focused suite failed 12 cases against the supplied implementation. After the corrections, the focused suite passed 17/17.

## Post-integration verification

Executed from the fresh environment against validated remediation commit `d195f52ce8aba360d9398d9cd1456882f45a0187`, which contains implementation commit `24b9e65c97e5db09d9f850231c1d6ea003fc3a89`:

| Command | Result |
|---|---|
| `make test-all PYTHON=../herm-220-work/fresh-venv/bin/python` | PASS |
| canonical `unittest` stage within `make test-all` | 19 passed, 0 failed, 0 skipped |
| functional `pytest` stage within `make test-all` | 193 passed, 0 failed, 0 skipped |
| release-guard `pytest` stage within `make test-all` | 13 passed, 0 failed, 0 skipped |
| `make score PYTHON=../herm-220-work/fresh-venv/bin/python` | PASS — exit 0 |
| `git diff --check e29cc31ec1f7480f624ffc33aa83fc9eb5db27a9..d195f52ce8aba360d9398d9cd1456882f45a0187` | PASS — exit 0, 0 findings |

The remediation replaces eight trailing-space Markdown hard breaks with explicit `<br>` markers, preserving rendered line separation while making the complete continuation-base-to-remediation range whitespace-clean. It does not change runtime behavior, governing semantics, or authority boundaries.

## Live binding gate

Status: `FAILED_CLOSED_AT_ATTESTATION`.

Herman Wang authorized the HERM-222-derived route on 2026-09-02. The execution
used PR #5 head `422b921aae9e06667ed41da5dfb88b733405b9ac`, Python `3.9.6`, provider
runtime `v0.3.0 (commit b037c3f, built 2026-08-21T18:26:14Z)`, and adapter
revision `fdi-grafel-adapter@0.4`.

Before attestation, the session-level `grafel_index_status` tool was called with
`group="herm-220-live"` and `repo="trading-pipeline"`. Its complete result was:

```json
{"repos":[{"repo":"/Users/herman_mbp2023/multica_workspaces_desktop-api.multica.ai/herman-lab-74d8e0781f12/herm-222-5f1f7030d3b5/worktree/trading-pipeline","group":"herm-220-live","state":"current","dirty":false,"indexed_commit_short":"c30646e5838d","at_head":true}],"any_indexing":false,"parsing":0,"busy":false,"concurrency":{"indexing":0,"queued":0,"cap":2},"elapsed_ms":62}
```

The same provider runtime also returned the following foreground read-back from
the pinned Product checkout before the attestor invocation:

```text
$ grafel status --json
{"status":"ok","engine_pid":78145,"heartbeat_at":"2026-09-02T02:41:35.096135Z","version":"v0.3.0 (commit b037c3f, built 2026-08-21T18:26:14Z)","repo_path":"/Users/herman_mbp2023/multica_workspaces_desktop-api.multica.ai/herman-lab-74d8e0781f12/herm-222-5f1f7030d3b5/worktree/trading-pipeline","indexed_commit":"c30646e5838d","entities":9615,"relationships":79027,"graph_fb_mtime":1788316067924061237,"indexing":false,"engine_started_at":"0001-01-01T00:00:00Z","engine_busy_started_at":"0001-01-01T00:00:00Z"}
```

Thus the provider read-back remained current, clean, and not indexing at
`c30646e5838d`, a 12-hex prefix of the full canonical revision
`c30646e5838d42921061a0924c1328c46fd280ff`. The confirmed indexed/provider ref
supplied to the attestor was `fdi/herm-220-live`; the full canonical revision
vector, route, and repository mapping supplied to the attestor were:

```json
{
  "StructuralSnapshotRef": {
    "adapter_version": "fdi-grafel-adapter@0.4",
    "created_at": "2026-09-02T02:43:03.636305Z",
    "provider": {
      "name": "grafel",
      "version": "v0.3.0 (commit b037c3f, built 2026-08-21T18:26:14Z)"
    },
    "snapshot_id": "struct:herm-220-live:c30646e5838d42921061a0924c1328c46fd280ff",
    "source_snapshots": [
      {
        "repository": "https://github.com/hermanwangd/trading-pipeline",
        "revision": "c30646e5838d42921061a0924c1328c46fd280ff"
      }
    ]
  },
  "provider_scope_id": "herm-220-live",
  "provider_ref": "fdi/herm-220-live",
  "repository_map": {
    "https://github.com/hermanwangd/trading-pipeline": "trading-pipeline"
  }
}
```

The exact execution command was:

```text
PYTHONPATH=<PR-5-worktree> python3 ./h220_live_gate_attempt.py
```

It exited `2`. The complete execution result was:

```json
{
  "StructuralSnapshotRef": {
    "adapter_version": "fdi-grafel-adapter@0.4",
    "created_at": "2026-09-02T02:43:03.636305Z",
    "provider": {
      "name": "grafel",
      "version": "v0.3.0 (commit b037c3f, built 2026-08-21T18:26:14Z)"
    },
    "snapshot_id": "struct:herm-220-live:c30646e5838d42921061a0924c1328c46fd280ff",
    "source_snapshots": [
      {
        "repository": "https://github.com/hermanwangd/trading-pipeline",
        "revision": "c30646e5838d42921061a0924c1328c46fd280ff"
      }
    ]
  },
  "adapter_revision": "fdi-grafel-adapter@0.4",
  "attestation": null,
  "attestor_result": {
    "error": "GrafelSnapshotBindingAttestor requires provider.name=GRAFEL",
    "error_type": "GrafelBindingAttestorError",
    "status": "FAILED"
  },
  "bounded_query": {
    "reason": "stop condition: attestation check failed",
    "result": null,
    "status": "NOT_EXECUTED",
    "timestamp": null
  },
  "execution_timestamp": "2026-09-02T02:43:03.636305Z",
  "group_metadata_invocations": [],
  "provider_ref": "fdi/herm-220-live",
  "provider_scope_id": "herm-220-live",
  "repository_map": {
    "https://github.com/hermanwangd/trading-pipeline": "trading-pipeline"
  },
  "runtime_revision": "422b921aae9e06667ed41da5dfb88b733405b9ac",
  "transport_invocations": []
}
```

The immutable confirmed input uses provider name `grafel`; the integrated
attestor requires the exact provider identity `GRAFEL`. This check failed before
the provider transport or group-metadata client was invoked, so no attestation
payload was produced (`attestation: null`). The authorized stop condition was
applied immediately: the input was not changed or retried, and the required
bounded `GrafelAdapter` query was not executed. Consequently there is no query
timestamp or bounded-query result to report. This is a fail-closed result, not a
successful live binding and not evidence for any authority or proof upgrade.

## Claim and authority boundary

- Canonical/local source-tree integration: `PASS` on the isolated branch.
- Live Grafel binding: `FAILED_CLOSED_AT_ATTESTATION`.
- Real Product binding: `NOT_ESTABLISHED`.
- DEV-204 fresh-context behavior: `NOT_EXECUTED`.
- F001: `NOT_EXECUTED`; F002–F005: `NOT_POPULATED`.
- Empirical MVP proof: `NOT_ESTABLISHED`.
- Canonical runtime release: `NOT_ESTABLISHED`.
- `Execution-verified`: `NOT_CLAIMED`.

The change does not add a Layer 1 transition, Product Asset family, candidate basis, FT-T2 Skill, canonical gate, or current-truth authority. Structural Intelligence remains candidate/investigation support and cannot establish `CONFIRMED`, `EXCLUDED`, `ChangeSurfaceSet`, `SPEC_READY`, Product Asset publication, or lifecycle transitions.
