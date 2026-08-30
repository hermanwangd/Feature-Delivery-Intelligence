---
name: intention-to-spec
description: Produce the five-member Delivery Spec using a staged, bounded, non-circular source selector.
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

Produce the five-member Delivery Spec using a staged, bounded, non-circular source selector.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: 2 Intention -> Delivery Spec / Spec agent
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
- .fdi/context/domain/glossary.md; revision qualifier required at execution.
- .fdi/context/domain/rules.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md; revision qualifier required at execution.
- .fdi/context/codebase/relations.md; revision qualifier required at execution.
- .fdi/context/codebase/system-context.md; revision qualifier required at execution.
- .fdi/context/codebase/integrations.md; revision qualifier required at execution.
- .fdi/context/codebase/data.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/intention-to-spec/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/request.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/intention.md; revision qualifier required at execution.
- Exact outputs/use: .fdi/features/{feature-id}/spec/index.md; .fdi/features/{feature-id}/spec/requirements.md; .fdi/features/{feature-id}/spec/design.md; .fdi/features/{feature-id}/spec/tasks.md; .fdi/features/{feature-id}/spec/vv-plan.md. Gate at .fdi/features/{feature-id}/spec/index.md#gate-record; evidence destinations at .fdi/features/{feature-id}/spec/vv-plan.md#evidence-destinations.
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
- .fdi/context/domain/glossary.md; revision qualifier required at execution.
- .fdi/context/domain/rules.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md; revision qualifier required at execution.
- .fdi/context/codebase/relations.md; revision qualifier required at execution.
- .fdi/context/codebase/system-context.md; revision qualifier required at execution.
- .fdi/context/codebase/integrations.md; revision qualifier required at execution.
- .fdi/context/codebase/data.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/intention-to-spec/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/request.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/intention.md; revision qualifier required at execution.

### Bounded selectors

Select repository projections through .fdi/context/codebase/catalog.md. Draft .fdi/features/{feature-id}/spec/index.md#preflight-source-scope before source content; validate repo ID/SHA/root/exact paths/extensions/exclusions/max; enumerate names only; pass cardinality; then read only concrete matches. Record matches in each Spec member and .fdi/features/{feature-id}/spec/index.md#change-surface-summary. Final .fdi/features/{feature-id}/spec/design.md#change-surface never authorizes its own discovery.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.git-ls-tree | required | Git | repo@sha + exact path scope -> path names | commit exists and object listing succeeds |
| capability.git-show | required | Git | repo@sha:path -> bytes | only passed concrete path is addressed |
| capability.filesystem-write | required | local UTF-8 filesystem | validated Spec -> five exact paths | write root bounded |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed writes: `.fdi/features/{feature-id}/spec/index.md`; `.fdi/features/{feature-id}/spec/requirements.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/spec/tasks.md`; `.fdi/features/{feature-id}/spec/vv-plan.md`; and only `.fdi/features/{feature-id}/evidence/{evidence-id}.md` whose exact investigation ID is allocated at `.fdi/features/{feature-id}/spec/index.md#gate-record` before creation. No source, Change Set, V&V, Baseline, current Context, Skill, or registry write is allowed.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

1. Read literal inputs/registries. 2. Select repository projection. 3. Draft selector preflight. 4. Pass syntax/authority. 5. Enumerate names only. 6. Pass zero/excess cardinality. 7. Read selected content. 8. Complete five members, traceability, evidence allocations, and gate.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Invalid authority blocks before repository access; zero/excess blocks before content. A new path requires Spec re-entry and cannot be authorized by a same-transition final output.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

All five members are consistent; every criterion maps to stable requirement/design/task/V&V IDs, exact output/evidence method/threshold/owner, and bounded selectors; gate records actual reads and review.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.1
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
