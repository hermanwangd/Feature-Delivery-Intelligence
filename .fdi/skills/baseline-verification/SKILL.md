---
name: baseline-verification
description: Independently verify same-revision Baseline bundles for B2 or sealed refresh candidates for B3b.
version: 0.1.1
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

Independently verify same-revision Baseline bundles for B2 or sealed refresh candidates for B3b.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: B2 Baseline -> Independent As-Is Verification, or B3b helper; not invoked by HERM-209
- Exact fixed inputs:
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
- .fdi/context/domain/glossary.md; revision qualifier required at execution.
- .fdi/context/domain/rules.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/baseline/snapshot.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/baseline-verification/SKILL.md; revision qualifier required at execution.
- Exact outputs/use: B2 may write `.fdi/baseline/capabilities/{capability-id}/verification.md`, `.fdi/baseline/catalog.md`, and `.fdi/baseline/snapshot.md#gate-record`. B3b may write `.fdi/baseline/capabilities/{capability-id}/verification.md`, `.fdi/baseline/catalog.md`, `.fdi/baseline/snapshot.md#refresh-verification`, `.fdi/baseline/snapshot.md#refresh-verification-gate`, `.fdi/context/codebase/catalog.md`, `.fdi/context/codebase/relations.md`, `.fdi/context/codebase/system-context.md`, `.fdi/context/codebase/integrations.md`, `.fdi/context/codebase/data.md`, `.fdi/context/codebase/repositories/{repo-id}.md`, `.fdi/context/codebase/views/{view-id}.md`, and preallocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md`. It never authors B3a candidate content or handoff.
- Logical artifacts remain distinct from their physical bundle members.

<a id="context-selection"></a>
## Context selection

### Literal reads

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
- .fdi/context/domain/glossary.md; revision qualifier required at execution.
- .fdi/context/domain/rules.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/baseline/snapshot.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/baseline-verification/SKILL.md; revision qualifier required at execution.

### Bounded selectors

Select only ACTIVE, applicable, fresh, non-superseded Baseline catalog IDs; read exact capability.md and implementation-map.md plus their pinned refs. Exclude producer claims not independently reproduced. B3b uses only this sealed handoff allowlist, each at both `base_sha` and `candidate_content_sha`: `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/codebase/repositories/{repo-id}.md`; `.fdi/context/codebase/views/{view-id}.md`; `.fdi/baseline/capabilities/{capability-id}/capability.md`; `.fdi/baseline/capabilities/{capability-id}/implementation-map.md`; and preallocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md`.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.git-independent-read | required | Git | pinned refs -> observed bytes/results | objects resolve independently |
| capability.observation-read | conditional | authorized environment query | deployed revision/query -> observation | permission and revision verified |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed writes for B2: `.fdi/baseline/capabilities/{capability-id}/verification.md`, `.fdi/baseline/catalog.md`, and `.fdi/baseline/snapshot.md`. Allowed writes for B3b: exactly `.fdi/baseline/capabilities/{capability-id}/verification.md`; `.fdi/baseline/catalog.md`; `.fdi/baseline/snapshot.md#refresh-verification`; `.fdi/baseline/snapshot.md#refresh-verification-gate`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/codebase/repositories/{repo-id}.md`; `.fdi/context/codebase/views/{view-id}.md`; and preallocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md`, plus an external `verified_candidate_ref` and authenticated compare-and-swap adoption/non-adoption receipt. No B3a handoff, source, Intention, Spec, Change Set, V&V report, Skill, deployment, release, merge, or unlisted Context write is allowed.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

Establish verifier independence; reproduce exact evidence at the same bundle revision; record owner confirmations where required; write verdict. For B3b also perform the sealed handoff allowlist of `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/codebase/repositories/{repo-id}.md`; `.fdi/context/codebase/views/{view-id}.md`; `.fdi/baseline/capabilities/{capability-id}/capability.md`; `.fdi/baseline/capabilities/{capability-id}/implementation-map.md`; and preallocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md`, each at both revisions, plus these eight fixed base/candidate reads, each individually revision-qualified: `base_sha:.fdi/context/codebase/catalog.md`; `candidate_content_sha:.fdi/context/codebase/catalog.md`; `base_sha:.fdi/context/codebase/relations.md`; `candidate_content_sha:.fdi/context/codebase/relations.md`; `base_sha:.fdi/baseline/snapshot.md`; `candidate_content_sha:.fdi/baseline/snapshot.md`; `base_sha:.fdi/baseline/catalog.md`; `candidate_content_sha:.fdi/baseline/catalog.md`. HERM-209 does not invoke B2/B3b.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Mismatch, unavailable evidence/owner, stale bundle, or independence failure retains staged state and records FAIL/INCONCLUSIVE; no VERIFIED-AS-IS promotion or adoption.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

Only supported same-revision three-file bundles become VERIFIED-AS-IS. HERM-209 remains NOT_INVOKED/NOT_CLAIMED for B2 and B3b.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.1
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
