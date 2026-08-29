---
name: release-to-codebase-baseline-refresh
description: Govern two separate post-release entry points: B3a authors a non-current refresh candidate; B3b independently verifies and may atomically adopt only after PASS.
version: 0.1.0
source: FDI adopted profile at 54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
compatible_runtime: Multica/Codex >=1.0 <2.0
owner: FDI workflow owner
authority: adopted-profile procedure
status: ACTIVE
last_reviewed: 2026-08-30
next_review: 2026-11-28
supersedes: ""
superseded_by: ""
---

# Purpose and applicability

Govern two separate post-release entry points: B3a authors a non-current refresh candidate; B3b independently verifies and may atomically adopt only after PASS.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: B3a released Change Set -> refresh candidate / refresh agent; B3b sealed candidate -> independent verification and atomic adoption / distinct verifier; neither invoked by HERM-209
- Exact fixed inputs:
- authenticated release event with environment, deployed revision, event ID, observed-at, method, and digest; revision qualifier required at execution.
- .fdi/README.md; revision qualifier required at execution.
- .fdi/context/contract.md; revision qualifier required at execution.
- .fdi/context/index.md; revision qualifier required at execution.
- .fdi/context/steering/product.md; revision qualifier required at execution.
- .fdi/context/steering/tech.md; revision qualifier required at execution.
- .fdi/context/steering/structure.md; revision qualifier required at execution.
- .fdi/context/steering/architecture.md; revision qualifier required at execution.
- .fdi/context/steering/agent-policy.md; revision qualifier required at execution.
- .fdi/context/steering/delivery.md; revision qualifier required at execution.
- .fdi/context/steering/governance.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md; revision qualifier required at execution.
- .fdi/context/codebase/relations.md; revision qualifier required at execution.
- .fdi/context/codebase/system-context.md; revision qualifier required at execution.
- .fdi/context/codebase/integrations.md; revision qualifier required at execution.
- .fdi/context/codebase/data.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/baseline/snapshot.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/change-set/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/vv-report.md; revision qualifier required at execution.
- B3b has the separate fixed-read list in the B3b entry point below; revision qualifier required at execution.
- Exact outputs/use: B3a non-current content candidate then seal-only .fdi/baseline/snapshot.md#refresh-handoff and .fdi/baseline/snapshot.md#refresh-candidate-gate, returning external sealed_candidate_ref. B3b independent candidate verification, .fdi/baseline/snapshot.md#refresh-verification and .fdi/baseline/snapshot.md#refresh-verification-gate, external verified_candidate_ref, and provider compare-and-swap adoption/non-adoption receipt.
- Logical artifacts remain distinct from their physical bundle members.

<a id="context-selection"></a>
## Context selection

### Literal reads

- authenticated release event with environment, deployed revision, event ID, observed-at, method, and digest; revision qualifier required at execution.
- .fdi/README.md; revision qualifier required at execution.
- .fdi/context/contract.md; revision qualifier required at execution.
- .fdi/context/index.md; revision qualifier required at execution.
- .fdi/context/steering/product.md; revision qualifier required at execution.
- .fdi/context/steering/tech.md; revision qualifier required at execution.
- .fdi/context/steering/structure.md; revision qualifier required at execution.
- .fdi/context/steering/architecture.md; revision qualifier required at execution.
- .fdi/context/steering/agent-policy.md; revision qualifier required at execution.
- .fdi/context/steering/delivery.md; revision qualifier required at execution.
- .fdi/context/steering/governance.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md; revision qualifier required at execution.
- .fdi/context/codebase/relations.md; revision qualifier required at execution.
- .fdi/context/codebase/system-context.md; revision qualifier required at execution.
- .fdi/context/codebase/integrations.md; revision qualifier required at execution.
- .fdi/context/codebase/data.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/baseline/snapshot.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/change-set/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/vv-report.md; revision qualifier required at execution.
- B3b has the separate fixed-read list in the B3b entry point below; revision qualifier required at execution.

### Bounded selectors

B3a selects only released Change-Set refs, affected Baseline IDs via catalog, and matching current rows. B3b at both base_sha and candidate_content_sha permits only eight handoff-listed templates: system-context.md; integrations.md; data.md; repositories/{repo-id}.md; views/{view-id}.md; capabilities/{capability-id}/capability.md; capabilities/{capability-id}/implementation-map.md; features/{feature-id}/evidence/{evidence-id}.md. Every placeholder derives from the sealed signed manifest; maximum is twice its entry count; exclude unlisted IDs, mutable evidence, producer-only claims, and prior-revision verification.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.git-seal | required | Git/provider | candidate content -> immutable external ref | base/content/seal ancestry resolves |
| capability.release-observation | required | authorized provider/environment | event/deployed revision -> reproduced evidence | event auth, environment, revision, time, digest pass |
| capability.compare-and-swap | B3b required | repository provider | expected current + verified ref -> adoption/non-adoption receipt | provider CAS and authenticated receipt available |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed: bounded authenticated reads; safe Markdown artifact writes; immutable Git inspection; transition-specific branch/PR operations when named above.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

B3a: require PASS V&V, authenticated release, and owner authorization; write non-current content candidate without verification.md/current Context; later seal-only handoff records base_sha, preceding candidate_content_sha, changed paths/rows, proposed registry revision, manifests/digests, evidence IDs/digests, and planned->candidate->V&V->released lineage; containing seal never embeds itself; provider returns sealed_candidate_ref. B3b: require a different identity and load context-selection, this Skill, and baseline-verification; perform every fixed read below, independently reproduce evidence, write verification, and permit CAS only for PASS plus owner authorization. HERM-209 materializes but does not execute either entry point.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

B3a FAIL/INCONCLUSIVE/missing release or authorization creates no current write and returns exact gap. B3b FAIL/INCONCLUSIVE/stale base/interruption/retry preserves prior current ref and returns non-adoption/rollback receipt. PASS without provider receipt is verified but not adopted. Idempotency keys bind event, base, content, seal, verifier, and expected current ref.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

B3a gate is .fdi/baseline/snapshot.md#refresh-candidate-gate and external sealed_candidate_ref. B3b gate is .fdi/baseline/snapshot.md#refresh-verification-gate and external verified_candidate_ref plus CAS receipt. Producer/verifier identities differ. HERM-209 state is NOT_INVOKED and NOT_CLAIMED.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.0
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.

<a id="b3a-entry-point"></a>
## B3a entry point

Exact fixed reads:
- authenticated release event with environment, deployed revision, event ID, observed-at, method, and digest; revision qualifier required at execution.
- .fdi/README.md; revision qualifier required at execution.
- .fdi/context/contract.md; revision qualifier required at execution.
- .fdi/context/index.md; revision qualifier required at execution.
- .fdi/context/steering/product.md; revision qualifier required at execution.
- .fdi/context/steering/tech.md; revision qualifier required at execution.
- .fdi/context/steering/structure.md; revision qualifier required at execution.
- .fdi/context/steering/architecture.md; revision qualifier required at execution.
- .fdi/context/steering/agent-policy.md; revision qualifier required at execution.
- .fdi/context/steering/delivery.md; revision qualifier required at execution.
- .fdi/context/steering/governance.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md; revision qualifier required at execution.
- .fdi/context/codebase/relations.md; revision qualifier required at execution.
- .fdi/context/codebase/system-context.md; revision qualifier required at execution.
- .fdi/context/codebase/integrations.md; revision qualifier required at execution.
- .fdi/context/codebase/data.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/baseline/snapshot.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/change-set/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/vv-report.md; revision qualifier required at execution.

Candidate-only writes: non-current verified-ID Context/Baseline content (excluding verification.md), then a later seal-only refresh-handoff/candidate-gate. It cannot write current Context or claim adoption.

<a id="b3b-entry-point"></a>
## B3b entry point

The verifier identity must differ from B3a. Exact fixed reads, each separately qualified:
- authenticated sealed_candidate_ref; revision qualifier required at execution.
- sealed_candidate_ref:.fdi/baseline/snapshot.md#refresh-handoff; revision qualifier required at execution.
- .fdi/README.md; revision qualifier required at execution.
- .fdi/context/contract.md; revision qualifier required at execution.
- .fdi/context/index.md; revision qualifier required at execution.
- .fdi/context/steering/agent-policy.md; revision qualifier required at execution.
- .fdi/context/steering/delivery.md; revision qualifier required at execution.
- .fdi/context/steering/governance.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- base_sha:.fdi/context/codebase/catalog.md; revision qualifier required at execution.
- candidate_content_sha:.fdi/context/codebase/catalog.md; revision qualifier required at execution.
- base_sha:.fdi/context/codebase/relations.md; revision qualifier required at execution.
- candidate_content_sha:.fdi/context/codebase/relations.md; revision qualifier required at execution.
- base_sha:.fdi/baseline/snapshot.md; revision qualifier required at execution.
- candidate_content_sha:.fdi/baseline/snapshot.md; revision qualifier required at execution.
- base_sha:.fdi/baseline/catalog.md; revision qualifier required at execution.
- candidate_content_sha:.fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/release-to-codebase-baseline-refresh/SKILL.md; revision qualifier required at execution.
- .fdi/skills/baseline-verification/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/change-set/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/vv-report.md; revision qualifier required at execution.

At both base_sha and candidate_content_sha, only the eight sealed-handoff templates declared in Context selection may be read. Record every concrete match in affected .fdi/baseline/capabilities/{capability-id}/verification.md#evidence-and-provenance and .fdi/baseline/snapshot.md#refresh-verification. Only independent PASS plus authorization may request CAS adoption.
