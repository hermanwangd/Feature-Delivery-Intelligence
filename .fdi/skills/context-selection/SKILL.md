---
name: context-selection
description: Validate literal and bounded registry-first Context selection for every adopted-profile execution.
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

Validate literal and bounded registry-first Context selection for every adopted-profile execution.

<a id="transition-contract"></a>
## Transition contract

- Transition/entry point: helper for transitions 1, 2, 3, 4, B1, B2, B3a, and B3b; never a canonical artifact producer
- Exact fixed inputs:
- .fdi/context/contract.md; revision qualifier required at execution.
- .fdi/context/index.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md when repository projections are selectable; revision qualifier required at execution.
- .fdi/context/knowledge/index.md when Knowledge is selectable; revision qualifier required at execution.
- .fdi/context/external/references.md when external reviews are selectable; revision qualifier required at execution.
- .fdi/baseline/catalog.md when Baseline bundles are selectable; revision qualifier required at execution.
- .fdi/skills/catalog.md and exact parent SKILL.md when Skill resources are selectable; revision qualifier required at execution.
- Exact outputs/use: Validated selected-read set plus exclusions written only to the invoking transition's declared Context-consulted/selection-proof/gate destination.
- Logical artifacts remain distinct from their physical bundle members.

<a id="context-selection"></a>
## Context selection

### Literal reads

- .fdi/context/contract.md; revision qualifier required at execution.
- .fdi/context/index.md; revision qualifier required at execution.
- .fdi/context/codebase/catalog.md when repository projections are selectable; revision qualifier required at execution.
- .fdi/context/knowledge/index.md when Knowledge is selectable; revision qualifier required at execution.
- .fdi/context/external/references.md when external reviews are selectable; revision qualifier required at execution.
- .fdi/baseline/catalog.md when Baseline bundles are selectable; revision qualifier required at execution.
- .fdi/skills/catalog.md and exact parent SKILL.md when Skill resources are selectable; revision qualifier required at execution.

### Bounded selectors

Allowed templates are exactly those in .fdi/context/contract.md#bounded-selectors and the invoking transition. Placeholder values derive from a completed preceding artifact, current literal registry, or passed preflight. Every selector states immutable revision, root/extensions, exclusions, finite maximum, zero/excess behavior, and concrete-match destination.

Read the governing registry in the same execution before each conditional leaf. Record registry path/revision, stable entry ID, ACTIVE lifecycle, applies_to intersection, owner, trust, freshness/expiry, empty superseded_by, selected path/digest, concrete matches, reason, and exclusions at the named gate/output. Exclude inactive, stale, superseded, unrelated, unsafe, mutable, unregistered, planned-as-current, cache, generated, vendored, and secret material.

<a id="capability-bindings"></a>
## Capability bindings

| Capability ID | State | Provider/runtime | Input -> output | Availability check |
| --- | --- | --- | --- | --- |
| capability.filesystem-read | required | local UTF-8 filesystem | exact path -> bytes | path exists, readable, inside registered root |
| capability.sha256 | required | standard SHA-256 | bytes -> lowercase digest | known-vector check and digest length 64 |
| capability.registry-validate | required | agent procedure | registry row + selector -> match/exclusion proof | all mandatory registry fields parse |

A missing required capability, runtime, schema, permission, owner, review, lifecycle, or binding fails preflight. No unregistered substitute is permitted.

<a id="permissions-and-approvals"></a>
## Permissions and approvals

- Allowed: bounded authenticated reads; safe Markdown artifact writes; immutable Git inspection; transition-specific branch/PR operations when named above.
- Required approvals: product intent, source scope, repository candidate, independent verdict, release, and Context adoption stay with their named owners.
- Prohibited: credentials, unsafe raw payloads, unbounded or mutable source reads, copied source trees, destructive history rewrites, external deployment, fabricated evidence, or scope expansion.
- Sensitive data: retain safe identifiers/digests/redacted observations only.

<a id="procedure"></a>
## Procedure

1. Verify ADOPTED profile and exact invoking Skill. 2. Read literal registries. 3. Validate IDs, lifecycle, applicability, freshness, trust, successor, path/digest, permissions, and finite bounds. 4. Return exact matches/exclusions. 5. Record proof before leaf use.

<a id="failure-escalation-and-idempotency"></a>
## Failure, escalation, and idempotency

Missing registry/entry/digest, zero/excess cardinality, stale review, successor, trust gap, invalid placeholder, or authority conflict returns NOT_CONTRACT_READY and exact re-entry. Never inspect a rejected leaf.

Retries re-resolve immutable inputs, compare existing artifact identity, and never duplicate or silently overwrite a successful gate. Stale or conflicting upstream state re-enters the earliest invalid artifact.

<a id="completion-and-evidence"></a>
## Completion and evidence

Complete only when every selected leaf is preceded by its registry proof and every exclusion/reason is recorded at the invoking gate.

Global Execution-verified remains NOT_CLAIMED until all HERM-209 transition reviews and independent V&V pass.

<a id="version-and-provenance"></a>
## Version and provenance

- Package version: 0.1.0
- Lifecycle: ACTIVE
- Source profile: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-context-taxonomy-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Workflow semantics: feature-delivery-intelligence:docs/superpowers/specs/2026-08-29-fdi-workflow-semantics-design.md@54db6e2879abd5ac8e7319efe8ef06a5b7ae5482
- Reviewed candidate provenance: f4561614ba1a1d0f222ef838ff6c4815c051dd01
- Review: 2026-08-30; next review 2026-11-28; superseded_by none.
