# HERM-209 Intention

<a id="artifact-identity"></a>
## Artifact identity

- Feature key: HERM-209
- Logical artifact: Intention
- Bundle members: request.md and intention.md
- Artifact revision: intention-v2 (reissued after independent-review re-entry)
- Producer: Intention agent (same producer as request.md)
- Input request: `.fdi/features/HERM-209/request.md#artifact-identity`; request revision: request-v2

<a id="inputs"></a>
## Inputs

- `.fdi/features/HERM-209/request.md#artifact-identity`; request revision: request-v2
- Authenticated issue 01a04e70-c387-72a2-bf4e-f97db187c8db revision 5@sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Authenticated trigger 01a04eca-8fc6-722b-a903-1934b48a1897 revision 1@sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6
- Independent-review re-entry authority 01a04ee7-acea-798e-846a-a5de98a97349 revision 1@sha256:7574e8ec5345a239fff2098686cd9c92c33901ca7b1ec52c8eb3afb5e43a52e7
- Corrective supplement 01a04eea-1752-74bd-b9f2-345947574cf2 revision 1@sha256:6671245a74ac6fab4b93a85bd6c1974959eae6835f54e6a0b87b3a89b556b6d8

<a id="context-consulted"></a>
## Context consulted

| Consulted path@revision | Purpose | Authority/trust | Selection proof | Exclusions |
| --- | --- | --- | --- | --- |
| .fdi/README.md@sha256:fadbd405a33b7d440df9b60f27647614bbb2c2c9eb5b852499c04d8037db727a | confirm adopted profile and starting revision | adopted profile; governance-owned | literal fixed read; exact bytes resolved; one ACTIVE adopted-profile row | mutable refs, unsafe payloads, unrelated and superseded material, future revisions |
| .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000 | apply profile schemas, selectors, and anchors | normative adopted-profile contract | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered extensions, future/superseded contract versions |
| .fdi/context/index.md@sha256:67b01c0f28649da22e1ffb70c899e69dd7a0f291445f06333b10137e7a569bde | validate extensions/views/areas/runbooks | canonical conditional registry | literal fixed registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, and planned-as-current leaves |
| .fdi/context/steering/product.md@sha256:c0c8bcc3d1c6f33e53263184ea5d569495475f627264ed471f961fad255cb97f | constrain product outcome and scope | normative product-owner Steering | literal fixed read; exact bytes resolved | source copies, mutable refs, superseded product guidance, unregistered steering material |
| .fdi/context/steering/tech.md@sha256:9cd3f7e53fbe030ae16ab5d9058e72eb1d39a1de508946132dbc76b68995fe84 | apply technical and dependency constraints | normative architecture/security Steering | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered constraints, draft/exceptions without approval |
| .fdi/context/steering/structure.md@sha256:3cf35ff0e05565bcd465396e165e720d0ad44ac7588e5096cb353ce99b824f10 | apply placement, naming, and instruction precedence | normative organization policy | literal fixed read; exact bytes resolved | source copies, mutable refs, topology claims outside catalog/relations, unregistered placement |
| .fdi/context/steering/architecture.md@sha256:1cb3143c9a7bfcbbb5534ce399485c04c8a407cc92e4ffdcfa039543bb388bcd | apply boundaries and quality constraints | normative architecture policy | literal fixed read; exact bytes resolved | source copies, mutable refs, unapproved exceptions, unregistered architecture material |
| .fdi/context/steering/agent-policy.md@sha256:27c84ed4e418f92bf7d2ff65d22bbf327da01be4c384a3a97159e8538dc33c85 | apply autonomy, redaction, and permission limits | normative governance/security policy | literal fixed read; exact bytes resolved | source copies, mutable refs, permissions beyond policy, unregistered agent instructions |
| .fdi/context/steering/delivery.md@sha256:c56e06b23966b27823cab55d07f0c1509d5ae32d4effa34d5b9e5dece823a5a3 | apply gates, evidence, and re-entry | normative delivery policy | literal fixed read; exact bytes resolved | source copies, mutable refs, collapsed gates, unregistered delivery instructions |
| .fdi/context/steering/governance.md@sha256:c50acafe71ae655eeb0f1ae177a8134c7a58987f927498ca467af617627beef0 | resolve owners and authority | normative governance policy | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered owners, mutable authority claims |
| .fdi/context/domain/glossary.md@sha256:328369bdec1b0377a5b2e077888267175ca87b6acc6cd8c74490090b046d550c | normalize terms | definitional Domain Context | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered terms, conflicting aliases |
| .fdi/context/domain/rules.md@sha256:c8e2ad06ad1e0640da456d0b860048fe8fe282a54403e77c52ecbbbe00b51f34 | check invariants | normative Domain Context | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered invariants, exceptions without approval |
| .fdi/context/codebase/catalog.md@sha256:9220e21cbab2f61db7de552bebd7a42a419ef8bd578760500e902eebcaa01060 | resolve entities and repository registry | canonical entity registry `catalog-v1` | literal fixed registry read before projection; exact bytes resolved; ACTIVE/non-superseded | planned entities, source copies, mutable refs, unregistered paths, future registry revisions |
| .fdi/context/codebase/relations.md@sha256:1a5603cb06b27d3c2665ab373a1e51c2064735a377e2b529b3a7eddb54d802cd | resolve current relations | canonical relation registry `relations-v1` | literal fixed read; no planned relation selected | planned relations, source copies, mutable refs, unregistered paths, future registry revisions |
| .fdi/context/knowledge/index.md@sha256:f76a43ac06ca26050ce98086bd026506222fd78ef694f8766dff67e63eeeb156 | perform Knowledge selection | retrieval-only registry | literal registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/context/external/references.md@sha256:6a224a8f41eeacdd907f7872055b2e37b1ad05521ac132970c98f0729abb5010 | perform external-review selection | sole external registry | literal registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/baseline/catalog.md@sha256:3a66b988d1bf7a715da3e2ea38737db304995dba9d5641957128ab423eb29694 | perform Baseline selection | sole Baseline registry | literal registry read; empty capability table; zero selection | active or unsupported capabilities, source copies, mutable refs, unregistered baseline paths |
| .fdi/skills/catalog.md@sha256:0eecbf6118e6836a241f941560940f969f054ec59a85e49808928150f4e27cc0 | validate Skill versions/digests | canonical Skill registry | literal registry read before exact Skill files; rows ACTIVE/current/non-superseded | inactive, superseded, unregistered, or digest-mismatched Skill rows |
| .fdi/skills/context-selection/SKILL.md@sha256:da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe | govern registry-first selection | active executable Context v0.1.1 | literal fixed read after catalog validation; no Skill resource selected | source copies, mutable refs, unregistered skills, draft skill versions |
| .fdi/skills/human-to-intention/SKILL.md@sha256:f48c36bfb5fcf7ca00b048d25cc4e929748a79609d337a690a9fa43b2b80e52f | govern T1 production | active transition procedure v0.1.1 | literal fixed read after catalog validation; exact allowed writes checked | source copies, mutable refs, unregistered skills, draft skill versions, disallowed writes |
| .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:8aa0596904e2799b421194329f022d02ffbcf254acab4bca3fa3c9a5615cf8f5 | obtain repository boundary/navigation | derived projection after registry proof | `.fdi/context/codebase/catalog.md#entities` read first (registry revision `catalog-v1`); row ACTIVE, owner-authenticated, reviewed 2026-08-30, next 2026-11-28, `superseded_by` none, digest matched; row `applies_to` and impacted set intersect only on `{product-feature-delivery-intelligence}`; HERM/System/Component direct applicability excluded | source copies, mutable refs, unregistered paths, future/superseded registry revisions |

<a id="rationale"></a>
## Rationale

Contributors and agents need an adopted, physically reviewable coordination profile and a safe root entry point so feature intent can be converted into complete, evidence-backed implementation work without hidden repository or authority assumptions.

<a id="stakeholders"></a>
## Stakeholders

Product owner; FDI governance/architecture/security/delivery/release owners; repository owner; contributors; transition agents; independent V&V agent.

<a id="outcome"></a>
## Outcome

A conforming .fdi mandatory core, honest empty Baseline, fully traced HERM-209 pilot, and source-owned root README candidate are reviewable in a linked PR with exact immutable evidence and an independent verdict.

<a id="use-scenarios"></a>
## Use scenarios

1. A contributor opens README and learns purpose/workflow/start steps/design links/boundaries. 2. An agent selects only current registry-backed Context and exact pinned source. 3. A reviewer navigates request -> criteria -> Spec -> README candidate -> evidence/verdict. 4. A future post-release event can invoke but cannot collapse B3a/B3b.

<a id="scope"></a>
## Scope

In scope: one Product, one coordination System, one documentation Component, Repository feature-delivery-intelligence; mandatory .fdi core; Baseline initialization; four canonical HERM-209 transitions; repository-root README; one GitHub PR. Multi-repository support is preserved by contract, but execution is one repository/documentation only.

<a id="impacted-entity-candidates"></a>
## Impacted entity candidates

Current seeds: product-feature-delivery-intelligence; system-fdi-coordination; component-fdi-documentation; feature-delivery-intelligence. Planned source path: feature-delivery-intelligence:README.md at a future candidate head. No planned topology relation is required.

<a id="constraints"></a>
## Constraints

Exact profile start 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; literal path contracts; registry-first conditional reads; stable anchors; exact Skill bindings/digests; candidate base/head adjacency; README-only source diff; independent V&V; B1/B2/B3 NOT_INVOKED; release NOT_OBSERVED.

<a id="non-goals"></a>
## Non-goals

FDI platform/control plane; runtime service; manifest ledger; universal schema; fifth stage; historical feature fabrication; bulk Knowledge/Baseline; multi-source-repository execution; deployment/release; B1/B2/B3 execution; product-wide future verification claim.

<a id="success-criteria"></a>
## Success criteria

| Criterion | Request fragment | Measurable outcome | Authority | Validation class |
| --- | --- | --- | --- | --- |
| CRIT-001 | REQ-FRAG-001 | Start dependencies, immutable PR #1 merge SHA, and immutable HERM-209 input revision are recorded at required destinations. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-002 | REQ-FRAG-002 | Every mandatory core file exists and conforms without secret, local absolute path, copied source, or fabricated evidence; adoption is ADOPTED. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-003 | REQ-FRAG-003 | Every cross-file target uses an explicit stable lowercase kebab-case anchor and no generated/numbered authority fragment. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-004 | REQ-FRAG-004 | Catalog and relations are sole current-topology registries; structure is placement policy; planned relations are never current Context. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-005 | REQ-FRAG-005 | Every conditional selection is registry-first with lifecycle, applicability, freshness, successor, trust, path/digest, reason, and exclusions; no placeholder exists. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-006 | REQ-FRAG-006 | Eight core Skills are ACTIVE, versioned, current, cataloged, digest-resolvable, bound, permissioned, and provenance-complete. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-007 | REQ-FRAG-007 | Refresh Skill separates B3a/B3b and permits atomic adoption only after independent PASS; HERM-209 does not execute B3. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-008 | REQ-FRAG-008 | Baseline honestly records pinned empty/staged state; no unsupported capability or B1/B2/B3/VERIFIED-AS-IS claim exists. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-009 | REQ-FRAG-009 | Request and intention form one authenticated, redacted, reviewable, criterion-mapped bundle with one producer and sole gate. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-010 | REQ-FRAG-010 | Transition 2 writes/passes preflight source scope before bounded content reads and never self-authorizes from final change surface. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-011 | REQ-FRAG-011 | All four canonical transitions execute in order with literal/selected reads, writes, Context revisions, exclusions, mappings, evidence, and gate reviews. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-012 | REQ-FRAG-012 | Completed profile/Intention/Spec is candidate base and its immediate child changes exactly repository-root README.md. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-013 | REQ-FRAG-013 | Every Change Set deviation has disposition and proposed blocking state before V&V; PASS has no unresolved blocker. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-014 | REQ-FRAG-014 | Repository-root README satisfies its contract and all fresh local validation checks pass. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-015 | REQ-FRAG-015 | Bidirectional traceability is explicit from authenticated fragment through criterion/Spec/candidate/evidence/verdict. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-016 | REQ-FRAG-016 | Independent V&V records separate verification/validation, per-criterion/overall verdict, earliest re-entry, and truthful execution claim. | Product owner through authenticated issue revision | measurable by planned V&V |
| CRIT-017 | REQ-FRAG-017 | A HERM-209-linked PR targets `main`, distinguishes corrected `candidate_base_sha`, `candidate_head_sha`, and current PR head, records exact verification commands/results and remaining gaps, and is not merged unless the independent overall verdict is `PASS`. | Product owner through authenticated issue revision | measurable by planned V&V |

<a id="authorization"></a>
## Authorization

Authorized desired-behavior scope: captured immutable HERM-209 issue revision 5 plus explicit start trigger revision 1. Evidence: `.fdi/features/HERM-209/evidence/intention-authorization.md#evidence-identity`; evidence revision: intention-authorization-v2. Corrective comments re-entered T1/T2 but did not replace Human intent. Source/topology truth still requires pinned design/Git evidence; verdict authority remains independent.

<a id="traceability"></a>
## Traceability

Every REQ-FRAG-001..017 maps one-to-one to CRIT-001..017 above. Following mapping is `.fdi/features/HERM-209/spec/index.md#intention-mapping`; no downstream link is inferred.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

None blocking after corrective re-entry. Repository-root README does not exist at the starting revision and is a planned new output, not a current source read. Intention-v1 and its downstream T2/T3 artifacts are rejected and superseded; their commits remain only as forward-only audit history.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Product authorization: captured issue/trigger. Independent-review re-entry authority: 01a04ee7-acea-798e-846a-a5de98a97349/1 with supplement 01a04eea-1752-74bd-b9f2-345947574cf2/1. Review state: reissued PASS on 2026-08-30 for request-v2 and all 17 criteria. Invalidated by authenticated replacement/revocation, failed gate, or upstream revision. Supersedes: intention-v1. Successor: none.

<a id="gate-record"></a>
## Gate record

- Gate: Human -> Intention
- Producer: Intention agent
- Re-entry authority: corrective comment 01a04ee7-acea-798e-846a-a5de98a97349/1 invalidated intention-v1; this record is the reissued sole T1 gate.
- Skills: context-selection@0.1.1/sha256:da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe; human-to-intention@0.1.1/sha256:f48c36bfb5fcf7ca00b048d25cc4e929748a79609d337a690a9fa43b2b80e52f
- Capabilities: capability.multica-issue-read; capability.filesystem-read; capability.sha256; capability.registry-validate; capability.filesystem-write
- Preflight: CONTRACT_READY
- Selection proof: `.fdi/context/codebase/catalog.md#entities` read before the repository projection (registry revision `catalog-v1`); Product-only applicability intersection reproduced; dedicated registries read before zero selection; concrete read rows and exclusions are recorded in `.fdi/features/HERM-209/intention.md#context-consulted`.
- Evidence: `.fdi/features/HERM-209/evidence/intention-authorization.md#evidence-identity`; evidence revision: intention-authorization-v2
- Transition execution review: PASS for preserved capture, exact LF-inclusive digest reproduction, redaction, every literal read, registry-first selection, 17 criteria, bundle membership, and sole-gate mapping.
- Criterion/gate count: 17/17 mapped; one sole gate in this file; request gate remains backlink-only.
- Verdict: PASS
- Execution-verified: NOT_CLAIMED (global HERM-209 transitions 2-4 and independent V&V remain pending).
