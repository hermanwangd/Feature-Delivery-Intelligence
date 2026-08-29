# HERM-209 Delivery Spec requirements

<a id="artifact-identity"></a>
## Artifact identity

- Feature: HERM-209
- Logical artifact: Delivery Spec
- Member: requirements.md
- Artifact revision: requirements-v1
- Producer: Spec agent
- Intention input: intention.md@sha256:90550317a9ea6a34fe089de99d030266be24f971da9d19240e4024d341c9ef3b

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

<a id="functional-requirements"></a>
## Functional requirements

| Requirement | Criterion | Obligation | Priority |
| --- | --- | --- | --- |
| REQ-001 | CRIT-001 | Start dependencies and immutable input revisions | Required |
| REQ-002 | CRIT-002 | Mandatory core adoption/schema/safety | Required |
| REQ-003 | CRIT-003 | Explicit stable cross-file anchors | Required |
| REQ-004 | CRIT-004 | Singular canonical topology and planned/current separation | Required |
| REQ-005 | CRIT-005 | Registry-first conditional selection and no placeholders | Required |
| REQ-006 | CRIT-006 | Eight current digest-resolvable Skill packages | Required |
| REQ-007 | CRIT-007 | Materialized but unexecuted B3a/B3b split | Required |
| REQ-008 | CRIT-008 | Honest pinned empty Baseline and no support claim | Required |
| REQ-009 | CRIT-009 | Authenticated single-gate Intention bundle | Required |
| REQ-010 | CRIT-010 | Staged non-circular source preflight | Required |
| REQ-011 | CRIT-011 | Ordered four-transition execution records | Required |
| REQ-012 | CRIT-012 | Adjacent candidate base/head with README-only diff | Required |
| REQ-013 | CRIT-013 | Complete deviation disposition and blocking state | Required |
| REQ-014 | CRIT-014 | README contributor entry-point contract | Required |
| REQ-015 | CRIT-015 | Bidirectional request-to-verdict traceability | Required |
| REQ-016 | CRIT-016 | Independent V&V and truthful execution claim | Required |

<a id="quality-requirements"></a>
## Quality requirements

| Requirement | Attribute | Threshold |
| --- | --- | --- |
| QREQ-001 | Determinism | Every live source read uses repo:feature-delivery-intelligence@immutable-sha:path and every conditional leaf has registry proof. |
| QREQ-002 | Auditability | Every cross-file target has an explicit stable anchor; evidence and traceability are bidirectional. |
| QREQ-003 | Safety | No secret, credential, email, local absolute path, unsafe raw payload, mutable evidence, source copy, or fabricated claim. |
| QREQ-004 | Independence | Transition 4 uses a distinct agent/run and reproduces rather than trusts producer checks. |
| QREQ-005 | Multi-repository compatibility | Repository IDs, owners, pins, paths, and control boundaries remain explicit although the pilot has one repository. |

<a id="constraints"></a>
## Constraints

Immutable profile/source start 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482; no mutable branch evidence; exact physical schemas; no unregistered conditional leaf; root README is the only source-candidate output; B1/B2/B3 and release remain unexecuted; no claim beyond exact HERM-209 evidence.

<a id="acceptance-mapping"></a>
## Acceptance mapping

| Requirement | Intention criterion | V&V ID | Planned evidence IDs |
| --- | --- | --- | --- |
| REQ-001 | CRIT-001 | VV-001 | intention-authorization; artifact-conformance |
| REQ-002 | CRIT-002 | VV-002 | artifact-conformance |
| REQ-003 | CRIT-003 | VV-003 | artifact-conformance |
| REQ-004 | CRIT-004 | VV-004 | artifact-conformance |
| REQ-005 | CRIT-005 | VV-005 | artifact-conformance |
| REQ-006 | CRIT-006 | VV-006 | artifact-conformance |
| REQ-007 | CRIT-007 | VV-007 | artifact-conformance |
| REQ-008 | CRIT-008 | VV-008 | artifact-conformance |
| REQ-009 | CRIT-009 | VV-009 | intention-authorization; artifact-conformance |
| REQ-010 | CRIT-010 | VV-010 | artifact-conformance |
| REQ-011 | CRIT-011 | VV-011 | artifact-conformance |
| REQ-012 | CRIT-012 | VV-012 | source-diff |
| REQ-013 | CRIT-013 | VV-013 | source-diff; artifact-conformance |
| REQ-014 | CRIT-014 | VV-014 | readme-entrypoint |
| REQ-015 | CRIT-015 | VV-015 | artifact-conformance |
| REQ-016 | CRIT-016 | VV-016 | readme-entrypoint; artifact-conformance |

<a id="open-questions"></a>
## Open questions

None blocking. Final independent verdict and provider PR/check state are intentionally unresolved until their producing transitions.

<a id="traceability"></a>
## Traceability

Each REQ-001..016 maps one-to-one to CRIT-001..016 and onward through .fdi/features/HERM-209/spec/index.md#intention-mapping. QREQ-001..005 apply to every relevant row.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

No Spec deviation. Runtime/release evidence is explicitly out of pre-release scope.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Product/architecture/repository review state: PASS for documentation-only scope on 2026-08-30. Valid only with intention@sha256:90550317a9ea6a34fe089de99d030266be24f971da9d19240e4024d341c9ef3b and source 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482. Successor: none.

<a id="gate-record"></a>
## Gate record

This member participates in the sole Delivery Spec gate at .fdi/features/HERM-209/spec/index.md#gate-record and does not create a competing gate.
