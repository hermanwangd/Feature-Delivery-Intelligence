# HERM-209 Verification and Validation plan

<a id="artifact-identity"></a>
## Artifact identity

- Feature: HERM-209
- Logical artifact: Delivery Spec
- Member: vv-plan.md
- Artifact revision: vv-plan-v1
- Producer: Spec agent
- Planned independent consumer: distinct V&V agent/run

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

<a id="verification-matrix"></a>
## Verification matrix

| V&V ID | Mapped IDs | Method | Environment | PASS threshold | Evidence IDs | Owner |
| --- | --- | --- | --- | --- | --- | --- | --- |
| VV-001 | CRIT-001; REQ-001; DES-001; TASK-001 | Independently inspect/reproduce start dependencies and immutable input revisions using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | intention-authorization; artifact-conformance | Independent V&V agent |
| VV-002 | CRIT-002; REQ-002; DES-002; TASK-002 | Independently inspect/reproduce mandatory core adoption/schema/safety using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-003 | CRIT-003; REQ-003; DES-003; TASK-003 | Independently inspect/reproduce explicit stable cross-file anchors using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-004 | CRIT-004; REQ-004; DES-004; TASK-004 | Independently inspect/reproduce singular canonical topology and planned/current separation using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-005 | CRIT-005; REQ-005; DES-005; TASK-005 | Independently inspect/reproduce registry-first conditional selection and no placeholders using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-006 | CRIT-006; REQ-006; DES-006; TASK-006 | Independently inspect/reproduce eight current digest-resolvable skill packages using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-007 | CRIT-007; REQ-007; DES-007; TASK-007 | Independently inspect/reproduce materialized but unexecuted b3a/b3b split using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-008 | CRIT-008; REQ-008; DES-008; TASK-008 | Independently inspect/reproduce honest pinned empty baseline and no support claim using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-009 | CRIT-009; REQ-009; DES-009; TASK-009 | Independently inspect/reproduce authenticated single-gate intention bundle using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | intention-authorization; artifact-conformance | Independent V&V agent |
| VV-010 | CRIT-010; REQ-010; DES-010; TASK-010 | Independently inspect/reproduce staged non-circular source preflight using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-011 | CRIT-011; REQ-011; DES-011; TASK-011 | Independently inspect/reproduce ordered four-transition execution records using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-012 | CRIT-012; REQ-012; DES-012; TASK-012 | Reproduce Git parent, merge-base, diff-check, name-status, and .fdi equality checks. | candidate-git plus github-pr where applicable | candidate_head parent/merge-base equals candidate_base; diff is exactly A README.md. | source-diff | Independent V&V agent |
| VV-013 | CRIT-013; REQ-013; DES-013; TASK-013 | Independently inspect/reproduce complete deviation disposition and blocking state using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | source-diff; artifact-conformance | Independent V&V agent |
| VV-014 | CRIT-014; REQ-014; DES-014; TASK-014 | Inspect candidate README required sections and resolve all relative links from candidate Git tree. | candidate-git plus github-pr where applicable | Every required section present; three required links resolve; no overclaim. | readme-entrypoint | Independent V&V agent |
| VV-015 | CRIT-015; REQ-015; DES-015; TASK-015 | Independently inspect/reproduce bidirectional request-to-verdict traceability using immutable files, digests, registries, and exact check IDs. | candidate-git plus github-pr where applicable | All required fields/mappings/checks pass with no unresolved blocking deviation. | artifact-conformance | Independent V&V agent |
| VV-016 | CRIT-016; REQ-016; DES-016; TASK-016 | Verify distinct agent/run identity and independently reproduce every planned check and mapping. | candidate-git plus github-pr where applicable | Separate verification/validation and per-criterion/overall verdict; no producer trust or unresolved blocker for PASS. | readme-entrypoint; artifact-conformance | Independent V&V agent |

<a id="validation-scenarios"></a>
## Validation scenarios

VAL-001 contributor entry: from repository root, understand product/purpose, canonical flow, start instructions, design links, readiness distinction, and safety boundary. VAL-002 reviewer audit: navigate every request fragment to criterion/Spec/candidate/evidence/verdict with no inference. VAL-003 future support safety: confirm B1/B2/B3 are materialized as contracts but NOT_INVOKED and release is NOT_OBSERVED.

<a id="independence"></a>
## Independence

Transition 4 must use a distinct agent/run from the implementation producer. It reads exact immutable candidate artifacts, runs fresh checks, and may not repair producer artifacts during the verdict run. Agent report alone is not evidence; reproduced output is required.

<a id="environments"></a>
## Environments

candidate-git: immutable local Git objects/content/diffs. github-pr: provider target/head/check/review snapshot. No production/runtime/deployment environment is claimed.

<a id="capability-bindings"></a>
## Capability bindings

Required: capability.filesystem-read; capability.sha256; capability.registry-validate; capability.git-independent-read; capability.markdown-conformance; capability.github-pr-read. Availability checks must resolve exact objects/paths, current PR head, and validator/check identity.

<a id="evidence-destinations"></a>
## Evidence destinations

| Evidence ID | Exact path | Producer | Claims |
| --- | --- | --- | --- |
| intention-authorization | .fdi/features/HERM-209/evidence/intention-authorization.md | Intention agent | authenticated request/source/safe digest/authorization/criteria |
| source-diff | .fdi/features/HERM-209/evidence/source-diff.md | implementation agent | candidate base/head adjacency, README-only diff, producer checks, later coordination head |
| readme-entrypoint | .fdi/features/HERM-209/evidence/readme-entrypoint.md | independent V&V agent | required README sections/links/boundary/overclaim scan |
| artifact-conformance | .fdi/features/HERM-209/evidence/artifact-conformance.md | independent V&V agent | inventory/schema/anchor/registry/Skill/topology/B3/traceability/execution-review audit |

No other evidence path is allocated unless .fdi/features/HERM-209/vv-report.md#gate-record records an exact justified exception ID before creation.

<a id="decision-rules"></a>
## Decision rules

Per-criterion and overall values are PASS, FAIL, or INCONCLUSIVE. Overall PASS requires all CRIT-001..016 PASS, all required check IDs fresh and successful, no unresolved blocking deviation, valid evidence, and independence. FAIL identifies earliest defective artifact; INCONCLUSIVE states missing evidence. Pre-release observation remains NOT_OBSERVED.

<a id="traceability"></a>
## Traceability

The verification matrix covers exact set CRIT/REQ/DES/TASK/VV 001..016. Evidence inventory in vv-report must contain the four allocated IDs and exact candidate identities.

<a id="open-gaps-and-deviations"></a>
## Open gaps and deviations

Candidate SHAs, PR number/current head, producer source-diff, and independent outputs are intentionally pending their producing transitions.

<a id="review-validity-and-supersession"></a>
## Review, validity, and supersession

Plan review: PASS for bounded documentation candidate on 2026-08-30. Invalidated by any mapped artifact/source-scope/evidence-allocation revision. Successor: none.

<a id="gate-record"></a>
## Gate record

This member participates in the sole Delivery Spec gate at .fdi/features/HERM-209/spec/index.md#gate-record and does not create a competing gate.
