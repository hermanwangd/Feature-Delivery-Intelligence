---
name: spec-to-implementation
description: Implement only the completed Delivery Spec in source repositories while preserving local authority and exact candidate identity.
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

Implement only the completed Delivery Spec in source repositories while preserving local authority and exact candidate identity.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: 3 Delivery Spec -> Change Set / implementation agent
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
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/spec-to-implementation/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/intention.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/requirements.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/tasks.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/vv-plan.md; revision qualifier required at execution.
- Exact outputs/use: Source candidate commits/PRs; .fdi/features/{feature-id}/change-set/index.md; allocated evidence. Gate at .fdi/features/{feature-id}/change-set/index.md#gate-record.
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
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/spec-to-implementation/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/intention.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/requirements.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/tasks.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/vv-plan.md; revision qualifier required at execution.

### Bounded selectors

After catalog validation, select repository projection, recorded local instructions, and only exact repo:{repo-id}@{sha}:{path} entries authorized by completed .fdi/features/{feature-id}/spec/index.md#change-surface-summary. Maximum equals that finite entry count. Any discovered extra path is not read; record deviation/disposition and re-enter Spec.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.git-candidate | required | Git | authorized diff -> immutable commit | clean scoped index and parent/base checks pass |
| capability.github-pr | required | authenticated GitHub CLI | branch/head/base/body -> PR | auth and target repository/base verified |
| capability.filesystem-write | required | local UTF-8 filesystem | coordination records -> exact allocated paths | write set matches Spec |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed: bounded authenticated reads; safe Markdown artifact writes; immutable Git inspection; transition-specific branch/PR operations when named above.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

1. Read literals and selected repository controls. 2. Commit completed profile/Intention/Spec as candidate_base_sha. 3. Immediately create candidate_head_sha whose diff is exactly the planned source output. 4. Open/link PR. 5. Reproduce checks. 6. Record later coordination head separately from candidate head. 7. Complete mappings/deviations/gate.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Out-of-scope path, permission failure, stale base, check failure, or PR mismatch stops source expansion. Record a deviation with proposed disposition/blocking state; only revised Spec authorizes later reads. Git retry verifies object/PR identity before mutation.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

Every repository has immutable base/head/PR, exact paths/checks, mappings, candidate relations, and declared deviations; candidate base/head adjacency and evidence destination checks pass.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.0
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
