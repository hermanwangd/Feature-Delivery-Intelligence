# Feature Delivery Intelligence — Recovery Workspace v0.4.8.1

**Classification:** `RECOVERY_WORKSPACE_HERM219_REQUIRED`  
**Active governing baseline inside bundle:** NONE  
**Canonical runtime proof:** NO  
**Live Grafel proof:** NOT EXECUTED  
**Real Product binding:** NOT POPULATED  
**F001 empirical uplift:** NOT ESTABLISHED

This package is a clean recovery workspace for rebuilding a single FDI authority chain after the prior Multica project became internally inconsistent.

It is **not** a byte-for-byte reconstruction of every lost approved source. It deliberately refuses to turn recovery summaries into governing authority. Exact approved normative source bytes must be rehydrated and pinned through HERM-219 before semantic implementation/proof work resumes.

## Start here

Read in this order:

1. `MULTICA-HANDOFF.md`
2. `governance/CURRENT`
3. `governance/README.md`
4. `governance/baselines/GB-0001-CANDIDATE.yaml`
5. `governance/reconciliation/SOURCE-INVENTORY.json`
6. `multica/CONTINUE-DEVELOPMENT.md`
7. `implementation/README.md`
8. `implementation/structural-intelligence/GRAFEL-BOUNDARY.md`
9. `implementation/source-integration/AZURE-REPOS.md`
10. `implementation/product-intelligence/PRODUCT-INTELLIGENCE-STORE.md`

## Authority rule

```text
governance/CURRENT = NONE
        ↓
no active semantic baseline in this bundle
        ↓
HERM-219 must rehydrate exact approved sources
        ↓
GB-0001-CANDIDATE + exact digests + compatibility checks + approval
        ↓
GB-0001 APPROVED
        ↓
CURRENT = GB-0001
        ↓
implementation/proof work may resume
```

Recovery references and implementation schemas exist only to prevent known regressions while the exact approved Markdown/contracts are restored. They do not supersede the approved sources.

## Frozen recovery invariants

These are guardrails, not a substitute for exact normative source bytes:

```text
Layer 1 = T1 Intention → T2 Delivery Spec → T3 Implementation → T4 Correctness
FT-T2 HERM-211 helper contracts = exact six identities
FT-T2 helper Skills = exact five identities
T2 canonical gate = SPEC_READY | BLOCKED
Layer 2 = durable Product Intelligence, not current Feature truth
PA-03 + PA-05 are the only fully specified Product Asset Profiles in approved v0.1
PA-01 remains candidate
Grafel = preferred CodeIntelligenceProvider, non-authoritative
Git-backed Product Intelligence Store = MVP physicalization candidate
Registry = derived selection/navigation projection
Current feature-specific pinned Evidence = current Change Surface authority
```

## Repository boundary

```text
governance/ + normative/
    authority selection and exact approved source rehydration

candidates/
    non-governing successor work, including PA-01

implementation/
    non-normative runtime/tooling recovery material

product-intelligence-template/
    candidate physical shape for a Product-owned durable PK repository

.fdi-work/ (runtime only, never committed)
    temporary pinned worktrees, Grafel indexes, observations, proposals
```

Run:

```bash
python scripts/verify_bundle.py .
python scripts/validate_schemas.py .
python scripts/validate_baseline.py . --expect-recovery-blocked
python -m unittest discover -s tests -v
```
