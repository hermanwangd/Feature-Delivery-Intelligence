# MULTICA HANDOFF — FDI Recovery Workspace v0.4.8.1

## 1. Purpose

Use this package as the **sole active recovery workspace**, not as a newly invented semantic authority. Prior corrupted Multica project content must remain archived/untrusted unless a specific artifact is independently verified and deliberately reintroduced through HERM-219.

`governance/CURRENT` is intentionally `NONE`. This means semantic development/proof gates are paused until the exact approved normative source set is recovered, digested, reconciled, and explicitly promoted as `GB-0001`.

## 2. First rule: REC-000 before implementation

Do not replay old v0.4.6.x/v0.4.7.x overlays in sequence and do not reconstruct missing contracts from summaries.

First execute HERM-219 recovery:

```text
approved Layer 1 v0.2 bytes
+ approved Layer 1 Markdown I/O v0.1 bytes
+ exact HERM-211 FT-T2 package
+ approved Layer 2 Framework v0.1 bytes
+ approved Product Asset Profile v0.1 bytes
+ approved PA Maintenance Skill Contract v0.1 bytes
        ↓
exact local digests / compatibility / reconciliation
        ↓
GB-0001-CANDIDATE
        ↓
explicit approval
        ↓
GB-0001 + CURRENT
```

If an exact approved source cannot be recovered, **stop baseline promotion**. Do not manufacture a replacement from this handoff or from Agent memory.

## 3. Non-negotiable recovery guardrails

```text
Layer 1 = T1 → T2 → T3 → T4
HERM-211 Feature Closure remains inside T2
Six helper contracts:
  IntentSpec
  CandidateRepoSet
  ChangeSurfaceSet
  EvidenceRecord
  ClosurePackage
  ClosureReview
Five helper Skills:
  feature-intent-analysis
  repo-discovery
  changesurface-investigation
  dependency-closure
  closure-review
Closure status:
  OPEN | PARTIAL | CLOSED_WITHIN_DECLARED_SCOPE
Sole T2 canonical gate:
  SPEC_READY | BLOCKED
```

`CLOSED_WITHIN_DECLARED_SCOPE` never implies `SPEC_READY` and never authorizes T3.

Layer 2 / Structural Intelligence may orient, constrain, prioritize and generate candidates. They do not establish current `CONFIRMED`, `EXCLUDED`, Change Surface truth, or `SPEC_READY`; material current claims require current feature-specific pinned Evidence.

## 4. Layer 2 recovery boundary

The recovery schemas under `implementation/product-intelligence/contracts/` have been hardened back to the approved Layer 2 v0.1 descriptor/ref semantics to prevent runtime regression, including:

- legal lifecycle combinations only;
- `maintenance_mode` and `publication_policy`;
- authority dimensions;
- faceted trust profile;
- freshness/invalidation/dependencies;
- fail-closed active-lineage registry projection.

These schemas are **recovery conformance guards**, not substitutes for the approved normative Markdown source.

Product Asset Profile v0.1 fully specifies **PA-03 Codebase and PA-05 Delivery History only**. PA-01 remains under `candidates/PA-01/`.

## 5. Structural Intelligence recovery boundary

Grafel remains behind `CodeIntelligenceProvider`.

This recovery line restores:

- full Git revision binding;
- exact per-repository binding evidence;
- runtime/wire/adapter version attestation;
- cross-field revalidation of stored evidence;
- provider-side mapping of repository/relation/depth/result bounds;
- post-result finite bounds;
- no Grafel schema in FDI semantic authority.

Live Grafel compatibility remains **NOT EXECUTED**.

## 6. Product Knowledge physicalization

Durable Product Knowledge is still intended to accumulate in a Product-owned `ProductIntelligenceStore`; MVP candidate backend is a Product-scoped Git repository.

`GitStoreAdapter` in this recovery package is a **SCAFFOLD**, not a complete publication/lifecycle implementation. Do not claim full Product Intelligence Store reference implementation until immutable publication, lifecycle/supersession, conflict handling, atomic registry rebuild, and conformance tests are implemented against the approved baseline.

## 7. Ordered Multica sequence

Follow `multica/CONTINUE-DEVELOPMENT.md` exactly:

```text
REC-000  HERM-219 exact source recovery + GB-0001 approval
REC-001  recovery integrity / exact normative binding
REC-002  restore/verify Layer 2 exact contract runtime
REC-003  complete Git Product Intelligence Store
REC-004  Azure Repos exact source binding
REC-005  Grafel live exact binding
REC-006  PA-03 bootstrap
REC-007  PA-01 candidate / semantic synthesis (still non-governing unless separately promoted)
REC-008  publication + Registry
REC-009  DEV-204 fresh-context validation
REC-010  F001 calibration
```

Do not advance to REC-002+ while `governance/CURRENT` is `NONE`.

## 8. Claim boundary

```text
Recovery packaging / known regression hardening  IMPLEMENTED_LOCAL
Approved governing baseline embedded/promoted     NOT_ESTABLISHED
Exact approved source byte identity               NOT_VERIFIED
Git Product Intelligence Store                    SCAFFOLD
Azure Repos provider                              REFERENCE SCAFFOLD / LIVE AUTH NOT CONFIGURED
Grafel provider adapter                           MOCK-TESTED / LIVE NOT EXECUTED
Real 20-repo Product bootstrap                    NOT EXECUTED
DEV-204                                            NOT EXECUTED
F001                                               NOT EXECUTED
Empirical FDI uplift                               NOT ESTABLISHED
```
