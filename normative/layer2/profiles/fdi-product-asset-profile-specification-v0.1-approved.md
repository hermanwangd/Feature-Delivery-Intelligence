# FDI Product Asset Profile Specification v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Depends on:** FDI Layer 2 — Product Intelligence Asset Framework v0.1 (`Contract-ready: APPROVED`)  
> **Scope:** Product Asset Profiles; v0.1 fully specifies Codebase and Delivery History only  
> **Primary actor:** Frontier Team; Agents may assist under `PA-*` maintenance Skills  
> **Design only:** No repository crawler, relation extractor, historical correlator, validator, migration, or publication execution is authorized by this specification

---

# 0. Purpose

Layer 2 defines the common Product Asset contract. This specification defines the next level down: **what a Frontier Team must maintain for a specific Product Asset family so Layer 1 Skills can use it reliably.**

A Product Asset Profile is not a new Layer 1 transition and is not an execution Context. It is the durable maintenance contract for one reusable Product Intelligence family.

```text
Layer 2 Framework
    |
    | defines universal Product Asset semantics
    v
Product Asset Profile
    |
    | defines what the Frontier Team maintains
    v
Product Asset revisions
    |
    | selected/resolved for one feature execution
    v
ResolvedContextRef
    |
    v
Layer 1 FT-* Skill
```

The central distinction remains:

> **The Profile defines durable product intelligence. Layer 1 decides which subset becomes execution Context and which current `EvidenceRef`s are required to establish a feature-specific claim.**

---

# 1. Profile Registry

v0.1 uses the following semantic profile IDs.

| Profile ID | Product Asset family | v0.1 status | Priority |
| --- | --- | --- | --- |
| `PA-01` | Product | Interface reserved | Later |
| `PA-02` | Architecture | Interface reserved | Later |
| `PA-03` | Codebase | **Fully specified** | P0 |
| `PA-04` | Domain | Interface reserved | Later |
| `PA-05` | Delivery History | **Fully specified** | P0 |
| `PA-06` | Operations | Interface reserved | Later |
| `PA-07` | Knowledge | Interface reserved | Later |
| `PA-08` | Reference | Interface reserved | Later |

The numeric IDs are stable semantic identifiers only. They do not require numbered folders or a fixed physical layout.

---

# 2. Common Product Asset Profile Contract

Every Product Asset Profile MUST define the following.

| Contract field | Required meaning |
| --- | --- |
| `profile_id` | Stable Product Asset Profile identity |
| Profile conformance | Exact profile-spec revision under which the Asset semantics are interpreted |
| Asset family/type | Layer 2 family plus specific reusable Asset types |
| Purpose | Why this Product Intelligence should be maintained once and reused |
| Non-goals | What the Asset explicitly does not claim |
| Product scope | Product/system/repository/environment applicability |
| Durable semantic records | Minimum reusable information maintained by the Frontier Team |
| Upstream source classes | Systems of record or evidence from which the Asset is curated, derived, or referenced |
| Source authority mapping | Which source is authoritative for which field/claim dimension |
| Maintenance mode | `CURATED`, `DERIVED`, or `REFERENCED` |
| Accountable owner | Frontier Team/product authority responsible for usefulness and publication |
| Maintenance Skill | Optional `PA-*` Skill contract used to assist creation/refresh |
| Publication policy | `HUMAN_APPROVAL`, `RULE_BASED_AUTO`, or `SOURCE_REFERENCE` |
| Publication quality gate | Conditions required before `PUBLISHED + ACTIVE` |
| Freshness/invalidation | What source or policy changes require recheck or stale marking |
| Supersession | How a new semantic revision replaces the prior active revision |
| Selection metadata | Metadata needed for bounded Layer 1 retrieval |
| Layer 1 consumers | Which FT Skills are expected to select the Asset and for what purpose |
| Evidence boundary | What still requires feature-specific Layer 1 `EvidenceRef` |
| Success measures | Whether maintaining the Asset improves Layer 1 enough to justify its cost |

## 2.1 Profile does not imply one file

A Profile defines semantic Product Assets, not a mandatory Markdown bundle.

An Asset may be:

- materialized Markdown;
- a derived structured index;
- another governed representation;
- a descriptor that points to an authoritative existing source.

Every Asset still obeys the approved Layer 2 `ProductAssetDescriptor` contract.

## 2.2 Profile does not create feature truth

A durable Product Asset can provide:

- `DURABLE_CONSTRAINT`;
- `CURRENT_BEHAVIOR_SUPPORT`;
- `RATIONALE_SUPPORT`.

It cannot own:

- Layer 1 Desired Outcome;
- Layer 1 Technical Obligation;
- Layer 1 Procedure authority;
- a feature-specific `CONFIRMED` Change Surface finding without current applicable Layer 1 Evidence.

## 2.3 Profile conformance metadata

Every Asset governed by this specification MUST expose, either in its descriptor extension or Product Intelligence registry, metadata equivalent to:

```yaml
profile_conformance:
  profile_id: "PA-03|PA-05"
  profile_spec_revision: "0.1"
```

This metadata does not replace `asset_revision`. `asset_revision` versions the Product Asset; `profile_spec_revision` identifies the contract used to interpret that Asset. A future Profile revision does not automatically invalidate previously published Assets unless the newer Profile explicitly declares a compatibility or migration requirement.

## 2.4 Completeness is always scope-qualified

Labels such as `COMPLETE_FOR_DECLARED_SCOPE` are valid only when the Asset exposes the declared coverage boundary that makes the statement meaningful. A maintainer MUST NOT publish an unqualified claim of completeness.

Examples of a declared coverage boundary include:

- one named product/system;
- one repository organization or registry partition;
- one historical delivery period/source set;
- one explicitly bounded relation class.

Unknown or partially observed coverage MUST remain `PARTIAL` or `UNKNOWN`.

---

# 3. PA-03 — Codebase Product Asset Profile

## 3.1 Purpose

The Codebase Profile makes the product's current code estate **navigable enough for bounded feature investigation and implementation** without requiring the Frontier Team to maintain a complete enterprise dependency graph.

It answers reusable questions such as:

- Which repositories belong to this product/system?
- What is each repository responsible for at a useful navigation level?
- Who owns it?
- What stable contracts, manifests, or entry points help an Agent investigate it?
- Which high-value inter-repository relations are worth maintaining because they are repeatedly useful?

It does **not** answer the feature-specific question:

> Which repositories must change for this feature?

That remains FT-T2 Change Surface responsibility.

## 3.2 Asset types

PA-03 defines two v0.1 Asset types:

```text
CB-01 Repository Inventory
CB-02 Known High-Value Relation
```

`CB-01` is P0 and expected for initial FDI operation.

`CB-02` is optional and ROI-driven. It is materialized only for relation classes that repeatedly improve Layer 1 investigation.

---

## 3.3 CB-01 — Repository Inventory Asset

### Purpose

Provide a compact, current, reusable repository navigation surface.

### Minimum semantic record

Each repository record MUST expose semantics equivalent to:

```yaml
repository_record:
  repo_id: "<stable-product-intelligence-id>"
  canonical_ref: "<canonical-repository-reference>"
  repository_state: "ACTIVE|ARCHIVED|REPLACED|UNKNOWN"
  alias_refs: []
  lineage_refs: []

  product_system_refs: []
  owner_refs: []

  role_summary: "<bounded reusable description>"
  languages_platforms: []

  known_entrypoint_refs: []
  known_contract_refs: []
  manifest_refs: []
  deployment_refs: []

  source_state:
    revision_or_as_of: "<source-state>"

  completeness:
    declared_scope_ref: "<coverage-boundary-ref>"
    inventory: "COMPLETE_FOR_DECLARED_SCOPE|PARTIAL|UNKNOWN"
    semantic_description: "CURATED|DERIVED|MINIMAL|UNKNOWN"

  source_refs: []
  limitations: []
  selection_metadata:
    product_terms: []
    system_terms: []
    capability_terms: []
    technology_terms: []
```

Not every field needs a value. Unknown information MUST remain explicit rather than inferred merely to fill the record.

The **semantic maintenance unit is the repository record**, even when implementations materialize multiple records in one file/index or shard them across files. `repo_id` is intended to remain stable across a repository rename/move when the underlying repository identity remains the same. `alias_refs` and evidence-backed `lineage_refs` preserve continuity. A split, merge, replacement, or migration MUST NOT be collapsed into a rename unless supported by source evidence.

`source_state.revision_or_as_of` is a compact summary only. Every materially authoritative `source_ref` MUST still carry its own pinned revision/as-of semantics under the Layer 2 source contract.

### Upstream source classes

Typical sources include:

- Git/repository provider inventory;
- organization/repository registry;
- repository canonical URL/identity;
- `CODEOWNERS` or approved ownership system;
- service catalog;
- build/package manifests;
- repository-local descriptors;
- deployment descriptors;
- approved product/system mappings.

### Source authority is field-specific

PA-03 MUST NOT define one global source precedence for the whole repository record.

Examples:

- repository existence/identity comes from the canonical repository provider/registry;
- repository ownership comes from the approved ownership source for that organization/repository;
- language/platform observations may be derived from manifests/source;
- product/system membership may come from an approved product map or service catalog;
- `role_summary` may be curated or derived but MUST preserve its provenance/trust profile.

If materially authoritative sources conflict, the Asset revision MUST expose the conflict or remain `DRAFT`; the maintainer/maintenance contract MUST NOT silently choose the convenient source.

### Maintenance mode

Primary mode:

```text
DERIVED
```

Some fields may be `CURATED` or `REFERENCED`, but the published Asset descriptor MUST preserve the resulting provenance/trust semantics.

### Recommended PA Skill

```text
PA-Codebase-Inventory
```

Conceptually:

```text
RepositoryInventoryAsset
=
f(
  repository/provider metadata,
  ownership sources,
  service/product mappings,
  manifests/descriptors,
  PA-Codebase-Inventory@revision
  ; supporting ProductAssetRefs
)
```

The Skill may normalize/extract/correlate information. It MUST NOT invent product ownership, repository responsibility, or architecture policy.

### Publication policy

A mixed publication policy is allowed by field/source class, but the v0.1 default is:

```text
RULE_BASED_AUTO
```

only for deterministic inventory fields when all declared source and integrity checks pass.

Semantic descriptions, ambiguous ownership reconciliation, or product/system classification requiring judgment MUST fall back to:

```text
HUMAN_APPROVAL
```

An Agent-generated semantic description is `DRAFT` unless the approved maintenance policy explicitly permits its publication.

### Publication quality gate

Before a CB-01 revision becomes `PUBLISHED + ACTIVE`, it MUST establish:

1. stable `repo_id` and canonical repository reference;
2. declared product/system scope or explicit `UNKNOWN`;
3. ownership source or explicit ownership gap;
4. source/as-of state;
5. provenance/trust profile consistent with each materially influential source;
6. no silently unresolved repository identity collision;
7. limitations/completeness state;
8. bounded selection metadata;
9. declared coverage boundary for any completeness claim;
10. repository lifecycle/identity continuity is explicit when rename/archive/replacement is known;
11. invalidation triggers;
12. no claim that the inventory proves feature-specific impact.

A missing optional semantic field does not block publication. A broken repository identity/provenance contract does.

### Freshness / invalidation

Typical triggers:

```text
repository created / archived / deleted
canonical repository moved or renamed
approved ownership changed
product/system mapping changed
relevant service catalog record changed
material manifest/descriptor change when indexed semantics depend on it
manual correction
```

The preferred freshness mode is `SOURCE_CHANGE` for deterministically tracked fields. Curated semantic fields may use `MANUAL` or `UNTIL_SUPERSEDED` as appropriate.

### Layer 1 consumption

| Layer 1 Skill | Use |
| --- | --- |
| FT-T1 | High-level product/system/repository orientation and seed normalization |
| **FT-T2** | **Primary repository candidate navigation and bounded investigation** |
| **FT-T3** | Resolve canonical repo identity, ownership, repository-local references |
| FT-T4 | Candidate/source coverage and repository identity checks when applicable |

### Layer 1 evidence boundary

CB-01 can tell FT-T2:

> `repo-X` exists, belongs to product/system Y, and is worth investigating.

CB-01 cannot by itself establish:

> `repo-X` is `CONFIRMED` as impacted by this feature.

That requires current feature-specific Layer 1 `EvidenceRef` under the approved Change Surface contract.

---

## 3.4 CB-02 — Known High-Value Relation Asset

### Purpose

Persist only inter-repository/system relations that are sufficiently reusable and expensive to rediscover repeatedly.

Examples:

```text
repo-A --API_CONSUMER--> repo-B
repo-C --EVENT_CONSUMER--> repo-D
repo-E --SCHEMA_OWNER--> contract-X
repo-F --PACKAGE_DEPENDENCY--> repo-G
```

PA-03 does **not** require a complete graph.

Each `relation_type` MUST have stable **directed semantics**. `from_ref -> to_ref` cannot be interpreted differently by different consumers. `OTHER` requires an explicit relation description. Relation verification establishes that the declared relation is supported at the stated source state; it does **not** establish that the relation is relevant to a particular feature.

### Relation record

A materialized relation MUST expose semantics equivalent to:

```yaml
relation_record:
  relation_id: "<stable-id>"
  relation_type: "API|EVENT|SCHEMA|PACKAGE|CONFIG|DEPLOYMENT|DATA|OTHER"
  relation_semantics_ref: "<stable-directed-relation-definition>"
  relation_description: "<required-when-OTHER-or-ambiguous>"

  from_ref: "<repo/system/component>"
  to_ref: "<repo/system/component/contract>"

  source_refs: []
  revision_or_as_of: "<source-state>"

  provenance: "DIRECT|DERIVED|ASSERTED"
  verification: "NOT_VERIFIED|VERIFIED"

  completeness: "PARTIAL|BOUNDED|UNKNOWN"
  scope: {}
  limitations: []

  selection_metadata:
    relation_terms: []
    product_system_terms: []
```

### Upstream source classes

High-value relation extraction may use:

- OpenAPI/protobuf/IDL ownership and references;
- event definitions/subscriptions;
- schema/data ownership;
- build/package dependencies;
- deployment/configuration metadata;
- service catalog relations;
- bounded source analysis;
- other governed current-state evidence.

### Publication policy

A relation may use `RULE_BASED_AUTO` only when its derivation rule is deterministic, its source refs are complete enough for the claimed relation, and no authority elevation occurs.

Ambiguous semantic relations remain `DRAFT` or require `HUMAN_APPROVAL`.

### Maintenance principle

> **Do not materialize a relation merely because it can be extracted. Materialize it when repeated Layer 1 use justifies maintenance cost.**

Repeated FT-T2 investigation misses or repeated rediscovery of the same relation type are valid signals to create or enhance CB-02 assets.

### Feature-specific boundary

CB-02 means:

> This relation is useful current navigation intelligence as of the declared source state.

It does not mean:

> This relation is materially relevant to the active feature.

FT-T2 still establishes feature relevance with current applicable Evidence.

---

## 3.5 PA-03 Selection contract

The Codebase Profile MUST expose selection metadata sufficient for bounded queries such as:

```text
product/system = X
repo seed = Y
capability terms = {...}
technology/contract terms = {...}
relation types = {...}
```

A valid selection MUST NOT mean:

```text
load every repository
load every relation
crawl all organization source
```

The normal pattern is:

```text
ContextRequirement
    |
    v
CB-01 bounded repository candidates
    |
    + optional CB-02 high-value neighbor hints
    |
    v
ProductAssetRef(s)
    |
    v
ResolvedContextRef(s)
    |
    v
FT-T2 targeted current investigation
```

---

## 3.6 PA-03 Success measures

Recommended measures:

| Metric | Meaning |
| --- | --- |
| Repository inventory coverage | Known relevant product repos represented in CB-01 |
| Identity/ownership defect rate | Incorrect or unresolved canonical repo/owner mappings |
| Stale-use rate | Layer 1 executions materially affected by stale CB-01/CB-02 data |
| T2 discovery uplift | Improvement in critical repo candidate recall versus no Codebase Asset |
| Selection efficiency | Reduction in irrelevant repositories loaded/investigated |
| Relation ROI | Reuse frequency and investigation time avoided for CB-02 relations |
| Maintenance cost | Frontier Team effort required to keep high-value records useful |

No target threshold is prescribed by this design; pilot evaluation establishes product-specific thresholds.

---

# 4. PA-05 — Delivery History Product Asset Profile

## 4.1 Purpose

The Delivery History Profile turns prior feature-delivery experience into durable, reusable **historical search and change-pattern intelligence**.

It connects historical product-change semantics with observed delivery evidence such as repositories, paths, interfaces, schemas, configuration, tests, and reviews.

Its primary value is to help FT-T2 ask:

> Have similar product changes historically touched repositories or change surfaces that are not obvious from the current feature description?

It does **not** answer:

> What must change now?

Current applicability remains a Layer 1 T2 investigation responsibility.

## 4.2 Asset types

PA-05 defines two v0.1 Asset types:

```text
DH-01 Historical Delivery Record
DH-02 Delivery History Index
```

`DH-01` is the source-backed durable unit.

`DH-02` is a navigation projection over published DH-01 records and MUST NOT become independent historical authority.

---

## 4.3 DH-01 — Historical Delivery Record

### Historical delivery unit

A DH-01 record represents one bounded historical product change/delivery unit identified by a stable historical feature/work-item identity plus the delivery evidence correlated to that unit.

One record MAY include:

- one Feature/Epic and multiple Backlog/Issue items;
- multiple PRs across multiple repositories;
- multiple commits;
- reviews and CI results;
- release/deployment observations where available.

It MUST declare when the reconstructed delivery set is incomplete or uncertain.

`delivery_unit_id` is the stable Product Intelligence identity. A Feature/Epic is common but not mandatory; a delivery unit may be anchored by another stable work item when the historical system did not use a Feature object. The original source identity remains in `primary_work_item_ref`.

### Primary upstream source classes

```text
Historical Feature / Epic
Backlog / Issues
PRs
Commits
Review history
CI / test results
Release/deployment evidence when available
```

These source objects remain their own systems of record. DH-01 is a derived reusable Product Asset with backlinks.

### Minimum semantic record

A DH-01 record MUST expose semantics equivalent to:

```yaml
historical_delivery_record:
  delivery_unit_id: "<stable-product-intelligence-id>"
  primary_work_item_ref: "<historical-feature-epic-backlog-or-other-source-ref>"
  delivered_as_of:
    value: "<historical-time-or-release>"
    basis: "MERGE|RELEASE|WORK_ITEM_DONE|OTHER|UNKNOWN"

  delivery_outcome:
    state: "EFFECTIVE|PARTIALLY_EFFECTIVE|REVERTED|SUPERSEDED|UNKNOWN"
    successor_or_replacement_refs: []

  feature_semantics:
    product_system_refs: []
    capability_terms: []
    requirement_terms: []
    source_refs: []
    semantic_derivation: "DIRECT|DERIVED|MIXED"

  linked_work_items:
    backlog_refs: []
    issue_refs: []

  observed_delivery:
    facts: []
    summary:
      repositories: []
      change_types: []
      interface_impacts: []
      schema_data_impacts: []
      configuration_impacts: []
      operations_impacts: []
      test_validation_refs: []

  delivery_evidence:
    pr_refs: []
    commit_refs: []
    review_refs: []
    ci_refs: []
    release_refs: []

  correlation:
    links: []
    declared_scope_ref: "<historical-source-coverage-boundary>"
    completeness: "COMPLETE_FOR_DECLARED_SCOPE|PARTIAL|UNKNOWN"
    unresolved_refs: []

  limitations: []

  selection_metadata:
    product_terms: []
    capability_terms: []
    requirement_terms: []
    repo_terms: []
    change_type_terms: []
    delivery_outcome_terms: []
    correlation_quality_terms: []
```

The exact physical schema is not prescribed. The semantics and provenance are.

Every materially reusable `observed_delivery.fact` MUST carry fact-level provenance equivalent to:

```yaml
observed_delivery_fact:
  fact_id: "<stable-within-delivery-unit>"
  kind: "REPOSITORY|PATH|API|EVENT|SCHEMA_DATA|CONFIG|OPERATIONS|TEST_VALIDATION|OTHER"
  subject_ref: "<historical-repo-path-contract-or-other-ref>"
  detail: "<bounded-semantic-description>"
  evidence_refs: []
  delivery_relevance: "FEATURE_DELIVERY|CO_DELIVERED|INCIDENTAL|UNKNOWN"
  limitations: []
```

The `summary` block is a retrieval convenience only and MUST be reproducible from or backlinked to the underlying facts. A summary entry without fact-level provenance cannot establish a reusable historical claim.

---

## 4.4 Correlation contract

The hardest part of DH-01 is not extracting a PR diff; it is establishing that the PR/commit/review belongs to the historical product change being represented.

PA-05 therefore requires every materially linked delivery source to have a correlation basis.

Recommended correlation methods include:

```text
EXPLICIT_FEATURE_LINK
EXPLICIT_BACKLOG_LINK
EXPLICIT_PR_WORKITEM_LINK
EXPLICIT_COMMIT_WORKITEM_LINK
BRANCH_OR_PR_METADATA_LINK
RELEASE_LINK
DERIVED_SEMANTIC_LINK
DERIVED_TEMPORAL_LINK
MANUAL_LINK
```

The maintenance process MUST preserve which method established each material linkage. A single record-level list of methods is insufficient. Each material linked source MUST expose correlation semantics equivalent to:

```yaml
correlation_link:
  source_ref: "<PR-commit-review-CI-release-or-work-item-ref>"
  method: "<correlation-method>"
  strength: "STRONG|AMBIGUOUS"
  review: "UNREVIEWED|REVIEWED"
  notes: []
```

Where the reusable historical record classifies whether an observed repository/path/change was actually part of feature delivery, that classification MUST also be explicit:

```text
FEATURE_DELIVERY
CO_DELIVERED
INCIDENTAL
UNKNOWN
```

`UNKNOWN` is the safe default when the evidence establishes that a source was linked/touched but does not establish semantic delivery relevance.

### Strong versus ambiguous linkage

Explicit source-system links may support rule-based publication when source integrity checks pass.

Derived semantic/temporal linkage MAY generate a candidate correlation, but it MUST NOT silently be treated as equivalent to an explicit link.

When ambiguous linkage materially changes the historical repositories/change surface recorded by the Asset:

```text
Asset revision remains DRAFT
or
publication requires HUMAN_APPROVAL
```

### No forced completeness

DH-01 MUST NOT claim complete historical truth merely because all currently linked PRs were processed.

For example, the record may still miss:

- an unlinked repository PR;
- a direct commit;
- an operations/configuration change outside the primary source repository;
- a reverted or replacement change;
- a later fix required to complete the feature.

The declared `correlation.completeness` and limitations make this visible.

---

## 4.5 Historical feature semantics

Feature/Backlog text is a source for **historical semantics**, not current product authority.

The maintenance Skill may derive normalized terms such as:

```text
product/system
capability
requirement concepts
feature type
```

but MUST preserve:

- the source references;
- whether the terms were direct or derived;
- ambiguity/limitations.

An Agent MUST NOT convert a guessed historical intent into an organizational rule or current requirement.

---

## 4.6 Observed delivery semantics

Observed delivery should capture what actually changed as supported by historical delivery evidence.

Useful reusable dimensions include:

```text
repository touched
path touched
API/interface impact
event impact
schema/data impact
configuration impact
operations/release impact
test/validation impact
```

The Asset MAY retain only summarized reusable semantics plus backlinks rather than copying raw diffs, CI artifacts, or review conversations.

Every materially reusable observed-delivery fact MUST backlink to the historical evidence that supports it. Historical repository identity MUST be preserved. An optional mapping to a current `repo_id` may be supplied through PA-03 identity/lineage evidence, but that mapping is navigation support only and MUST NOT rewrite the historical identity.

The historical Asset is allowed to say:

> Feature F-123 historically touched repo A and repo B, supported by PR/commit evidence.

It is not allowed to say:

> Therefore repo A and repo B must be changed by the current feature.

---

## 4.7 Maintenance mode and PA Skill

Primary mode:

```text
DERIVED
```

Recommended maintenance Skill:

```text
PA-Historical-Delivery
```

Conceptually:

```text
HistoricalDeliveryAsset
=
f(
  historical feature/backlog/issues,
  PRs/commits/reviews/CI/release evidence,
  PA-Historical-Delivery@revision
  ; supporting ProductAssetRefs
)
```

The Skill MAY:

- collect explicit links;
- normalize source identities;
- derive reusable feature terms;
- extract observed repositories/paths/change types;
- identify correlation gaps;
- propose ambiguous correlations;
- preserve evidence backlinks.

It MUST NOT:

- fabricate missing source links;
- treat semantic similarity as confirmed delivery linkage without declaring derivation;
- infer current repository relevance;
- turn a historical pattern into a durable architecture/domain rule;
- hide incomplete or conflicting evidence.

---

## 4.8 Publication policy

`RULE_BASED_AUTO` MAY be used for a DH-01 revision when all materially influential delivery correlations are based on declared strong source links and deterministic extraction checks pass. Deterministic publication may record source-backed facts such as "linked PR X touched repo Y" with delivery relevance left `UNKNOWN`. Classifying an ambiguous change as `FEATURE_DELIVERY`, excluding a material linked change as `INCIDENTAL`, or otherwise making a semantic judgment that materially changes the reusable pattern requires `HUMAN_APPROVAL` unless an explicitly approved deterministic rule covers that classification.

`HUMAN_APPROVAL` is required when publication depends materially on:

- ambiguous semantic/temporal correlation;
- conflicting historical sources;
- manual reconstruction of missing links;
- interpretation that changes which repositories/change types are recorded;
- unresolved evidence that could materially alter the reusable pattern.

Agent-produced candidate records default to `DRAFT` unless the approved Asset contract explicitly qualifies for rule-based publication.

---

## 4.9 Publication quality gate

Before DH-01 becomes `PUBLISHED + ACTIVE`, it MUST establish:

1. stable `delivery_unit_id` plus original primary work-item source identity;
2. historical product-change semantics with explicit derivation/provenance;
3. every materially recorded repository/change-surface fact has historical evidence backlinks;
4. every materially linked delivery source has an explicit correlation link/method/strength;
5. semantic delivery relevance is explicit or remains `UNKNOWN`;
6. correlation completeness is scope-qualified and explicit;
7. conflicting/reverted/replacement evidence and delivery outcome are represented when material;
8. historical `delivered_as_of` value and basis are explicit;
9. limitations are explicit;
10. trust profile matches the actual derivation/review/verification path;
11. selection metadata supports bounded similarity retrieval;
12. the Asset does not claim present-day applicability.

---

## 4.10 Freshness / invalidation

A closed historical delivery fact normally does not become stale because the current codebase changes.

Typical maintenance triggers are instead:

```text
new historical PR/commit linkage discovered
source history corrected
historical feature/backlog record corrected
revert/replacement evidence discovered
historical release evidence added
manual correlation correction
```

Typical freshness mode:

```text
EVENT_DRIVEN or MANUAL
```

A new current product architecture does **not** rewrite the historical fact. Layer 1 simply evaluates whether the historical pattern remains applicable to a new feature.

---

## 4.11 DH-02 — Delivery History Index

DH-02 is a derived navigation index over published DH-01 records.

It MAY expose retrieval dimensions such as:

```text
product/system
capability terms
requirement terms
historical repositories
change types
interface/schema/config/operations impacts
delivery period
delivery outcome
correlation quality/completeness
```

It MAY compute retrieval-oriented summaries such as:

```text
similar historical records
frequently co-touched repositories
frequently observed change types
```

Any aggregate statement such as "frequently co-touched repositories" MUST expose enough support metadata to prevent an opaque historical heuristic from becoming implied authority, including at least:

```text
support_count
eligible_record_count / denominator basis
source_record_refs or reproducible source set
time window / as-of semantics
filter/aggregation rule revision
```

But:

> **DH-02 is a retrieval projection, not independent historical truth and never current feature truth.**

Every result MUST backlink to the underlying DH-01 record(s).

Publication may use `RULE_BASED_AUTO` when index integrity checks pass and it does not elevate semantic authority.

---

## 4.12 Layer 1 consumption

PA-05 is primarily consumed by FT-T2.

```text
intention.md
    |
    v
FT-T2 ContextRequirement
    |
    v
DH-02 bounded similarity lookup
    |
    v
selected DH-01 ProductAssetRefs
    |
    v
ResolvedContextRefs
    |
    v
historical candidate hypotheses
    |
    v
current feature-specific investigation
    |
    v
EvidenceRef
    |
    +--> CONFIRMED
    +--> EXCLUDED
    `--> UNRESOLVED
```

Recommended role by Layer 1 transition:

| Layer 1 Skill | Use |
| --- | --- |
| FT-T1 | Rare; only when historical terminology/context helps interpret the Human signal |
| **FT-T2** | **Primary: candidate generation, investigation prioritization, historical change-pattern comparison** |
| FT-T3 | Normally not required; may be consulted for known migration pitfalls without creating new scope |
| FT-T4 | Normally not required; historical outcomes do not replace current V&V evidence |

---

## 4.13 Historical replay boundary

DH-01 may contain full post-delivery historical information because its purpose is reusable historical intelligence.

If the organization later uses Delivery History Assets to benchmark an FDI Skill against a historical feature, the benchmark harness MUST enforce its own temporal cutoff and prevent post-cutoff information leakage.

Historical replay semantics are therefore **evaluation-harness policy**, not a restriction on the durable DH-01 product asset.

---

## 4.14 PA-05 Success measures

Recommended measures:

| Metric | Meaning |
| --- | --- |
| Historical linkage coverage | Historical features with usable linked delivery evidence |
| Correlation defect rate | Published records later found to have wrong feature↔delivery linkage |
| Candidate recall uplift | Improvement in T2 critical repo candidate recall when PA-05 is available |
| Candidate noise | Irrelevant repository candidates induced by historical patterns |
| Change-surface uplift | Improvement in discovery of API/schema/config/event/operations impacts |
| Reuse rate | How frequently published DH records materially inform later T2 investigations |
| Maintenance cost | Frontier Team effort per useful published historical record |
| Provenance completeness | Material historical claims with valid evidence backlinks |

The goal is not to maximize the number of historical records. It is to maintain records whose future discovery value exceeds their maintenance cost.

---

# 5. PA-03 + PA-05 Combined FT-T2 Use

The initial Product Intelligence bootstrap intentionally combines Codebase and Delivery History rather than trying to pre-build a complete current relation graph.

```text
                PA-03 Codebase
              /                 \
Repository inventory        known high-value relations
              \                 /
               \               /
                v             v
                 FT-T2 candidate discovery
                ^             ^
               /               \
              /                 \
      similar historical     historical repo/change patterns
              \                 /
               PA-05 Delivery History
```

The resulting candidate set is **not** the approved Change Surface.

FT-T2 then performs bounded current-state investigation:

```text
Codebase navigation
+ Delivery History hypotheses
        |
        v
candidate repositories / change obligations
        |
        v
pinned current source / config / schema / test / interface evidence
        |
        v
Layer 1 Change Surface finding
  CANDIDATE
  CONFIRMED
  EXCLUDED
  UNRESOLVED
```

This creates the intended division of responsibility:

> **PA-03 says where the product is. PA-05 says where similar changes went before. FT-T2 establishes what the current feature actually requires.**

---

# 6. Layer 1 Context-Resolution Mapping

The Product Asset Profiles expose reusable Assets. Layer 1 continues to own the approved `ContextRequirement -> ResolvedContextRef` interface.

Recommended FT-T2 requirement patterns include:

### Codebase navigation

```yaml
context_requirement:
  purpose: "bounded repository/system navigation for Change Surface discovery"
  authority_dimension: "CURRENT_BEHAVIOR_SUPPORT"
  mode: "ON_DEMAND"
  selector: "bounded by product/system scope, repo seeds, capability/technology terms"
  applicability: "when Codebase Product Assets are available and useful for bounded repository/system discovery"
  freshness_requirement: "active/current enough for navigation"
```

### Delivery-history retrieval

```yaml
context_requirement:
  purpose: "historical candidate generation and investigation prioritization"
  authority_dimension: "RATIONALE_SUPPORT"
  mode: "ON_DEMAND"
  selector: "bounded similarity by product/system/capability/requirement terms"
  freshness_requirement: "published active historical record/index"
```

The exact Layer 1 requirement syntax remains governed by Layer 1. The examples above are Profile-to-Layer-1 mapping guidance, not a change to the approved Layer 1 schema.

---

# 7. Frontier Team Maintenance Boundary

The Frontier Team maintains Product Assets for reuse. It does not manually author every field forever.

The preferred operating model is:

```text
Deterministic/reliable source change
        |
        v
PA-* Skill proposes or derives revision
        |
        v
DRAFT
        |
        +--> rule-based quality gate where permitted
        |
        +--> Human review where judgment/authority is required
        v
PUBLISHED + ACTIVE
```

Repeated Layer 1 findings also provide maintenance signals:

```text
Repeated T2 miss
Repeated rediscovery
Repeated stale Asset
Repeated wrong historical candidate
        |
        v
Product Asset maintenance candidate
```

A Layer 1 miss does not automatically modify Layer 2. It creates a maintenance signal that the accountable Asset owner may act on.

---

# 8. Deferred Profiles

PA-01, PA-02, PA-04, PA-06, PA-07, and PA-08 remain governed by the Layer 2 common contract but are not fully specified in this v0.1 document.

Their future profiles MUST use the same common Profile Contract and MUST NOT change the approved Layer 1 canonical flow.

| Profile | Deferred question |
| --- | --- |
| PA-01 Product | Minimum durable capability/boundary model worth maintaining |
| PA-02 Architecture | Which architecture decisions are curated vs referenced and how applicability is expressed |
| PA-04 Domain | How derived domain summaries gain accountable review/authorization |
| PA-06 Operations | Which runtime/release metadata is durable Asset versus Layer 1 execution evidence |
| PA-07 Knowledge | Promotion/review/retirement policy for reusable learnings |
| PA-08 Reference | Registration/version/expiry semantics for governed external/internal references |

---

# 9. v0.1 Non-Goals

This specification does not define or authorize:

- a complete repository dependency graph;
- organization-wide semantic code indexing;
- a universal relation extractor;
- automatic interpretation of every historical PR;
- a full knowledge graph;
- a vector database requirement;
- a mandatory Markdown representation for every Asset;
- automatic publication of Agent-generated semantic conclusions;
- T2 feature-specific Change Surface confirmation from historical/indexed data alone;
- Product/Architecture/Domain/Operations/Knowledge/Reference profile implementation;
- historical replay execution;
- any physical repository migration or crawler deployment.

---

# 10. Design Approval Checklist

Before Product Asset Profile Specification v0.1 can be called `Contract-ready`, approve:

- [x] Common Product Asset Profile Contract
- [x] Profile registry and v0.1 scope limited to PA-03 and PA-05
- [x] Profile conformance metadata and scope-qualified completeness rule
- [x] PA-03 CB-01 Repository Inventory semantics, repository identity continuity, and publication boundary
- [x] PA-03 CB-02 high-value relations are optional/ROI-driven, directionally defined, and not a complete graph
- [x] Field-specific source authority/conflict handling for Codebase Assets
- [x] Codebase Asset vs feature-specific `CONFIRMED` Change Surface boundary
- [x] PA-05 DH-01 stable delivery-unit identity, delivered-as-of basis, delivery outcome, and source/evidence model
- [x] Historical Feature + Backlog + PR/Commit/Review/CI are upstream sources for DH-01
- [x] Per-source explicit/derived historical correlation links, delivery-relevance classification, and ambiguity publication rules
- [x] DH-01 completeness/limitations semantics
- [x] DH-02 index is navigation only, backlinked to DH-01, and aggregate patterns expose support/denominator/as-of metadata
- [x] Delivery History generates candidates but never current feature truth
- [x] Historical replay temporal cutoff is an evaluation-harness concern, not DH-01 Asset semantics
- [x] Combined PA-03 + PA-05 FT-T2 discovery model
- [x] Frontier Team maintenance signals and no automatic Layer 1→Layer 2 mutation
- [x] Deferred-profile boundary and v0.1 non-goals

Current state:

```text
Layer 1 Contract-ready: APPROVED
Layer 2 Product Intelligence Contract-ready: APPROVED
Product Asset Profile v0.1 Contract review: PASS
Product Asset Profile v0.1 Contract-ready: APPROVED
Herman design approval: APPROVED
Product Asset Profile execution-verified: NOT_CLAIMED
Product Asset implementation: NOT_AUTHORIZED_BY_THIS_DESIGN
```

---

# 11. Compact Model

```text
                FRONTIER TEAM MAINTAINS

       PA-03 Codebase Product Assets
       ├── CB-01 Repository Inventory
       └── CB-02 High-Value Relations (optional)

       PA-05 Delivery History Product Assets
       ├── DH-01 Historical Delivery Records
       └── DH-02 Delivery History Index
                       |
                       | bounded selection
                       v
                 ProductAssetRefs
                       |
                       v
               ResolvedContextRefs
                       |
───────────────────────┼────────────────────────
                       |
                       v
                 FT-T2 Skill
                       |
                       | current feature evidence
                       v
             Confirmed Change Surface
                       |
                       v
                    spec.md
```

The v0.1 governing principle is:

> **Maintain only durable Product Intelligence that reduces repeated discovery cost or improves Layer 1 quality. Preserve identity, provenance, scope, and uncertainty rather than normalizing them away. Use historical and indexed Assets to guide investigation; use current feature-specific Evidence to establish the actual Change Surface.**
