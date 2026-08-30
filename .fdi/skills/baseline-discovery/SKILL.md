---
name: baseline-discovery
description: Discover evidence-backed as-is capability candidates without inventing historical intent or independent verification.
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

Discover evidence-backed as-is capability candidates without inventing historical intent or independent verification.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: B1 pinned source -> Baseline Discovery / discovery agent; not invoked by HERM-209
- Exact fixed inputs:
- authenticated B1 invocation naming active repository IDs and immutable pins; revision qualifier required at execution.
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
- .fdi/context/domain/glossary.md; revision qualifier required at execution.
- .fdi/context/domain/rules.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/baseline-discovery/SKILL.md; revision qualifier required at execution.
- Exact outputs/use: `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; and, for each selected `{capability-id}`, exactly `.fdi/baseline/capabilities/{capability-id}/capability.md` plus `.fdi/baseline/capabilities/{capability-id}/implementation-map.md` at `DISCOVERED`. `.fdi/baseline/capabilities/{capability-id}/verification.md` is forbidden. Gate: `.fdi/baseline/snapshot.md#gate-record`.
- Logical artifacts remain distinct from their physical bundle members.

<a id="context-selection"></a>
## Context selection

### Literal reads

- authenticated B1 invocation naming active repository IDs and immutable pins; revision qualifier required at execution.
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
- .fdi/context/domain/glossary.md; revision qualifier required at execution.
- .fdi/context/domain/rules.md; revision qualifier required at execution.
- .fdi/context/operations/environments.md; revision qualifier required at execution.
- .fdi/context/operations/observability.md; revision qualifier required at execution.
- .fdi/context/knowledge/index.md; revision qualifier required at execution.
- .fdi/context/external/references.md; revision qualifier required at execution.
- .fdi/skills/catalog.md; revision qualifier required at execution.
- .fdi/skills/context-selection/SKILL.md; revision qualifier required at execution.
- .fdi/skills/baseline-discovery/SKILL.md; revision qualifier required at execution.

### Bounded selectors

After registry-first repository projection selection, draft .fdi/baseline/snapshot.md#preflight-source-scope, pass syntax/authority, enumerate names only, pass finite cardinality, then read only matched source/test/config/schema/doc/runtime evidence. Exclude history/chat, secrets, caches, mutable refs, and fabricated intent.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |
| capability.git-ls-tree | required | Git | invocation pin/scope -> names | immutable commit resolves |
| capability.observation-read | optional | authorized environment query | named query -> timestamped observation | permission and deployed revision verified |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed writes: `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; `.fdi/baseline/capabilities/{capability-id}/capability.md`; `.fdi/baseline/capabilities/{capability-id}/implementation-map.md`. `{capability-id}` must be selected by the passed B1 preflight and recorded before creation. No `verification.md`, feature artifact, source, current Context, Skill, registry outside Baseline, PR, deployment, or release write is allowed.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

Require a separately authenticated B1 invocation. Run staged selector, capture only observed behavior and exact refs, label unknown intent, create two-file discovered bundles, and map gaps. HERM-209 does not invoke these steps.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Without authenticated scope/pins, valid selector, or concrete evidence return NOT_INVOKED/NOT_CONTRACT_READY and create no capability path. Retry cannot promote evidence status.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

DISCOVERED only when concrete refs exist; never VERIFIED-AS-IS. HERM-209 support state remains NOT_INVOKED and Execution-verified NOT_CLAIMED.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.1
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
