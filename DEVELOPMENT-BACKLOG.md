# Development Backlog — v0.4.8.2

## DEV-218 — Rehydrate approved source bytes
Optional for non-semantic implementation work; mandatory before any semantic spec change or canonical digest claim. Copy the five approved source files + exact HERM-211 helper package into `specs/approved/`, compute SHA-256, and replace the external identity lock with a digest-pinned baseline.

## DEV-219 — Complete Git Product Intelligence Store
Implement immutable published revisions, legal lifecycle transitions, supersession/retirement, conflict handling, publication gates, and atomic/rebuildable Registry behavior.

## DEV-220 — Azure Repos exact source binding
Bind configured repositories to full Git revisions in isolated local worktrees; preserve credential separation and source provenance.

## DEV-221 — Grafel live exact binding
Run real Grafel against the frozen worktrees. Record exact provider route, per-repo full revisions, runtime/wire/adapter versions, compatibility, and `EXACTLY_BOUND` evidence. Fail closed on mismatch.

## DEV-222 — PA-03 bootstrap
Use Grafel StructuralObservationSet plus field-specific source authority to propose PA-03 repository inventory/high-value relations. Do not full-sync the Grafel graph.

## DEV-223 — Product Knowledge synthesis / PA-01 proposal
Generate Product/SubProduct/Capability, Product Realization, DomainConcept/BusinessRule candidates from code + docs + history. Keep semantic proposals DRAFT / non-governing until explicit promotion.

## DEV-224 — Publication + Context Registry
Publish eligible Product Assets through approved Layer 2 policy, rebuild Registry, and resolve bounded exact ProductAssetRefs / ResolvedContextRefs.

## DEV-204 — Fresh-context Agent RED/GREEN
Execute independent behavioral validation; deterministic tests alone do not establish behavior.

## F001 — Four-arm calibration
Execute baseline / structural-only / Product-Intelligence-only / full-FDI calibration with frozen inputs and leakage-safe evidence boundaries.
