# Feature Delivery Intelligence Phase 1 package

This repository is the dedicated FDI coordination repository. The Phase 1 package implements six framework/agent contracts, five closure Skills, one manual FT-T2 Feature Closure workflow, and one deterministic offline replay scorer. Product Intelligence remains the mandatory second core layer, and source repositories retain authority for their code, tests, CI, review, release, and rollback.

## Validate

```sh
make bootstrap
make validate
make score
```

`make validate` validates all six Draft 2020-12 schemas, positive/negative/cross-contract fixtures, all five Skill package contracts and trigger boundaries, workflow readiness boundaries, frozen fixture/package manifests, and deterministic scorer behavior.

See `validation/PHASE1-EVIDENCE.md` for metrics and the explicit distinction between contract-fixture evidence and a qualifying independently executed historical blind proof. `Execution-verified` is not claimed.
