---
name: implementation-to-correctness
description: Independently reproduce the Change Set evidence and issue verification, validation, relation, criterion, and overall verdicts.
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

Independently reproduce the Change Set evidence and issue verification, validation, relation, criterion, and overall verdicts.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: 4 Change Set -> V&V Report / independent V&V agent
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
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/implementation-to-correctness/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/intention.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/requirements.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/tasks.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/vv-plan.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/change-set/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/evidence/intention-authorization.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/evidence/source-diff.md; revision qualifier required at execution.
- Exact outputs/use: .fdi/features/{feature-id}/vv-report.md; .fdi/features/{feature-id}/evidence/readme-entrypoint.md; .fdi/features/{feature-id}/evidence/artifact-conformance.md; exception evidence only if allocated at the gate. Gate at .fdi/features/{feature-id}/vv-report.md#gate-record.
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
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/release.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/baseline/catalog.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/implementation-to-correctness/SKILL.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/intention.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/requirements.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/design.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/tasks.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/spec/vv-plan.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/change-set/index.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/evidence/intention-authorization.md; revision qualifier required at execution.
- .fdi/features/{feature-id}/evidence/source-diff.md; revision qualifier required at execution.

### Bounded selectors

Read candidate paths at exact candidate_head_sha and only plan/Change-Set evidence IDs. Additional Baseline/Knowledge/runbook/review selection requires the literal registry and complete proof. Maximum equals the finite plan/Change-Set IDs and paths. Record matches in .fdi/features/{feature-id}/vv-report.md#context-consulted and .fdi/features/{feature-id}/vv-report.md#evidence-inventory.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.git-independent-read | required | Git | candidate SHA/path/diff -> independently observed bytes/results | candidate object and ancestry resolve |
| capability.markdown-conformance | required | independent validator | profile tree -> findings | validator identity/version and fresh run recorded |
| capability.github-pr-read | required | authenticated GitHub CLI | PR number/head -> provider snapshot | snapshot head equals assessed head |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed: bounded authenticated reads; safe Markdown artifact writes; immutable Git inspection; transition-specific branch/PR operations when named above.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

1. Establish identity independence. 2. Read literal inputs and registries. 3. Resolve candidate SHA and reproduce planned checks without producer conclusions. 4. Validate README output and full artifact contract. 5. Map every criterion/requirement/design/task/relation/deviation to evidence. 6. Write separate verification/validation and overall verdict. 7. Record NOT_OBSERVED release state and earliest re-entry.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Evidence mismatch, stale candidate, unresolved blocker, unavailable required capability, failed check, or incomplete traceability yields FAIL or INCONCLUSIVE with exact next step. Verifier cannot repair producer artifacts during the same verdict run.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

Every mapped claim has fresh independent evidence and PASS/FAIL/INCONCLUSIVE; PASS requires all blockers resolved. Global execution verification may be claimed only when every mandatory execution-review item and criterion passes.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.0
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
