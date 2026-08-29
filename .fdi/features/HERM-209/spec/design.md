# HERM-209 Delivery Spec design

<a id="artifact-identity"></a>
## Artifact identity

- Feature: HERM-209
- Logical artifact: Delivery Spec
- Member: design.md
- Artifact revision: design-v1
- Producer: Spec agent
- Source base: feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482

<a id="inputs"></a>
## Inputs

- .fdi/features/HERM-209/request.md@sha256:e521ee446d2714b891147d09a9d0957ac229bcc1c417bfd95699391c6ff64b62
- .fdi/features/HERM-209/intention.md@sha256:90550317a9ea6a34fe089de99d030266be24f971da9d19240e4024d341c9ef3b
- repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@sha256:e6639321db931da5bf5c177edf9836157ce4e25250b92ccc27ed406cf91a86c2
- repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@sha256:31f42a66960ba9502e413587d6344f9772a9148c736eafcb8c93e6144d4d0a3c

<a id="context-consulted"></a>
## Context consulted

- .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000
- .fdi/context/steering/product.md@sha256:c0c8bcc3d1c6f33e53263184ea5d569495475f627264ed471f961fad255cb97f
- .fdi/context/steering/architecture.md@sha256:1cb3143c9a7bfcbbb5534ce399485c04c8a407cc92e4ffdcfa039543bb388bcd
- .fdi/context/steering/delivery.md@sha256:c56e06b23966b27823cab55d07f0c1509d5ae32d4effa34d5b9e5dece823a5a3
- .fdi/context/codebase/catalog.md@sha256:a592034ac750e796d78f05137c2e030a36e3d2754b723437eceec99aabdd509a
- .fdi/context/codebase/relations.md@sha256:820c3b5df3ddac87c58e6f7f3999cd93ec50969fbbe283cf3d3ad51630153696
- .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:a72aec299a1517df6c08b6ff089aff9fe58f7f591ad3634e1246d3bc0de56af4 after catalog proof
- .fdi/skills/context-selection/SKILL.md@sha256:e327dcc6ecfcdbf2085762c8b1883a59aeabdd5beac35f687c1c1eec001524b8
- .fdi/skills/intention-to-spec/SKILL.md@sha256:29aa863b3a099d4274ec1c58582271f76b3eeb8d2b75f1e362f8a7d4c1af8f13
- Full literal reads, selected source matches, proof, and exclusions are in .fdi/features/HERM-209/spec/index.md#context-consulted.

<a id="current-state"></a>
## Current state

At 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482, the repository tree contains exactly the two approved design documents selected by .fdi/features/HERM-209/spec/index.md#preflight-source-scope. Repository-root README.md and physical .fdi profile do not exist at that source revision. The semantic document remains storage-neutral; the companion profile becomes binding only through .fdi/README.md#adoption-state.

<a id="proposed-design"></a>
## Proposed design

| Design ID | Criterion | Design obligation |
| --- | --- | --- |
| DES-001 | CRIT-001 | Implement start dependencies and immutable input revisions through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-002 | CRIT-002 | Implement mandatory core adoption/schema/safety through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-003 | CRIT-003 | Implement explicit stable cross-file anchors through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-004 | CRIT-004 | Implement singular canonical topology and planned/current separation through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-005 | CRIT-005 | Implement registry-first conditional selection and no placeholders through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-006 | CRIT-006 | Implement eight current digest-resolvable skill packages through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-007 | CRIT-007 | Implement materialized but unexecuted b3a/b3b split through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-008 | CRIT-008 | Implement honest pinned empty baseline and no support claim through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-009 | CRIT-009 | Implement authenticated single-gate intention bundle through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-010 | CRIT-010 | Implement staged non-circular source preflight through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-011 | CRIT-011 | Implement ordered four-transition execution records through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-012 | CRIT-012 | Implement adjacent candidate base/head with readme-only diff through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-013 | CRIT-013 | Implement complete deviation disposition and blocking state through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-014 | CRIT-014 | Implement readme contributor entry-point contract through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-015 | CRIT-015 | Implement bidirectional request-to-verdict traceability through the exact profile, artifact, candidate, or independent-evidence contract. |
| DES-016 | CRIT-016 | Implement independent v&v and truthful execution claim through the exact profile, artifact, candidate, or independent-evidence contract. |

<a id="impacted-entity-and-relation-ids"></a>
## Impacted entity and relation IDs

Current entity IDs: product-feature-delivery-intelligence, system-fdi-coordination, component-fdi-documentation, feature-delivery-intelligence. Current relation IDs: relation-product-contains-coordination, relation-coordination-contains-documentation, relation-documentation-implemented-by-repository. Canonical definitions remain in .fdi/context/codebase/catalog.md#entities and .fdi/context/codebase/relations.md#relations.

<a id="planned-relations"></a>
## Planned relations

None. README.md is a new source file within an existing Repository/Component authority boundary and does not create a topology edge. No planned relation may be written to or selected from current Codebase.

<a id="change-surface"></a>
## Change surface

- Coordination/profile candidate-base content: the 32 mandatory core paths, Baseline snapshot/catalog, HERM-209 request/intention/intention-authorization evidence, and all five Spec members.
- Transition-3 bounded source reads after registry selection: repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md; repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md. Maximum 2; exclude every other path and mutable ref.
- Source candidate write: repository-root README.md only, created in the immediate child of candidate_base_sha.
- Later coordination writes: change-set/index.md and source-diff evidence, followed by independent vv-report/readme-entrypoint/artifact-conformance evidence. These are never candidate_head_sha.
- No code, config, schema, dependency, runtime, deployment, data, or release change.

<a id="interfaces"></a>
## Interfaces

README provides relative links to .fdi/README.md and both approved design documents. It introduces no runtime API. Every link must resolve at candidate_head_sha.

<a id="data"></a>
## Data

No data model/store/flow change. Evidence stores only safe identifiers, revisions, digests, timestamps, observations, owners, limitations, and validity.

<a id="operations"></a>
## Operations

Local immutable Git checks and GitHub PR review only. No deployment/release. vv-report release observation is NOT_OBSERVED. B3 waits for a later authenticated release event.

<a id="rollout-rollback"></a>
## Rollout/rollback

Rollout is review via PR targeting main. Before merge, amend/close PR. After merge/release, source owner controls rollback. Current Context cannot change via B3 without separate B3a candidate and distinct B3b PASS/CAS receipt.

<a id="risks"></a>
## Risks

Primary risks: implicit selectors, stale/mutable evidence, anchor/link breakage, self-referential commit IDs, collapsed authority roles, and overclaiming execution/release. Controls: exact pins, finite selectors, later coordination records, external final PR-head evidence, and independent V&V.

<a id="traceability"></a>
## Traceability

DES-001..016 map one-to-one to CRIT/REQ/TASK/VV rows in .fdi/features/HERM-209/spec/index.md#intention-mapping. The source relation target is feature-delivery-intelligence:README.md@candidate_head_sha.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No blocking design gap. Final candidate and PR IDs are intentionally assigned by Transition 3, then independently assessed.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Architecture/repository review: PASS for one-repository documentation-only pilot on 2026-08-30. Valid at source 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 and intention@sha256:90550317a9ea6a34fe089de99d030266be24f971da9d19240e4024d341c9ef3b. Successor: none.

<a id="gate-record"></a>
## Gate record

This member participates in the sole Delivery Spec gate at .fdi/features/HERM-209/spec/index.md#gate-record and does not create a competing gate.
