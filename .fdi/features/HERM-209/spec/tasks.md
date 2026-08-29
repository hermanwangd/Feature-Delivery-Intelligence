# HERM-209 Delivery Spec tasks

<a id="artifact-identity"></a>
## Artifact identity

- Feature: HERM-209
- Logical artifact: Delivery Spec
- Member: tasks.md
- Artifact revision: tasks-v1
- Producer: Spec agent

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

<a id="task-registry"></a>
## Task registry

| Task ID | Action | Owner | Requirement/design/V&V mapping | Evidence IDs |
| --- | --- | --- | --- | --- |
| TASK-001 | Record dependency/input identities and safe digests at required destinations. | Implementation owner except repository/profile owner | CRIT-001; REQ-001; DES-001; VV-001 | intention-authorization; artifact-conformance |
| TASK-002 | Materialize and schema/safety-validate the exact mandatory core. | Implementation owner except repository/profile owner | CRIT-002; REQ-002; DES-002; VV-002 | artifact-conformance |
| TASK-003 | Add/resolve explicit stable anchors for every cross-file target. | Implementation owner except repository/profile owner | CRIT-003; REQ-003; DES-003; VV-003 | artifact-conformance |
| TASK-004 | Register exact current entities/relations and audit derived/structure boundaries. | Implementation owner except repository/profile owner | CRIT-004; REQ-004; DES-004; VV-004 | artifact-conformance |
| TASK-005 | Execute/record registry-first selection proofs and absence of conditional placeholders. | Implementation owner except repository/profile owner | CRIT-005; REQ-005; DES-005; VV-005 | artifact-conformance |
| TASK-006 | Finalize eight Skill packages, catalog metadata, bindings, permissions, lifecycle, and byte digests. | Implementation owner except repository/profile owner | CRIT-006; REQ-006; DES-006; VV-006 | artifact-conformance |
| TASK-007 | Materialize B3a/B3b split contract and confirm no support execution. | Implementation owner except repository/profile owner | CRIT-007; REQ-007; DES-007; VV-007 | artifact-conformance |
| TASK-008 | Initialize pinned honest empty Baseline and audit absent capability directories/claims. | Implementation owner except repository/profile owner | CRIT-008; REQ-008; DES-008; VV-008 | artifact-conformance |
| TASK-009 | Complete authenticated request/intention bundle and sole gate. | Implementation owner except repository/profile owner | CRIT-009; REQ-009; DES-009; VV-009 | intention-authorization; artifact-conformance |
| TASK-010 | Execute Transition-2 staged selector and complete five-member Spec. | Implementation owner except repository/profile owner | CRIT-010; REQ-010; DES-010; VV-010 | artifact-conformance |
| TASK-011 | Record exact per-transition reads/writes/Context/evidence/gate review. | Implementation owner except repository/profile owner | CRIT-011; REQ-011; DES-011; VV-011 | artifact-conformance |
| TASK-012 | Commit candidate base, then immediate README-only candidate head, and prove adjacency. | Implementation owner except repository/profile owner | CRIT-012; REQ-012; DES-012; VV-012 | source-diff |
| TASK-013 | Record every deviation/disposition/proposed blocker before V&V. | Implementation owner except repository/profile owner | CRIT-013; REQ-013; DES-013; VV-013 | source-diff; artifact-conformance |
| TASK-014 | Create root README with required sections, boundaries, and resolving relative links. | Implementation owner except repository/profile owner | CRIT-014; REQ-014; DES-014; VV-014 | readme-entrypoint |
| TASK-015 | Complete bidirectional fragment/criterion/Spec/candidate/evidence/verdict mappings. | Implementation owner except repository/profile owner | CRIT-015; REQ-015; DES-015; VV-015 | artifact-conformance |
| TASK-016 | Run a separate independent V&V agent/run and record truthful verdict/re-entry/release state. | Implementation owner except independent V&V owner | CRIT-016; REQ-016; DES-016; VV-016 | readme-entrypoint; artifact-conformance |

<a id="dependencies"></a>
## Dependencies

TASK-001 -> TASK-002..009 -> TASK-010 -> TASK-012/TASK-014 -> TASK-013 -> TASK-015 -> TASK-016. TASK-003..008 may be audited in parallel but all must pass before candidate_base_sha. TASK-016 begins only after Change Set gate/evidence exists.

<a id="repository-ownership"></a>
## Repository ownership

Repository feature-delivery-intelligence owns exact source reads, README candidate, Git history, PR, CI/review, merge/release, and rollback. The coordination profile owns .fdi feature artifacts/mappings/safe evidence. Independent V&V owns verdict only.

<a id="requirement-design-mapping"></a>
## Requirement/design mapping

Set equality is defined in .fdi/features/HERM-209/spec/index.md#intention-mapping: every CRIT/REQ/DES/TASK/VV ID appears exactly once and no orphan/unknown ID is allowed.

<a id="completion-evidence"></a>
## Completion evidence

TASK-001/009 -> intention-authorization; TASK-012/013 -> source-diff; TASK-014 -> readme-entrypoint; TASK-002..011/013/015/016 -> artifact-conformance and vv-report. Raw Git/PR artifacts remain at source authority.

<a id="traceability"></a>
## Traceability

Every task row names criterion, requirement, design, V&V, and evidence IDs. Following candidate path is feature-delivery-intelligence:README.md@candidate_head_sha where applicable.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No planned deviation. Any discovered path outside the completed change-surface summary must not be read; record deviation/disposition and re-enter Spec.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Dependency/ownership review: PASS on 2026-08-30. Invalidated by Intention/Spec/source-scope revision. Successor: none.

<a id="gate-record"></a>
## Gate record

This member participates in the sole Delivery Spec gate at .fdi/features/HERM-209/spec/index.md#gate-record and does not create a competing gate.
