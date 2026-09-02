# DEV-219 — Git Product Intelligence Store validation

Repository-native tests cover the append-only `ProductIntelligenceStore` lifecycle:

- immutable descriptor revision creation and conflicting-byte rejection;
- legal `CREATE`, `REVISE`, `MARK_STALE`, `SUPERSEDE`, and `RETIRE` transitions;
- terminal retirement and optimistic current-revision conflict handling;
- evidence-bearing publication authorization that fails closed;
- lineage/path validation, fork rejection, deterministic Registry rebuild, and atomic Registry replacement;
- exclusion of Git worktree metadata from bundle verification.

All lifecycle tests use temporary Product Intelligence roots. No Product Asset is published by this package, no governing source is modified, and Registry membership remains a derived selection view rather than current Feature truth. Exact candidate revision and command results are recorded in the DEV-219 issue handoff and linked pull request.
