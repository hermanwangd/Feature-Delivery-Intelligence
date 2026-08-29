# HERM-209 Intention

<a id="artifact-identity"></a>
## Artifact identity

- Feature key: HERM-209
- Logical artifact: Intention
- Bundle members: request.md and intention.md
- Artifact revision: intention-v1
- Producer: Intention agent (same producer as request.md)
- Input request: request.md@sha256:e521ee446d2714b891147d09a9d0957ac229bcc1c417bfd95699391c6ff64b62

<a id="inputs"></a>
## Inputs

- .fdi/features/HERM-209/request.md@sha256:e521ee446d2714b891147d09a9d0957ac229bcc1c417bfd95699391c6ff64b62
- Authenticated issue 01a04e70-c387-72a2-bf4e-f97db187c8db revision 5@sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Authenticated trigger 01a04eca-8fc6-722b-a903-1934b48a1897 revision 1@sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6

<a id="context-consulted"></a>
## Context consulted

| Consulted path@revision | Mode | Authority/trust | Purpose/selection proof | Result |
| --- | --- | --- | --- | --- |
| .fdi/README.md@sha256:fadbd405a33b7d440df9b60f27647614bbb2c2c9eb5b852499c04d8037db727a | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/index.md@sha256:67b01c0f28649da22e1ffb70c899e69dd7a0f291445f06333b10137e7a569bde | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/product.md@sha256:c0c8bcc3d1c6f33e53263184ea5d569495475f627264ed471f961fad255cb97f | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/tech.md@sha256:9cd3f7e53fbe030ae16ab5d9058e72eb1d39a1de508946132dbc76b68995fe84 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/structure.md@sha256:8a95e6bf54dd74416ca71e3555f93fadc41f2a02ba5e3da04cb368264493a3aa | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/architecture.md@sha256:1cb3143c9a7bfcbbb5534ce399485c04c8a407cc92e4ffdcfa039543bb388bcd | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/agent-policy.md@sha256:27c84ed4e418f92bf7d2ff65d22bbf327da01be4c384a3a97159e8538dc33c85 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/delivery.md@sha256:c56e06b23966b27823cab55d07f0c1509d5ae32d4effa34d5b9e5dece823a5a3 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/steering/governance.md@sha256:c50acafe71ae655eeb0f1ae177a8134c7a58987f927498ca467af617627beef0 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/domain/glossary.md@sha256:328369bdec1b0377a5b2e077888267175ca87b6acc6cd8c74490090b046d550c | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/domain/rules.md@sha256:c8e2ad06ad1e0640da456d0b860048fe8fe282a54403e77c52ecbbbe00b51f34 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/codebase/catalog.md@sha256:a592034ac750e796d78f05137c2e030a36e3d2754b723437eceec99aabdd509a | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/codebase/relations.md@sha256:820c3b5df3ddac87c58e6f7f3999cd93ec50969fbbe283cf3d3ad51630153696 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/knowledge/index.md@sha256:f76a43ac06ca26050ce98086bd026506222fd78ef694f8766dff67e63eeeb156 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/external/references.md@sha256:6a224a8f41eeacdd907f7872055b2e37b1ad05521ac132970c98f0729abb5010 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/baseline/catalog.md@sha256:3a66b988d1bf7a715da3e2ea38737db304995dba9d5641957128ab423eb29694 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/skills/catalog.md@sha256:9aba4e502a42b1651b6e0e3070d725c583bb1ea82b60a38d691306b958628d25 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/skills/context-selection/SKILL.md@sha256:e327dcc6ecfcdbf2085762c8b1883a59aeabdd5beac35f687c1c1eec001524b8 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/skills/human-to-intention/SKILL.md@sha256:079f0e209b4787b3bc21f83fd4f94de5a9775326c6f560c6be118588d1ca3b47 | literal | adopted profile/procedure | required for authenticated capture or registry-first selection | selected |
| .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:a72aec299a1517df6c08b6ff089aff9fe58f7f591ad3634e1246d3bc0de56af4 | selected after catalog | derived navigation; trusted after digest/review | catalog@sha256:a592034ac750e796d78f05137c2e030a36e3d2754b723437eceec99aabdd509a; ID feature-delivery-intelligence; ACTIVE; applies_to product-feature-delivery-intelligence/HERM-209; owner Repository owner; reviewed 2026-08-30; next 2026-11-28; superseded_by none; digest matched; reason repository seed; source copies/mutable refs excluded | selected |
| knowledge/external/Baseline/extensions | registry exclusion | explanatory/support only | knowledge index@sha256:f76a43ac06ca26050ce98086bd026506222fd78ef694f8766dff67e63eeeb156; external registry@sha256:6a224a8f41eeacdd907f7872055b2e37b1ad05521ac132970c98f0729abb5010; Baseline catalog@sha256:3a66b988d1bf7a715da3e2ea38737db304995dba9d5641957128ab423eb29694; Context index@sha256:67b01c0f28649da22e1ffb70c899e69dd7a0f291445f06333b10137e7a569bde; no ACTIVE applicable leaf; all conditional leaves excluded; zero match is valid | none selected |

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

<a id="authorization"></a>
## Authorization

Authorized desired-behavior scope: authenticated HERM-209 issue revision 5 plus explicit start trigger revision 1. Evidence: intention-authorization.md@sha256:c0fa7d1627a72fd41b6f3e1ba48f7c376c8b6a5142a56381e4cb4cee38e8921e. Source/topology truth still requires pinned design/Git evidence; verdict authority remains independent.

<a id="traceability"></a>
## Traceability

Every REQ-FRAG-001..016 maps one-to-one to CRIT-001..016 above. Following mapping is .fdi/features/HERM-209/spec/index.md#intention-mapping; no downstream link is inferred.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

None blocking at Intention. Repository-root README does not exist at the starting revision and is explicitly a planned new output, not a current source read.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Product authorization: authenticated issue/trigger. Review state: PASS on 2026-08-30. Valid for request@sha256:e521ee446d2714b891147d09a9d0957ac229bcc1c417bfd95699391c6ff64b62. Invalidated by upstream revision, revoked scope, or failed gate. Predecessor: request-v1; successor: none.

<a id="gate-record"></a>
## Gate record

- Gate: Human -> Intention
- Producer: Intention agent
- Skills: context-selection@sha256:e327dcc6ecfcdbf2085762c8b1883a59aeabdd5beac35f687c1c1eec001524b8; human-to-intention@sha256:079f0e209b4787b3bc21f83fd4f94de5a9775326c6f560c6be118588d1ca3b47
- Capabilities: capability.multica-issue-read; capability.filesystem-read; capability.sha256; capability.registry-validate; capability.filesystem-write
- Preflight: CONTRACT_READY
- Selection proof: .fdi/context/codebase/catalog.md read before repository projection; dedicated empty registries read before zero selection; details at #context-consulted.
- Evidence: .fdi/features/HERM-209/evidence/intention-authorization.md@sha256:c0fa7d1627a72fd41b6f3e1ba48f7c376c8b6a5142a56381e4cb4cee38e8921e
- Transition execution review: PASS for capture, redaction, literal reads, registry-first selection, criteria, bundle membership, and sole-gate mapping.
- Verdict: PASS
- Execution-verified: NOT_CLAIMED (global HERM-209 transitions 2-4 and independent V&V remain pending).
