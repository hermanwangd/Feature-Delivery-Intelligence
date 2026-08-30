# HERM-209 authenticated request

<a id="artifact-identity"></a>
## Artifact identity

- Feature key: HERM-209
- Logical artifact: Intention (supporting authenticated-input member)
- Artifact revision: request-v2 (request-v1 invalidated by corrective review and superseded in place)
- Producer: Intention agent
- Profile starting revision: 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Issue ID/revision: 01a04e70-c387-72a2-bf4e-f97db187c8db/5
- Trigger ID/revision: 01a04eca-8fc6-722b-a903-1934b48a1897/1

<a id="inputs"></a>
## Inputs

- Authenticated issue safe canonical payload@sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Authenticated trigger safe canonical payload@sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6
- Independent-review re-entry authority 01a04ee7-acea-798e-846a-a5de98a97349 revision 1@sha256:7574e8ec5345a239fff2098686cd9c92c33901ca7b1ec52c8eb3afb5e43a52e7
- Corrective supplement 01a04eea-1752-74bd-b9f2-345947574cf2 revision 1@sha256:6671245a74ac6fab4b93a85bd6c1974959eae6835f54e6a0b87b3a89b556b6d8
- Received: 2026-08-29T18:31:33Z
- Assurance: workspace-scoped authenticated Multica CLI/API response; immutable ID+revision capture

<a id="context-consulted"></a>
## Context consulted

| Consulted path@revision | Purpose | Authority/trust | Selection proof | Exclusions |
| --- | --- | --- | --- | --- |
| .fdi/README.md@sha256:fadbd405a33b7d440df9b60f27647614bbb2c2c9eb5b852499c04d8037db727a | confirm adopted profile and starting revision | adopted profile; governance-owned | literal fixed read; exact bytes resolved; one ACTIVE adopted-profile row | mutable refs, unsafe payloads, unrelated and superseded material, future revisions |
| .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000 | apply profile schemas, selectors, and anchors | normative adopted-profile contract | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered extensions, future/superseded contract versions |
| .fdi/context/index.md@sha256:67b01c0f28649da22e1ffb70c899e69dd7a0f291445f06333b10137e7a569bde | validate extension/view/area/runbook registry | canonical conditional registry | literal fixed registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, and planned-as-current leaves |
| .fdi/context/steering/product.md@sha256:c0c8bcc3d1c6f33e53263184ea5d569495475f627264ed471f961fad255cb97f | constrain product outcome and scope | normative product-owner Steering | literal fixed read; exact bytes resolved | source copies, mutable refs, superseded product guidance, unregistered steering material |
| .fdi/context/steering/tech.md@sha256:9cd3f7e53fbe030ae16ab5d9058e72eb1d39a1de508946132dbc76b68995fe84 | apply technical and dependency constraints | normative architecture/security Steering | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered constraints, draft/exceptions without approval |
| .fdi/context/steering/structure.md@sha256:3cf35ff0e05565bcd465396e165e720d0ad44ac7588e5096cb353ce99b824f10 | apply placement, naming, and instruction precedence | normative organization policy | literal fixed read; exact bytes resolved | source copies, mutable refs, topology claims outside catalog/relations, unregistered placement |
| .fdi/context/steering/architecture.md@sha256:1cb3143c9a7bfcbbb5534ce399485c04c8a407cc92e4ffdcfa039543bb388bcd | apply boundaries and quality constraints | normative architecture policy | literal fixed read; exact bytes resolved | source copies, mutable refs, unapproved exceptions, unregistered architecture material |
| .fdi/context/steering/agent-policy.md@sha256:27c84ed4e418f92bf7d2ff65d22bbf327da01be4c384a3a97159e8538dc33c85 | apply autonomy, redaction, and permission limits | normative governance/security policy | literal fixed read; exact bytes resolved | source copies, mutable refs, permissions beyond policy, unregistered agent instructions |
| .fdi/context/steering/delivery.md@sha256:c56e06b23966b27823cab55d07f0c1509d5ae32d4effa34d5b9e5dece823a5a3 | apply four-transition gates, evidence, and re-entry | normative delivery policy | literal fixed read; exact bytes resolved | source copies, mutable refs, collapsed gates, unregistered delivery instructions |
| .fdi/context/steering/governance.md@sha256:c50acafe71ae655eeb0f1ae177a8134c7a58987f927498ca467af617627beef0 | resolve owners, authority, cadence, and conflicts | normative governance policy | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered owners, mutable authority claims |
| .fdi/context/domain/glossary.md@sha256:328369bdec1b0377a5b2e077888267175ca87b6acc6cd8c74490090b046d550c | normalize feature and entity terms | definitional Domain Context | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered terms, conflicting aliases |
| .fdi/context/domain/rules.md@sha256:c8e2ad06ad1e0640da456d0b860048fe8fe282a54403e77c52ecbbbe00b51f34 | check durable product invariants | normative Domain Context | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered invariants, exceptions without approval |
| .fdi/context/codebase/catalog.md@sha256:9220e21cbab2f61db7de552bebd7a42a419ef8bd578760500e902eebcaa01060 | resolve current entities and repository projection registry | canonical current entity registry `catalog-v1` | literal fixed registry read before projection; exact bytes resolved; ACTIVE/non-superseded | planned entities, source copies, mutable refs, unregistered paths, future registry revisions |
| .fdi/context/codebase/relations.md@sha256:1a5603cb06b27d3c2665ab373a1e51c2064735a377e2b529b3a7eddb54d802cd | resolve evidence-backed current relations | canonical current relation registry `relations-v1` | literal fixed read; no planned relation selected | planned relations, source copies, mutable refs, unregistered paths, future registry revisions |
| .fdi/context/knowledge/index.md@sha256:f76a43ac06ca26050ce98086bd026506222fd78ef694f8766dff67e63eeeb156 | perform registry-first Knowledge selection | retrieval-only Knowledge registry | literal registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/context/external/references.md@sha256:6a224a8f41eeacdd907f7872055b2e37b1ad05521ac132970c98f0729abb5010 | perform registry-first external-review selection | sole external-review registry | literal registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/baseline/catalog.md@sha256:3a66b988d1bf7a715da3e2ea38737db304995dba9d5641957128ab423eb29694 | perform registry-first Baseline selection | sole Baseline capability registry | literal registry read; empty capability table; zero selection | active or unsupported capabilities, source copies, mutable refs, unregistered baseline paths |
| .fdi/skills/catalog.md@sha256:0eecbf6118e6836a241f941560940f969f054ec59a85e49808928150f4e27cc0 | validate active Skill versions and digests | canonical Skill registry | literal registry read before exact Skill files; all required rows ACTIVE/current/non-superseded | inactive, superseded, unregistered, or digest-mismatched Skill rows |
| .fdi/skills/context-selection/SKILL.md@sha256:da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe | govern bounded registry-first selection | active executable Context v0.1.1 | literal fixed read after Skill catalog validation; no Skill resource selected | source copies, mutable refs, unregistered skills, draft skill versions |
| .fdi/skills/human-to-intention/SKILL.md@sha256:f48c36bfb5fcf7ca00b048d25cc4e929748a79609d337a690a9fa43b2b80e52f | govern authenticated capture and Intention production | active transition procedure v0.1.1 | literal fixed read after Skill catalog validation; exact allowed writes checked | source copies, mutable refs, unregistered skills, draft skill versions, disallowed writes |
| .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:8aa0596904e2799b421194329f022d02ffbcf254acab4bca3fa3c9a5615cf8f5 | obtain repository navigation and authority boundary | derived projection; trusted only after registry proof | `.fdi/context/codebase/catalog.md#entities` read first (registry revision `catalog-v1`); row `feature-delivery-intelligence` is ACTIVE, owner-authenticated, reviewed 2026-08-30, next review 2026-11-28, `superseded_by` none, digest matched; row `applies_to` is only `product-feature-delivery-intelligence`, impacted set contains that Product, exact intersection is `{product-feature-delivery-intelligence}` | HERM/System/Component as direct applicability, source copies, mutable refs, unregistered paths, future/superseded registry revisions |

<a id="human-signal"></a>
## Human signal

Authenticated desired-behavior source: captured immutable HERM-209 issue revision 5 and explicit start trigger revision 1, received 2026-08-29T18:31:33Z. Current issue revisions are not replacement Human requests. Corrective comments are independent-review re-entry authority, not replacement Human intent. Raw payload is not copied.

<a id="requester"></a>
## Requester

Workspace-authorized product intent represented by the authenticated Multica issue workflow. Initiating actor type: agent acting within workspace authority. No personal identity or email is persisted or inferred.

<a id="capture-authentication"></a>
## Capture authentication

- Method: authenticated multica issue/comment reads.
- Assurance: workspace-scoped access, stable IDs, explicit revisions, provider timestamps.
- Issue projection: `{id,revision,title,description,updated_at}` from the authenticated revision-5 response (`updated_at` `2026-08-29T18:31:33Z`). Command: `jq -cS '{id,revision,title,description,updated_at}' | shasum -a 256`. `jq -cS` serializes one compact key-sorted UTF-8 JSON line and emits a trailing LF; the SHA-256 input includes that LF. Reproduced digest: `4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7`.
- Trigger projection: `{id,revision,content,created_at,author_id,author_type}` from comment revision 1. Command: `jq -cS '{id,revision,content,created_at,author_id,author_type}' | shasum -a 256`. UTF-8 and the emitted trailing LF are included. Reproduced digest: `122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6`.
- Corrective comments use the same safe comment projection and LF-inclusive serialization; their digests are recorded under Inputs. They invalidate/re-enter artifacts but do not alter the captured Human projection.
- Redaction: credentials, email, transport/auth material, and unsafe raw payload excluded.

<a id="requested-change"></a>
## Requested change

Adopt the approved coordination profile, materialize the exact mandatory .fdi core and honest Baseline, execute the four HERM-209 transitions, create a repository-root README contributor entry point, produce adjacent candidate commits and PR, and obtain an independent evidence-backed V&V verdict.

<a id="constraints"></a>
## Constraints

Preserve taxonomy, authority, provenance, registry-first selection, Skill/Tool boundaries, literal paths, B3a/B3b separation, and multi-repository ownership. Use immutable source SHA 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Do not execute B1/B2/B3, fabricate evidence, read mutable source, create placeholders, or self-award Execution-verified.

<a id="source-references"></a>
## Source references

- Issue 01a04e70-c387-72a2-bf4e-f97db187c8db revision 5@sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Trigger 01a04eca-8fc6-722b-a903-1934b48a1897 revision 1@sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6
- Independent-review re-entry authority 01a04ee7-acea-798e-846a-a5de98a97349 revision 1@sha256:7574e8ec5345a239fff2098686cd9c92c33901ca7b1ec52c8eb3afb5e43a52e7
- Corrective supplement 01a04eea-1752-74bd-b9f2-345947574cf2 revision 1@sha256:6671245a74ac6fab4b93a85bd6c1974959eae6835f54e6a0b87b3a89b556b6d8
- Profile start 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Request artifact `.fdi/features/HERM-209/request.md#artifact-identity`; artifact revision: request-v2
- Authorization evidence `.fdi/features/HERM-209/evidence/intention-authorization.md#evidence-identity`; evidence revision: intention-authorization-v2

<a id="ambiguities"></a>
## Ambiguities

None blocking. The same repository has coordination and source roles in this one-repository pilot, while authority remains explicitly separate. Final execution-verification status is reserved to the independent evidence gate.

<a id="traceability"></a>
## Traceability

| Request fragment | Intention criterion | Captured obligation |
| --- | --- | --- |
| REQ-FRAG-001 | CRIT-001 | Start dependencies, immutable PR #1 merge SHA, and immutable HERM-209 input revision are recorded at required destinations. |
| REQ-FRAG-002 | CRIT-002 | Every mandatory core file exists and conforms without secret, local absolute path, copied source, or fabricated evidence; adoption is ADOPTED. |
| REQ-FRAG-003 | CRIT-003 | Every cross-file target uses an explicit stable lowercase kebab-case anchor and no generated/numbered authority fragment. |
| REQ-FRAG-004 | CRIT-004 | Catalog and relations are sole current-topology registries; structure is placement policy; planned relations are never current Context. |
| REQ-FRAG-005 | CRIT-005 | Every conditional selection is registry-first with lifecycle, applicability, freshness, successor, trust, path/digest, reason, and exclusions; no placeholder exists. |
| REQ-FRAG-006 | CRIT-006 | Eight core Skills are ACTIVE, versioned, current, cataloged, digest-resolvable, bound, permissioned, and provenance-complete. |
| REQ-FRAG-007 | CRIT-007 | Refresh Skill separates B3a/B3b and permits atomic adoption only after independent PASS; HERM-209 does not execute B3. |
| REQ-FRAG-008 | CRIT-008 | Baseline honestly records pinned empty/staged state; no unsupported capability or B1/B2/B3/VERIFIED-AS-IS claim exists. |
| REQ-FRAG-009 | CRIT-009 | Request and intention form one authenticated, redacted, reviewable, criterion-mapped bundle with one producer and sole gate. |
| REQ-FRAG-010 | CRIT-010 | Transition 2 writes/passes preflight source scope before bounded content reads and never self-authorizes from final change surface. |
| REQ-FRAG-011 | CRIT-011 | All four canonical transitions execute in order with literal/selected reads, writes, Context revisions, exclusions, mappings, evidence, and gate reviews. |
| REQ-FRAG-012 | CRIT-012 | Completed profile/Intention/Spec is candidate base and its immediate child changes exactly repository-root README.md. |
| REQ-FRAG-013 | CRIT-013 | Every Change Set deviation has disposition and proposed blocking state before V&V; PASS has no unresolved blocker. |
| REQ-FRAG-014 | CRIT-014 | Repository-root README satisfies its contract and all fresh local validation checks pass. |
| REQ-FRAG-015 | CRIT-015 | Bidirectional traceability is explicit from authenticated fragment through criterion/Spec/candidate/evidence/verdict. |
| REQ-FRAG-016 | CRIT-016 | Independent V&V records separate verification/validation, per-criterion/overall verdict, earliest re-entry, and truthful execution claim. |
| REQ-FRAG-017 | CRIT-017 | A HERM-209-linked PR targets `main`, distinguishes corrected `candidate_base_sha`, `candidate_head_sha`, and current PR head, records exact verification commands/results and remaining gaps, and is not merged unless the independent overall verdict is `PASS`. |

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No capture gap after corrective re-entry. Request-v1, its first T1/T2 gates, commits `11306cacad93f3b2eb341cfd5e8eb1e78ff1638e` / `bf4e12d44be77063cdfa334815a1be8146b7561c`, and downstream commits `4b7a45311d63c851891cc45e82512c8b1c2e59c0` / `427e7170728b2863a3d5ce290aba3b7e27fdaad1` are explicitly rejected and non-candidate. They remain in forward-only history only.

<a id="capture-validity-and-supersession"></a>
## Capture validity and supersession

VALID for captured issue revision 5 and trigger revision 1; received 2026-08-29T18:31:33Z. Corrective authority revision 1 caused T1/T2 re-entry and request-v2 supersedes request-v1 without changing the Human source. A separately authenticated revocation or replacement would invalidate downstream artifacts. Successor: none.

<a id="intention-gate"></a>
## Intention gate

Sole gate: .fdi/features/HERM-209/intention.md#gate-record. This section is a backlink only and owns no second gate.
