# HERM-209 Intention authorization evidence

<a id="evidence-identity"></a>
## Evidence identity

- Evidence ID: intention-authorization
- Evidence revision: intention-authorization-v2
- Feature: HERM-209
- Captured: 2026-08-30
- Issue safe digest: sha256:4d8f386bf55b1d9f0a0d7490643eba5e6b7b79f0f117a7f3daac9fa3eda937a7
- Trigger safe digest: sha256:122cfeb48812a58aed3118bc4a68568c6b067f2f9cf68fe6c77ed4d35f8f7ee6

<a id="claim"></a>
## Claim

The HERM-209 desired outcome and pilot scope were supplied through captured immutable Multica issue revision 5 and trigger revision 1, with workspace-authorized product intent and seventeen stable criterion identities. Corrective review re-entered T1/T2 without replacing that Human signal.

<a id="method"></a>
## Method

Authenticated Multica CLI read; resolve IDs/revisions once; project issue fields with `jq -cS '{id,revision,title,description,updated_at}'` and comment fields with `jq -cS '{id,revision,content,created_at,author_id,author_type}'`; hash the emitted compact key-sorted UTF-8 bytes with SHA-256. The input includes `jq`'s trailing LF. Exclude credentials, email addresses, transport metadata, and unsafe raw payload.

<a id="candidate-environment"></a>
## Candidate/environment

Multica workspace issue 01a04e70-c387-72a2-bf4e-f97db187c8db revision 5 (`updated_at` `2026-08-29T18:31:33Z`); trigger 01a04eca-8fc6-722b-a903-1934b48a1897 revision 1; received 2026-08-29T18:31:33Z; profile start 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Re-entry authority: 01a04ee7-acea-798e-846a-a5de98a97349/1; supplement: 01a04eea-1752-74bd-b9f2-345947574cf2/1.

### Context consulted

| Consulted path@revision | Purpose | Authority/trust | Selection proof | Exclusions |
| --- | --- | --- | --- | --- |
| .fdi/README.md@sha256:fadbd405a33b7d440df9b60f27647614bbb2c2c9eb5b852499c04d8037db727a | confirm adopted profile and starting revision | adopted profile; governance-owned | literal fixed read; exact bytes resolved; one ACTIVE adopted-profile row | mutable refs, unsafe payloads, unrelated and superseded material, future revisions |
| .fdi/context/contract.md@sha256:b9089be300bbff8932c5c1e1ac98a54505e9b623cd48f8d597d4968cfea9b000 | apply profile schemas, selectors, and anchors | normative adopted-profile contract | literal fixed read; exact bytes resolved | source copies, mutable refs, unregistered extensions, future/superseded contract versions |
| .fdi/context/index.md@sha256:67b01c0f28649da22e1ffb70c899e69dd7a0f291445f06333b10137e7a569bde | validate conditional extension/view/area/runbook registry | canonical conditional registry | literal fixed registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, and planned-as-current leaves |
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
| .fdi/context/knowledge/index.md@sha256:f76a43ac06ca26050ce98086bd026506222fd78ef694f8766dff67e63eeeb156 | perform Knowledge selection | retrieval-only Knowledge registry | literal registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/context/external/references.md@sha256:6a224a8f41eeacdd907f7872055b2e37b1ad05521ac132970c98f0729abb5010 | perform external-review selection | sole external-review registry | literal registry read; zero ACTIVE applicable row | inactive, stale, superseded, unrelated, unsafe, mutable, planned-as-current leaves |
| .fdi/baseline/catalog.md@sha256:3a66b988d1bf7a715da3e2ea38737db304995dba9d5641957128ab423eb29694 | perform Baseline selection | sole Baseline capability registry | literal registry read; empty capability table; zero selection | active or unsupported capabilities, source copies, mutable refs, unregistered baseline paths |
| .fdi/skills/catalog.md@sha256:0eecbf6118e6836a241f941560940f969f054ec59a85e49808928150f4e27cc0 | validate active Skill versions and digests | canonical Skill registry | literal registry read before exact Skill files; all required rows ACTIVE/current/non-superseded | inactive, superseded, unregistered, or digest-mismatched Skill rows |
| .fdi/skills/context-selection/SKILL.md@sha256:da661dd387f6a3232072b06f67eb1c1959b7d84773254a7a6675398a9f317dbe | govern bounded registry-first selection | active executable Context v0.1.1 | literal fixed read after Skill catalog validation; no Skill resource selected | source copies, mutable refs, unregistered skills, draft skill versions |
| .fdi/skills/human-to-intention/SKILL.md@sha256:f48c36bfb5fcf7ca00b048d25cc4e929748a79609d337a690a9fa43b2b80e52f | govern authenticated capture and Intention production | active transition procedure v0.1.1 | literal fixed read after Skill catalog validation; exact allowed writes checked | source copies, mutable refs, unregistered skills, draft skill versions, disallowed writes |
| .fdi/context/codebase/repositories/feature-delivery-intelligence.md@sha256:8aa0596904e2799b421194329f022d02ffbcf254acab4bca3fa3c9a5615cf8f5 | obtain repository navigation and authority boundary | derived projection; trusted only after registry proof | `.fdi/context/codebase/catalog.md#entities` read first (registry revision `catalog-v1`); row `feature-delivery-intelligence` is ACTIVE, owner-authenticated, reviewed 2026-08-30, next review 2026-11-28, `superseded_by` none, digest matched; row `applies_to` is only `product-feature-delivery-intelligence`, impacted set contains that Product, exact intersection is `{product-feature-delivery-intelligence}` | HERM/System/Component as direct applicability, source copies, mutable refs, unregistered paths, future/superseded registry revisions |

<a id="observation"></a>
## Observation

The trigger authorizes immediate implementation/pilot after HERM-204/HERM-205 and PR #1 gates, requires exact merged-contract preservation, candidate branch/PR/evidence, independent V&V, and forbids inferred execution verification. The later independent-review comment invalidated the first T1/T2 gates and old candidate pair, required a 17th PR chain, and preserved the original Human signal.

<a id="result"></a>
## Result

PASS for authenticated capture, exact LF-inclusive digest reproduction, preserved Human authority, corrective re-entry, and approved pilot scope. Criterion IDs CRIT-001 through CRIT-017 are allocated; authorization does not establish current topology/source behavior or a future verdict.

<a id="integrity-and-access"></a>
## Integrity and access

Digests are over the documented safe field projections serialized with `jq -cS`; compact key-sorted UTF-8 bytes and the trailing LF are included. The issue digest was reproduced in the original authenticated revision-5 capture; the trigger digest was freshly reproduced from revision 1. Source remains in Multica authority; no credential, email, unsafe raw payload, or local absolute path is persisted.

<a id="producer-and-owner"></a>
## Producer and owner

Producer: Intention agent. Product authorization source: captured immutable issue revision 5 and trigger revision 1. Corrective re-entry authority is separately identified and does not replace the Human source. Evidence owner: product/governance owner.

<a id="limitations"></a>
## Limitations

This evidence proves capture/authenticated authorization only. It does not prove implementation, source truth, release, B1/B2/B3, or V&V.

<a id="validity-expiry-and-supersession"></a>
## Validity, expiry, and supersession

State: VALID for captured issue revision 5, trigger revision 1, and request/intention v2. The corrective comments supersede the first T1/T2 gate attempt, not the captured Human signal. Invalidated only by authenticated revocation/replacement or failed reissued gate. Review at pilot completion; successor: none.
