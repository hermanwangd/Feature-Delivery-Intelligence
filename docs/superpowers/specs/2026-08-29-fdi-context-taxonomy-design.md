# FDI Context Taxonomy and Markdown Contract v0.1

**Status:** Proposed for approval (contract-ready design; not execution-verified)

**Date:** 2026-08-29

**Scope:** The dedicated FDI coordination repository for one product, including products implemented across multiple source repositories.

## 1. Decision and boundary

FDI uses a **small mandatory core plus governed extensions**. Stable core paths make every workflow interoperable. An extension is trusted Context only when its concrete path matches a pattern in this contract and is registered in `.fdi/context/index.md`; empty extension placeholders are prohibited.

The coordination repository owns durable product-level Context, cross-repository workflow artifacts, baseline summaries, and aggregate evidence references. Source repositories retain authority for source, repository-local instructions, tests, configuration, schemas, ownership approvals, branch protection, deployment, and release execution. The coordination repository points to those sources at immutable revisions; it does not copy whole repositories or bypass their controls.

The logical flow remains:

```text
Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report
```

Each logical artifact maps to the physical bundle defined below. Baseline reconstruction is an as-is support workflow, not a fifth stage. Skills are executable procedural Context and declare their Tools; there is no `.fdi/context/tools/` category.

## 2. Normative vocabulary

- **MUST / REQUIRED**: necessary for contract conformance.
- **CONDITIONAL**: required only when its matching rule is true; otherwise the file MUST be absent rather than empty.
- **Persistent**: loaded in every applicable transition.
- **Transition-load**: loaded for a named transition and then only when its scope matches.
- **Retrieval-only**: discovered through a catalog or query and loaded only for a declared need.
- **Ephemeral**: execution input that is not durable Context; only its safe reference and interpretation are persisted.
- **Current**: its refresh trigger has not fired unresolved, its review date has not expired, and its cited sources remain resolvable at the declared revision.
- **Superseded**: retained for traceability but excluded from default selection; the successor is named.
- **Pinned source**: an immutable commit SHA, artifact digest, release identifier, or timestamped environment observation.

## 3. Complete coordination-repository tree

```text
.fdi/
├── README.md
├── product/
│   └── repositories.yaml
├── context/
│   ├── index.md
│   ├── steering/
│   │   ├── product.md
│   │   ├── tech.md
│   │   ├── structure.md
│   │   ├── agent-policy.md
│   │   ├── delivery.md
│   │   ├── governance.md
│   │   └── extensions/{policy-id}.md
│   ├── codebase/
│   │   ├── product-map.md
│   │   ├── integration-map.md
│   │   ├── repos/{repo-id}.md
│   │   └── views/{view-id}.md
│   ├── domain/
│   │   ├── glossary.md
│   │   ├── rules.md
│   │   └── areas/{domain-id}.md
│   ├── architecture/
│   │   ├── system.md
│   │   ├── interfaces.md
│   │   ├── data.md
│   │   └── components/{component-id}.md
│   ├── knowledge/
│   │   ├── index.md
│   │   ├── decisions/{knowledge-id}.md
│   │   ├── learnings/{knowledge-id}.md
│   │   ├── incidents/{knowledge-id}.md
│   │   └── patterns/{knowledge-id}.md
│   ├── operations/
│   │   ├── environments.md
│   │   ├── release.md
│   │   └── runbooks/{runbook-id}.md
│   └── external/
│       ├── references.md
│       └── reviews/{source-id}.md
├── skills/
│   ├── context-selection/SKILL.md
│   ├── human-to-intention/SKILL.md
│   ├── intention-to-spec/SKILL.md
│   ├── spec-to-implementation/SKILL.md
│   ├── implementation-to-correctness/SKILL.md
│   ├── baseline-discovery/SKILL.md
│   ├── baseline-verification/SKILL.md
│   ├── {skill-id}/SKILL.md
│   └── {skill-id}/
│       ├── references/{reference-id}.md
│       ├── scripts/{script-id}.{sh,py,js,ts}
│       └── assets/{asset-id}.{json,yaml,yml,txt,png,svg}
├── baseline/
│   ├── snapshot.md
│   ├── catalog.md
│   └── capabilities/{capability-id}/
│       ├── capability.md
│       ├── implementation-map.md
│       └── verification.md
└── features/{feature-id}/
    ├── request.md
    ├── intention.md
    ├── spec/
    │   ├── index.md
    │   ├── requirements.md
    │   ├── design.md
    │   ├── tasks.md
    │   └── vv-plan.md
    ├── change-set/
    │   └── index.md
    ├── vv-report.md
    └── evidence/{evidence-id}.md
```

### 3.1 Bounded-pattern rules

All identifiers are lowercase ASCII slugs matching `[a-z0-9]+(?:-[a-z0-9]+)*`; the only exception is `{feature-id}`, which is the exact case-preserving issue or delivery key accepted by the delivery system. Identifiers MUST NOT contain `/`, `..`, whitespace, a URI scheme, or a user-specific path.

| Pattern | Match and inclusion rule | Exclusions | Where concrete matches are recorded |
| --- | --- | --- | --- |
| `.fdi/context/steering/extensions/{policy-id}.md` | One approved normative policy not expressible without overloading a core steering file | Team notes, project plans, duplicate core content | `.fdi/context/index.md#Governed extension registry`; every consuming artifact's `Context consulted` table |
| `.fdi/context/codebase/repos/{repo-id}.md` | Exactly one file for every active ID in `.fdi/product/repositories.yaml` | Source copies, generated trees, unregistered repositories | Repository registry plus `.fdi/context/index.md`; selected matches in the consuming artifact |
| `.fdi/context/codebase/views/{view-id}.md` | A curated cross-cutting navigation view spanning at least two registered repositories or components | Single-file summaries and source excerpts | Context extension registry; consuming artifact |
| `.fdi/context/domain/areas/{domain-id}.md` | A bounded domain area with a named domain owner | Architecture, implementation, or project-specific requirements | Context extension registry; consuming artifact |
| `.fdi/context/architecture/components/{component-id}.md` | A stable logical component listed in `system.md` whose detail would obscure the system overview | Source-file inventories and feature-local designs | Context extension registry; consuming artifact |
| `.fdi/context/knowledge/{decisions,learnings,incidents,patterns}/{knowledge-id}.md` | One reviewed knowledge item of the matching type, cataloged in `knowledge/index.md` | Raw chats, raw Git history, personal preferences, unverified agent notes, duplicate items | `knowledge/index.md`; consuming artifact |
| `.fdi/context/operations/runbooks/{runbook-id}.md` | An approved product-level cross-repository or shared-service runbook | Repository-local commands better owned beside source; secrets | Context extension registry; consuming artifact |
| `.fdi/context/external/reviews/{source-id}.md` | A review of one external source registered in `references.md` when its interpretation will be reused | Copied publications, raw web pages, uncited summaries | `references.md`; consuming artifact |
| `.fdi/skills/{skill-id}/SKILL.md` | One product-specific executable procedure registered as a skill extension; the seven fixed core skill IDs are reserved | Duplicate core procedures, Tool implementations, credentials, vendored dependencies | `.fdi/context/index.md#Executable skill extensions`; actual Skill version in the transition gate record |
| `.fdi/skills/{skill-id}/references/{reference-id}.md` | A reusable reference explicitly linked from the parent `SKILL.md` with a load condition | Unlinked notes, copied source repositories, raw transcripts | Parent `SKILL.md#Context selection`; actual match in the transition's `Context consulted` table |
| `.fdi/skills/{skill-id}/scripts/{script-id}.{sh,py,js,ts}` | An executable helper explicitly listed by the parent `SKILL.md`, using only the four allowed extensions | Binaries, vendored dependencies, generated code, credentials | Parent `SKILL.md#Tool bindings` or `#Procedure`; actual use/version in the transition gate record |
| `.fdi/skills/{skill-id}/assets/{asset-id}.{json,yaml,yml,txt,png,svg}` | A non-executable resource explicitly listed by the parent `SKILL.md`, using only the six allowed extensions | Secrets, raw sensitive transcripts, executable content, unlisted assets | Parent `SKILL.md#Procedure`; actual use/version in the transition gate record |
| `.fdi/baseline/capabilities/{capability-id}/{capability.md,implementation-map.md,verification.md}` | Exactly one complete, three-file allowlisted bundle per ID in `baseline/catalog.md` | Any other capability file and fabricated historical Intention/Spec/Change Set/V&V artifacts | `baseline/catalog.md`; selected IDs in feature artifacts |
| `.fdi/features/{feature-id}/{request.md,intention.md,vv-report.md}` | The three exact top-level feature files for the delivery key recorded in `request.md` | Ad-hoc aliases, personal scratch files, unrelated project docs | `request.md#Artifact identity`; downstream artifact identity sections |
| `.fdi/features/{feature-id}/spec/{index.md,requirements.md,design.md,tasks.md,vv-plan.md}` | The five exact Delivery Spec members for a registered feature | Extra spec members, generated drafts, historical copies outside VCS | `spec/index.md#Bundle membership`; downstream artifact identity sections |
| `.fdi/features/{feature-id}/change-set/index.md` | The single coordination-repository member of the logical Change Set; actual changes remain in source repositories | Copied source, patches used as substitute authority, unpinned candidate descriptions | `change-set/index.md#Candidate identity` and `#Repository revisions and PRs` |
| `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | One safe evidence record allocated by `spec/vv-plan.md` or a gate record | Secrets, raw sensitive transcripts, mutable unlabeled output, source-repository binaries | `spec/vv-plan.md#Evidence destinations`; `vv-report.md#Evidence inventory` |

No other Markdown path under `.fdi/` is trusted Context. Adding a new pattern requires owner approval through `steering/governance.md` and a revision of this contract.

## 4. Registries and common document schemas

### 4.1 `.fdi/product/repositories.yaml`

Although it is not Markdown, this registry is mandatory because all repository selectors depend on it. Each entry requires `repo_id`, canonical clone URI, provider, default branch, product role, owning team, repository-local instruction paths, source-of-truth scopes, and status (`active`, `retiring`, or `retired`). A `pinned_revision` belongs in a feature or baseline artifact, not this mutable registry. The product owner owns identity; each repository owner approves its entry. A repository addition, removal, rename, ownership change, or instruction-path change triggers refresh.

### 4.2 Curated Context schema `C`

Every Markdown file under `.fdi/context/` MUST contain:

1. `# <Title>`
2. `## Status` — `state` (`active`, `superseded`, `deprecated`), `scope`, `owners`, `approved_by`, `version`, `last_reviewed_at`, `next_review_due`, and `supersedes`/`superseded_by` when applicable.
3. `## Purpose`
4. The file-specific headings in section 6.
5. `## Provenance` — exact `source_refs`, revision/timestamp, producer, and validation method.
6. `## Freshness and supersession` — refresh triggers, staleness response, and successor path when applicable.

An expired or trigger-invalidated file remains discoverable but is not authoritative. The consuming agent MUST either verify it against the source, select the successor, or block with a conflict/gap.

### 4.3 Workflow artifact schema `F`

Every feature Markdown artifact except an evidence record MUST contain:

1. `# <Artifact title>`
2. `## Artifact identity` — feature ID, logical artifact, revision, status, producer, produced_at.
3. `## Inputs` — exact prior artifact paths/revisions and Human-source reference where applicable.
4. `## Context consulted` — exact path/URI, revision or timestamp, purpose, authority class, trust class, and selection reason; this is where bounded selector matches become concrete.
5. File-specific headings in section 7.
6. `## Traceability` — file-and-section anchors or project-native IDs to preceding and following obligations.
7. `## Open gaps and deviations` — owner, impact, disposition, and blocking state.
8. `## Gate record` — contract-ready status, failure reason if any, preflight evidence anchor, execution-review state/verdict, exact evidence paths, producing agent, Skill version, and Tools actually used.

Before execution, `execution-review` MUST say `NOT_CLAIMED` and name planned evidence destinations. It may be changed only after execution review.

### 4.4 Baseline schema `B`

Every baseline Markdown file MUST contain:

1. `# <Baseline title>`
2. `## Baseline identity` — snapshot/capability ID, revision, state, producer, observed_at.
3. `## Source scope` — repository IDs, immutable SHAs, environment/timestamp if runtime was observed, and exclusions.
4. File-specific headings in section 8.
5. `## Evidence and provenance`
6. `## Confidence and gaps`
7. `## Review and freshness` — repository-owner/domain-owner review, refresh triggers, next review, and supersession.
8. `## Gate record` when the file is a named gate destination.

Baseline status is `DISCOVERED`, `OWNER-CONFIRMED`, or `VERIFIED-AS-IS`. It never asserts unavailable historical intent.

### 4.5 Skill schema `S`

Every `.fdi/skills/*/SKILL.md` MUST contain YAML front matter with `name`, `description`, `version`, `source`, and compatible runtime range, followed by:

1. `# Purpose and applicability`
2. `## Transition contract` — exact artifact inputs/outputs and applicable transition.
3. `## Context selection` — always-read sources, bounded selectors, exclusions, precedence, and record destination.
4. `## Tool bindings` — stable tool identifiers, required/optional state, provider/runtime assumptions, and input/output contract.
5. `## Permissions and approvals` — allowed, prohibited, destructive/external/sensitive actions, and human approval boundaries.
6. `## Procedure`
7. `## Failure, escalation, and idempotency`
8. `## Completion and evidence`
9. `## Version and provenance`

Skills contain policies and bindings, never credentials or tool implementations. Preflight fails if a required Skill version or Tool is unavailable.

## 5. Category contracts

| Category | Semantic boundary and purpose | Authority / trust | Owner and producers | Consumers and load policy | Refresh, staleness, and conflict behavior |
| --- | --- | --- | --- | --- | --- |
| `context/steering/` | Product-wide desired policy: why, approved technology, layout conventions, agent boundaries, delivery policy, and governance | Normative within its named dimension; highest persistent policy trust, but cannot invent current behavior or override an approved feature outcome without formal reconciliation | Product, architecture, security, engineering, and governance owners; approved human or governed workflow | All FDI transitions; all six core files are persistent and extensions transition-load by registered scope | Event-triggered on policy/ownership/strategy change; maximum 180-day review. A conflict blocks the affected gate and is routed to the named policy owner |
| `context/codebase/` | Curated navigation to product components, repository roles, integrations, and useful entry points | Navigational, not evidence of current behavior | Repository owners produce repo maps; architecture owner owns cross-repo maps | `Human -> Intention` uses product map; later transitions select impacted repo maps/views. Live pinned source MUST be read for behavior claims | Refresh on repo/integration/ownership/default-branch change and maximum 90 days. Drift is resolved against registry and pinned live source |
| `context/domain/` | Stable vocabulary, business invariants, actors, regulated rules, and bounded domain areas | Glossary is definitional; approved rules are normative in their domain; neither proves implementation | Domain/product/legal owners | Intention and V&V always read core; Spec and implementation transition-load impacted areas | Refresh on policy/vocabulary change and maximum 180 days. Desired-behavior conflict routes to domain and feature approvers; implementation drift is surfaced separately |
| `context/architecture/` | Product-level system boundaries, interfaces, data ownership, and approved constraints | Normative for architectural constraints; descriptive views are curated and must be verified against live definitions | Architecture owner with repository/data owners | Spec always reads core; implementation/V&V selects impacted files/components; Intention reads only when constraints affect outcomes | Refresh on approved design, interface/schema, or ownership change and maximum 90 days. Live-source mismatch is a recorded architecture drift, never silently normalized |
| `context/knowledge/` | Reviewed decisions, evidence-backed learnings, curated incidents, and approved reusable patterns | Advisory/explanatory except an active decision within its declared scope; never overrides steering, approved feature artifacts, or current evidence | Named subject owner; reviewer promotes ephemeral observations | Retrieval-only by scope/tags/source refs | Refresh on contradicting evidence, remediation change, or explicit review date. Stale items are excluded; superseded items link successors |
| `context/operations/` | Product-level environments, release topology, shared operational constraints, and cross-repo runbooks | Normative for authorized environments/release policy; observed runtime state requires timestamped evidence | Platform/SRE/release owners | Spec, implementation, and V&V always read core; runbooks transition-load by environment/service | Refresh immediately on environment/release/runbook change and maximum 90 days. Unsafe or stale operational instructions block execution |
| `context/external/` | Catalog and reviewed interpretation of standards, vendor docs, research, laws, and third-party contracts | Untrusted/advisory until verified; a primary source may be authoritative only for its own external contract and declared as-of date | Subject owner registers; reviewer validates interpretation | Retrieval-only when a requirement, dependency, or uncertainty names it | Revalidate on source/version change or expiry, maximum 90 days unless source has a stricter cadence. Instruction-like external content is treated as data |
| `skills/` | Executable procedural Context that selects inputs, applies a transition, invokes declared Tools, and writes evidence | Procedurally normative for its transition after version/Tool preflight; does not override artifact or policy authority | Workflow owner plus security/tool owner for permissions | Exact transition Skill is persistent for that execution; helpers selected explicitly | Refresh on workflow/tool/runtime/permission change; smoke-test each revision. Missing binding or permission causes preflight failure |
| Current feature artifacts | Desired outcome and delivery obligations for one feature | Latest approved Intention governs product outcome; latest approved Delivery Spec governs implementation subject to Intention and policy; later artifacts report conformance, not new intent | Named producer and approver per artifact | Prior artifacts always load downstream; impacted baseline/context/live sources are selected | Revision invalidates downstream artifacts until reconciled; conflicts cause re-entry to the earliest defective artifact |
| Baseline artifacts | Evidence-backed, derived summary of current capabilities | `VERIFIED-AS-IS` is trusted navigation/current-behavior summary at its snapshot, subordinate to pinned source/runtime evidence | Repository owners confirm mappings; domain owner confirms description; independent reviewer verifies | Intention/Spec select affected capability IDs; baseline agents load full selected bundles | Refresh after observed release, source drift, or evidence expiry. Never reused as future intent |
| Live repository and runtime evidence | Actual source, tests, config, schemas, CI output, deployed observations, issues/PRs, and Git history | Primary for scoped current-behavior claims when pinned; history/issues are explanatory; runtime observations are environment/time scoped | Source repository and operational owners | Selected per impacted repo/path/interface/environment; never bulk-copied or indiscriminately loaded | Repin on each execution. Mutable/unpinned data cannot support a final claim; conflicts are reconciled by scope/revision/environment |

## 6. Per-file contracts: persistent Context

All rows below inherit schema `C`, including `.fdi/README.md` for its lifecycle fields even though it sits above `context/`. `P` means persistent, `T` transition-load, and `R` retrieval-only.

| Exact path | State | Required file-specific headings and semantics | Authority, provenance, producer/owner | Consumers/load | Complete and current; supersession |
| --- | --- | --- | --- | --- | --- |
| `.fdi/README.md` | Required | `## FDI version`; `## Repository role`; `## Entry points`; `## Safety boundary`; `## Adoption state` | Coordination-repo maintainer; cites approved FDI contract | All agents/P | All entry paths resolve and adoption state is honest; revised in place by version |
| `.fdi/context/index.md` | Required | `## Category catalog`; `## Mandatory core`; `## Governed extension registry` (exact path, category, purpose, owner, scope/tags, load rule, status); `## Executable skill extensions`; `## Selection rules` | Governance owner; registry entries approved by category owner | All agents/P | Core inventory and every extension match disk; removed entries become deprecated with successor |
| `.fdi/context/steering/product.md` | Required | `## Product purpose`; `## Users and stakeholders`; `## Value and outcomes`; `## Product boundaries`; `## Non-goals`; `## Principles` | Product owner; approved strategy sources | All transitions/P | Approved and reviewed <=180 days; successor/version recorded |
| `.fdi/context/steering/tech.md` | Required | `## Approved platforms`; `## Technology constraints`; `## Dependency policy`; `## Security and compliance constraints`; `## Exceptions` | Architecture/security owners; approved standards | All transitions/P | Stack/policy matches approved state; exceptions expire or renew |
| `.fdi/context/steering/structure.md` | Required | `## Repository topology`; `## Naming`; `## Placement`; `## Navigation`; `## Repository-local instruction precedence` | Architecture and repository owners | All transitions/P | Registry/topology aligned; superseded rules link replacement |
| `.fdi/context/steering/agent-policy.md` | Required | `## Autonomy levels`; `## Required approvals`; `## Security and sensitive data`; `## Tool boundaries`; `## Escalation`; `## Prohibited actions` | Governance/security owner | All agent executions/P | Matches current permission policy; stale policy blocks privileged actions |
| `.fdi/context/steering/delivery.md` | Required | `## Workflow semantics`; `## Transition gates`; `## Evidence policy`; `## Change and release rules`; `## Re-entry policy` | Delivery/release owner; cites approved semantics | All transitions/P | Matches approved workflow and source-repo release controls |
| `.fdi/context/steering/governance.md` | Required | `## Ownership model`; `## Authority by dimension`; `## Approval matrix`; `## Review cadence`; `## Conflict resolution`; `## Extension admission`; `## Deprecation` | Product governance owner | All transitions/P | Named active owners and valid cadences; changes use approved governance |
| `.fdi/context/steering/extensions/{policy-id}.md` | Conditional | `## Policy statement`; `## Applicability`; `## Obligations`; `## Exceptions`; `## Approval` | Named policy owner; approved decision/source | Matching transitions/T | Registry entry, active approval, review <=180 days; superseded file remains with successor |
| `.fdi/context/codebase/product-map.md` | Required | `## Product components`; `## Repository responsibilities`; `## Capability entry points`; `## Navigation queries`; `## Known gaps` | Architecture owner with repo owners; cites registry and pinned inspections | Intention P; others T | Every active repo represented; refresh <=90 days or topology change |
| `.fdi/context/codebase/integration-map.md` | Required | `## Integration inventory`; `## Direction and ownership`; `## Contract locations`; `## Failure boundaries`; `## Navigation queries` | Architecture/integration owners; exact live contract refs | Spec P; implementation/V&V T | Each integration has owners and resolvable refs; drift recorded, not concealed |
| `.fdi/context/codebase/repos/{repo-id}.md` | Conditional per active repo (therefore required for each) | `## Repository role`; `## Owned surfaces`; `## Entry points`; `## Tests and checks`; `## Local instructions`; `## Interfaces`; `## Navigation queries`; `## Known gaps` | Repository owner; registry and pinned source provenance | Selected by repo impact/T | ID exists in registry, refs resolve, owner confirms <=90 days; delete only after registry retirement and successor/archive note |
| `.fdi/context/codebase/views/{view-id}.md` | Conditional | `## Question answered`; `## Included repositories/components`; `## Navigation map`; `## Exclusions`; `## Verification queries` | Named cross-repo owner; pinned source refs | Matching transition/R | Registered, answers one stable cross-cutting query, refresh <=90 days |
| `.fdi/context/domain/glossary.md` | Required | `## Terms` (term, definition, owner, aliases, forbidden ambiguity); `## Actors`; `## State vocabulary` | Domain owner; approved domain sources | Intention and V&V/P; other transitions/T | No duplicate/conflicting active definition; review <=180 days |
| `.fdi/context/domain/rules.md` | Required | `## Invariants`; `## Decision rules`; `## Regulatory obligations`; `## Exceptions`; `## Validation implications` | Domain/legal/product owners | Intention, Spec, V&V/P; implementation/T | Every rule has scope, owner, source, effective date; expired rules excluded |
| `.fdi/context/domain/areas/{domain-id}.md` | Conditional | `## Scope`; `## Concepts and actors`; `## Rules and invariants`; `## Scenarios`; `## Boundaries`; `## Validation implications` | Domain-area owner | Selected by capability/requirement/R | Registered, source-backed, review <=180 days; successor linked |
| `.fdi/context/architecture/system.md` | Required | `## System context`; `## Components`; `## Boundaries and ownership`; `## Quality attributes`; `## Constraints`; `## Known drift` | Architecture owner; approved designs plus live validation | Spec/P; others/T | Component/owner inventory current <=90 days; drift explicitly separates desired from observed |
| `.fdi/context/architecture/interfaces.md` | Required | `## Interface inventory`; `## Producers and consumers`; `## Contract source locations`; `## Compatibility policy`; `## Versioning`; `## Known drift` | Interface and repo owners | Spec/P; implementation/V&V T | Each interface points to live schema/API path and owner; refresh on contract change |
| `.fdi/context/architecture/data.md` | Required | `## Data domains`; `## Ownership`; `## Stores and schemas`; `## Data flows`; `## Privacy and retention`; `## Migration constraints`; `## Known drift` | Data/security/architecture owners | Spec/P; implementation/V&V T | Live schema refs and policy review current <=90 days |
| `.fdi/context/architecture/components/{component-id}.md` | Conditional | `## Responsibility`; `## Interfaces`; `## Data`; `## Dependencies`; `## Constraints`; `## Failure modes`; `## Source anchors` | Component/architecture owners | Selected by change surface/R | Registered in `system.md` and context index; refresh with component contract |
| `.fdi/context/knowledge/index.md` | Required | `## Admission policy`; `## Active catalog` (ID, type, scope/tags, owner, status, validated_at, path); `## Superseded catalog`; `## Promotion process` | Knowledge governance owner; item owners | Context selector/P; items R | Catalog matches files; unreviewed/raw material never admitted |
| `.fdi/context/knowledge/decisions/{knowledge-id}.md` | Conditional | `## Decision`; `## Context`; `## Rationale`; `## Alternatives`; `## Consequences`; `## Scope and status` | Decision owner/approver; exact source refs | Selected by scope/R | Active/superseded status, owner, source refs, validated_at; successor required on supersession |
| `.fdi/context/knowledge/learnings/{knowledge-id}.md` | Conditional | `## Learning`; `## Evidence`; `## Confidence`; `## Applicability`; `## Counterevidence`; `## Recommended use` | Subject owner/reviewer | Selected by scope/R | Evidence-backed, confidence stated, revalidated on counterevidence |
| `.fdi/context/knowledge/incidents/{knowledge-id}.md` | Conditional | `## Incident summary`; `## Impact`; `## Contributing conditions`; `## Evidence`; `## Corrective actions`; `## Prevention checks`; `## Applicability` | Incident owner and service owner | Selected by affected service/risk/R | Postmortem approved; actions/status current; sensitive raw material excluded |
| `.fdi/context/knowledge/patterns/{knowledge-id}.md` | Conditional | `## Problem`; `## Applicability`; `## Pattern`; `## Constraints`; `## Examples`; `## Counterexamples`; `## Evidence` | Architecture/engineering owner | Selected by task type/R | Approved and demonstrated; deprecated on contradicting standard/source |
| `.fdi/context/operations/environments.md` | Required | `## Environment inventory`; `## Purpose and owners`; `## Access and approval classes`; `## Configuration sources`; `## Observability`; `## Data constraints` | Platform/SRE/security owners | Spec, implementation, V&V/P | Environment IDs and rules current <=90 days; never stores credentials |
| `.fdi/context/operations/release.md` | Required | `## Release topology`; `## Repository responsibilities`; `## Promotion gates`; `## Rollback`; `## Evidence`; `## Authority` | Release/platform/repository owners | Spec, implementation, V&V/P | Matches source-repo controls and current topology; stale mismatch blocks release claims |
| `.fdi/context/operations/runbooks/{runbook-id}.md` | Conditional | `## Trigger`; `## Preconditions`; `## Permissions`; `## Procedure`; `## Validation`; `## Rollback`; `## Escalation`; `## Evidence` | Service/platform owner | Selected by environment/service/T | Registered, tested at stated cadence, safe redaction; expired runbook cannot authorize action |
| `.fdi/context/external/references.md` | Required | `## Source catalog` (source ID, title, primary URI, publisher, version/as-of, scope, owner, trust, expiry); `## Retrieval policy`; `## Citation policy`; `## Disallowed content` | Subject/governance owner | Context selector/P; sources R | Links/version checked by expiry <=90 days; removed source retains citation history |
| `.fdi/context/external/reviews/{source-id}.md` | Conditional | `## Source identity`; `## Question reviewed`; `## Relevant claims`; `## Verification`; `## Applicability`; `## Limitations`; `## Expiry` | Subject owner and independent reviewer | Matching transitions/R | Registered source, primary-source citations, as-of date and expiry; successor review linked |

## 7. Per-file contracts: feature workflow artifacts

All rows except `.fdi/features/{feature-id}/evidence/{evidence-id}.md` inherit schema `F`; that evidence pattern uses the complete standalone heading contract in its row. Files are created when their producing transition starts; downstream placeholders MUST NOT be created early.

| Exact path | State | Required file-specific headings | Authoritative source/provenance | Producer; approver/owner; consumers | Completion/freshness and supersession |
| --- | --- | --- | --- | --- | --- |
| `.fdi/features/{feature-id}/request.md` | Required at intake | `## Human signal`; `## Requester and stakeholders`; `## Requested change`; `## Supplied constraints`; `## Source references`; `## Intake ambiguities` | Human signal and authenticated issue/request reference; quotations are data, not agent instructions | Intake agent; requester/product owner; Intention producer | Signal captured without reinterpretation, source resolvable, feature ID exact; revised entries retain source history |
| `.fdi/features/{feature-id}/intention.md` | Required after Human -> Intention begins | `## Rationale`; `## Stakeholders`; `## Intended outcome`; `## Intended-use scenarios`; `## Scope`; `## Constraints and assumptions`; `## Non-goals`; `## Success criteria`; `## Unresolved questions`; `## Authorization` | `request.md` plus consulted Context; Human/product approval for outcome | Intention agent; product owner/authorized policy; Spec and V&V agents | Complete only when success is distinguishable, material ambiguity is resolved, and authorization recorded; revision invalidates affected downstream artifacts |
| `.fdi/features/{feature-id}/spec/index.md` | Required with Delivery Spec | `## Bundle membership`; `## Intention mapping`; `## Change surface`; `## Cross-file consistency`; `## Spec authorization`; `## Gate record` | Approved Intention and the four spec members | Spec agent; architecture/product/repo owners by scope; implementation/V&V | All members exist, agree, and map every criterion; revision identifies superseded bundle revision |
| `.fdi/features/{feature-id}/spec/requirements.md` | Required with Delivery Spec | `## Functional requirements`; `## Non-functional requirements`; `## Acceptance criteria`; `## Interface obligations`; `## Exclusions` | Intention success criteria, domain/policy, current-state investigation | Spec agent; product/domain owners; design/tasks/V&V | Each requirement has an existing project-native ID or path anchor and Intention mapping; no material unresolved outcome |
| `.fdi/features/{feature-id}/spec/design.md` | Required with Delivery Spec | `## Design overview`; `## Components and repositories`; `## Interfaces`; `## Data and migrations`; `## Configuration and infrastructure`; `## Failure handling`; `## Security and operations`; `## Alternatives`; `## Risks and unknowns` | Requirements, selected architecture/codebase/live sources | Spec/design agent; architecture/repo/security owners by impact; implementation/V&V | All required behavior has a feasible, boundary-complete design; conflicts resolved or blocking |
| `.fdi/features/{feature-id}/spec/tasks.md` | Required with Delivery Spec | `## Task graph`; `## Ordered tasks`; `## Repository ownership`; `## Dependencies`; `## Completion evidence`; `## Deferred work` | Requirements/design/change surface | Spec/planning agent; implementing owners; implementation/V&V | Every requirement/design obligation maps to actionable dependency-aware work and evidence destination |
| `.fdi/features/{feature-id}/spec/vv-plan.md` | Required with Delivery Spec | `## Verification matrix`; `## Validation matrix`; `## Environments`; `## Methods and independence`; `## Evidence destinations`; `## Verdict rules`; `## Unavailable evidence handling` | Intention, requirements, design, operations, tool availability | Spec/V&V planner; quality/product owners; implementation and V&V agents | Every requirement, material design obligation, scenario, and success criterion has method, conditions, exact evidence record path, and expected result |
| `.fdi/features/{feature-id}/change-set/index.md` | Required after Spec -> Change Set begins | `## Candidate identity`; `## Repository revisions and PRs`; `## Changed paths` (exact repo ID + path + base/head SHA); `## Requirement/design/task mapping`; `## Producer checks`; `## Generated and operational artifacts`; `## Deviations`; `## Readiness for assessment` | Actual source-repository commits/PRs and producer evidence; never copied source | Implementation agent(s); repository owners; V&V agent | Exact assessable candidate pinned, changes mapped, checks recorded, no silent deviation; new commit supersedes candidate and requires reassessment |
| `.fdi/features/{feature-id}/vv-report.md` | Required after Change Set -> V&V begins | `## Assessed artifacts`; `## Evidence inventory`; `## Verification results`; `## Validation results`; `## Gaps and limitations`; `## Overall verdict`; `## Required disposition`; `## Baseline refresh eligibility`; `## Gate record` | Exact Intention, Spec, Change Set, independently generated/reproduced evidence | Independent V&V agent; quality/product/repo owners; release/baseline consumers | Complete with explicit result for every planned claim; `PASS` only with no material gap; new candidate or upstream revision supersedes report |
| `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | Conditional per allocated evidence item | `## Evidence identity`; `## Claim tested`; `## Method`; `## Source and execution conditions`; `## Raw evidence reference`; `## Observation`; `## Integrity`; `## Result`; `## Limitations` | Pinned CI/test/runtime/review output or reproducible inspection; sensitive material remains referenced in authorized system | Named executor/reviewer; V&V owner; change-set/V&V consumers | Source resolvable, candidate/environment/timestamp pinned, result reproducible or independently reviewed; immutable after cited, correction creates successor |

## 8. Per-file contracts: baseline artifacts

All rows inherit schema `B`. `snapshot.md` and `catalog.md` are mandatory after coordination-repository initialization and MUST state `NOT_BOOTSTRAPPED` truthfully until bootstrap begins; they are not empty placeholders.

| Exact path | State | Required file-specific headings | Source/provenance; producer/owner; consumers | Completion/freshness and supersession |
| --- | --- | --- | --- | --- |
| `.fdi/baseline/snapshot.md` | Required | `## Adoption state`; `## Repository snapshot`; `## Runtime snapshot`; `## Coverage`; `## Exclusions`; `## Capability summary`; `## Gate record` | Registry plus pinned repos/runtime; discovery agent; product/architecture owner; all baseline and feature agents | Every in-scope repo pinned, time/scope/exclusions explicit; refreshed after observed release or scope drift; old snapshot retained in VCS |
| `.fdi/baseline/catalog.md` | Required | `## Status semantics`; `## Capability catalog` (ID, title, owner, repos, status, confidence, bundle path); `## Coverage gaps`; `## Retired capabilities` | Capability bundles and snapshot; discovery agent; product/domain owner; Intention/Spec selection | IDs unique/stable and every active bundle resolves; retirement links last verified revision |
| `.fdi/baseline/capabilities/{capability-id}/capability.md` | Conditional per catalog ID | `## Observed actors and triggers`; `## Observed behavior`; `## Inputs and outputs`; `## Constraints`; `## Operating conditions`; `## Unknown intent`; `## Product-owner confirmation` | Pinned source/runtime/docs as cited; discovery agent; product/domain owner; feature agents | Product-facing statement evidence-backed, unknown intent explicit, owner-confirmed for `OWNER-CONFIRMED` or later |
| `.fdi/baseline/capabilities/{capability-id}/implementation-map.md` | Conditional per catalog ID | `## Repository coverage`; `## Paths and symbols`; `## Interfaces`; `## Data stores`; `## Dependencies`; `## Tests and configuration`; `## Repository-owner confirmation` | Pinned source, schemas, config, tests; discovery agent; repo owners; Spec/implementation/V&V | At least one concrete path/interface and evidence ref, all SHAs pinned, repository owners confirm mapping |
| `.fdi/baseline/capabilities/{capability-id}/verification.md` | Conditional per catalog ID | `## Claims assessed`; `## Methods`; `## Evidence`; `## Gaps`; `## Independent review`; `## As-is verdict`; `## Gate record` | Independent source/test/runtime evidence; baseline verifier; independent reviewer; feature and refresh consumers | `VERIFIED-AS-IS` only when observed behavior and map are supported; never historical validation; superseded on source/release drift |

## 9. Skill package contracts

Every `SKILL.md` inherits schema `S`; supporting reference files use the complete standalone heading contract in their row. The seven core packages are mandatory. Product-specific packages are conditional and admitted through `.fdi/context/index.md#Executable skill extensions`.

| Exact path | Required transition/applicability | Required special obligations | Owner and consumers; freshness |
| --- | --- | --- | --- |
| `.fdi/skills/context-selection/SKILL.md` | Helper used by every FDI transition | Resolve core + bounded selectors; reject stale/conflicting Context; write concrete selections into the output `Context consulted` table | Context governance owner; all agents; retest on taxonomy/runtime change |
| `.fdi/skills/human-to-intention/SKILL.md` | Human -> Intention | Preserve signal provenance; distinguish outcome from solution; require clarification/authorization | Product workflow owner; Intention agent; retest on Intention contract change |
| `.fdi/skills/intention-to-spec/SKILL.md` | Intention -> Delivery Spec | Discover full multi-repo change surface; produce all five spec files; enforce bidirectional traceability | Architecture/delivery owner; Spec agent; retest on spec/category change |
| `.fdi/skills/spec-to-implementation/SKILL.md` | Delivery Spec -> Change Set | Respect repository-local rules/owners; pin base/head; declare deviations; never bypass approvals | Engineering/repository owners; implementation agents; retest on SCM/CI/runtime change |
| `.fdi/skills/implementation-to-correctness/SKILL.md` | Change Set -> V&V Report | Require independent/reproduced evidence; separate verification/validation; enforce verdict/re-entry semantics | Quality/product owner; V&V agent; retest on V&V/tool change |
| `.fdi/skills/baseline-discovery/SKILL.md` | Pinned sources -> Capability Baseline | Describe only observed behavior; forbid fabricated intent; produce snapshot/catalog/capability/map | Architecture/product owners; discovery agent; retest on baseline contract change |
| `.fdi/skills/baseline-verification/SKILL.md` | Capability Baseline -> independently verified as-is baseline | Reproduce evidence, require repository and product confirmation, enforce `VERIFIED-AS-IS` boundary | Quality/repository/product owners; verifier; retest on baseline/evidence change |
| `.fdi/skills/{skill-id}/SKILL.md` | One registered product-specific procedure | State whether it composes with or specializes a core skill; may not weaken core gates or permissions | Named workflow/security/tool owners; selected agents; versioned review and smoke test required |
| `.fdi/skills/{skill-id}/references/{reference-id}.md` | Conditional reusable instruction/reference owned by one skill | Title, purpose, when to load, authority/trust, source refs, freshness; SKILL.md must link it | Skill owner; retrieval-only; review with parent Skill |

For conditional scripts/assets, `SKILL.md#Tool bindings` or `#Procedure` MUST list every concrete package-relative path, checksum or VCS revision, purpose, required permission, and output/evidence handling. Scripts are treated as code and reviewed under source-repository controls. Assets cannot contain secrets or raw sensitive transcripts.

## 10. Logical-to-physical bundle mapping

| Logical artifact/source | Physical bundle root | Required members | Conditional members | Producer | Consumers |
| --- | --- | --- | --- | --- | --- |
| Human signal | `.fdi/features/{feature-id}/` | `request.md` | None | Intake agent | Intention agent |
| Intention | `.fdi/features/{feature-id}/` | `intention.md` | Allocated evidence records | Intention agent | Spec and V&V agents |
| Delivery Spec | `.fdi/features/{feature-id}/spec/` | `index.md`, `requirements.md`, `design.md`, `tasks.md`, `vv-plan.md` | Evidence records allocated by plan | Spec agent(s) | Implementation and V&V agents |
| Change Set | Source repositories plus `.fdi/features/{feature-id}/change-set/` | `index.md` plus pinned commits/PRs at registered repository URIs | Generated/operational artifacts referenced by index | Implementation agents/repo owners | V&V/release/baseline agents |
| V&V Report | `.fdi/features/{feature-id}/` | `vv-report.md` | `evidence/{evidence-id}.md` selected by plan/findings | Independent V&V agent | Approvers/release/baseline refresh |
| Capability Baseline | `.fdi/baseline/` | `snapshot.md`, `catalog.md`; three files per registered capability | Runtime evidence refs | Discovery + verification agents | All feature transitions |
| Passive Context | `.fdi/context/` | Core files in tree | Only registered bounded extensions | Category owners | Context selector/all agents |
| Executable Context | `.fdi/skills/` | Seven core `SKILL.md` files | Registered Skill packages and listed resources | Workflow/tool/security owners | Transition agents |

## 11. Transition and Context-selection matrix

Every required read below is a literal repository-relative path or a current feature/baseline path under a bounded pattern from section 3.1. In rows 2 through B3, the exact lexical macro `all six literal steering paths from row 1` expands only to `.fdi/context/steering/product.md`, `.fdi/context/steering/tech.md`, `.fdi/context/steering/structure.md`, `.fdi/context/steering/agent-policy.md`, `.fdi/context/steering/delivery.md`, and `.fdi/context/steering/governance.md`; it never means an open-ended Context query. The following compact labels also expand only to their section 3.1 patterns: codebase views = `.fdi/context/codebase/views/{view-id}.md`; domain areas = `.fdi/context/domain/areas/{domain-id}.md`; architecture components = `.fdi/context/architecture/components/{component-id}.md`; knowledge items = `.fdi/context/knowledge/{decisions,learnings,incidents,patterns}/{knowledge-id}.md`; external reviews = `.fdi/context/external/reviews/{source-id}.md`; runbooks = `.fdi/context/operations/runbooks/{runbook-id}.md`; capability bundles = the three files under `.fdi/baseline/capabilities/{capability-id}/`. Every selected read names its bounded pattern and selection rule; the producing artifact records the concrete match.

| Order | Transition / producer | Exact required reads | Bounded selected reads and exclusions | Exact writes and gate destination | Completion and planned evidence | Contract gate |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Human -> Intention / Intention agent | `.fdi/README.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/product/repositories.yaml`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/product-map.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/human-to-intention/SKILL.md`; current `.fdi/features/{feature-id}/request.md` | `.fdi/baseline/capabilities/{capability-id}/{capability.md,implementation-map.md,verification.md}` for IDs named by intake; registered `.fdi/context/domain/areas/{domain-id}.md`, knowledge items, and external sources whose declared scope/tags match request terms. Exclude unverified notes, unrelated repos, and source internals unless a current-behavior ambiguity requires a pinned check | Current `.fdi/features/{feature-id}/intention.md`, including `.fdi/features/{feature-id}/intention.md#gate-record`; allocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | All Intention fields and criterion mappings complete; authorization evidence at an exact evidence path allocated in `.fdi/features/{feature-id}/intention.md#gate-record` | Preflight `CONTRACT_READY` when schema/selectors/evidence path resolve; execution `NOT_CLAIMED` until review |
| 2 | Intention -> Delivery Spec / Spec agent | `.fdi/README.md`; `.fdi/context/index.md`; all six literal steering paths from row 1; `.fdi/product/repositories.yaml`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/product-map.md`; `.fdi/context/codebase/integration-map.md`; `.fdi/context/architecture/system.md`; `.fdi/context/architecture/interfaces.md`; `.fdi/context/architecture/data.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/intention-to-spec/SKILL.md`; current `.fdi/features/{feature-id}/request.md`; current `.fdi/features/{feature-id}/intention.md` | Impacted `.fdi/context/codebase/repos/{repo-id}.md`, codebase views, domain areas, architecture components, knowledge items, external reviews, and runbooks; for every impacted repo, repository-local instruction files plus source/tests/config/schema at a pinned base SHA. Exclude unrelated repository trees and mutable unpinned reads | Current `.fdi/features/{feature-id}/spec/index.md`, `requirements.md`, `design.md`, `tasks.md`, and `vv-plan.md`; allocated evidence records; gate at `.fdi/features/{feature-id}/spec/index.md#gate-record` | Every criterion maps to requirements/design/tasks/planned V&V; change surface includes all repos/interfaces; exact review evidence paths allocated in `.fdi/features/{feature-id}/spec/vv-plan.md#evidence-destinations` | `CONTRACT_READY`; execution `NOT_CLAIMED` until produced/reviewed |
| 3 | Delivery Spec -> Change Set / implementation agent(s) | `.fdi/README.md`; `.fdi/context/index.md`; all six literal steering paths from row 1; `.fdi/product/repositories.yaml`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/spec-to-implementation/SKILL.md`; current `.fdi/features/{feature-id}/intention.md`; current `.fdi/features/{feature-id}/spec/index.md`, `requirements.md`, `design.md`, `tasks.md`, and `vv-plan.md` | Each impacted `.fdi/context/codebase/repos/{repo-id}.md`, repository-local instruction files, and exact planned source/test/config/schema paths at the pinned base SHA; applicable architecture components, domain areas, runbooks, knowledge items, and required Tool bindings. Exclude any repo/path not in the Spec unless recorded as a discovered scope change | Actual changes in registered source repositories; current `.fdi/features/{feature-id}/change-set/index.md`; producer evidence records; gate at `.fdi/features/{feature-id}/change-set/index.md#gate-record` | Candidate pins base/head/PR for every repo, exact changed paths and checks, all tasks mapped, and deviations reconciled or blocking; evidence at paths allocated in `vv-plan.md` | `CONTRACT_READY`; execution `NOT_CLAIMED` until candidate/evidence exist |
| 4 | Change Set -> V&V Report / independent V&V agent | `.fdi/README.md`; `.fdi/context/index.md`; all six literal steering paths from row 1; `.fdi/product/repositories.yaml`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/implementation-to-correctness/SKILL.md`; current `.fdi/features/{feature-id}/intention.md`; current `.fdi/features/{feature-id}/spec/index.md`, `requirements.md`, `design.md`, `tasks.md`, and `vv-plan.md`; current `.fdi/features/{feature-id}/change-set/index.md`; every evidence record named by the V&V plan and Change Set | Exact changed source plus impacted tests/config/interfaces at pinned head SHAs; affected baseline capability bundles; applicable architecture components, domain areas, runbooks, knowledge items, external sources, and independent Tool bindings. Exclude implementation-agent assertions not reproduced or independently inspected | New `.fdi/features/{feature-id}/evidence/{evidence-id}.md` records; current `.fdi/features/{feature-id}/vv-report.md`, including `.fdi/features/{feature-id}/vv-report.md#gate-record` | Every requirement/design obligation and success criterion has result/evidence; verification and validation remain separate; overall `PASS`, `FAIL`, or `INCONCLUSIVE` and re-entry target recorded | `CONTRACT_READY`; execution `NOT_CLAIMED` until independent assessment |
| B1 | Pinned sources -> Baseline Discovery / discovery agent | `.fdi/README.md`; `.fdi/context/index.md`; all six literal steering paths from row 1; `.fdi/product/repositories.yaml`; `.fdi/context/codebase/product-map.md`; `.fdi/context/codebase/integration-map.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/architecture/system.md`; `.fdi/context/architecture/interfaces.md`; `.fdi/context/architecture/data.md`; `.fdi/context/operations/environments.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/external/references.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-discovery/SKILL.md` | Every in-scope `.fdi/context/codebase/repos/{repo-id}.md`, repository-local instructions, and source/tests/config/schemas/docs at an exact SHA; authorized runtime observations; cited ADRs/issues/PRs/Git history; matching registered extensions. Exclude fabricated intent and raw uncited history/chat | `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; each discovered `.fdi/baseline/capabilities/{capability-id}/capability.md` and `implementation-map.md`; gate at `.fdi/baseline/snapshot.md#gate-record` | All repos pinned; every capability has concrete implementation/evidence refs; descriptions label unknown intent | `CONTRACT_READY`; execution `NOT_CLAIMED` until discovery review |
| B2 | Capability Baseline -> Independent As-Is Verification / baseline verifier | `.fdi/README.md`; `.fdi/context/index.md`; all six literal steering paths from row 1; `.fdi/product/repositories.yaml`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/architecture/system.md`; `.fdi/context/architecture/interfaces.md`; `.fdi/context/architecture/data.md`; `.fdi/context/operations/environments.md`; `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-verification/SKILL.md`; each selected `.fdi/baseline/capabilities/{capability-id}/capability.md` and `implementation-map.md` | Exact pinned source/tests/config/schema/runtime references cited by each selected capability plus evidence-generation Tools. Exclude producer-only claims not reproduced or independently inspected | Each selected `.fdi/baseline/capabilities/{capability-id}/verification.md`; updated status/confidence in `.fdi/baseline/catalog.md`; aggregate gate at `.fdi/baseline/snapshot.md#gate-record` | Repository owners confirm implementation maps, product/domain owner confirms descriptions, and independent verdicts are recorded; only supported items reach `VERIFIED-AS-IS` | `CONTRACT_READY`; execution `NOT_CLAIMED` until independent evidence |
| B3 | Released Change Set -> Baseline Refresh / baseline discovery + verifier | `.fdi/README.md`; `.fdi/context/index.md`; all six literal steering paths from row 1; `.fdi/product/repositories.yaml`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-discovery/SKILL.md`; `.fdi/skills/baseline-verification/SKILL.md`; current `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; released `.fdi/features/{feature-id}/change-set/index.md`; released `.fdi/features/{feature-id}/vv-report.md` | Exact released SHAs, affected capability bundles, release evidence, and affected source/runtime. Exclude unreleased candidates and feature claims without a `PASS` verdict | Revised `.fdi/baseline/snapshot.md`, `.fdi/baseline/catalog.md`, and affected capability bundles; gate at `.fdi/baseline/snapshot.md#gate-record` | Release observed, affected capabilities added/updated/retired, owners and independent verifier confirm, and prior snapshot remains in VCS | `CONTRACT_READY`; execution `NOT_CLAIMED` until release/refreshed evidence |

Every transition writes concrete selector matches, actual Skill/Tool versions, and actual evidence paths into its declared `Gate record` and `Context consulted` sections. A mismatch from the plan is either reconciled there with owner approval or fails execution review.

## 12. End-to-end traceability contract

The coordination repository uses existing feature IDs, requirement/task identifiers, repository paths, and Markdown anchors; it introduces no universal ledger.

| Link | Required representation |
| --- | --- |
| Human request -> Intention | `request.md#Requested change` and source reference map to each `intention.md#Success criteria` item |
| Intention -> Delivery Spec | `spec/index.md#Intention mapping` maps each success criterion to exact anchors in `requirements.md`, `design.md`, `tasks.md`, and `vv-plan.md` |
| Delivery Spec -> changed repository file | `change-set/index.md#Requirement/design/task mapping` maps each obligation to `repo-id:path@head-sha`, PR, or an explicit justified no-code outcome |
| Changed file -> evidence | `vv-plan.md` allocates the evidence record; `vv-report.md#Evidence inventory` maps the exact candidate and evidence record to the tested claim |
| Evidence -> verdict | `vv-report.md` records per-claim result and the overall verdict; missing/invalid evidence yields `INCONCLUSIVE`, nonconformance yields `FAIL`, and `PASS` requires both verification and validation with no material gap |

A broken link is a blocking gap. The workflow re-enters the earliest artifact that can correct it; the report alone is never edited to conceal the gap.

## 13. Desired-behavior and current-behavior authority

### 13.1 Desired behavior

Authority is separated by dimension so two documents cannot silently compete:

1. The latest approved `intention.md` owns the stakeholder outcome, scope, non-goals, intended use, and success criteria.
2. The latest approved Delivery Spec owns requirements and technical implementation obligations, but cannot change the Intention.
3. Steering owns persistent product/technical/security/delivery constraints; domain rules own domain invariants; architecture owns approved system/interface/data constraints.
4. A feature artifact that conflicts with a normative constraint is not automatically overridden or allowed to override it. The transition blocks until the Intention/Spec owner and the relevant policy/domain/architecture owner approve a revision or explicit governed exception.
5. Knowledge, baseline, codebase maps, and external reviews may inform or expose a conflict but cannot establish new desired behavior.

### 13.2 Current behavior

Current-behavior claims are scoped by repository revision, environment, and time:

1. Pinned source, configuration, schemas, and executable tests are primary for the candidate/source revision. A test supports a claim only with its result and execution conditions.
2. Timestamped runtime/telemetry evidence is primary for what the named deployed environment actually did; the deployed revision MUST be identified or the result is `INCONCLUSIVE` for revision-specific claims.
3. Repository-local authoritative documentation and ownership files define local procedures and controls, not observed behavior unless verified.
4. `VERIFIED-AS-IS` baseline artifacts summarize evidence at their snapshot and are subordinate to newer pinned evidence.
5. Architecture/codebase maps are navigation; knowledge and Git/issues/PR history explain why; external sources describe outside contracts. None outranks pinned current evidence.

Apparent conflicts are first reconciled by revision/environment/scope. A genuine mismatch is recorded in `Open gaps and deviations` or baseline `Confidence and gaps`, routed to the owner, and blocks any claim that depends on it.

## 14. Multi-repository ownership boundaries

| Concern | Coordination repository authority | Source repository authority | Required handshake |
| --- | --- | --- | --- |
| Product intent and cross-repo scope | Canonical Intention and aggregate Spec | Provides feasibility/current-state evidence | Product owner approves outcome; impacted repo owners confirm change surface |
| Source/config/schema/tests | Stores only pinned references and mappings | Canonical content, local rules, reviews, CI, branch protection | Spec names exact repos/paths; repo owners approve changes locally |
| Interfaces/data ownership | Product-level map and cross-boundary obligation | Canonical interface/schema implementation | Producer and consumer/data owners approve compatibility/migration obligations |
| Change Set | Canonical aggregate index across commits/PRs | Actual candidate commits/PRs | Index pins all heads and statuses; no aggregate `PASS` with missing repo candidate |
| Evidence | Safe index/records and aggregate interpretation | Raw CI/build/test artifacts when locally owned | Evidence record preserves URI/digest/revision/conditions without copying secrets |
| Release | Records planned gates and observed release evidence | Executes and authorizes release/rollback | Aggregate report cannot bypass local release authority; baseline refresh waits for observed release |
| Context upkeep | Product/category owners maintain shared Context | Repo owners maintain local instructions and truth | Repo maps link local sources; drift triggers refresh and owner confirmation |

## 15. Failure and staleness handling

- Missing mandatory core: transition preflight fails `NOT_CONTRACT_READY`.
- Required bounded selector has no concrete match: record a Context gap and stop; do not choose a nearby file by guess.
- Stale curated file: verify against its authoritative source and record the newer evidence, or block until refreshed. Do not silently refresh ownership-sensitive policy.
- Conflicting desired/current sources: record both exact sources and route using section 13; do not collapse desired behavior into observed behavior.
- Missing Skill/Tool/permission: preflight fails before execution; request the named approval or binding.
- Unsafe evidence: retain only an authorized reference, digest, redacted observation, and access classification. Never persist secrets or raw sensitive transcripts.
- Revision of Intention, Spec, or candidate: mark affected downstream artifact revisions superseded and rerun the required transition/review.

## 16. Preflight review of this design

### 16.1 Mandatory contract preflight

| Check | Result | Evidence in this document |
| --- | --- | --- |
| Logical artifacts distinguished from physical bundles | PASS | Sections 1 and 10 |
| Complete tree with mandatory files and bounded conditional patterns | PASS | Sections 3 and 3.1 |
| Category boundaries, authority, ownership, loading, freshness, conflict | PASS | Section 5 |
| Exact per-file Markdown headings and lifecycle contracts | PASS | Sections 4, 6, 7, 8, and 9 |
| Skill packages declare Tools, permissions, selection, failures, completion, evidence | PASS | Sections 4.5 and 9 |
| Exact transition reads/writes/selectors/gate destinations | PASS | Section 11 |
| Desired and current authority separated | PASS | Section 13 |
| Multi-repository boundary explicit | PASS | Section 14 |
| End-to-end traceability concrete | PASS | Section 12 |
| No `context/tools/`, bulk source copies, secrets, raw chats, or invented baseline intent | PASS | Sections 1, 3, 3.1, 5, and 15 |

### 16.2 Gate result

- **Contract-ready:** `PASS` for review. The mandatory preflight is fully specified, all patterns are bounded, and no design placeholder remains.
- **Execution-verified:** `NOT_CLAIMED`. No physical `.fdi/` repository implementation, Skill packaging, baseline run, feature transition, or evidence-producing execution was performed by this design task.
- **Approval required before implementation:** Herman must approve this contract. Only then may a separate implementation task create `.fdi/` files or revise the installed `fdi-workflow-harness`.
