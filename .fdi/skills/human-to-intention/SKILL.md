---
name: human-to-intention
description: Capture an authenticated Human signal safely and produce the single two-member Intention bundle and authorization evidence.
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

Capture an authenticated Human signal safely and produce the single two-member Intention bundle and authorization evidence.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: 1 Human -> Intention / Intention agent
- Exact fixed inputs:
- authenticated HERM-209 issue revision and trigger comment; revision qualifier required at execution.
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
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/human-to-intention/SKILL.md; revision qualifier required at execution.
- Exact outputs/use: .fdi/features/{feature-id}/request.md; .fdi/features/{feature-id}/intention.md; allocated .fdi/features/{feature-id}/evidence/{evidence-id}.md. Sole gate is .fdi/features/{feature-id}/intention.md#gate-record; .fdi/features/{feature-id}/request.md#intention-gate is a backlink only.
- Logical artifacts remain distinct from their physical bundle members.

<a id="context-selection"></a>
## Context selection

### Literal reads

- authenticated HERM-209 issue revision and trigger comment; revision qualifier required at execution.
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
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/human-to-intention/SKILL.md; revision qualifier required at execution.

### Bounded selectors

Repository projections derive only from safely extracted active Repository/entity IDs; Domain/Knowledge/external/Baseline leaves require their literal registries and an ACTIVE, applicable, fresh, non-superseded entry. Concrete selection proof is written to .fdi/features/{feature-id}/intention.md#context-consulted. Maximum is one repository projection plus the finite registry matches; zero repository matches blocks.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.multica-issue-read | required | authenticated Multica CLI | issue/comment ID -> revisioned safe payload | workspace-scoped authenticated read succeeds |
| capability.filesystem-write | required | local UTF-8 filesystem | validated content -> exact feature paths | parent root registered and write bounded |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed: bounded authenticated reads; safe Markdown artifact writes; immutable Git inspection; transition-specific branch/PR operations when named above.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

1. Resolve issue/comment revision once. 2. Authenticate channel/assurance. 3. Redact and digest safe canonical fields. 4. Read literal Context and registries. 5. Select repository projection registry-first. 6. Map fragments to criteria/entity/repository seeds. 7. Write request, authorization evidence, and intention under one producer. 8. Review the sole intention gate.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Ambiguous identity, authorization, scope, alias, owner, registry match, or unsafe capture blocks the affected criterion and returns to authenticated Human input; no requirement is invented.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

Capture is reviewable; scope/non-goals/scenarios/measurable criteria/authorization and impacted seeds resolve; request and intention share producer and sole PASS/FAIL gate with exact evidence.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.0
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
