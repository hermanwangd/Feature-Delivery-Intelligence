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

<a id="current-state"></a>
## Current state

At 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482, the repository tree contains exactly the two approved design documents selected by `.fdi/features/HERM-209/spec/index.md#preflight-source-scope`. Repository-root README.md and physical .fdi profile do not exist at that source revision. The semantic document remains storage-neutral; the companion profile becomes binding only through `.fdi/README.md#adoption-state`.

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
| DES-017 | CRIT-017 | Implement HERM-209-linked PR targeting `main` with distinct candidate base/head/current PR head and no merge unless independent overall verdict is `PASS`. |

<a id="impacted-entity-and-relation-ids"></a>
## Impacted entity and relation IDs

Current entity IDs: product-feature-delivery-intelligence, system-fdi-coordination, component-fdi-documentation, feature-delivery-intelligence. Current relation IDs: relation-product-contains-coordination, relation-coordination-contains-documentation, relation-documentation-implemented-by-repository. Canonical definitions remain in `.fdi/context/codebase/catalog.md#entities` (registry revision `catalog-v1`) and `.fdi/context/codebase/relations.md#relations` (registry revision `relations-v1`).

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

README provides relative links to `.fdi/README.md` and both approved design documents. It introduces no runtime API. Every link must resolve at candidate_head_sha.

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

DES-001..017 map one-to-one to CRIT/REQ/TASK/VV rows in `.fdi/features/HERM-209/spec/index.md#intention-mapping`. The source relation target is feature-delivery-intelligence:README.md@candidate_head_sha.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No blocking design gap. Final candidate and PR IDs are intentionally assigned by Transition 3, then independently assessed.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Architecture/repository review: PASS for one-repository documentation-only pilot on 2026-08-30. Valid at source 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 and intention revision intention-v2. Successor: none.

<a id="gate-record"></a>
## Gate record

This member participates in the sole Delivery Spec gate at `.fdi/features/HERM-209/spec/index.md#gate-record` and does not create a competing gate.
