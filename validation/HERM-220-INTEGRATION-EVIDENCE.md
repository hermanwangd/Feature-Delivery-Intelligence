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

Status: `NOT_EXECUTED`.

Exact missing authorized capabilities:

- no Grafel MCP/dashboard tools are available to this run;
- no `grafel` CLI is installed;
- no Grafel endpoint/configuration is supplied;
- the project resources provide only the FDI coordination repository, not an authorized real Product repository set and immutable revision vector; and
- no authorized Product-to-Grafel `group/ref` plus repository-slug route map is supplied.

No synthetic live result was created. Consequently there is no real `StructuralSnapshotRef`, live attestation payload, bounded provider query, query timestamp, or provider runtime version to retain.

## Claim and authority boundary

- Canonical/local source-tree integration: `PASS` on the isolated branch.
- Live Grafel binding: `NOT_EXECUTED`.
- Real Product binding: `NOT_POPULATED`.
- DEV-204 fresh-context behavior: `NOT_EXECUTED`.
- F001: `NOT_EXECUTED`; F002–F005: `NOT_POPULATED`.
- Empirical MVP proof: `NOT_ESTABLISHED`.
- Canonical runtime release: `NOT_ESTABLISHED`.
- `Execution-verified`: `NOT_CLAIMED`.

The change does not add a Layer 1 transition, Product Asset family, candidate basis, FT-T2 Skill, canonical gate, or current-truth authority. Structural Intelligence remains candidate/investigation support and cannot establish `CONFIRMED`, `EXCLUDED`, `ChangeSurfaceSet`, `SPEC_READY`, Product Asset publication, or lifecycle transitions.
