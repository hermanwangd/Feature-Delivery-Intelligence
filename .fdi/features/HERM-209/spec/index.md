# HERM-209 Delivery Spec index

<a id="artifact-identity"></a>
## Artifact identity

- Feature: HERM-209
- Logical artifact: Delivery Spec
- Artifact revision: delivery-spec-v1
- Producer: Spec agent
- Intention input: `.fdi/features/HERM-209/intention.md#artifact-identity`; intention revision: intention-v2
- Source base: feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482

<a id="inputs"></a>
## Inputs

- `.fdi/features/HERM-209/request.md#artifact-identity`; request revision: request-v2
- `.fdi/features/HERM-209/intention.md#artifact-identity`; intention revision: intention-v2
- repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@sha256:e6639321db931da5bf5c177edf9836157ce4e25250b92ccc27ed406cf91a86c2
- repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@sha256:31f42a66960ba9502e413587d6344f9772a9148c736eafcb8c93e6144d4d0a3c
- Exact fixed Context inputs and selected reads are listed at `.fdi/features/HERM-209/spec/index.md#context-consulted`.

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
| .fdi/context/codebase/catalog.md#entities | anchor target for registry citation | canonical entity registry `catalog-v1` | explicit stable lowercase kebab anchor exists adjacent to H2 | generated/numbered fragments, bare authority references, revision-qualified fragment citations |
| .fdi/context/codebase/relations.md#relations | anchor target for registry citation | canonical relation registry `relations-v1` | explicit stable lowercase kebab anchor exists adjacent to H2 | generated/numbered fragments, bare authority references, revision-qualified fragment citations |

<a id="bundle-membership"></a>
## Bundle membership

| Member | SHA-256 | Purpose |
| --- | --- | --- |
| .fdi/features/HERM-209/spec/index.md | self; external candidate_base_sha after commit | identity, mapping, selector, sole gate |
| .fdi/features/HERM-209/spec/requirements.md | 53bf65ffb571c991437be6b2de9f09a4aa4eb15bf020ca0c62ea4d958bb67568 | requirements/acceptance |
| .fdi/features/HERM-209/spec/design.md | c1608575895f007440dc27ee979bb1a9f25d32ffd1faafff8fc43b2735e52fbe | current/proposed design/change surface |
| .fdi/features/HERM-209/spec/tasks.md | f1acb954686f690093507f95bbaccda20fe0804ce637dbdb06c1e80f97e0b38c | actionable owner/dependency/evidence tasks |
| .fdi/features/HERM-209/spec/vv-plan.md | 2f73fb8e6704636fb652e4ef20b1aebeed8d56d650053a60b3f5229ffce6d5fa | independent methods/thresholds/evidence allocation |

<a id="intention-mapping"></a>
## Intention mapping

| Criterion | Requirement | Design | Task | V&V | Evidence IDs |
| --- | --- | --- | --- | --- | --- |
| CRIT-001 | REQ-001 | DES-001 | TASK-001 | VV-001 | intention-authorization; artifact-conformance |
| CRIT-002 | REQ-002 | DES-002 | TASK-002 | VV-002 | artifact-conformance |
| CRIT-003 | REQ-003 | DES-003 | TASK-003 | VV-003 | artifact-conformance |
| CRIT-004 | REQ-004 | DES-004 | TASK-004 | VV-004 | artifact-conformance |
| CRIT-005 | REQ-005 | DES-005 | TASK-005 | VV-005 | artifact-conformance |
| CRIT-006 | REQ-006 | DES-006 | TASK-006 | VV-006 | artifact-conformance |
| CRIT-007 | REQ-007 | DES-007 | TASK-007 | VV-007 | artifact-conformance |
| CRIT-008 | REQ-008 | DES-008 | TASK-008 | VV-008 | artifact-conformance |
| CRIT-009 | REQ-009 | DES-009 | TASK-009 | VV-009 | intention-authorization; artifact-conformance |
| CRIT-010 | REQ-010 | DES-010 | TASK-010 | VV-010 | artifact-conformance |
| CRIT-011 | REQ-011 | DES-011 | TASK-011 | VV-011 | artifact-conformance |
| CRIT-012 | REQ-012 | DES-012 | TASK-012 | VV-012 | source-diff |
| CRIT-013 | REQ-013 | DES-013 | TASK-013 | VV-013 | source-diff; artifact-conformance |
| CRIT-014 | REQ-014 | DES-014 | TASK-014 | VV-014 | readme-entrypoint |
| CRIT-015 | REQ-015 | DES-015 | TASK-015 | VV-015 | artifact-conformance |
| CRIT-016 | REQ-016 | DES-016 | TASK-016 | VV-016 | readme-entrypoint; artifact-conformance |
| CRIT-017 | REQ-017 | DES-017 | TASK-017 | VV-017 | artifact-conformance |

<a id="revision-state"></a>
## Revision state

COMPLETE. Five members share Intention/source inputs, exact 001..017 ID sets, repository authority, source scope, evidence allocations, and the sole gate.

<a id="authorizations"></a>
## Authorizations

Authenticated Intention gate PASS. Repository feature-delivery-intelligence is ACTIVE and owner-authenticated at immutable source 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Writes are limited to completed .fdi candidate-base content and repository-root README.md source candidate; branch/PR remains source-owner controlled.

Product-only applicability: `applies_to` is only `product-feature-delivery-intelligence`; the exact intersection is `{product-feature-delivery-intelligence}`.

<a id="preflight-source-scope"></a>
## Preflight source scope

- Selector ID: herm-209-authoritative-design-inputs
- Derivation anchor: `.fdi/features/HERM-209/intention.md#scope`
- Registry read: `.fdi/context/codebase/catalog.md#entities` (registry revision `catalog-v1`)
- Matched ID/lifecycle: feature-delivery-intelligence; ACTIVE
- applies_to: product-feature-delivery-intelligence only; exact impacted-set intersection `{product-feature-delivery-intelligence}`; HERM/System/Component direct applicability explicitly excluded
- Owner/trust/review/successor: Repository owner; owner-authenticated pinned Git; 2026-08-30/2026-11-28; superseded_by none
- Selected projection: `.fdi/context/codebase/repositories/feature-delivery-intelligence.md` (derived after catalog proof)
- Immutable revision/root: repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; docs/superpowers/specs
- Exact paths: docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md; docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md
- Allowed extension/max: .md; 2
- Placeholder validation: no placeholders; normalized repository-relative exact paths under root
- Exclusions: README.md planned new output; every other path; directories; mutable refs; caches; generated/vendor trees; secrets; local/unregistered sources
- Syntax/authority gate: PASS before formal enumeration
- Name-only enumeration: git ls-tree limited to exact paths; concrete count 2
- Cardinality gate: PASS (expected 2; maximum 2); zero/excess would block before content
- Concrete read 1: repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@sha256:31f42a66960ba9502e413587d6344f9772a9148c736eafcb8c93e6144d4d0a3c
- Concrete read 2: repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@sha256:e6639321db931da5bf5c177edf9836157ce4e25250b92ccc27ed406cf91a86c2
- Concrete-match destinations: this section, `.fdi/features/HERM-209/spec/index.md#change-surface-summary`, and every Spec member `.fdi/features/HERM-209/spec/{member}.md#context-consulted`
- Content-read state: COMPLETE after both preflight gates passed

<a id="change-surface-summary"></a>
## Change-surface summary

- Selected repository projection: `.fdi/context/codebase/repositories/feature-delivery-intelligence.md`; registry proof above.
- Transition-3 maximum selected source reads (2): repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md; repo:feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md.
- Recorded local instructions: none at starting revision; authenticated runtime instructions remain external controls.
- Source candidate write (exactly 1): feature-delivery-intelligence:README.md@candidate_head_sha, created new.
- Candidate base content: exact mandatory core + Baseline + Intention + authorization evidence + five Spec members.
- Exclusions: all other source paths, mutable refs, code/config/schema/test/runtime/deployment/data changes, conditional placeholders, B1/B2/B3 execution.
- If another path appears, stop before reading it, record deviation/disposition/proposed blocking state, and re-enter Delivery Spec. This summary is a completed output and did not authorize its own discovery.

<a id="traceability"></a>
## Traceability

Exact bidirectional set: REQ-FRAG-001..017 -> CRIT-001..017 -> REQ/DES/TASK/VV-001..017 -> planned feature-delivery-intelligence:README.md@candidate_head_sha or explicit profile/evidence obligation -> four allocated evidence IDs -> future criterion verdict. No inferred edge.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No blocking Spec gap or deviation. Candidate base/head, PR, Change Set evidence, and independent verdict are intentionally pending their producing transitions.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Product/architecture/repository review: PASS on 2026-08-30. Valid for intention revision intention-v2, source 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482, exact selected content digests, and Skill digests above. Any upstream/source/selector change re-enters Transition 2. Successor: none.

<a id="gate-record"></a>
## Gate record

- Gate: Intention -> Delivery Spec
- Producer: Spec agent
- Skills: context-selection@0.1.1/sha256:da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe; intention-to-spec@0.1.1/sha256:6ff39b93bb65b750e1dacecb7e31a2dc2cc94b159cf2642943a5a14fee6effe6
- Capabilities used: filesystem-read/write; sha256; registry-validate; git-ls-tree; git-show
- Literal-read review: PASS; all fixed paths individually revision-qualified at `.fdi/features/HERM-209/spec/index.md#context-consulted`
- Registry-first review: PASS; catalog read before projection; dedicated empty registries read before zero selections
- Staged selector: syntax/authority PASS -> name-only count 2 -> cardinality PASS -> two exact immutable content reads
- Bundle/mapping/evidence-destination review: PASS; five members, exact 001..017 sets, four fixed evidence IDs
- Preflight: CONTRACT_READY
- Transition execution review: PASS
- Verdict: PASS
- Execution-verified: NOT_CLAIMED (global HERM-209 transitions 3-4 and independent V&V remain pending).
