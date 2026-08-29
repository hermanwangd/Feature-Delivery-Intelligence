# FDI Context Taxonomy and Markdown Contract v0.1

**Status:** Proposed coordination-repository profile (`Contract-ready: PASS`; `Execution-verified: NOT_CLAIMED`)

**Date:** 2026-08-29

**Scope:** A dedicated FDI coordination repository for one product, including products implemented across multiple source repositories.

## 1. Decision, semantic boundary, and conformance

FDI Workflow Semantics v0.1 is storage- and schema-neutral. It defines the four-stage logical flow but does not prescribe a universal directory layout, Markdown schema, or repository topology:

```text
Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report
```

This document is the dedicated **coordination-repository profile** for teams that choose that operating model. It specializes the semantic baseline without redefining it. Every normative `MUST`, `MUST NOT`, and `REQUIRED` in this document applies only to a repository that adopts this profile.

The profile uses a small mandatory core plus governed extensions. Stable core paths make workflow runs interoperable; bounded extensions avoid forcing irrelevant files on every product. The coordination repository owns durable product Context, cross-repository feature artifacts, baseline summaries, and safe evidence references. Source repositories retain authority for source, local instructions, tests, configuration, schemas, reviews, CI, branch protection, deployment, and release execution.

Baseline reconstruction is an as-is support workflow, not a fifth logical artifact or stage. Skills are executable procedural Context and declare the capabilities they use; capabilities are not a peer Context category.

## 2. Normative vocabulary and state

- **Required:** present for every conforming profile.
- **Conditional:** present only when its bounded matching rule is true; empty placeholders are prohibited.
- **Always-load:** read for every transition named by the contract.
- **Transition-load:** read only for a named transition after its scope selector matches.
- **Retrieval-only:** discovered through an index and read only after a bounded applicability match.
- **Ephemeral:** used during execution but not persisted as Context; only an authorized reference and interpretation may be recorded.
- **Current:** approved, within its review interval, resolvable at its cited revision, and unaffected by an unresolved refresh trigger.
- **Planned relation:** proposed by an approved Delivery Spec but not yet verified in a released implementation. It MUST NOT be selected or represented as current Context.
- **Implemented candidate relation:** present at a pinned Change Set head but not yet released.
- **Current relation:** independently verified and observed in a released revision, then refreshed into Codebase.
- **Retired relation:** no longer present in the current released topology; retained only for traceability and excluded from default selection.
- **Superseded:** retained for traceability, excluded from default selection, and linked to a named successor.
- **Pinned source:** an immutable commit SHA, artifact digest, release identifier, or timestamped environment observation tied to a deployed revision.

## 3. Coordination-repository tree

```text
.fdi/
├── README.md
├── context/
│   ├── contract.md
│   ├── index.md
│   ├── steering/
│   │   ├── product.md
│   │   ├── tech.md
│   │   ├── structure.md
│   │   ├── architecture.md
│   │   ├── agent-policy.md
│   │   ├── delivery.md
│   │   ├── governance.md
│   │   └── extensions/{policy-id}.md
│   ├── codebase/
│   │   ├── catalog.md
│   │   ├── relations.md
│   │   ├── system-context.md
│   │   ├── integrations.md
│   │   ├── data.md
│   │   ├── repositories/{repo-id}.md
│   │   └── views/{view-id}.md
│   ├── domain/
│   │   ├── glossary.md
│   │   ├── rules.md
│   │   └── areas/{domain-id}.md
│   ├── knowledge/
│   │   ├── index.md
│   │   ├── decisions/{knowledge-id}.md
│   │   ├── incidents/{knowledge-id}.md
│   │   ├── learnings/{knowledge-id}.md
│   │   └── patterns/{knowledge-id}.md
│   ├── operations/
│   │   ├── environments.md
│   │   ├── release.md
│   │   ├── observability.md
│   │   └── runbooks/{runbook-id}.md
│   └── external/
│       ├── references.md
│       └── reviews/{source-id}.md
├── skills/
│   ├── catalog.md
│   ├── context-selection/SKILL.md
│   ├── human-to-intention/SKILL.md
│   ├── intention-to-spec/SKILL.md
│   ├── spec-to-implementation/SKILL.md
│   ├── implementation-to-correctness/SKILL.md
│   ├── baseline-discovery/SKILL.md
│   ├── baseline-verification/SKILL.md
│   └── {skill-id}/
│       ├── SKILL.md
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
    ├── change-set/index.md
    ├── vv-report.md
    └── evidence/{evidence-id}.md
```

### 3.1 Bounded conditional patterns

All IDs except `{feature-id}` MUST match `[a-z0-9]+(?:-[a-z0-9]+)*`. `{feature-id}` is the exact case-preserving delivery key. IDs MUST NOT contain `/`, `..`, whitespace, URI schemes, or user-local paths.

| Pattern | Matching rule | Exclusions | Concrete-match record |
| --- | --- | --- | --- |
| `.fdi/context/steering/extensions/{policy-id}.md` | One approved normative policy whose obligations do not fit a core steering file | Notes, plans, duplicate core policy | `.fdi/context/index.md#Governed-extensions` and the consumer's `Context consulted` |
| `.fdi/context/codebase/repositories/{repo-id}.md` | Exactly one file for each active Repository entity in `catalog.md` | Source copies, generated trees, unregistered repositories | `catalog.md#Entities` and the consumer's `Context consulted` |
| `.fdi/context/codebase/views/{view-id}.md` | A derived navigation view over IDs in `catalog.md` and current edges in `relations.md` | Independently maintained topology facts, planned edges presented as current | `.fdi/context/index.md#Governed-extensions`; query and matched IDs in `Context consulted` |
| `.fdi/context/domain/areas/{domain-id}.md` | One bounded domain area with an owner listed in `glossary.md` | Implementation maps and feature-local requirements | Context index and consuming artifact |
| `.fdi/context/knowledge/{decisions,incidents,learnings,patterns}/{knowledge-id}.md` | One reviewed record admitted by `knowledge/index.md` | Feature copies, raw chat/Git history, unverified notes | `knowledge/index.md#Active-catalog` and consuming artifact |
| `.fdi/context/operations/runbooks/{runbook-id}.md` | Approved shared or cross-repository procedure | Secrets and repository-local procedures | Context index and consuming artifact |
| `.fdi/context/external/reviews/{source-id}.md` | Reviewed interpretation of one entry in `external/references.md` | Copied publications and uncited summaries | `external/references.md#Source-catalog` and consuming artifact |
| `.fdi/skills/{skill-id}/SKILL.md` | Registered product-specific procedure; seven core IDs are reserved | Credentials, duplicate core procedures, vendored capability implementations | `.fdi/skills/catalog.md#Skill-registry` and the gate record |
| `.fdi/skills/{skill-id}/references/{reference-id}.md` | Linked from the parent `SKILL.md` with an explicit load condition | Unlinked notes and raw transcripts | Parent `SKILL.md#Context-selection` and gate record |
| `.fdi/skills/{skill-id}/scripts/{script-id}.{sh,py,js,ts}` | Listed by the parent Skill with digest and invocation contract | Binaries, vendored dependencies, credentials | Parent `SKILL.md#Capability-bindings` and gate record |
| `.fdi/skills/{skill-id}/assets/{asset-id}.{json,yaml,yml,txt,png,svg}` | Listed non-executable resource with digest and use condition | Executables, secrets, unlisted assets | Parent `SKILL.md#Procedure` and gate record |
| `.fdi/baseline/capabilities/{capability-id}/{capability.md,implementation-map.md,verification.md}` | One complete three-file bundle per ID in `.fdi/baseline/catalog.md` | Fabricated historical feature artifacts and extra bundle files | `.fdi/baseline/catalog.md#Capability-registry` and consuming artifact |
| `.fdi/features/{feature-id}/{request.md,intention.md,vv-report.md}` | Three exact top-level members for the feature key in `request.md` | Aliases, scratch files, unrelated documents | `request.md#Artifact-identity` and downstream identities |
| `.fdi/features/{feature-id}/spec/{index.md,requirements.md,design.md,tasks.md,vv-plan.md}` | Five exact Delivery Spec members | Extra spec members and generated drafts | `spec/index.md#Bundle-membership` |
| `.fdi/features/{feature-id}/change-set/index.md` | One aggregate index referencing pinned source-repository candidates | Copied source and unpinned candidate descriptions | `change-set/index.md#Repository-revisions-and-PRs` |
| `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | Safe evidence record allocated by `vv-plan.md` or a gate | Secrets, mutable unlabeled output, binary artifacts | `vv-plan.md#Evidence-destinations` and `vv-report.md#Evidence-inventory` |

No other path under `.fdi/` is trusted Context. A new pattern requires governance approval and a revision to `.fdi/context/contract.md`.

### 3.2 Bounded source-repository selectors

Live reads use `repo:{repo-id}@{sha}:{path}`. `{repo-id}` MUST identify an active Repository entity in `catalog.md`; `{sha}` MUST be immutable; `{path}` MUST be one of:

1. an exact repository-local instruction path recorded in `repositories/{repo-id}.md#Local-instructions`;
2. an exact source/test/config/schema/interface path recorded in a feature artifact or baseline implementation map; or
3. a repository-relative glob recorded in `.fdi/features/{feature-id}/spec/design.md#Change-surface` or `.fdi/baseline/snapshot.md#Source-scope`, with its root prefix, allowed extensions, maximum match count, and exclusions.

Directory-wide reads, mutable branch-only reads, dependency caches, build outputs, vendored trees, secrets, and paths outside the registered repository are excluded. Every concrete match is recorded as `repo-id:path@sha` in the producing artifact's `Context consulted`; zero matches or an exceeded maximum is a blocking gap.

## 4. Common schemas and canonical topology contracts

### 4.1 Curated Context schema `C`

Every Markdown file under `.fdi/context/`, plus `.fdi/README.md`, MUST contain `# Title`, `## Status`, `## Purpose`, its section 6 headings, `## Provenance`, and `## Freshness and supersession`. Status records state, scope, owners, approvers, version, review dates, and successor links. Provenance records exact paths/anchors or immutable identifiers, producer, revision/time, and validation method.

### 4.2 Workflow artifact schema `F`

Every feature artifact except an evidence record MUST contain `# Title`, `## Artifact identity`, `## Inputs`, `## Context consulted`, its section 7 headings, `## Traceability`, `## Open gaps and deviations`, and `## Gate record`. The gate records the producing agent, Skill version, bound capability identifiers, preflight status/evidence, execution-review state/verdict, and exact evidence paths. Before real execution, execution review MUST remain `NOT_CLAIMED`.

### 4.3 Baseline schema `B`

Every baseline file MUST contain `# Title`, `## Baseline identity`, `## Source scope`, its section 8 headings, `## Evidence and provenance`, `## Confidence and gaps`, and `## Review and freshness`; `snapshot.md` also contains `## Gate record`. Status is `DISCOVERED`, `OWNER-CONFIRMED`, or `VERIFIED-AS-IS` and never asserts unavailable historical intent.

### 4.4 `catalog.md`: canonical entity registry

`.fdi/context/codebase/catalog.md` is the sole canonical registry for current topology entities. Its `## Entities` table MUST contain:

- stable ID and entity type: `Product`, `Domain`, `System`, `Component`, `API`, `Resource`, or `Repository`;
- name, description, owners, lifecycle status, and product role;
- Repository mapping for implementation-bearing entities;
- exact source reference as `repo-id:path@sha`, approved registry URI, or evidence anchor;
- last verification revision/date.

Stable IDs survive renames. One Product contains the adopted profile; Domains group Systems by business purpose; Systems group Components, APIs, and Resources into a product function; Components are deployable or executable implementation units; APIs are provided contracts; Resources are runtime or data dependencies; Repositories are source-control authority boundaries. A Repository is not a Product or Component.

### 4.5 `relations.md`: canonical relationship registry

`.fdi/context/codebase/relations.md` is the sole canonical registry for topology edges. Each row MUST contain stable relation ID, source entity ID, relation type, target entity ID, owner, exact evidence, state, and last verification revision/date.

Allowed types are `contains`, `implemented-by`, `provides`, `consumes`, `depends-on`, `stores-in`, and `deployed-as`. Source and target types MUST satisfy the validation matrix in `relations.md#Allowed-relationship-types`; invalid pairs fail preflight. `current` edges require released evidence; `planned` edges remain canonical only in the Delivery Spec and MUST NOT be written to or selected from Codebase; `retired` edges remain traceable but are excluded from current queries.

`catalog.md` and `relations.md` are canonical. `system-context.md`, `integrations.md`, `data.md`, repository files, Codebase views, baseline maps, and diagrams are derived views or evidence-backed projections and MUST cite the entity/relation IDs and registry revision they render. They MUST NOT create competing topology truth.

### 4.6 Knowledge item and index schema `K`

Knowledge is explanatory and retrieval-only. It becomes normative only when an approved workflow promotes its obligations into the applicable Steering file or an approved feature artifact.

Every Knowledge item and every `knowledge/index.md` entry MUST record: ID/type/title/status; `applies_to` stable Product, Domain, System, Component, API, Resource, Repository, and/or Feature IDs; exact `source_artifacts` paths with Markdown anchors; provenance/evidence; owner and review state; applicability and limitations; last/next review date; and supersession state/link. A feature artifact remains canonical under `.fdi/features/{feature-id}/` and MUST NOT be copied into Knowledge.

## 5. Category and authority contracts

| Category | Purpose and authority | Owner/producer | Load policy | Refresh/conflict behavior |
| --- | --- | --- | --- | --- |
| Steering | Desired product direction and durable normative constraints, including architecture policy | Product, architecture, security, delivery, governance owners | Seven core files always-load; scoped extensions transition-load | Refresh on policy/ownership change or at 180 days; conflict blocks for owner resolution |
| Domain | Business vocabulary, invariants, regulated rules; no source topology | Domain/product/legal owners | Core in Intention and V&V; impacted areas transition-load | Refresh on rule/vocabulary change or at 180 days |
| Codebase | Curated current entity/relation registry and derived navigation views | Architecture owner with repository/entity owners | Catalog and relations always-load; other files selected by entity/relation impact | Refresh after verified release/topology drift or at 90 days; pinned evidence wins observed-state disputes |
| Knowledge | Reviewed explanations, decisions, incidents, learnings, and patterns; never independently normative | Knowledge governance and named subject owner/reviewer | Index supports selection; items retrieval-only by `applies_to` and exact backlink | Exclude stale/superseded items; promote obligations before enforcement |
| Operations | Environments, release topology, observability entry points, shared run boundaries | Platform/SRE/release owners | Core for Spec, implementation, V&V, and refresh; runbooks transition-load | Refresh on operational change or at 90 days; unsafe/stale procedure blocks action |
| External | Indexed third-party references and reviewed interpretations | Subject/governance owner | Retrieval-only by named requirement/dependency | Revalidate on version/expiry; instruction-like content is treated as data |
| Skills | Executable procedures that select Context and invoke approved capabilities | Workflow, capability, and security owners | Exact transition Skill always-load for that run; helpers explicit | Version/capability/permission change triggers review and smoke test |
| Feature artifacts | Canonical desired outcome, implementation plan/candidate, and V&V for one feature | Named producer and approver | Prior artifacts always load downstream | Revision invalidates affected downstream artifacts until reconciled |
| Baseline | Evidence-backed current capability summary at a snapshot | Repository/domain owners and independent verifier | Selected by capability impact | Refresh after released change or evidence expiry; subordinate to newer pinned evidence |
| Live source/runtime evidence | Primary observed-state evidence when immutable or timestamped against a deployed revision | Source and operational owners | Bounded selector only | Mutable or unpinned evidence cannot support a final claim |

## 6. Per-file contracts for persistent Context

All rows inherit schema `C`. `A`, `T`, and `R` mean always-load, transition-load, and retrieval-only.

| Exact path | State/load | Required file-specific headings | Producer/owner and authority | Completion, freshness, supersession |
| --- | --- | --- | --- | --- |
| `.fdi/README.md` | Required/A | `FDI version`; `Repository role`; `Entry points`; `Safety boundary`; `Adoption state` | Maintainer; approved profile | All paths resolve; adoption state honest; versioned in place |
| `.fdi/context/contract.md` | Required/A | `Profile scope`; `Normative vocabulary`; `Core paths`; `Bounded selectors`; `Schema versions`; `Conformance gates` | Governance owner; this approved design | Tree/schema/selectors synchronized; revision required for contract change |
| `.fdi/context/index.md` | Required/A | `Category catalog`; `Mandatory core`; `Governed extensions`; `Selection rules` | Governance and category owners | Inventory matches disk; deprecated entries name successor |
| `.fdi/context/steering/product.md` | Required/A | `Product purpose`; `Users and stakeholders`; `Value and outcomes`; `Boundaries`; `Non-goals`; `Principles` | Product owner; normative | Approved and reviewed within 180 days |
| `.fdi/context/steering/tech.md` | Required/A | `Approved platforms`; `Technology constraints`; `Dependency policy`; `Security and compliance`; `Exceptions` | Architecture/security owners; normative | Stack/policy current; exceptions expire or renew |
| `.fdi/context/steering/structure.md` | Required/A | `Coordination layout`; `Source-repository topology`; `Naming`; `Placement`; `Instruction precedence` | Architecture/repository owners; normative | Aligns with active Repository entities |
| `.fdi/context/steering/architecture.md` | Required/A | `Principles`; `System boundaries`; `Quality attributes`; `Approved patterns`; `Prohibited patterns`; `Interface and data constraints`; `Exceptions` | Architecture/data/security owners; normative | Approved obligations current; descriptive claims link to Codebase IDs |
| `.fdi/context/steering/agent-policy.md` | Required/A | `Autonomy`; `Approvals`; `Sensitive data`; `Capability boundaries`; `Escalation`; `Prohibited actions` | Governance/security owner; normative | Current permission policy; staleness blocks privileged work |
| `.fdi/context/steering/delivery.md` | Required/A | `Workflow semantics`; `Transition gates`; `Evidence policy`; `Change and release`; `Re-entry` | Delivery/release owner; normative | Matches semantic baseline and local controls |
| `.fdi/context/steering/governance.md` | Required/A | `Ownership`; `Authority by dimension`; `Approval matrix`; `Review cadence`; `Conflict resolution`; `Extension admission`; `Deprecation` | Governance owner; normative | Active owners/cadences; governed exceptions only |
| `.fdi/context/steering/extensions/{policy-id}.md` | Conditional/T | `Policy`; `Applicability`; `Obligations`; `Exceptions`; `Approval` | Named policy owner; normative in scope | Registered/approved/reviewed within 180 days |
| `.fdi/context/codebase/catalog.md` | Required/A | `Entity model`; `Entities`; `ID lifecycle`; `Validation`; `Known gaps` | Architecture owner plus entity/repository owners; canonical current registry | Required fields in 4.4; released evidence; refresh within 90 days |
| `.fdi/context/codebase/relations.md` | Required/A | `Relationship model`; `Allowed relationship types`; `Relations`; `State semantics`; `Validation`; `Known gaps` | Architecture owner plus edge owners; canonical current registry | Required fields in 4.5; no planned-as-current edge; refresh within 90 days |
| `.fdi/context/codebase/system-context.md` | Required/T | `Product boundary`; `Users`; `Systems`; `External systems`; `Interactions`; `Rendered registry revision` | Architecture owner; derived view | Every node/edge cites current IDs; regenerate on registry change |
| `.fdi/context/codebase/integrations.md` | Required/T | `Integration inventory`; `Direction`; `Owners`; `Contract locations`; `Compatibility`; `Failure boundaries`; `Rendered registry revision` | Integration/repository owners; derived view | Each integration cites relation IDs and pinned contracts |
| `.fdi/context/codebase/data.md` | Required/T | `Data domains`; `Owners`; `Stores and schemas`; `Flows`; `Privacy and retention`; `Migration constraints`; `Rendered registry revision` | Data/security owners; derived view | IDs and live schema refs resolve; refresh on data relation change |
| `.fdi/context/codebase/repositories/{repo-id}.md` | Conditional/T | `Repository identity`; `Product role`; `Owned entities`; `Entry points`; `Tests and checks`; `Local instructions`; `Interfaces`; `Known gaps` | Repository owner; navigation projection | One per active Repository ID; refs resolve; review within 90 days |
| `.fdi/context/codebase/views/{view-id}.md` | Conditional/R | `Question`; `Registry query`; `Included IDs`; `Exclusions`; `Rendered registry revision`; `Verification query` | Named owner; derived view | Registered query reproducible; refresh on cited registry revision |
| `.fdi/context/domain/glossary.md` | Required/T | `Terms`; `Actors`; `State vocabulary` | Domain owner; definitional | No conflicting active definitions; review within 180 days |
| `.fdi/context/domain/rules.md` | Required/T | `Invariants`; `Decision rules`; `Regulatory obligations`; `Exceptions`; `Validation implications` | Domain/legal/product owners; normative | Every rule scoped/sourced/effective; expired rules excluded |
| `.fdi/context/domain/areas/{domain-id}.md` | Conditional/R | `Scope`; `Concepts`; `Rules`; `Scenarios`; `Boundaries`; `Validation implications` | Domain-area owner | Registered/source-backed/reviewed within 180 days |
| `.fdi/context/knowledge/index.md` | Required/T | `Admission policy`; `Active catalog`; `Superseded catalog`; `Promotion process`; `Retrieval rules` | Knowledge governance owner; retrieval index | Every entry satisfies schema `K`; catalog matches files |
| `.fdi/context/knowledge/decisions/{knowledge-id}.md` | Conditional/R | `Decision`; `Context`; `Rationale`; `Alternatives`; `Consequences`; schema `K` fields | Decision owner/reviewer; explanatory | Approved, source-backed; normative obligations promoted elsewhere |
| `.fdi/context/knowledge/incidents/{knowledge-id}.md` | Conditional/R | `Summary`; `Impact`; `Response`; `Contributing conditions`; `Corrective actions`; `Prevention checks`; schema `K` fields | Incident/service owners; explanatory | Blameless review approved; action states current; sensitive raw data excluded |
| `.fdi/context/knowledge/learnings/{knowledge-id}.md` | Conditional/R | `Learning`; `Evidence`; `Confidence`; `Counterevidence`; `Recommended use`; schema `K` fields | Subject owner/reviewer; explanatory | Verified and reviewed; reopen on counterevidence |
| `.fdi/context/knowledge/patterns/{knowledge-id}.md` | Conditional/R | `Problem`; `Pattern`; `Constraints`; `Examples`; `Counterexamples`; `Evidence`; schema `K` fields | Architecture/engineering owner; explanatory | Approved/demonstrated; supersede on conflicting standard |
| `.fdi/context/operations/environments.md` | Required/T | `Environment inventory`; `Owners`; `Access and approvals`; `Configuration references`; `Data constraints` | Platform/SRE/security owners | Current within 90 days; no credentials |
| `.fdi/context/operations/release.md` | Required/T | `Release topology`; `Repository responsibilities`; `Promotion gates`; `Rollback`; `Evidence`; `Authority` | Release/platform/repository owners | Matches source controls; mismatch blocks release claim |
| `.fdi/context/operations/observability.md` | Required/T | `Signals`; `Service/entity mapping`; `Environment mapping`; `Query entry points`; `Access/redaction`; `Retention`; `Evidence capture`; `Known gaps` | SRE/service/security owners | Every signal maps to IDs and environment; query tested within 90 days |
| `.fdi/context/operations/runbooks/{runbook-id}.md` | Conditional/T | `Trigger`; `Preconditions`; `Permissions`; `Procedure`; `Validation`; `Rollback`; `Escalation`; `Evidence` | Service/platform owner; operational | Registered, tested at cadence; expired procedure cannot authorize action |
| `.fdi/context/external/references.md` | Required/T | `Source catalog`; `Retrieval policy`; `Citation policy`; `Disallowed content` | Subject/governance owner | Primary URI/version/as-of/trust/expiry recorded |
| `.fdi/context/external/reviews/{source-id}.md` | Conditional/R | `Source identity`; `Question`; `Claims`; `Verification`; `Applicability`; `Limitations`; `Expiry` | Subject owner and reviewer | Primary citations, as-of, expiry, successor review |
| `.fdi/skills/catalog.md` | Required/A | `Skill registry`; `Transition mapping`; `Version and digest`; `Capability dependencies`; `Permission classes`; `Status` | Workflow/security owner; canonical Skill inventory | Every installed Skill resolves; required bindings and owners named |

## 7. Per-file contracts for feature artifacts

Rows inherit schema `F`, except evidence records.

| Exact path | Required headings | Producer/owner and source | Complete/current and mappings |
| --- | --- | --- | --- |
| `.fdi/features/{feature-id}/request.md` | `Human signal`; `Requester`; `Requested change`; `Constraints`; `Source references`; `Ambiguities` | Intake agent; authenticated human signal | Exact feature ID/source; maps request fragments to Intention criteria |
| `.fdi/features/{feature-id}/intention.md` | `Rationale`; `Stakeholders`; `Outcome`; `Use scenarios`; `Scope`; `Constraints`; `Non-goals`; `Success criteria`; `Authorization` | Intention agent; product owner | Criteria testable/approved; maps request -> criteria -> Spec anchors |
| `.fdi/features/{feature-id}/spec/index.md` | `Bundle membership`; `Intention mapping`; `Revision state`; `Approvals`; `Change-surface summary` | Spec agent; product/architecture/repository owners | Five members consistent; maps every criterion to requirements/design/tasks/V&V plan |
| `.fdi/features/{feature-id}/spec/requirements.md` | `Functional requirements`; `Quality requirements`; `Constraints`; `Acceptance mapping`; `Open questions` | Spec agent; product/domain owners | Stable requirement IDs and exact criterion backlinks |
| `.fdi/features/{feature-id}/spec/design.md` | `Current state`; `Proposed design`; `Impacted entity and relation IDs`; `Planned relations`; `Change surface`; `Interfaces`; `Data`; `Operations`; `Rollout/rollback`; `Risks` | Spec agent; architecture/repository/operations owners | Planned edges remain here; every repo path/glob bounded per 3.2 |
| `.fdi/features/{feature-id}/spec/tasks.md` | `Task registry`; `Dependencies`; `Repository ownership`; `Requirement/design mapping`; `Completion evidence` | Spec agent; repo owners | Every task owned and mapped to exact obligation/evidence destination |
| `.fdi/features/{feature-id}/spec/vv-plan.md` | `Verification matrix`; `Validation scenarios`; `Independence`; `Environments`; `Capability bindings`; `Evidence destinations`; `Decision rules` | Spec agent; independent verifier/approvers | Every criterion/obligation has method, owner, destination, threshold |
| `.fdi/features/{feature-id}/change-set/index.md` | `Candidate identity`; `Repository revisions and PRs`; `Changed paths`; `Implemented relation candidates`; `Checks performed`; `Requirement/design/task mapping`; `Deviations`; `Release state` | Implementation agents/repo owners; pinned commits/PRs | Every impacted repo has base/head and exact paths; candidate edges map planned relation IDs |
| `.fdi/features/{feature-id}/vv-report.md` | `Candidate assessed`; `Evidence inventory`; `Verification results`; `Validation results`; `Relation verification`; `Criterion verdicts`; `Overall verdict`; `Re-entry`; `Release observation` | Independent V&V agent and approvers | Every claim maps to evidence; `PASS`, `FAIL`, or `INCONCLUSIVE`; verified edges named |
| `.fdi/features/{feature-id}/evidence/{evidence-id}.md` | `Evidence identity`; `Claim`; `Method`; `Candidate/environment`; `Observation`; `Result`; `Integrity and access`; `Producer`; `Limitations` | Allocated producer; evidence authority remains at cited origin | Immutable/timestamped reference and digest; exact plan/report backlinks; unsafe payload excluded |

Downstream placeholders MUST NOT be created before their producing transition starts. Revised upstream artifacts supersede and invalidate affected downstream revisions until re-entry completes.

## 8. Per-file contracts for baseline artifacts

Rows inherit schema `B`.

| Exact path | Required headings | Producer/owner | Complete/current |
| --- | --- | --- | --- |
| `.fdi/baseline/snapshot.md` | `Snapshot scope`; `Repository pins`; `Environment observations`; `Capability summary`; `Exclusions`; `Gate record` | Discovery agent; repository/operations owners | All scoped repos pinned; evidence dates/deployed revisions known |
| `.fdi/baseline/catalog.md` | `Capability registry`; `Entity/relation mappings`; `Status/confidence`; `Bundle paths`; `Review state` | Discovery/verifier; product/domain owners | Every ID has complete bundle and current registry links |
| `.fdi/baseline/capabilities/{capability-id}/capability.md` | `Observed behavior`; `Actors`; `Scenarios`; `Inputs/outputs`; `Rules`; `Limits` | Discovery agent; domain/product owner | Describes evidence only; unknown historical intent labeled unknown |
| `.fdi/baseline/capabilities/{capability-id}/implementation-map.md` | `Entity/relation IDs`; `Repository pins`; `Source anchors`; `Interfaces`; `Data`; `Runtime`; `Tests`; `Known gaps` | Discovery agent; repository owners | Exact `repo-id:path@sha` refs; registry revision recorded |
| `.fdi/baseline/capabilities/{capability-id}/verification.md` | `Claims`; `Methods`; `Independent evidence`; `Results`; `Owner confirmations`; `Verdict` | Independent verifier | Only supported items become `VERIFIED-AS-IS` |

## 9. Skill package contract

Every `.fdi/skills/*/SKILL.md` MUST have front matter fields `name`, `description`, `version`, `source`, and compatible runtime range, followed by:

1. `# Purpose and applicability`;
2. `## Transition contract` with exact artifact inputs/outputs;
3. `## Context selection` with literal reads, bounded selectors, exclusions, precedence, and record destination;
4. `## Capability bindings` with stable identifiers, required/optional state, provider/runtime assumptions, input/output schemas, and availability check;
5. `## Permissions and approvals` with allowed, prohibited, destructive, external-audience, and sensitive-data boundaries;
6. `## Procedure`;
7. `## Failure, escalation, and idempotency`;
8. `## Completion and evidence`;
9. `## Version and provenance`.

Skills contain procedure and bindings, never credentials or capability implementations. A missing required binding, permission, version, or digest fails transition preflight. `.fdi/skills/catalog.md` is the only Skill registry; resources are trusted only when listed by their parent Skill and catalog entry.

## 10. Logical artifacts and physical bundles

| Logical concern | Canonical physical bundle | Referenced, not copied | Producer | Consumer |
| --- | --- | --- | --- | --- |
| Intention | `.fdi/features/{feature-id}/request.md` and `.fdi/features/{feature-id}/intention.md` | Authenticated human signal | Intention agent | Spec and V&V agents |
| Delivery Spec | Five files under `.fdi/features/{feature-id}/spec/` | Pinned source and reviewed Knowledge | Spec agent | Implementation and V&V agents |
| Change Set | `.fdi/features/{feature-id}/change-set/index.md` | Source-repository commits/PRs/checks | Implementation agents | V&V/release/refresh agents |
| V&V Report | `.fdi/features/{feature-id}/vv-report.md` plus evidence records | CI/runtime artifacts by URI/digest | Independent V&V agent | Approvers/release/refresh agents |
| Capability Baseline | `.fdi/baseline/snapshot.md`, `.fdi/baseline/catalog.md`, and capability bundles | Pinned source/runtime evidence | Discovery and verifier | Feature transitions |
| Passive Context | `.fdi/context/` core plus registered extensions | Source repositories and primary references | Category owners | Context selector/all agents |
| Executable Context | `.fdi/skills/catalog.md` and registered Skill packages | Bound runtime capabilities | Workflow/security owners | Transition agents |

## 11. Transition and Context-selection matrix

Each row uses schemas `F` or `B` from section 4. Selected reads use section 3.1 patterns and the source selector in 3.2. A selector match is driven only by IDs/paths named in the row's preceding artifact; Knowledge selection additionally requires an active index entry whose `applies_to` intersects those IDs. Every concrete read is written to the output's `Context consulted` or `Source scope`. Planned edges are read only from `spec/design.md#Planned-relations` and cannot satisfy a current-topology query.

| Order / producer | Literal reads | Bounded selected reads, matching, exclusions, concrete-match destination | Exact writes, schema, preceding/following mapping | Gate/evidence destination, completion, preflight/execution state |
| --- | --- | --- | --- | --- |
| 1 Human -> Intention / Intention agent | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/human-to-intention/SKILL.md`; `.fdi/features/{feature-id}/request.md` | Capability bundles whose IDs are named in request intake; domain areas whose IDs match request terms through glossary aliases; active Knowledge items whose `applies_to` intersects named feature/entity IDs; external reviews named by an explicit dependency. Exclude retired/currently inapplicable records and source internals unless an ambiguity names a specific entity. Record exact matches in `.fdi/features/{feature-id}/intention.md#Context-consulted` | Write `.fdi/features/{feature-id}/intention.md` using `F` and allocated `.fdi/features/{feature-id}/evidence/{evidence-id}.md` records. Map each request fragment to success criterion IDs; following mapping targets `.fdi/features/{feature-id}/spec/index.md#Intention-mapping` | Gate: `.fdi/features/{feature-id}/intention.md#Gate-record`; planned authorization/review evidence is allocated there. Complete when scope/non-goals/scenarios/criteria/authorization resolve. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until reviewed |
| 2 Intention -> Delivery Spec / Spec agent | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/intention-to-spec/SKILL.md`; `.fdi/features/{feature-id}/request.md`; `.fdi/features/{feature-id}/intention.md` | `.fdi/context/codebase/repositories/{repo-id}.md` for Repository IDs reached from impacted entity IDs by current `implemented-by` edges; source reads at pinned base SHAs matching exact paths/globs proposed under `.fdi/features/{feature-id}/spec/design.md#Change-surface`; domain areas, views, Knowledge items, reviews, and runbooks whose registry scope intersects impacted IDs/requirements. Exclude retired/planned-as-current edges, unrelated trees, and mutable reads. Record matches in each Spec member's `Context consulted` and `.fdi/features/{feature-id}/spec/index.md#Change-surface-summary` | Write `.fdi/features/{feature-id}/spec/index.md`, `requirements.md`, `design.md`, `tasks.md`, and `vv-plan.md` using `F`, plus allocated evidence records. Map criterion IDs to requirement/design/task/V&V IDs; keep planned relation IDs only in `design.md`; following mapping targets Change Set candidate relation IDs and paths | Gate: `.fdi/features/{feature-id}/spec/index.md#Gate-record`; planned evidence: `.fdi/features/{feature-id}/spec/vv-plan.md#Evidence-destinations`. Complete when every criterion is mapped, all repository/interface/data/operations surfaces and owner approvals are named, and selectors are bounded. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until produced/reviewed |
| 3 Delivery Spec -> Change Set / implementation agents | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/spec-to-implementation/SKILL.md`; `.fdi/features/{feature-id}/intention.md`; `.fdi/features/{feature-id}/spec/index.md`; `.fdi/features/{feature-id}/spec/requirements.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/spec/tasks.md`; `.fdi/features/{feature-id}/spec/vv-plan.md` | `.fdi/context/codebase/repositories/{repo-id}.md` for IDs in `.fdi/features/{feature-id}/spec/index.md#Change-surface-summary`; recorded local instructions; exact planned source/test/config/schema/interface paths at pinned base SHAs; scoped domain/Codebase/Knowledge/runbook records whose IDs occur in tasks/design; capability identifiers listed in `.fdi/skills/spec-to-implementation/SKILL.md#Capability-bindings`. Exclude any repo/path outside the Spec unless `.fdi/features/{feature-id}/change-set/index.md#Deviations` records a scope-change decision. Record every match/use in that index's `Context consulted` | Write commits/PRs in each named source repository and `.fdi/features/{feature-id}/change-set/index.md` using `F`; write evidence only to `.fdi/features/{feature-id}/evidence/{evidence-id}.md` IDs allocated by the plan. Map every requirement/design/task ID to `repo-id:path@head-sha` or justified no-code outcome; map planned relation IDs to candidate relation IDs. No Codebase registry write occurs here | Gate: `.fdi/features/{feature-id}/change-set/index.md#Gate-record`; evidence IDs come from `.fdi/features/{feature-id}/spec/vv-plan.md#Evidence-destinations`. Complete when every impacted repo has base/head/PR, changed paths/checks, candidate relations, and reconciled deviations. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until candidates/evidence exist |
| 4 Change Set -> V&V Report / independent V&V agent | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/implementation-to-correctness/SKILL.md`; `.fdi/features/{feature-id}/intention.md`; `.fdi/features/{feature-id}/spec/index.md`; `.fdi/features/{feature-id}/spec/requirements.md`; `.fdi/features/{feature-id}/spec/design.md`; `.fdi/features/{feature-id}/spec/tasks.md`; `.fdi/features/{feature-id}/spec/vv-plan.md`; `.fdi/features/{feature-id}/change-set/index.md` | `.fdi/features/{feature-id}/evidence/{evidence-id}.md` for IDs named by the V&V plan/Change Set; exact changed paths plus impacted tests/config/schemas/interfaces at pinned head SHAs; capability bundles named by criterion mapping; scoped Knowledge/runbooks/reviews by intersecting IDs; capability identifiers listed in `.fdi/skills/implementation-to-correctness/SKILL.md#Capability-bindings`. Exclude unreproduced assertions and evidence for another candidate/environment. Record matches in `.fdi/features/{feature-id}/vv-report.md#Context-consulted` and `#Evidence-inventory` | Write new evidence records and `.fdi/features/{feature-id}/vv-report.md` using `F`. Map every requirement/design/task/candidate relation/criterion to evidence and verdict; following mapping names release/refresh eligibility or earliest re-entry artifact | Gate: `.fdi/features/{feature-id}/vv-report.md#Gate-record`; evidence inventory in the same file. Complete with separate verification/validation, relation verdicts, overall `PASS`/`FAIL`/`INCONCLUSIVE`, owners, and re-entry. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until independent assessment |
| B1 Pinned source -> Baseline Discovery / discovery agent | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/observability.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/external/references.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-discovery/SKILL.md` | `.fdi/context/codebase/repositories/{repo-id}.md` for in-scope active Repository IDs; recorded local instructions; source/tests/config/schemas/docs at SHAs bounded in `.fdi/baseline/snapshot.md#Source-scope`; observations through named observability query entry points; cited ADR/issue/PR/commit identifiers and registered extensions. Exclude fabricated intent, uncited history/chat, caches, and secrets. Record matches in Baseline `Source scope` and provenance | Write `.fdi/baseline/snapshot.md`, `.fdi/baseline/catalog.md`, and each discovered `.fdi/baseline/capabilities/{capability-id}/capability.md` and `implementation-map.md` using `B`. Map capability IDs to exact entity/relation IDs and source anchors; following mapping targets verification claims | Gate: `.fdi/baseline/snapshot.md#Gate-record`; planned evidence paths named there. Complete when all scoped repos are pinned and each capability has concrete refs/gaps. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until discovery review |
| B2 Baseline -> Independent As-Is Verification / baseline verifier | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/domain/glossary.md`; `.fdi/context/domain/rules.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/observability.md`; `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md`; `.fdi/skills/catalog.md`; `.fdi/skills/context-selection/SKILL.md`; `.fdi/skills/baseline-verification/SKILL.md` | `.fdi/baseline/capabilities/{capability-id}/capability.md` and `implementation-map.md` for selected catalog IDs; exact source/test/config/schema/runtime refs cited by each bundle at the same pins; capability identifiers listed in `.fdi/skills/baseline-verification/SKILL.md#Capability-bindings`. Exclude producer claims not independently inspected/reproduced. Record matches/results in `.fdi/baseline/capabilities/{capability-id}/verification.md#Evidence-and-provenance` | Write each selected `.fdi/baseline/capabilities/{capability-id}/verification.md`, update `.fdi/baseline/catalog.md`, and revise `.fdi/baseline/snapshot.md#Gate-record` using `B`. Map every observed-behavior claim/source anchor to method/result/owner confirmation; following state is `VERIFIED-AS-IS` or gap | Gate: `.fdi/baseline/snapshot.md#Gate-record`; evidence in each verification file. Complete when repository owners confirm maps, product/domain owners confirm descriptions, and independent verdicts exist. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until evidence exists |
| B3 Released Change Set -> Codebase/Baseline refresh and optional Knowledge promotion / refresh agent plus independent verifier | `.fdi/README.md`; `.fdi/context/contract.md`; `.fdi/context/index.md`; `.fdi/context/steering/product.md`; `.fdi/context/steering/tech.md`; `.fdi/context/steering/structure.md`; `.fdi/context/steering/architecture.md`; `.fdi/context/steering/agent-policy.md`; `.fdi/context/steering/delivery.md`; `.fdi/context/steering/governance.md`; `.fdi/context/codebase/catalog.md`; `.fdi/context/codebase/relations.md`; `.fdi/context/codebase/system-context.md`; `.fdi/context/codebase/integrations.md`; `.fdi/context/codebase/data.md`; `.fdi/context/knowledge/index.md`; `.fdi/context/operations/environments.md`; `.fdi/context/operations/release.md`; `.fdi/context/operations/observability.md`; `.fdi/skills/catalog.md`; `.fdi/skills/baseline-discovery/SKILL.md`; `.fdi/skills/baseline-verification/SKILL.md`; `.fdi/features/{feature-id}/change-set/index.md`; `.fdi/features/{feature-id}/vv-report.md`; `.fdi/baseline/snapshot.md`; `.fdi/baseline/catalog.md` | Released `repo-id:path@sha` entries from Change Set, release evidence named in V&V, `.fdi/baseline/capabilities/{capability-id}/` bundles whose IDs are mapped by the feature, and current Codebase rows whose IDs equal verified candidate IDs. Exclude unreleased heads, non-`PASS` claims, unrelated IDs, and Knowledge candidates without reviewer approval. Record matches in refreshed files' provenance and snapshot source scope | Conditionally update `.fdi/context/codebase/catalog.md` only for added/changed/retired verified released entities; update `.fdi/context/codebase/relations.md` only for verified released candidate edges or retirements; regenerate affected `.fdi/context/codebase/system-context.md`, `integrations.md`, `data.md`, repository files, and registered views at the new registry revision; revise affected Baseline files. Optionally create/update one schema `K` record and `.fdi/context/knowledge/index.md` entry after review. Map Delivery Spec planned relation -> Change Set candidate -> V&V verified relation -> released current Codebase row -> optional Knowledge backlink. No new logical artifact/stage is created | Gate: `.fdi/baseline/snapshot.md#Gate-record`; release/verification evidence remains at `.fdi/features/{feature-id}/vv-report.md#Release-observation` and its cited evidence records; Codebase rows MUST name owner and exact evidence. Complete when release is observed, registry writes are owner-approved, derived views/Baseline agree, and optional promotion has reviewer/state/backlinks. Preflight `CONTRACT_READY`; execution `NOT_CLAIMED` until a real release/refresh run |

## 12. Topology refresh and Knowledge promotion lifecycle

```text
Delivery Spec planned relation
  -> Change Set implemented candidate
  -> V&V verified relation
  -> released Codebase catalog/relations refresh
  -> optional reviewed Knowledge promotion
```

Codebase is refreshed only after a `PASS` V&V Report and independently observed release. Entity/relation owners approve their rows and every write cites the released SHA plus V&V evidence anchor. Derived views are regenerated from the same registry revision. A durable conclusion may then be promoted through the Knowledge review process; its obligations have no normative force until copied as obligations—not as the feature artifact itself—into Steering or an approved future/current feature artifact.

## 13. Authority and conflict rules

### 13.1 Desired behavior

1. Latest approved Intention owns stakeholder outcome, scope, non-goals, scenarios, and success criteria.
2. Latest approved Delivery Spec owns technical obligations but cannot change Intention.
3. Steering owns persistent product, architecture, security, delivery, and governance constraints; Domain rules own business invariants.
4. A conflict blocks until the relevant owners approve a revision or governed exception.
5. Knowledge explains rationale and supports retrieval. It cannot establish desired behavior until obligations are promoted into Steering or an approved feature artifact.

### 13.2 Current behavior

1. Pinned source/config/schema/tests plus their results are primary for a named revision.
2. Timestamped telemetry is primary for a named environment only when the deployed revision is identified.
3. `catalog.md` and `relations.md` are canonical curated topology at their released evidence revision; newer pinned evidence triggers refresh rather than silent overwrite.
4. Verified Baseline summarizes evidence at its snapshot and is subordinate to newer pinned evidence.
5. Derived Codebase views, Knowledge, history, and third-party references explain or navigate; they do not outrank pinned observed-state evidence.

Conflicts are reconciled by revision, environment, scope, and authority dimension. A genuine mismatch is recorded in the relevant gap section, assigned to its owner, and blocks dependent claims.

## 14. Multi-repository ownership boundaries

| Concern | Coordination-repository authority | Source-repository authority | Required handshake |
| --- | --- | --- | --- |
| Product intent and cross-repo scope | Canonical Intention and aggregate Spec | Feasibility/current-state evidence | Product approval plus impacted repository-owner confirmation |
| Entity/relation topology | Canonical released catalog/relations rows | Implementation and contract evidence | Entity/edge owner approves row citing released source/V&V |
| Source/config/schema/tests | Pinned references and mappings only | Canonical content, local controls, CI | Spec names bounded paths; local review remains required |
| Change Set | Aggregate index across commits/PRs | Candidate commits/PRs | Every impacted repo has pinned base/head/status |
| Evidence | Safe records and aggregate interpretation | Raw CI/build/test artifacts where owned | URI/digest/revision/conditions preserved; secrets not copied |
| Release | Planned gates and observed release reference | Executes/authorizes release and rollback | Refresh waits for observed release |
| Context upkeep | Product/category owners maintain shared Context | Repo owners maintain local instructions and truth | Drift triggers owner-confirmed refresh |

## 15. Failure and staleness handling

- Missing core/schema/path: preflight fails `NOT_CONTRACT_READY`.
- Zero/excess selector matches: record a Context gap and stop.
- Stale curated file: verify against its authority and refresh with owner approval, or block.
- Planned edge selected as current: fail preflight and repair the selector/output.
- Missing Skill/capability/version/permission: fail before execution and name the missing binding.
- Unsafe evidence: retain only authorized URI/digest/redacted observation and classification.
- Upstream artifact revision: supersede affected downstream revisions and re-enter the earliest invalid transition.

## 16. Preflight review of this design

### 16.1 Mandatory contract preflight

| Check | Result | Exact evidence anchor |
| --- | --- | --- |
| Semantic baseline remains storage/schema neutral; profile scope is explicit | PASS | Section 1, paragraphs 1-3 |
| Tree and bounded patterns contain every mandatory/conditional path | PASS | Sections 3, 3.1, and 3.2 |
| Canonical entity and relation contracts are singular and complete | PASS | Sections 4.4 and 4.5 |
| Planned relations cannot be selected as current Context | PASS | Sections 2, 4.5, 11 opening rule, and 15 |
| Knowledge authority, fields, backlinks, and promotion are non-contradictory | PASS | Sections 4.6, 6 Knowledge rows, 12, and 13.1 |
| Feature artifacts remain canonical and are not copied to Knowledge | PASS | Sections 3.1 Knowledge exclusions, 4.6, 7, and 10 |
| Every persistent Markdown file has headings, owner, load, freshness, and supersession | PASS | Schemas in section 4 and table in section 6 |
| Skill catalog/packages define bindings, permissions, selection, failure, and evidence | PASS | Section 6 `.fdi/skills/catalog.md` row and section 9 |
| Logical bundles and physical paths agree | PASS | Sections 3, 7, 8, and 10 |
| Rows 1-4 and B1-B3 name producers, literal/selected reads, exact writes, mappings, gates, completion, evidence, and review state | PASS | Section 11, all seven rows |
| Released Codebase refresh and optional governed Knowledge promotion add no fifth stage | PASS | Section 11 B3 and section 12 |
| Desired/current authority and multi-repository ownership agree | PASS | Sections 13 and 14 |
| No disallowed category, repo registry, open-ended selector, bulk copy, secret, raw chat, or invented historical intent remains | PASS | Sections 1, 3.1, 3.2, 8, and 15 |

### 16.2 Gate result

- **Contract-ready:** `PASS`. Every mandatory preflight row above passed against its cited anchors; tree, schemas, bundle mapping, transition matrix, authority rules, ownership boundaries, and traceability lifecycle agree.
- **Execution-verified:** `NOT_CLAIMED`. No physical `.fdi/` profile, Skill package, baseline run, feature transition, release refresh, or evidence-producing execution was implemented or exercised by this design task.
- **Approval boundary:** Herman's approval is required before a separate implementation task creates the physical profile or revises the installed workflow harness.
