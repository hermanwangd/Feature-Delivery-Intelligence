# HERM-209 source-diff evidence

<a id="evidence-identity"></a>
## Evidence identity

- Evidence ID: source-diff
- Feature: HERM-209
- Evidence revision: source-diff-v2
- Candidate base/head: f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1/f5871c552e03dfc7a8248f2e4a5e4a4be378e451
- PR: #3 https://github.com/hermanwangd/Feature-Delivery-Intelligence/pull/3

<a id="claim"></a>
## Claim

The completed profile, Intention, and Delivery Spec are committed at candidate_base_sha f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1; candidate_head_sha f5871c552e03dfc7a8248f2e4a5e4a4be378e451 is its immediate child and adds exactly repository-root README.md without changing .fdi.

<a id="method"></a>
## Method

Resolve exact commits; inspect parent and merge-base; verify start-SHA ancestry; run git diff --check; run name-only and name-status diffs; compare .fdi trees with diff --exit-code; verify README absence/presence at base/head; count .fdi files at candidate base; compute SHA-256 over README bytes and the complete patch; observe PR target/head from the authenticated GitHub provider.

<a id="candidate-environment"></a>
## Candidate/environment

- Repository: feature-delivery-intelligence
- branch_base_sha/main base: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- candidate_base_sha: f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1
- candidate_head_sha: f5871c552e03dfc7a8248f2e4a5e4a4be378e451
- candidate environment: immutable local Git objects
- provider environment: GitHub PR #3, target main, head observed before this push 427e7170728b2863a3d5ce290aba3b7e27fdaad1

### Context consulted

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
| repository-local instructions at feature-delivery-intelligence@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 | apply repository-local instructions before source writes | repository projection local-instructions record | `.fdi/context/codebase/repositories/feature-delivery-intelligence.md#local-instructions` read after catalog proof; no repository-local instruction file exists at the pin; authenticated runtime instructions remain external controls | unregistered instruction files, mutable instruction refs, instructions outside the pinned revision |

<a id="observation"></a>
## Observation

- parent line: f5871c552e03dfc7a8248f2e4a5e4a4be378e451 f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1
- start ancestry: git merge-base --is-ancestor 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482 f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1 exit 0
- merge-base(candidate base, candidate head): f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1
- git diff --check: exit 0, empty output
- git diff --name-only: README.md
- git diff --name-status: A\tREADME.md
- .fdi diff exit: 0
- candidate base .fdi file count: 42
- README at candidate base: absent
- README at candidate head: present
- validator herm-209-conformance-v4 phase base: 34/34 PASS, result digest 18d316167e99959ba045f82213328c16a39f546170962ace050ff6d0858e5b2e
- validator herm-209-conformance-v4 phase candidate: 40/40 PASS, result digest 8faea2cabb7735c3a02cf3f45d4c75452bb5f36ebc359955dc41517e0000c7f6
- PR #3 pre-push snapshot: OPEN, target main@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482, head 427e7170728b2863a3d5ce290aba3b7e27fdaad1, mergeable/clean, no provider checks

<a id="result"></a>
## Result

PASS as producer evidence for candidate adjacency, exact README-only source diff, and PR identity. This result does not substitute for independent V&V or final PR-head evidence.

<a id="integrity-and-access"></a>
## Integrity and access

- README SHA-256: b70df44cd74b11d2588519e892ec76c60ddd9acb9bacd418a589c23ddcd68538
- candidate patch SHA-256: 3e6970c1f3571c35fbfd0f9dbbf6655a91037987847979df72537eb7287327d6
- Git object IDs are immutable.
- Provider observation used authenticated CLI access.
- Raw credentials/provider tokens and user-local paths are excluded.

<a id="producer-and-owner"></a>
## Producer and owner

Producer: implementation agent (corrective run under Advanced Backend Builder). Source/branch/PR owner: Repository owner. Evidence owner: HERM-209 Change Set. Independent reproduction owner: Transition 4 V&V agent.

<a id="limitations"></a>
## Limitations

Provider state can change after observation; the final PR head is this evidence's later coordination-record commit and must be recorded externally. No CI check existed at the pre-push snapshot. No release/runtime/B1/B2/B3 claim.

<a id="validity-expiry-and-supersession"></a>
## Validity, expiry, and supersession

VALID only for candidate pair f0aaf1713a3dd4fbd2b9e4db3f5978e6a2df7da1..f5871c552e03dfc7a8248f2e4a5e4a4be378e451 and exact Git objects. Invalidated by rewritten/unresolvable objects or mismatch. PR snapshot expires when provider head/state changes; successor is the final external PR-head observation. Backlinks: .fdi/features/HERM-209/spec/vv-plan.md#evidence-destinations and .fdi/features/HERM-209/change-set/index.md#gate-record.
