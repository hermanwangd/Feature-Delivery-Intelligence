# Feature Delivery Intelligence

This repository is the dedicated FDI coordination repository. It contains the Phase 1 contract package and the v0.4.7.2 provider-neutral Structural Intelligence runtime with a concrete Grafel snapshot-binding seam. Product Intelligence remains the mandatory second core layer, and source repositories retain authority for their code, tests, CI, review, release, and rollback.

## Governing specification baseline

`governance/baselines/GB-0001.yaml` is the digest-addressed approved authority
set. `governance/GOVERNING-SPEC.md` is generated from its selected exact modules
and must not be edited manually. `governance/CURRENT` selects `GB-0001` after
independent validation and explicit Human approval; the predecessor identity
and approval provenance are preserved in
`governance/reconciliation/GB-0001-PROMOTION.json`. Runtime or bundle versions
are not semantic authority.

```sh
python3 scripts/governance_baseline.py \
  --report governance/reconciliation/BASELINE-VERIFICATION.json
```

## FDI MVP v0.4.7.2 integration boundary

The v0.4.7.2 implementation overlay, originally prepared for a canonical v0.4.6.1 source tree, is integrated here without changing the H01–H05 freeze or the shared PA-03 CB-01 identity-only substrate. The DEV-204 harness still uses neutral `target_kind` and `target_loaded` fields.

The injected `binding_attestor` produces a full SnapshotBindingAttestation for either `LIVE_CURRENT` or `FROZEN_INDEXED`. The Grafel adapter translates each FDI repository identity to the explicitly attested Grafel slug before `orient`, `find`, or `diff`. Normalized outputs retain FDI repository identities. Route attestation requires affirmative queryability, exact `group/ref`, explicit non-warming/non-indexing state, exact group metadata identity, and an exact repository set.

Local deterministic tests do not establish live Grafel connectivity, real Product binding, DEV-204 behavior, F001 uplift, or a canonical runtime release.

Live status: live Grafel execution is `NOT_EXECUTED`; no real Product snapshot is claimed.

> Do not claim `fdi-mvp-v0.4.7.2` as a canonical release or live Grafel proof from this integration alone.

## Environment

- Python `3.9.6` (also pinned in `.python-version`)
- `jsonschema[format]==4.25.1`
- `pytest==8.4.2`

## Validate

```sh
make bootstrap
make validate
make score
make test-functional
make test-release
# or run the complete local gate
make test-all
```

`make validate` is the canonical Phase 1 native regression suite. `make test-functional` and `make test-release` run the integrated v0.4.7.2 functional and release-guard suites.

See `validation/PHASE1-EVIDENCE.md` for metrics and the explicit distinction between contract-fixture evidence and a qualifying independently executed historical blind proof. `Execution-verified` is not claimed.
