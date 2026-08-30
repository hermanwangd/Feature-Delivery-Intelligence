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

- `.fdi/features/HERM-209/request.md#artifact-identity`; request revision: request-v2
- `.fdi/features/HERM-209/intention.md#artifact-identity`; intention revision: intention-v2
- repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@sha256:e6639321db931da5bf5c177edf9836157ce4e25250b92ccc27ed406cf91a86c2
- repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@sha256:31f42a66960ba9502e413587d6344f9772a9148c736eafcb8c93e6144d4d0a3c

<a id="context-consulted"></a>
## Context consulted

| Consulted path@revision | Purpose | Authority/trust | Selection proof | Exclusions |
| --- | --- | --- | --- | --- |
| .fdi/README.md@sha256:fadbd405a33b7d440df9b60f27647614bbb2c2c9eb5b852499c04d8037db727a | confirm adopted profile and starting revision | adopted profile; governance-owned | literal fixed input; exact bytes resolved before bounded selection | mutable refs, unsafe payloads, unrelated and superseded material, future revisions |
| .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000 | apply profile schemas, selectors, and anchors | normative adopted-profile contract | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered extensions, future/superseded contract versions |
| .fdi/context/index.md@sha256:67b01c0f28649da22e1ffb70c899e69dd7a0f291445f06333b10137e7a569bde | validate extension/view/area/runbook registry | canonical conditional registry | literal fixed input; exact bytes resolved before bounded selection | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/context/steering/product.md@sha256:c0c8bcc3d1c6f33e53263184ea5d569495475f627264ed471f961fad255cb97f | constrain product outcome and scope | normative product-owner Steering | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, superseded product guidance, unregistered steering material |
| .fdi/context/steering/tech.md@sha256:9cd3f7e53fbe030ae16ab5d9058e72eb1d39a1de508946132dbc76b68995fe84 | apply technical and dependency constraints | normative architecture/security Steering | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered constraints, draft/exceptions without approval |
| .fdi/context/steering/structure.md@sha256:3cf35ff0e05565bcd465396e165e720d0ad44ac7588e5096cb353ce99b824f10 | apply placement, naming, and instruction precedence | normative organization policy | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, topology claims outside catalog/relations, unregistered placement |
| .fdi/context/steering/architecture.md@sha256:1cb3143c9a7bfcbbb5534ce399485c04c8a407cc92e4ffdcfa039543bb388bcd | apply boundaries and quality constraints | normative architecture policy | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unapproved exceptions, unregistered architecture material |
| .fdi/context/steering/agent-policy.md@sha256:27c84ed4e418f92bf7d2ff65d22bbf327da01be4c384a3a97159e8538dc33c85 | apply autonomy, redaction, and permission limits | normative governance/security policy | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, permissions beyond policy, unregistered agent instructions |
| .fdi/context/steering/delivery.md@sha256:c56e06b23966b27823cab55d07f0c1509d5ae32d4effa34d5b9e5dece823a5a3 | apply four-transition gates, evidence, and re-entry | normative delivery policy | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, collapsed gates, unregistered delivery instructions |
| .fdi/context/steering/governance.md@sha256:c50acafe71ae655eeb0f1ae177a8134c7a58987f927498ca467af617627beef0 | resolve owners, authority, cadence, and conflicts | normative governance policy | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered owners, mutable authority claims |
| .fdi/context/domain/glossary.md@sha256:328369bdec1b0377a5b2e077888267175ca87b6acc6cd8c74490090b046d550c | normalize feature and entity terms | definitional Domain Context | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered terms, conflicting aliases |
| .fdi/context/domain/rules.md@sha256:c8e2ad06ad1e0640da456d0b860048fe8fe282a54403e77c52ecbbbe00b51f34 | check durable product invariants | normative Domain Context | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered invariants, exceptions without approval |
| .fdi/context/codebase/catalog.md@sha256:9220e21cbab2f61db7de552bebd7a42a419ef8bd578760500e902eebcaa01060 | resolve current entities and repository projection registry | canonical current entity registry `catalog-v1` | literal fixed input; exact bytes resolved before bounded selection; ACTIVE/non-superseded | planned entities, source copies, mutable refs, unregistered paths, future registry revisions |
| .fdi/context/codebase/relations.md@sha256:1a5603cb06b27d3c2665ab373a1e51c2064735a377e2b529b3a7eddb54d802cd | resolve evidence-backed current relations | canonical current relation registry `relations-v1` | literal fixed input; exact bytes resolved before bounded selection; no planned relation selected | planned relations, source copies, mutable refs, unregistered paths, future registry revisions |
| .fdi/context/codebase/system-context.md@sha256:7f0b45623cae9ea6d0e0e98f66a2626b76170c2c893c73f99986e736efc9fea5 | verify derived system view | derived view over catalog/relations | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered derived views, topology claims outside catalog/relations |
| .fdi/context/codebase/integrations.md@sha256:2757d6d56d975c8fc743f4e4ac2cc4ea4b741c1a30917f2ca2b728cddd025e40 | verify derived integration view | derived view over catalog/relations | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered derived views, runtime integration claims |
| .fdi/context/codebase/data.md@sha256:b725c7f3d7f347f8eb53bd672296a39708193fcc0c1177f00944617f6ea76329 | verify derived data view | derived view over catalog/relations | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered derived views, data store/flow claims |
| .fdi/context/operations/environments.md@sha256:212e569032a9d9cb0c36ddcdd4ff63e859712a3d7b0d9432a63b0e8a9375c276 | confirm no environment claim | operations registry | literal fixed input; exact bytes resolved before bounded selection; zero applicable environment row | active environments, source copies, mutable refs, deployment/runtime claims |
| .fdi/context/operations/release.md@sha256:4f9a8a59107422c4af25eff71f6b47bec4467762dcd74e7e1cfe0a208bc08c64 | confirm release topology and gates | operations release registry | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, unregistered release events, executed release claims |
| .fdi/context/operations/observability.md@sha256:75b2c7cc76f0040b3dd0f663d71de97d904fa080cfd800896bd58c86ee0b23aa | confirm no observability signal claim | operations observability registry | literal fixed input; exact bytes resolved before bounded selection | live signals, source copies, mutable refs, unregistered observability claims |
| .fdi/context/knowledge/index.md@sha256:f76a43ac06ca26050ce98086bd026506222fd78ef694f8766dff67e63eeeb156 | perform Knowledge selection | retrieval-only Knowledge registry | literal fixed input; exact bytes resolved before bounded selection; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/context/external/references.md@sha256:6a224a8f41eeacdd907f7872055b2e37b1ad05521ac132970c98f0729abb5010 | perform external-review selection | sole external-review registry | literal fixed input; exact bytes resolved before bounded selection; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/baseline/catalog.md@sha256:3a66b988d1bf7a715da3e2ea38737db304995dba9d5641957128ab423eb29694 | perform Baseline selection | sole Baseline capability registry | literal fixed input; exact bytes resolved before bounded selection; empty capability table; zero selection | active or unsupported capabilities, source copies, mutable refs, unregistered baseline paths |
| .fdi/skills/catalog.md@sha256:0eecbf6118e6836a241f941560940f969f054ec59a85e49808928150f4e27cc0 | validate Skill versions/digests | canonical Skill registry | literal fixed input; exact bytes resolved before bounded selection; all required rows ACTIVE/current/non-superseded | inactive, superseded, unregistered, or digest-mismatched Skill rows |
| .fdi/skills/context-selection/SKILL.md@sha256:da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe | govern bounded selection procedure | active executable Context v0.1.1 | literal fixed input; exact bytes resolved before bounded selection; no Skill resource selected | source copies, mutable refs, unregistered skills, draft skill versions |
| .fdi/skills/intention-to-spec/SKILL.md@sha256:6ff39b93bb65b750e1dacecb7e31a2dc2cc94b159cf2642943a5a14fee6effe6 | govern Spec production | active transition procedure v0.1.1 | literal fixed input; exact bytes resolved before bounded selection; exact allowed writes checked | source copies, mutable refs, unregistered skills, draft skill versions, disallowed writes |
| .fdi/features/HERM-209/request.md@sha256:42a576396243a151fb39b25ff7e6789c540486e933d206427de8e9f475c5f8a5 | bind to authenticated request | T1 output; request revision: request-v2 | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, future request revisions, unregistered request artifacts |
| .fdi/features/HERM-209/intention.md@sha256:3725272577acde5905b8888d34e6e385e83c1dc98baa074ecb3ab9bc35c676c8 | bind to authorized intention | T1 output; intention revision: intention-v2 | literal fixed input; exact bytes resolved before bounded selection | source copies, mutable refs, future intention revisions, unregistered intention artifacts |
| .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:8aa0596904e2799b421194329f022d02ffbcf254acab4bca3fa3c9a5615cf8f5 | registry-first repository projection | derived projection; catalog read first | `.fdi/context/codebase/catalog.md#entities` read first (registry revision `catalog-v1`); ID feature-delivery-intelligence; ACTIVE; row `applies_to` is only `product-feature-delivery-intelligence`; impacted set contains that Product; exact intersection is `{product-feature-delivery-intelligence}`; owner Repository owner; owner-authenticated pinned Git; reviewed 2026-08-30; next 2026-11-28; superseded_by none; digest matched | HERM/System/Component direct applicability, source copies, mutable refs, unregistered repositories, future/superseded registry revisions, other repository IDs |
| repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@sha256:31f42a66960ba9502e413587d6344f9772a9148c736eafcb8c93e6144d4d0a3c | bounded source content | preflight exact path; authoritative adopted-profile schema | exact bytes resolved at source revision 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; selector syntax/authority/cardinality PASS | every other source path, mutable refs, directories, caches, generated/vendor trees, secrets, unregistered sources |
| repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@sha256:e6639321db931da5bf5c177edf9836157ce4e25250b92ccc27ed406cf91a86c2 | bounded source content | preflight exact path; authoritative storage-neutral semantics | exact bytes resolved at source revision 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; selector syntax/authority/cardinality PASS | every other source path, mutable refs, directories, caches, generated/vendor trees, secrets, unregistered sources |

<a id="task-registry"></a>
## Task registry

| Task ID | Action | Owner | Requirement/design/V&V mapping | Evidence IDs |
| --- | --- | --- | --- | --- |
| TASK-001 | Record dependency/input identities and safe digests at required destinations. | T3 implementation agent | CRIT-001; REQ-001; DES-001; VV-001 | intention-authorization; artifact-conformance |
| TASK-002 | Materialize and schema/safety-validate the exact mandatory core. | T3 implementation agent | CRIT-002; REQ-002; DES-002; VV-002 | artifact-conformance |
| TASK-003 | Add/resolve explicit stable anchors for every cross-file target. | T3 implementation agent | CRIT-003; REQ-003; DES-003; VV-003 | artifact-conformance |
| TASK-004 | Register exact current entities/relations and audit derived/structure boundaries. | T3 implementation agent | CRIT-004; REQ-004; DES-004; VV-004 | artifact-conformance |
| TASK-005 | Execute/record registry-first selection proofs and absence of conditional placeholders. | T3 implementation agent | CRIT-005; REQ-005; DES-005; VV-005 | artifact-conformance |
| TASK-006 | Finalize eight Skill packages, catalog metadata, bindings, permissions, lifecycle, and byte digests. | T3 implementation agent | CRIT-006; REQ-006; DES-006; VV-006 | artifact-conformance |
| TASK-007 | Materialize B3a/B3b split contract and confirm no support execution. | T3 implementation agent | CRIT-007; REQ-007; DES-007; VV-007 | artifact-conformance |
| TASK-008 | Initialize pinned honest empty Baseline and audit absent capability directories/claims. | T3 implementation agent | CRIT-008; REQ-008; DES-008; VV-008 | artifact-conformance |
| TASK-009 | Complete authenticated request/intention bundle and sole gate. | T1 Intention agent | CRIT-009; REQ-009; DES-009; VV-009 | intention-authorization; artifact-conformance |
| TASK-010 | Execute Transition-2 staged selector and complete five-member Spec. | T2 Spec agent | CRIT-010; REQ-010; DES-010; VV-010 | artifact-conformance |
| TASK-011 | Record exact per-transition reads/writes/Context/evidence/gate review. | T2 Spec agent | CRIT-011; REQ-011; DES-011; VV-011 | artifact-conformance |
| TASK-012 | Commit candidate base, then immediate README-only candidate head, and prove adjacency. | T3 implementation agent | CRIT-012; REQ-012; DES-012; VV-012 | source-diff |
| TASK-013 | Record every deviation/disposition/proposed blocker before V&V. | T3 implementation agent | CRIT-013; REQ-013; DES-013; VV-013 | source-diff; artifact-conformance |
| TASK-014 | Create root README with required sections, boundaries, and resolving relative links. | T3 implementation agent | CRIT-014; REQ-014; DES-014; VV-014 | readme-entrypoint |
| TASK-015 | Complete bidirectional fragment/criterion/Spec/candidate/evidence/verdict mappings. | T2 Spec agent | CRIT-015; REQ-015; DES-015; VV-015 | artifact-conformance |
| TASK-016 | Execute the independent T4 checks and own `vv-report.md`, `evidence/readme-entrypoint.md`, and `evidence/artifact-conformance.md`, recording truthful verdict/re-entry/release state; T3 prepares the handoff only and must not own or author T4 verdict content. | T4 independent V&V agent | CRIT-016; REQ-016; DES-016; VV-016 | readme-entrypoint; artifact-conformance |
| TASK-017 | Ensure HERM-209-linked PR targets `main`, records corrected candidate base/head/current PR head, exact commands/results/gaps, and remains unmerged unless independent overall verdict is `PASS`. | Source/PR owner | CRIT-017; REQ-017; DES-017; VV-017 | artifact-conformance |

<a id="dependencies"></a>
## Dependencies

Sequential chain: TASK-001 -> TASK-002 -> TASK-003 -> TASK-004 -> TASK-005 -> TASK-006 -> TASK-007 -> TASK-008 -> TASK-009 -> TASK-010 -> TASK-011 -> TASK-012 -> TASK-013 -> TASK-014 -> TASK-015 -> TASK-016 -> TASK-017. TASK-009 is produced by the T1 Intention agent; TASK-010 and TASK-011 are produced by the T2 Spec agent; TASK-001..008 and TASK-012..015 are produced by the T3 implementation agent, which also prepares the TASK-016 handoff without owning or authoring T4 verdict content. TASK-016 is produced by the distinct T4 independent V&V agent. Source/PR owner owns TASK-017 and the linked PR.

<a id="repository-ownership"></a>
## Repository ownership

Repository feature-delivery-intelligence owns exact source reads, README candidate, Git history, PR, CI/review, merge/release, and rollback. The coordination profile owns .fdi feature artifacts/mappings/safe evidence. Independent V&V owns verdict only.

<a id="requirement-design-mapping"></a>
## Requirement/design mapping

Set equality is defined in `.fdi/features/HERM-209/spec/index.md#intention-mapping`: every CRIT/REQ/DES/TASK/VV ID appears exactly once and no orphan/unknown ID is allowed.

<a id="completion-evidence"></a>
## Completion evidence

TASK-001/009 -> intention-authorization; TASK-012/013 -> source-diff; TASK-014/016 -> readme-entrypoint; TASK-016 -> vv-report and artifact-conformance as independent T4 outputs; TASK-002..011/013/015/017 -> artifact-conformance. Raw Git/PR artifacts remain at source authority.

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

This member participates in the sole Delivery Spec gate at `.fdi/features/HERM-209/spec/index.md#gate-record` and does not create a competing gate.
