# MULTICA HANDOFF — FDI Clean Project Baseline v0.4.8.2

This directory is the **new active FDI software project**, not a recovery workspace.

## Read first

1. `README.md`
2. `governance/CURRENT`
3. `governance/baselines/DB-0001.yaml`
4. `governance/approved-source-lock.json`
5. `governance/GOVERNING-SOURCES.md`
6. `STATUS.json`
7. `DEVELOPMENT-BACKLOG.md`

## Governing boundaries

- Layer 1 is T1 → T2 → T3 → T4.
- FT-T2 Feature Closure is subordinate to T2 and keeps exactly six helper contracts/five helper Skills.
- PA-03/PA-05 are the fully specified Layer 2 v0.1 profiles.
- PA-01 remains a proposal under `specs/proposals/PA-01/`.
- Product/Structural Intelligence generates context/candidates; current Change Surface truth requires current feature-specific pinned Evidence.
- Grafel is a replaceable `CodeIntelligenceProvider`.
- Azure Repos sources must be materialized to exact local Git revisions before Grafel analysis.
- Durable PK is intended to live in a Product-owned Git-backed Product Intelligence Store; the included GitStoreAdapter remains a scaffold until publication/supersession/atomic registry behavior is completed.

## External approved source lock

Approved source identities are known and pinned, but exact source bytes are not embedded in this ZIP. Continue implementation work; **do not modify governing semantics** until those bytes are rehydrated and digest-pinned.

## Next work

Follow `DEVELOPMENT-BACKLOG.md`; do not execute REC-* recovery tasks.
