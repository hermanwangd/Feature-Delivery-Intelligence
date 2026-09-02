# FDI Governing Specification

> GENERATED — DO NOT EDIT
> baseline_id: GB-0001
> baseline_status: APPROVED
> baseline_digest: 96d5f43a3c50ba2697907d4170f01997ab1b21e60f01e67c27ae5ed8f9fdc48e

This view contains only baseline-selected normative modules. The baseline
selects authority; the exact modules below define semantics.

## L1-SEM — layer1_semantics

- Semantic version: `0.2`
- Approval: `HERM-210; multica-attachment:01a05228-a42d-72fa-b388-558f59430632`
- Compatibility: `L1-IO@0.1; FT-T2@LOCKED-HERM-211`

### Source: `normative/layer1/semantic/fdi-layer1-specification-v0.2-approved.md`

SHA-256: `9442f7ad788d4ffa59f9b1d5ef77de9b119550846df1e09df77737aa3fc7307d`

# FDI Layer 1 — Feature Transformation Specification v0.2

> **Status:** APPROVED — Layer 1 v0.2 contract-ready  
> **Scope:** Layer 1 only — canonical feature flow, transformation contracts, Context-reference interface, lifecycle, Change Surface, traceability, and correctness  
> **Design only:** No Context Supply design, physical Context generation, repository change, validator, pilot, or execution claim  
> **Confirmed:** Four canonical feature artifacts; `f_skill` is the transformation contract; Agent/Squad is the executor; Context is independently governed and referenced by Skills; Baseline/history/memory production and maintenance remain outside Layer 1  
> **Current state:** `Contract-ready: APPROVED`, `Execution-verified: NOT_CLAIMED`

---

## 0. Purpose, scope, and invariants

FDI Layer 1 defines how a feature moves from an authenticated Human Signal to independently established Correctness.

```text
Human Signal
    |
    | f(T1 Intention Skill ; Context refs)
    v
intention.md
    |
    | f(T2 Delivery Spec Skill ; Context refs)
    v
spec.md
    |
    | f(T3 Implementation Skill ; Context refs)
    v
ImplementationBundle
    |
    | f(T4 Correctness Skill ; Context refs)
    v
CorrectnessBundle
```

The canonical transformation model is:

```text
OutputBundle = f(
    CanonicalInput(s),
    GovernedSkill@revision
    ; ResolvedContextRefs
)
```

The semicolon is normative: `ResolvedContextRefs` are governed execution dependencies, not additional canonical workflow stages.

### 0.1 Layer 1 invariants

1. **Four canonical transformations only.** T1, T2, T3, and T4 are the canonical feature flow.
2. **Skill defines transformation; Agent executes it.** Agent, model, Squad topology, parallelism, retries, and runtime are not part of the canonical equation.
3. **Context is referenced, not owned by Skills.** A Skill declares what Context it needs and how it may select it; Layer 1 does not define how Context products are generated.
4. **Canonical artifacts carry authority.** Context may constrain or support an artifact but cannot silently replace its authority.
5. **Exact dependencies matter.** Every downstream artifact pins exact upstream artifact revisions and records materially influential Context and Evidence references.
6. **Gate and validity are different.** An artifact may have passed its output gate and later become `STALE`.
7. **T2 owns feature-specific Change Surface discovery.** Repository seeds and historical hints are candidate-generation inputs, not proof of complete current scope.
8. **T3 may create governed external side effects.** Source-repository candidates are part of the T3 OutputBundle even though `implementation.md` is the canonical coordination artifact.
9. **T4 separates verification from validation.** Implementation completion never implies Correctness.
10. **Layer 1 stops at independently established candidate Correctness.** Merge, deployment, release readiness, rollout, and production operation remain governed elsewhere unless explicitly included in the Intention/Spec criteria and observed by T4.

### 0.2 Explicitly out of scope

Layer 1 does not define:

- how Context Markdown is produced, refreshed, verified, promoted, indexed, or retired;
- Baseline discovery, Baseline refresh, atomic adoption, Knowledge promotion, history consolidation, or memory maintenance;
- a Context graph or enterprise dependency graph;
- an orchestration platform, control plane, ledger, validator implementation, or runtime;
- Agent/model assignment or Squad topology;
- source-repository merge, deployment, or release policy.

Those are separate designs behind explicit Layer 1 interfaces.

---

# Contract L1 — Canonical Artifact Contract

## L1.1 Canonical artifacts

| Stage | Canonical input | Canonical output | Governing Skill | Output gate |
| --- | --- | --- | --- | --- |
| T1 | Authenticated Human Signal | `intention.md` | `T1-Intention-Skill` | `INTENTION_READY` / `BLOCKED` |
| T2 | Exact active `intention.md` revision | `spec.md` | `T2-Delivery-Spec-Skill` | `SPEC_READY` / `BLOCKED` |
| T3 | Exact active `spec.md` revision | `ImplementationBundle` whose canonical coordination artifact is `implementation.md` | `T3-Implementation-Skill` | `CHANGE_SET_READY` / `BLOCKED` |
| T4 | Exact active Intention, Spec, ImplementationBundle, and candidate revisions | `CorrectnessBundle` whose canonical artifact is `correctness.md` | `T4-Correctness-Skill` | `PASS` / `FAIL` / `INCONCLUSIVE` |

A simple feature requires only these four canonical Markdown files. Appendices MAY be created when a canonical artifact requires bounded supporting detail; appendices never create a new canonical stage or independent authority.

## L1.2 Authenticated Human Signal input contract

`AuthenticatedHumanSignal` is the logical canonical input to T1. It is not required to be a Markdown file and may be represented by a governed request, decision, ticket, conversation record, approval, or another authenticated source.

Layer 1 requires a logical envelope equivalent to:

```yaml
human_signal:
  signal_id: "<stable-signal-id>"
  source_ref: "<immutable-or-governed-source-reference>"
  source_identity: "<requester/decision-authority-identity>"
  captured_at: "<time>"
  authentication_state: "VERIFIED|UNVERIFIED"
  authorization_state: "AUTHORIZED|NOT_AUTHORIZED|UNCLEAR"
  content_ref_or_digest: "<immutable-content-reference-or-digest>"
```

The envelope establishes source identity and provenance; it does not normalize the Human's meaning into an Intention before T1. T1 owns that semantic transformation.

`CONTRACT_READY` for T1 requires `authentication_state: VERIFIED`, an identifiable accessible signal, and sufficient provenance to attempt interpretation. Unclear authorization or meaning MAY still produce a `BLOCKED` Intention; an unverified signal does not enter the canonical T1 transformation.

## L1.3 Canonical artifact envelope

Every canonical Markdown artifact MUST expose enough machine-readable metadata to establish identity, transformation provenance, gate, and validity without interpreting prose.

Minimum frontmatter:

```yaml
---
fdi_version: "0.2"
feature_id: "<stable-feature-id>"
artifact: "intention|spec|implementation|correctness"
revision: <positive-integer>

produced_by:
  skill: "<canonical-skill-id>"
  skill_revision: "<immutable-version-or-revision>"

canonical_owner: "<stable-accountable-role-or-owner-id>"
upstream: {}

gate: "<artifact-specific-gate>"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; derivable from lineage/dependencies
supersedes: <prior-revision-or-null>
---
```

Execution provenance SHOULD also record:

```yaml
executor:
  role_or_agent: "<stable-executor-id>"
  execution_id: "<run-id>"
```

`executor` is provenance only. It does not define artifact authority or transformation semantics.

Artifact `revision` is a logical immutable **semantic revision**. Any change to canonical meaning, gate-producing content, cross-artifact mapping, or a materially influential appendix MUST create a new revision. Prior revisions referenced by downstream artifacts MUST remain addressable through the governing storage/version-control mechanism.

`validity` is lifecycle state, not canonical semantic content. It is derived from the current lineage and dependencies and MAY be materialized in frontmatter as a lifecycle snapshot. A lifecycle-only change such as `ACTIVE -> STALE` does not by itself create a new semantic artifact revision; the governing storage/audit mechanism MUST preserve when and why the lifecycle state changed. `supersedes` is asserted by the newer canonical revision; prior content need not be rewritten merely to establish supersession.

For one `feature_id`, there MUST be at most one `ACTIVE` canonical revision of each artifact type in the active lineage. Alternative drafts, experiments, or branches are non-canonical until explicitly adopted; adoption supersedes the prior active canonical revision and triggers normal downstream invalidation.

## L1.4 Authority by artifact

| Artifact | Authoritative for | Must not silently redefine |
| --- | --- | --- |
| `intention.md` | Desired outcome, intended use, scope/non-goals, success criteria, authorization | Current source truth, technical feasibility, implementation design |
| `spec.md` | Technical obligations, design, Change Surface, ownership, tasks, V&V plan | Intention outcome or Human authorization |
| `implementation.md` | Aggregate mapping of exact candidate changes and implementation observations | Spec obligations, Correctness |
| `correctness.md` | Independent verification/validation evidence and criterion verdicts | Intention or Spec obligations |

## L1.5 Required artifact bodies

### `intention.md`

MUST contain:

1. identity and revision;
2. authenticated Human Signal summary and provenance;
3. stakeholders/intended users;
4. desired outcome and intended-use scenarios;
5. scope and non-goals;
6. constraints and assumptions;
7. measurable success criteria with stable criterion IDs;
8. known product/system/repository seeds, explicitly non-exhaustive;
9. materially influential Context references and exclusions;
10. unresolved questions/conflicts;
11. gate record.

### `spec.md`

MUST contain:

1. identity and exact Intention revision;
2. criterion-to-requirement mapping;
3. functional and quality requirements;
4. design and invariants;
5. current-state assumptions and supporting evidence refs;
6. Change Surface findings and impacted repository map;
7. interfaces/data/config/schema/security/operations/rollout/rollback obligations as applicable;
8. implementation tasks and accountable ownership;
9. V&V plan with method, evidence expectation, threshold, and independence;
10. governed appendix registry when used;
11. materially influential Context refs, selector proof, and exclusions;
12. risks, gaps, and deviations requiring authorization;
13. gate record.

### `implementation.md`

MUST contain:

1. identity and exact Spec revision;
2. candidate summary;
3. repository implementation map with `required_action`, owner, disposition, and task mappings; immutable candidate base/head/location are required when `required_action: CHANGE`, while evidence-backed dispositions are required for `VERIFY_ONLY` and `NO_CHANGE`;
4. changed-path and migration summary;
5. requirement/design/task mappings;
6. checks executed and observed results;
7. deviations from Spec with blocking classification and disposition;
8. governed appendix registry when used;
9. materially influential Context refs;
10. governing Skill/execution provenance;
11. known gaps and T4 handoff;
12. gate record.

### `correctness.md`

MUST contain:

1. identity and exact Intention/Spec/Implementation/candidate revisions;
2. independent verifier/executor provenance;
3. evidence inventory and integrity;
4. verification findings against Spec;
5. validation findings against Intention/intended use;
6. one verdict per Intention criterion;
7. requirement/design/task/repository coverage;
8. deviations, gaps, limitations, and unobserved scope;
9. release/production observation when present, otherwise `NOT_OBSERVED`;
10. earliest re-entry point and owner;
11. materially influential Context refs;
12. overall verdict and gate record.

## L1.6 OutputBundle

The generic output of an FDI Skill is an `OutputBundle`, not necessarily one file:

```text
OutputBundle
├── CanonicalArtifact      required
├── GovernedAppendices*    optional
└── GovernedSideEffects*   optional
```

Rules:

- T1 normally has no external side effects.
- T2 normally has no source-repository side effects.
- T3 MAY create source/config/schema/test candidates in approved repositories.
- T4 MAY create governed evidence records but MUST NOT repair the candidate it is independently judging.
- A side effect cannot create new canonical feature authority.

## L1.7 Shared structured record contracts

Narrative Markdown is allowed, but cross-artifact records that participate in gates or traceability MUST expose stable structured fields equivalent to the following.

### Intention criterion

```yaml
criterion:
  criterion_id: "C-<id>"
  statement: "<measurable desired outcome>"
  blocking: true
  success_measure: "<observable measure>"
  threshold_or_acceptance: "<pass condition>"
  human_signal_refs: ["<signal-fragment-ref>"]
```

Criteria are `blocking: true` by default. Only T1 may classify a criterion as non-blocking, and only when the authenticated Human Signal or an authorized Human decision supports that classification. T2-T4 MUST NOT downgrade criterion criticality.

### Spec requirement

```yaml
requirement:
  requirement_id: "R-<id>"
  criterion_ids: ["C-<id>"]
  statement: "<technical obligation>"
  owner: "<accountable owner>"
  repo_ids: ["<repo-id>"]
  vv_method_ids: ["<method-id>"]
```

### V&V method / disposition

```yaml
vv_disposition:
  criterion_id: "C-<id>"
  evaluation: "REQUIRED|OBSERVE_IF_AVAILABLE"
  method_id: "V-<id-or-null>"
  method: "<non-tautological-method-or-N/A>"
  evidence_expectation: "<required-evidence-or-observation-policy>"
  threshold_or_acceptance: "<pass-condition-or-N/A>"
  required_scope: "<scope-that-must-be-observed-or-N/A>"
  independence: "<required-independence-or-N/A>"
```

Every blocking criterion MUST use `evaluation: REQUIRED` and define `method`, `evidence_expectation`, `threshold_or_acceptance`, and `required_scope`. A non-blocking criterion MAY use `OBSERVE_IF_AVAILABLE` only when that treatment is consistent with the T1-authorized criterion classification. T4 still records a criterion verdict; lack of evidence for a non-blocking `OBSERVE_IF_AVAILABLE` criterion produces `INCONCLUSIVE` for that criterion without changing the overall gate.

### Implementation task

```yaml
task:
  task_id: "T-<id>"
  requirement_ids: ["R-<id>"]
  repo_ids: ["<repo-id>"]
  owner: "<accountable owner>"
  disposition: "PLANNED|IMPLEMENTED|NO_CHANGE|BLOCKED"
```

### Repository candidate reference

```yaml
candidate_ref:
  repo_id: "<repo-id>"
  base_revision: "<immutable-base>"
  head_revision: "<immutable-candidate-head>"
  location: "<branch/PR/commit/candidate-ref>"
  status: "REVIEWABLE|NOT_READY|SUPERSEDED"
  task_ids: ["T-<id>"]
```

A `candidate_ref` is required for every `CONFIRMED` repository whose Spec `required_action` is `CHANGE`.

### Repository implementation disposition

```yaml
repository_disposition:
  repo_id: "<repo-id>"
  required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE"
  disposition: "READY|BLOCKED|SUPERSEDED"
  task_ids: ["T-<id>"]
  candidate_ref: "<candidate-ref-id-or-null>"
  evidence_refs: ["E-<id>"]
  notes: "<bounded-disposition-summary>"
```

Rules:

- `CHANGE` requires a `candidate_ref` with immutable base/head and reviewable candidate location.
- `VERIFY_ONLY` requires evidence sufficient to establish the verification disposition declared by the active Spec and MUST NOT fabricate a source candidate.
- `NO_CHANGE` requires evidence-backed rationale that the active Spec obligation is satisfied without source change.
- every `CONFIRMED` repository MUST have exactly one active repository disposition in the T3 OutputBundle.

### Evidence reference

```yaml
evidence_ref:
  evidence_id: "E-<id>"
  ref: "<immutable-artifact/source/test-result-reference>"
  revision_or_as_of: "<revision/time>"
  method: "<how the observation was obtained>"
  environment: "<environment-or-N/A>"
  integrity: "<digest/signature/governed-result-ref when applicable>"
  claim_ids: ["<criterion/requirement/finding IDs>"]
```

An `EvidenceRef` is not a `ResolvedContextRef`. Context constrains or informs a transformation; evidence supports a specific finding, mapping, gate, or verdict. A Skill MAY gather new evidence through permitted capabilities during execution and MUST record it when materially used.

### Criterion verdict

```yaml
criterion_verdict:
  criterion_id: "C-<id>"
  verdict: "PASS|FAIL|INCONCLUSIVE"
  verification_finding: "<finding-or-N/A>"
  validation_finding: "<finding>"
  evidence_refs: ["E-<id>"]
  limitations: ["<limitation>"]
  earliest_reentry: "T1|T2|T3|T4|NONE"
```

## L1.8 Governed appendix contract

Appendices are bounded subordinate extensions of a canonical artifact, not additional authorities. A registered appendix may carry contract-relevant detail only through its owning core artifact; it cannot independently expand scope or alter authority. Every appendix MUST be registered by its owning core artifact with at least `appendix_id`, `type`, `trigger`, `status`, and backlink.

Rules:

1. a Spec appendix is allowed only when material detail cannot remain reviewable in `spec.md`; its ID is allocated by the Spec registry;
2. an implementation repository appendix is allowed only for a `CONFIRMED` repository present in the active Change Surface;
3. an evidence appendix is planned by the Spec V&V plan or allocated by T4 as supplemental evidence for an already authorized criterion;
4. supplemental T4 evidence MUST NOT introduce a new desired outcome, technical obligation, repository scope, or V&V obligation;
5. appendices have no independent gate and cannot self-authorize scope;
6. a materially influential appendix change MUST create a new owning core-artifact revision;
7. raw secrets, copied source trees, mutable unpinned evidence, and unrelated files are prohibited.

## L1.9 Multi-repository authority boundary

Layer 1 coordinates cross-repository delivery without transferring source-repository authority into the FDI coordination artifact.

| Concern | FDI canonical artifact responsibility | Source-repository responsibility |
| --- | --- | --- |
| Change Surface / cross-repo obligations | `spec.md` owns the aggregate technical contract, impacted-repository map, sequencing, and V&V obligations | Repository-local feasibility, constraints, and policy remain authoritative for that repository |
| Candidate implementation | `implementation.md` owns the aggregate mapping and disposition | Source/config/schema/test candidate content, branches/commits/PRs, and repository controls remain owned by the source repository |
| Evidence | FDI artifacts own claim/evidence mapping and interpretation | Raw CI/build/test/runtime artifacts remain where their governing system owns them |
| Merge/deploy/release | FDI records planned/observed state only when relevant | Authorization and execution remain under source/release policy |

Repository ownership MUST be resolved before T3 acts on a `CONFIRMED` repository. Resolved ownership does **not** imply mandatory manual acknowledgement for every feature. Explicit owner acknowledgement/approval is required only when repository policy, ownership ambiguity, material interface/governance impact, or another applicable control requires it.

The coordination artifact MUST NOT copy source trees, bypass source-repository review/control, or treat an aggregate Layer 1 gate as authorization to merge, deploy, or release.

---

# Contract L2 — Governed `f_skill` Transformation Contract

## L2.1 Generic function

Every canonical transformation MUST be expressible as:

```text
OutputBundle = f(
    CanonicalInput(s),
    GovernedSkill@revision
    ; ResolvedContextRefs
)
```

The same Skill contract MAY be executed by different Agents, models, Squads, or runtimes without changing the canonical semantics.

## L2.2 Required Skill interface

Every canonical FDI Skill MUST define:

| Field | Normative requirement |
| --- | --- |
| `skill_id` | Stable identifier |
| `skill_revision` | Exact version/revision |
| `purpose` | Single canonical transformation responsibility |
| `canonical_inputs` | Exact upstream artifact types and authority |
| `input_preconditions` | Required gate/validity and input integrity |
| `context_requirements` | What Context roles MAY/MUST be resolved |
| `context_selectors` | Bounded rules for resolving relevant Context |
| `authority_rules` | Authority applicable to each class of claim |
| `procedure` | Required transformation steps/invariants |
| `capability_requirements` | Capabilities needed to attempt the transformation |
| `evidence_rules` | Evidence the Skill may/must observe or generate and how it is pinned |
| `allowed_side_effects` | External mutations the Skill may create |
| `output_contract` | Required OutputBundle schema/semantics |
| `completion_rule` | Conditions under which work is complete |
| `gate_rule` | Allowed gate values and calculation |
| `failure_classes` | Failure/blocker classification |
| `reentry_rule` | Earliest valid upstream transition after a finding |
| `prohibitions` | Actions the Skill must never perform |

## L2.3 Root Skill and helper Skills

A canonical Skill MAY invoke helper Skills, investigators, reviewers, or specialized workers.

```text
Canonical Skill
├── helper Skill
├── investigator
├── reviewer
└── repository worker
```

Only the root canonical Skill defines the canonical transformation contract. Any helper Skill, reviewer, or worker whose output materially influences scope, obligations, mappings, gate, or verdict MUST also be recorded in execution provenance with its exact identity/revision; non-material helper telemetry MAY be omitted.

Helper Skills do not create additional canonical FDI transitions.

## L2.4 Preflight

Before a canonical Skill executes, its preflight returns:

```text
CONTRACT_READY
NOT_CONTRACT_READY
```

`CONTRACT_READY` means the required canonical inputs, Skill revision, required Context-resolution capability, permissions, and execution capabilities are sufficient to attempt the transformation.

It is not an output-quality or correctness claim. `NOT_CONTRACT_READY` does not advance the canonical workflow or create a new output-gate claim; an execution/runtime MAY record a non-canonical diagnostic or preflight record.

## L2.5 Determinism requirement

FDI does not require byte-identical LLM output.

It requires **contract determinism**:

- same artifact type and authority boundaries;
- same required inputs;
- bounded Context-resolution semantics;
- required traceability structure;
- deterministic gate calculation from observed state;
- explicit provenance for material differences.

A dependency is **materially influential** when removing, changing, or superseding it could reasonably change a canonical claim, criterion interpretation, technical obligation, Change Surface disposition, candidate mapping, gate, or verdict. Materially influential Context, Evidence, and helper-Skill dependencies MUST be recorded.

---

# Contract L3 — Context Reference Contract

## L3.1 Boundary

Layer 1 defines how a Skill **requests, resolves, uses, and records** Context.

Layer 1 MUST NOT define how a Context product is generated, refreshed, indexed, promoted, or maintained.

```text
Layer 2 Context Supply
        |
        | supplies governed Context products/references
        v
ResolvedContextRef
        |
        | used by
        v
Layer 1 f_skill
```

## L3.2 ContextRequirement

Each canonical Skill MUST declare Context needs using a requirement contract equivalent to:

```yaml
context_requirement:
  id: "<stable-requirement-id>"
  purpose: "<why this Context is needed>"
  authority_dimension: "<claim authority needed>"
  mode: "REQUIRED|CONDITIONAL|ON_DEMAND"
  selector: "<bounded selection rule>"
  applicability: "<scope/condition>"
  freshness_requirement: "<required revision/as-of semantics>"
  trust_requirement: "<minimum acceptable trust/provenance>"
  claims: ["<criterion/requirement/finding IDs when known>"]
```

`mode` semantics:

- `REQUIRED`: preflight cannot become `CONTRACT_READY` without an acceptable resolution.
- `CONDITIONAL`: required only when the declared applicability condition is true.
- `ON_DEMAND`: may be resolved during bounded investigation when a finding requires it.

The selector MUST be bounded. “Load all repositories/history/knowledge” is not a valid selector.

## L3.3 ResolvedContextRef

A materially influential resolved Context reference MUST record at least:

```yaml
resolved_context_ref:
  requirement_id: "<context-requirement-id>"
  ref: "<stable-context-ref-or-uri>"
  revision_or_as_of: "<immutable-revision-or-time>"
  selected_for: "<claim/purpose>"
  authority_dimension: "<authority dimension>"
  trust_state: "<declared trust state>"
  applicability: "<scope match>"
  freshness: "<fresh/stale/expiry semantics>"
  evidence_backlink: "<source/evidence reference when available>"
```

The exact Context-product schema behind `ref` is a Layer 2 concern.

## L3.4 Context versus execution evidence

Layer 1 distinguishes supporting Context from observed Evidence:

```text
ResolvedContextRef
  = selected governed information used to interpret/constrain work

EvidenceRef
  = pinned observation/source/result used to establish a specific claim
```

A T2 Skill may use Context to decide where to investigate and then collect pinned current-source Evidence. A T4 Skill may use Context to select the applicable V&V procedure and then collect independent test/runtime Evidence. Directly observed source/test/runtime evidence does not need to be materialized as a Layer 2 Context product before it can support a Layer 1 claim.

Context products MAY backlink to source evidence, but that does not make their indexed/derived claim equivalent to current source truth.

## L3.5 Authority dimensions

Layer 1 recognizes at least these authority dimensions:

| Dimension | Primary authority in Layer 1 |
| --- | --- |
| Desired outcome | Active authorized Intention |
| Technical obligation | Active Spec, subordinate to Intention |
| Durable organizational/domain constraint | Applicable governed Context |
| Current behavior/state | Pinned current-source/runtime `EvidenceRef`; Context may guide discovery/interpretation but does not replace the evidence |
| Procedure | Active canonical Skill and permitted capabilities |
| Rationale/support | Qualified supporting Context |

A source type does not receive global authority merely because it is called Baseline, history, memory, Knowledge, or External.

## L3.6 Conflict and gap rule

When resolved Context sources disagree, the Skill MUST reconcile by:

- disputed claim;
- authority dimension;
- revision/as-of;
- environment/scope;
- applicability;
- trust/provenance.

If a genuine conflict remains, the Skill MUST record a Context gap.

A Context gap blocks only the dependent claim when dependency isolation is demonstrated. Otherwise the producing transition is `BLOCKED` or T4 becomes `INCONCLUSIVE` as appropriate.

## L3.7 Context production is explicitly deferred

Layer 1 does not specify whether a Context reference resolves to:

- curated Markdown;
- derived Markdown;
- an indexed projection;
- a directly referenced authoritative artifact;
- an on-demand projection;
- another governed representation.

Layer 2 will define, per Context product, the source inputs, builder/resolver Skill, authority, trust, refresh/invalidation, and physical Markdown contract.

---

# Contract L4 — T1–T4 Canonical Transformation Contracts

## L4.1 T1 — Intention

### Function

```text
intention.md = f(
    AuthenticatedHumanSignal,
    T1-Intention-Skill@revision
    ; R1
)
```

### Input authority

The authenticated Human Signal is authoritative for expressed need and authorization. It is not authoritative for technical feasibility or implementation design.

### Context needs

T1 MAY require Context for:

- terminology/domain interpretation;
- product/system identity;
- durable constraints;
- known scope/impact seeds;
- clarification of ambiguous current-state claims.

Context MUST NOT silently redefine the Human's desired outcome.

### Required procedure

T1 MUST:

1. authenticate/safely summarize the Human Signal;
2. identify intended users/stakeholders;
3. define desired outcome and intended-use scenarios;
4. define scope and non-goals;
5. record constraints/assumptions;
6. define measurable success criteria;
7. assign stable criterion IDs and blocking/non-blocking classification under L1.7;
8. map every authorized requested outcome to criteria;
9. identify known product/system/repository seeds without completeness claim;
10. record influential Context refs/exclusions/conflicts;
11. calculate the output gate.

### Completion/gate

```text
INTENTION_READY
BLOCKED
```

`INTENTION_READY` requires that authorization is known, every requested outcome is represented by measurable criteria, criterion criticality is explicit, and no unresolved ambiguity materially changes desired outcome, intended use, scope, or success semantics.

### Re-entry/prohibitions

Re-enter Human/T1 when desired outcome, authorization, intended use, scope, or criterion semantics are ambiguous or changed.

T1 MUST NOT choose implementation architecture, convert repository hints into obligations, or turn historical behavior into desired outcome without Human authority.

---

## L4.2 T2 — Delivery Spec

### Function

```text
SpecBundle = f(
    intention.md@exact-active-revision,
    T2-Delivery-Spec-Skill@revision
    ; R2
)

core(SpecBundle) = spec.md
```

### Input authority

T2 MUST preserve the active Intention's outcome, intended use, scope/non-goals, and success criteria.

Repository seeds in Intention are advisory discovery starts, not authoritative completeness boundaries.

### Context needs

T2 MAY/MUST resolve Context required for:

- durable architecture/technology/domain constraints;
- current system/repository topology;
- repository ownership;
- pinned source/config/schema/test/interface evidence;
- operational/security/release constraints;
- historical/supporting evidence useful for candidate generation;
- external obligations when applicable.

### Required procedure

T2 MUST:

1. pin the exact active Intention revision;
2. map every criterion to technical obligations;
3. establish relevant current-state assumptions from pinned evidence;
4. perform bounded feature-specific Change Surface discovery under Contract L5, using historical/indexed relations only for candidate generation unless current applicability evidence confirms them;
5. resolve impacted repository ownership;
6. define functional/quality requirements;
7. define design/invariants;
8. define interface/data/config/schema/security/operations/rollout/rollback obligations as applicable;
9. define implementation tasks/ownership;
10. define a V&V disposition for every Intention criterion: a non-tautological method and evidence expectation when the criterion is to be evaluated, or an explicit authorized non-blocking observation policy when full evaluation is not required; every blocking criterion MUST have a non-tautological V&V method and evidence expectation;
11. record Context resolution, exclusions, risks, conflicts, and deviations;
12. calculate the output gate.

### Completion/gate

```text
SPEC_READY
BLOCKED
```

`SPEC_READY` requires:

- every blocking Intention criterion maps to technical obligations;
- every obligation maps to accountable ownership and implementation work or explicit no-change rationale;
- Change Surface satisfies L5 sufficiency;
- every Intention criterion has an explicit V&V disposition, and every blocking criterion has a defined non-tautological V&V method and evidence expectation;
- no unresolved issue remains that can materially change the technical contract.

### Re-entry/prohibitions

Return to T1 when the desired outcome/criterion/authorization itself must change.

Remain in/re-enter T2 for incomplete Change Surface, unresolved ownership, infeasible design, missing technical obligations, or inadequate V&V design.

T2 MUST NOT silently change Intention, implement source changes, or grant merge/release authority.

---

## L4.3 T3 — Implementation

### Function

```text
ImplementationBundle = f(
    spec.md@exact-active-revision,
    T3-Implementation-Skill@revision
    ; R3
)
```

```text
ImplementationBundle
├── implementation.md
├── CandidateSet
└── GovernedImplementationAppendices*
```

### Input authority

The active Spec is authoritative for the approved technical obligations and impacted repository set.

T3 MUST NOT silently reinterpret new scope as if it were already approved.

### Context needs

T3 MAY/MUST resolve Context only for the approved implementation surface, including repository-local instructions, exact source/config/schema/test state, interface contracts, applicable durable constraints, and operational requirements.

### Allowed side effects

T3 MAY create reviewable candidates in approved source repositories, including code/config/schema/test changes, branches, commits, or PRs as permitted by repository policy and execution permissions.

T3 MUST NOT merge/deploy/release unless separately authorized outside the Layer 1 `CHANGE_SET_READY` semantics.

### Required procedure

T3 MUST:

1. pin exact active Spec revision;
2. verify repository ownership and permissions;
3. pin immutable repository base revisions;
4. map implementation tasks to Spec obligations;
5. create the required candidates;
6. coordinate cross-repository dependencies;
7. execute applicable implementation checks;
8. pin candidate heads;
9. record changed paths/migrations/checks;
10. record Spec deviations and blocking classification;
11. stop affected work and re-enter T2 when new required scope exceeds the active Spec;
12. produce the aggregate implementation record and gate.

### Completion/gate

```text
CHANGE_SET_READY
BLOCKED
```

`CHANGE_SET_READY` requires every `CONFIRMED` repository to satisfy the action declared by the active Spec:

- `CHANGE`: a pinned reviewable candidate exists;
- `VERIFY_ONLY`: the required evidence-backed verification disposition exists;
- `NO_CHANGE`: the active Spec explicitly requires no source change and an evidence-backed no-change disposition exists.

It means ready for independent T4 V&V only. It does not mean correct, approved, merged, deployed, or released.

### Re-entry/prohibitions

Return to T2 for newly required repository scope, invalid/incomplete Spec obligations, or design/interface changes.

Remain in/re-enter T3 for implementation defects, candidate/check failures attributable to implementation, or incomplete candidate mappings.

T3 MUST NOT self-declare Correctness or bypass source-repository controls.

---

## L4.4 T4 — Correctness

### Function

```text
CorrectnessBundle = f(
    intention.md@exact-active-revision,
    spec.md@exact-active-revision,
    ImplementationBundle@exact-candidate-revisions,
    T4-Correctness-Skill@revision
    ; R4
)

core(CorrectnessBundle) = correctness.md
```

### Input authority

T4 judges two separate relationships:

```text
Verification: Implementation <-> Spec
Validation:   Implementation <-> Intention
```

T4 MUST NOT rely on T3's completion assertion as proof of either relationship.

### Independence

The `correctness.md` canonical owner MUST be a distinct accountable owner/role from the `implementation.md` canonical owner. T4 MUST execute in a distinct evaluation run/context from the T3 implementation execution, MUST independently evaluate the evidence, and MUST NOT inherit T3 self-verdicts as authoritative. The T4 evaluator MUST NOT have candidate-mutation authority over the candidate under judgment during that evaluation. The same underlying model family MAY be reused; stronger separation of Agent identity, model, reviewer, tools, or Human approval MAY be imposed by the execution profile.

### Context needs

T4 MAY/MUST resolve Context necessary to interpret the active V&V plan and MAY/MUST collect or reference Evidence necessary to independently evaluate intended-use scenarios, environment, applicable durable constraints, and evidence integrity.

### Required procedure

T4 MUST:

1. pin exact Intention, Spec, implementation, and candidate revisions;
2. establish evidence integrity;
3. evaluate every Intention criterion according to its active V&V disposition, with all blocking criteria evaluated as `REQUIRED`;
4. verify mapped Spec obligations required by those dispositions;
5. validate intended-use outcomes required by those dispositions;
6. report verification separately from validation;
7. assign one criterion verdict each;
8. record gaps, limitations, and unobserved scope;
9. verify that the observed V&V scope covers every required blocking-criterion scope declared by the active Spec;
10. determine earliest valid re-entry;
11. calculate the overall verdict.

### Completion/gate

```text
PASS
FAIL
INCONCLUSIVE
```

- `PASS`: every blocking criterion passes and the observed V&V scope satisfies the active Spec's required scope for every blocking criterion.
- `FAIL`: at least one blocking criterion fails.
- `INCONCLUSIVE`: required evidence/capability or required V&V scope is unavailable or insufficient to decide one or more blocking criteria.

`PASS` does not imply merge/deployment/release/production observation unless those are explicit Intention criteria or Spec V&V obligations.

### Re-entry/prohibitions

- wrong/changed desired outcome or criterion -> T1;
- wrong/incomplete technical obligation, design, Change Surface, ownership, or V&V plan -> T2;
- candidate does not conform to valid Spec -> T3;
- candidate remains valid but required evidence is unavailable -> T4 when evidence becomes available.

T4 MAY create non-candidate-mutating evidence/test artifacts as permitted by its Skill. T4 MUST NOT repair implementation and self-approve it as independent, mutate the candidate under judgment, rewrite Spec to make a candidate pass, or introduce new feature scope through supplemental evidence.

---

# Contract L5 — Feature-Specific Change Surface Contract

## L5.1 Purpose

Change Surface is the evidence-backed set of repositories and materially relevant change obligations that T2 determines are required by the active Intention and technical design.

It is **feature-specific**, not a generic enterprise dependency graph.

## L5.2 Candidate generation versus confirmation

T2 MAY generate candidates from allowed Context and/or collected Evidence, including:

- known product/system/repository seeds;
- curated topology/navigation indexes;
- historical delivery patterns;
- current dependency hints;
- targeted semantic/source investigation;
- interface/schema/event/config/runtime ownership evidence.

Candidate generation does not establish current applicability.

A repository becomes `CONFIRMED` only when feature-specific evidence supports its current relevance.

## L5.3 ChangeSurfaceFinding

Each materially considered repository MUST have a finding equivalent to:

```yaml
change_surface_finding:
  finding_id: "CS-<id>"
  repo_id: "<stable-repository-id>"
  status: "CANDIDATE|CONFIRMED|EXCLUDED|UNRESOLVED"
  relevance: "<why this repo may/must matter>"
  relation_types: ["<api|event|schema|data|library|config|runtime|ownership|other>"]
  criterion_ids: ["<intention-criterion-ids>"]
  requirement_ids: ["<spec-requirement-ids-if-known>"]
  context_refs: ["<resolved-context-ref-ids-used-for-candidate-generation-or-interpretation>"]
  evidence_refs: ["<pinned-current-or-feature-specific-evidence-ref-ids>"]
  owner: "<resolved-owner-or-null>"
  required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE|NOT_APPLICABLE|UNDECIDED"
  planned_change: "<expected change, verification obligation, or no-change rationale>"
  blocking: <true|false>
```

## L5.4 State semantics

- `CANDIDATE`: Context and/or evidence indicates possible relevance; current feature-specific disposition is not yet established. `required_action` MUST be `UNDECIDED`.
- `CONFIRMED`: current feature-specific `EvidenceRef` supports inclusion in the active Change Surface. Historical patterns, stale indexes, or unverified relation hints alone MUST NOT establish `CONFIRMED`. `required_action` MUST be `CHANGE`, `VERIFY_ONLY`, or `NO_CHANGE`.
- `EXCLUDED`: current feature-specific evidence supports non-inclusion for the active feature, with rationale retained. `required_action` MUST be `NOT_APPLICABLE`.
- `UNRESOLVED`: available evidence is insufficient or conflicting and the disposition can materially affect the Spec. `required_action` MUST remain `UNDECIDED`.

## L5.5 Bounded discovery

T2 discovery MUST be bounded by explicit selectors such as:

- authorized product/system scope;
- relation types;
- repository organization/ownership boundaries;
- traversal depth/budget;
- candidate relevance criteria;
- targeted source/evidence queries.

A selector that amounts to unrestricted organization-wide crawling is invalid unless separately authorized.

## L5.6 Sufficiency for `SPEC_READY`

T2 does not need to prove that no undiscovered repository exists anywhere in the organization.

Change Surface is sufficient for `SPEC_READY` when all of the following are true:

1. all materially supported candidates encountered within the bounded discovery process have a recorded disposition;
2. no blocking candidate remains `UNRESOLVED`;
3. every `CONFIRMED` repository maps to at least one Intention criterion or Spec obligation and has `required_action` equal to `CHANGE`, `VERIFY_ONLY`, or `NO_CHANGE`;
4. every required cross-repository interface/data/config/runtime obligation is represented;
5. accountable ownership is resolved for every `CONFIRMED` repository before T3;
6. exclusions retain enough evidence/rationale to explain why they were not included;
7. discovery gaps that could materially alter the technical contract cause `BLOCKED`, not silent assumption.

## L5.7 T3 scope discovery

If T3 discovers a repository or obligation that is required but absent from the active Spec:

```text
new required scope
    -> record evidence
    -> stop dependent work
    -> T2 re-entry
```

T3 does not self-promote the new repository into the approved Change Surface.

---

# Contract L6 — Lifecycle, Gate, Validity, Invalidation, and Re-entry

## L6.1 Gate versus validity

`gate` records the result achieved when a specific artifact revision was produced.

`validity` records whether that gate claim may still be relied upon against the currently referenced upstream state.

Example:

```yaml
gate: "SPEC_READY"
validity: "STALE"
```

means the Spec revision once satisfied its gate but can no longer authorize T3 against the changed upstream state.

## L6.2 Gate states

| Artifact | Output gate |
| --- | --- |
| Intention | `INTENTION_READY` / `BLOCKED` |
| Spec | `SPEC_READY` / `BLOCKED` |
| Implementation | `CHANGE_SET_READY` / `BLOCKED` |
| Correctness | `PASS` / `FAIL` / `INCONCLUSIVE` |

Preflight is separate:

```text
CONTRACT_READY | NOT_CONTRACT_READY
```

Gate effect is normative:

| Gate | Canonical effect |
| --- | --- |
| `INTENTION_READY` | Permits T2 preflight against this exact active Intention revision |
| `SPEC_READY` | Permits T3 preflight against this exact active Spec revision |
| `CHANGE_SET_READY` | Permits T4 preflight against the exact active ImplementationBundle/candidate set |
| `PASS` | Closes Layer 1 Correctness for the exact pinned lineage and required V&V scope |
| `BLOCKED` | Does not authorize the next canonical transition; follow recorded re-entry/blocker |
| `FAIL` | Does not close Layer 1; follow earliest re-entry |
| `INCONCLUSIVE` | Does not close Layer 1; obtain evidence/capability or follow earliest re-entry |

No Layer 1 gate grants merge, deployment, or release authorization by itself.

## L6.2A Validity derivation

Validity is evaluated against the artifact's pinned upstream revisions and materially influential dependencies. The authoritative lifecycle result is the result of that evaluation; a frontmatter `validity` field is a materialized snapshot for interoperability and MUST be reconciled if it disagrees with the current lineage. A validator/runtime MUST NOT treat a stale cached `validity: ACTIVE` value as overriding a demonstrably changed upstream dependency.

## L6.3 Validity states

```text
ACTIVE
STALE
SUPERSEDED
```

- `ACTIVE`: gate claim is usable against its pinned inputs/current lifecycle.
- `STALE`: gate claim was valid for prior inputs but must be re-evaluated before use against changed dependencies.
- `SUPERSEDED`: a newer canonical revision has replaced this revision for active workflow authority.

## L6.4 Minimum invalidation cascade

```text
Intention revision changes
  -> dependent Spec STALE
  -> dependent Implementation STALE
  -> dependent Correctness STALE

Spec revision changes
  -> dependent Implementation STALE
  -> dependent Correctness STALE

Active candidate implementation/head changes or is superseded
  -> dependent Implementation STALE until re-pinned in a new revision
  -> dependent Correctness STALE

Materially influential Context/Evidence dependency becomes invalid, expired, or superseded
  -> affected claim STALE/BLOCKED/INCONCLUSIVE according to dependency isolation
  -> owning artifact STALE when claim-local isolation cannot be demonstrated
```

A new Skill revision does not automatically invalidate historical artifacts produced by an older Skill. Re-execution is required only when policy, compatibility, risk, or an affected claim requires it.

## L6.5 Claim-local blocking/invalidation

Claim-local handling MAY be used when dependency isolation is demonstrated.

Example:

- a stale operational Context item affects only rollout criterion C-07;
- unrelated criteria MAY continue to be evaluated;
- C-07 is blocked/inconclusive;
- overall gate follows the normal gate rules.

If isolation cannot be demonstrated, invalidation/blocking propagates conservatively.

## L6.6 Earliest re-entry

| Finding | Earliest re-entry |
| --- | --- |
| Human need, authorization, intended use, scope, or success criterion is wrong/changed | T1 |
| Intention remains valid but technical obligation, design, Change Surface, ownership, or V&V plan is wrong/incomplete | T2 |
| Spec remains valid but implementation does not conform | T3 |
| Candidate remains valid but evidence/capability is insufficient | T4 |
| Upstream revision changes | Earliest affected downstream transition |

Re-entry MUST preserve the prior finding/evidence that caused the return; it must not restart blindly.

---

# Contract L7 — Traceability and Correctness Contract

## L7.1 End-to-end traceability

Every independently verifiable criterion MUST support forward and backward navigation:

```text
Human Signal fragment
  -> Intention criterion
  -> Spec requirement/design/task/repository
  -> repo-id:path@candidate-sha
  -> V&V evidence
  -> criterion verdict
```

Transformation provenance MUST additionally support:

```text
output artifact
  -> governing Skill@revision
  -> exact upstream revision(s)
  -> materially influential ResolvedContextRefs
  -> executor/run provenance
```

## L7.2 Stable identifiers

At minimum, Layer 1 requires stable IDs for:

- Intention criteria;
- Spec requirements;
- implementation tasks when referenced across sections/artifacts;
- repositories in Change Surface;
- evidence records when not represented by stable external URIs;
- criterion verdicts.

IDs MUST remain stable across non-semantic edits. A semantic replacement creates a new revision and records supersession as appropriate.

## L7.3 Verification versus validation

T4 MUST report two logically distinct claims:

### Verification

```text
Did the exact candidate conform to the active Spec?
```

Required relationship:

```text
Spec obligation
  <-> Candidate implementation
  <-> Evidence
```

### Validation

```text
Does the exact candidate make the active Intention true for intended use?
```

Required relationship:

```text
Intention criterion
  <-> Observed candidate behavior/outcome
  <-> Evidence
```

Verification success cannot substitute for validation success.

## L7.4 Criterion verdict

Every Intention criterion MUST receive:

```text
PASS
FAIL
INCONCLUSIVE
```

plus:

- evidence refs;
- verification finding where applicable;
- validation finding;
- limitations/unobserved scope;
- earliest re-entry when not `PASS`.

## L7.5 Overall Correctness gate

```text
PASS
= every blocking criterion PASS
  AND every required blocking-criterion V&V scope is observed
```

```text
FAIL
= at least one blocking criterion FAIL
```

```text
INCONCLUSIVE
= no blocking criterion FAIL,
  but at least one blocking criterion cannot be decided
  because required evidence/capability or required V&V scope is insufficient
```

A non-blocking criterion does not change the overall gate. Any different aggregation rule must be established by T1 from an authenticated authorized Human decision; T2-T4 cannot promote or downgrade criterion criticality or invent a different aggregation rule.

## L7.6 No-code result

A feature MAY legitimately require no source change.

A no-code result MUST still provide:

- evidence-backed reason no repository change is required;
- mapping from every relevant criterion/requirement to the no-change rationale;
- T4 validation evidence sufficient to judge the Intention.

“No diff” alone is not evidence of Correctness.

## L7.7 Correctness scope statement

Every `correctness.md` MUST state the observed scope of its verdict.

`PASS` means:

> The exact pinned candidate is independently established as conformant to the active Spec and fit for the active Intention, and the observed scope satisfies every required blocking-criterion V&V obligation.

It does not imply production deployment, rollout completion, operational stability, or release approval unless those are explicitly within the criteria and observed evidence.

---

# Layer 1 Design Approval Checklist

The Layer 1 contract may be called `Contract-ready` only after explicit approval of all items below:

- [x] Four canonical transformations/artifacts and the Human Signal boundary
- [x] Generic `f_skill` contract and root/helper Skill provenance
- [x] ContextRequirement / ResolvedContextRef interface and Context-vs-Evidence boundary
- [x] Criterion criticality/default-blocking rule and shared structured records
- [x] T1-T4 input authority, procedures, side-effect boundaries, and gates
- [x] Feature-specific Change Surface states, current-evidence confirmation, `required_action` semantics, and multi-repository authority boundary
- [x] Appendix bounds and supplemental-evidence rule
- [x] Gate/validity/revision/invalidation/re-entry lifecycle
- [x] T4 minimum independence (distinct owner + distinct evaluation context + no candidate mutation) and required-scope semantics
- [x] End-to-end traceability and Correctness calculation

Final contract review outcome:

```text
Contract review: PASS
Open contract blockers: NONE IDENTIFIED
Herman design approval: APPROVED
```

Current status remains:

```text
Contract-ready: APPROVED
Execution-verified: NOT_CLAIMED
Layer-2 Context Supply: OUT_OF_SCOPE / NOT_STARTED_BY_THIS_SPEC
Implementation/pilot: NOT_AUTHORIZED_BY_THIS_APPROVAL; requires a separate execution/pilot authorization
```

# Layer 1 Canonical Summary

The complete Layer 1 semantic model is:

```text
I = f(H, T1-Skill@r1 ; R1)

S = f(I@ri, T2-Skill@r2 ; R2)

B = f(S@rs, T3-Skill@r3 ; R3)

C = f(I@ri, S@rs, B@rb, T4-Skill@r4 ; R4)
```

where:

```text
H  = authenticated Human Signal
I  = intention.md
S  = spec.md
B  = ImplementationBundle, canonical coordination artifact implementation.md
C  = CorrectnessBundle, canonical artifact correctness.md
Rn = exact Context references resolved under the corresponding Skill contract
```

Evidence gathered during execution is recorded as `EvidenceRef` in the relevant OutputBundle. It is not promoted into the canonical function signature as a fifth workflow input; the governing Skill defines how permitted capabilities obtain and pin that evidence.

The execution plane is orthogonal:

```text
Agent / Squad / Model / Runtime / Tools
              |
              | executes
              v
       Canonical Skill Contract
```

Changing Agent, model, parallelism, retry strategy, or runtime does not change the Layer 1 transformation contract.

The Context Supply plane is also orthogonal:

```text
Layer 2 Context Supply
        |
        | produces/resolves governed Context products
        v
ResolvedContextRefs
        |
        | consumed by
        v
Layer 1 Canonical Skills
```

Layer 2 cannot silently change Layer 1 artifact authority or gates.

---

## L1-IO — layer1_physical_io

- Semantic version: `0.1`
- Approval: `HERM-210; multica-attachment:01a05228-a42d-72fa-b388-558f59430632`
- Compatibility: `L1-SEM@0.2`

### Source: `normative/layer1/io/fdi-layer1-markdown-io-profile-v0.1-approved.md`

SHA-256: `9793619861bf0745914746a2909a195131d318426f74d0eace6caabf34ac4c45`

# FDI Layer 1 — Markdown I/O Profile v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Purpose:** Fix the physical Markdown I/O contract for Layer 1 so an Agent can read and produce canonical artifacts without inventing file structure  
> **Scope:** `intention.md`, `spec.md`, `implementation.md`, `correctness.md`, and three governed appendix profiles  
> **Design only:** No validator, repository layout deployment, Skill implementation, pilot, or execution claim  
> **Current state:** `Markdown-I/O Contract-ready: NOT_CLAIMED`

---

# 0. Core Rule

FDI Layer 1 already defines the semantic transformation:

```text
OutputBundle = f(
    CanonicalInput(s),
    GovernedSkill@revision
    ; ResolvedContextRefs
)
```

This profile fixes the **physical Markdown representation** of each canonical Layer 1 input/output artifact.

The goal is:

> A compliant Agent MUST NOT need to invent headings, record placement, IDs, or machine-readable structure for a canonical Layer 1 artifact.

This profile does not change Layer 1 authority, gate, lifecycle, Change Surface, or Correctness semantics.

Execution-time Evidence and tool/capability use remain governed by the Skill and are **not additional canonical function inputs**. The physical artifact records the resulting `EvidenceRef`/provenance after observation.

---

# 1. Physical Markdown Rules

## 1.1 Required file structure

Every canonical Layer 1 Markdown file MUST contain:

```text
YAML frontmatter
        +
fixed ordered H1/H2 section structure
        +
structured YAML records in declared sections
        +
bounded human-readable narrative where permitted
```

The frontmatter and structured records are the machine-interoperable contract.

Narrative text explains rationale, interpretation, and bounded detail but MUST NOT contradict structured records.

If narrative and structured content conflict, the producing transition is non-compliant and the artifact MUST NOT claim a ready/pass gate.

## 1.2 Required sections are never omitted

Every section marked `REQUIRED` MUST be present even when empty.

Use one of:

```text
NONE
```

or:

```yaml
status: "NOT_APPLICABLE"
reason: "<why this section does not apply>"
```

Do not omit the heading because an Agent thinks it is irrelevant.

## 1.3 Optional sections

A section marked `CONDITIONAL` is required when its trigger is true. When the trigger is false, it MAY be omitted unless the owning core template explicitly requires an applicability record.

## 1.4 Stable IDs

IDs MUST be stable within one feature lineage.

Recommended prefixes:

```text
Human Signal fragment HSF-001
Criterion              C-001
Requirement            R-001
Design invariant       D-001
Task                   T-001
V&V method             V-001
Change Surface         CS-001
Context reference      CTX-001
Evidence               E-001
Candidate reference    CR-001
Deviation              DEV-001
Appendix               A-001
Check                  CHK-001
Criterion verdict      uses criterion_id
```

Renumbering existing IDs solely for presentation is prohibited because it breaks traceability.

## 1.5 Structured record rule

When this profile defines a YAML record schema, the artifact MUST expose semantically equivalent machine-readable fields.

The canonical physical profile uses fenced YAML blocks.

Example:

```yaml
criteria:
  - criterion_id: "C-001"
    statement: "..."
    blocking: true
    success_measure: "..."
    threshold_or_acceptance: "..."
    human_signal_refs:
      - "signal://..."
```

Free-form prose MAY follow the structured block for explanation.

## 1.6 References

Canonical references SHOULD use stable IDs and immutable revisions/as-of states.

Do not embed raw secrets, copied source trees, or mutable-only evidence.

The following remain distinct:

```text
ResolvedContextRef
    informs/constrains transformation

EvidenceRef
    establishes a specific claim/finding/verdict
```

## 1.7 Common artifact frontmatter

All four canonical Markdown files MUST begin with:

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<stable-feature-id>"
artifact: "intention|spec|implementation|correctness"
revision: <positive-integer>

produced_by:
  skill: "<canonical-skill-id>"
  skill_revision: "<immutable-version-or-revision>"

canonical_owner: "<stable-accountable-role-or-owner-id>"

upstream: {}

gate: "<artifact-specific-gate>"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<stable-executor-id-or-null>"
  execution_id: "<run-id-or-null>"
---
```

Artifact-specific profiles below define the required `upstream` fields.

---

# 2. `intention.md` Physical Contract

## 2.1 Function

```text
intention.md
=
f(
  AuthenticatedHumanSignal,
  T1-Intention-Skill@revision
  ;
  ResolvedContextRefs
)
```

## 2.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "intention"
revision: <positive-integer>

produced_by:
  skill: "T1-Intention-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T1-owner>"

upstream:
  human_signal_ids:
    - "<stable-signal-id>"

gate: "INTENTION_READY|BLOCKED"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<executor>"
  execution_id: "<run-id>"
---
```

## 2.3 Exact body structure

```markdown
# Intention

## 1. Human Signal

## 2. Stakeholders and Intended Users

## 3. Desired Outcome

## 4. Intended-Use Scenarios

## 5. Scope and Non-Goals

## 6. Constraints and Assumptions

## 7. Success Criteria

## 8. Product, System, and Repository Seeds

## 9. Context Used

## 10. Open Questions and Conflicts

## 11. Gate Record
```

All eleven H2 sections are `REQUIRED`.

## 2.4 Section contracts

### `## 1. Human Signal`

MUST contain:

```yaml
human_signals:
  - signal_id: "<stable-signal-id>"
    source_ref: "<governed-source-ref>"
    source_identity: "<requester/authority>"
    captured_at: "<timestamp>"
    authentication_state: "VERIFIED"
    authorization_state: "AUTHORIZED|NOT_AUTHORIZED|UNCLEAR"
    content_ref_or_digest: "<immutable-ref-or-digest>"
    summary: "<safe-faithful-summary>"
    fragments:
      - fragment_id: "HSF-001"
        content_locator: "<stable-location-within-signal-or-ref>"
        summary: "<faithful-fragment-summary>"
```

The summary MUST preserve the expressed need and MUST NOT introduce implementation design.

### `## 2. Stakeholders and Intended Users`

```yaml
stakeholders:
  - stakeholder_id: "<stable-local-id>"
    role: "<role>"
    relationship: "REQUESTER|APPROVER|USER|OWNER|AFFECTED|OTHER"

intended_users:
  - user_group_id: "<stable-local-id>"
    description: "<group>"
```

### `## 3. Desired Outcome`

```yaml
desired_outcome:
  statement: "<what must become true>"
  business_or_user_value: "<why it matters>"
```

### `## 4. Intended-Use Scenarios`

```yaml
intended_use_scenarios:
  - scenario_id: "S-001"
    actor: "<actor>"
    situation: "<situation>"
    expected_outcome: "<observable desired result>"
```

### `## 5. Scope and Non-Goals`

```yaml
scope:
  in_scope:
    - "<bounded item>"
  non_goals:
    - "<explicit exclusion>"
```

### `## 6. Constraints and Assumptions`

```yaml
constraints:
  - constraint_id: "CON-001"
    statement: "<constraint>"
    source: "HUMAN_SIGNAL|CONTEXT"
    ref: "<source-ref>"

assumptions:
  - assumption_id: "ASM-001"
    statement: "<assumption>"
    validation_needed: true
```

### `## 7. Success Criteria`

```yaml
criteria:
  - criterion_id: "C-001"
    statement: "<measurable desired outcome>"
    blocking: true
    success_measure: "<observable measure>"
    threshold_or_acceptance: "<pass condition>"
    human_signal_refs:
      - "HSF-001"
```

Rules:

- Every authorized requested outcome MUST map to one or more criteria.
- `blocking` defaults to `true`.
- Only T1 may set `blocking: false`, and only when Human authorization supports it.

### `## 8. Product, System, and Repository Seeds`

```yaml
impact_seeds:
  products:
    - "<product-ref>"
  systems:
    - "<system-ref>"
  repositories:
    - "<repo-ref-or-known-name>"
  completeness: "NON_EXHAUSTIVE"
```

Repository seeds MUST be explicitly marked non-exhaustive.

### `## 9. Context Used`

```yaml
resolved_context_refs:
  - context_ref_id: "CTX-001"
    requirement_id: "<T1-context-requirement-id>"
    ref: "<stable-context-ref>"
    revision_or_as_of: "<revision/time>"
    selected_for: "<purpose/claim>"
    authority_dimension: "<dimension>"
    trust_state: "<state>"
    applicability: "<scope>"
    freshness: "<state>"
    evidence_backlink: "<source/evidence-ref-or-null>"

context_exclusions:
  - requirement_id: "<context-requirement-id>"
    candidate_ref: "<context-candidate-ref>"
    reason: "<why it was not selected>"
```

If no Context was materially influential or excluded:

```yaml
resolved_context_refs: []
context_exclusions: []
```

### `## 10. Open Questions and Conflicts`

```yaml
open_items:
  - item_id: "Q-001"
    type: "QUESTION|AUTHORITY_CONFLICT|CONTEXT_GAP|AMBIGUITY"
    statement: "<issue>"
    blocking: true
    owner: "<resolution-owner>"
```

### `## 11. Gate Record`

```yaml
gate_record:
  gate: "INTENTION_READY|BLOCKED"
  evaluated_against:
    human_signal_ids:
      - "<signal-id>"
  blocking_items:
    - "<Q-id>"
  rationale: "<bounded gate rationale>"
```

---

# 3. `spec.md` Physical Contract

## 3.1 Function

```text
SpecBundle
=
f(
  intention.md@exact-active-revision,
  T2-Delivery-Spec-Skill@revision
  ;
  ResolvedContextRefs
)

core(SpecBundle) = spec.md
```

## 3.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "spec"
revision: <positive-integer>

produced_by:
  skill: "T2-Delivery-Spec-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T2-owner>"

upstream:
  intention_revision: <exact-active-revision>

gate: "SPEC_READY|BLOCKED"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<executor>"
  execution_id: "<run-id>"
---
```

## 3.3 Exact body structure

```markdown
# Delivery Spec

## 1. Upstream Intention

## 2. Criterion-to-Requirement Mapping

## 3. Requirements

## 4. Design and Invariants

## 5. Current-State Findings

## 6. Change Surface

## 7. Interface, Data, Security, and Operational Obligations

## 8. Implementation Tasks and Ownership

## 9. Verification and Validation Plan

## 10. Appendix Registry

## 11. Context Used and Selector Proof

## 12. Risks, Gaps, and Deviations

## 13. Gate Record
```

All thirteen H2 sections are `REQUIRED`.

## 3.4 Section contracts

### `## 1. Upstream Intention`

```yaml
upstream_intention:
  feature_id: "<feature-id>"
  revision: <exact-revision>
  gate: "INTENTION_READY"
  validity_at_execution: "ACTIVE"
  criterion_ids:
    - "C-001"
```

### `## 2. Criterion-to-Requirement Mapping`

```yaml
criterion_requirement_map:
  - criterion_id: "C-001"
    requirement_ids:
      - "R-001"
    rationale: "<required when requirement_ids is empty>"
```

Every Intention criterion MUST appear exactly once in this mapping section. A non-blocking criterion may map to an empty `requirement_ids` list only when the active Intention and V&V disposition make that treatment valid; the rationale is then mandatory.

### `## 3. Requirements`

```yaml
requirements:
  - requirement_id: "R-001"
    criterion_ids:
      - "C-001"
    statement: "<technical obligation>"
    owner: "<accountable owner>"
    repo_ids:
      - "<repo-id>"
    vv_method_ids:
      - "V-001"
```

### `## 4. Design and Invariants`

```yaml
design:
  summary: "<implementation-neutral-enough technical design>"
  invariants:
    - invariant_id: "D-001"
      statement: "<must remain true>"
      requirement_ids:
        - "R-001"
```

Narrative diagrams/rationale MAY follow, but obligations MUST remain traceable through IDs.

### `## 5. Current-State Findings`

All T2 `EvidenceRef` records materially used by `spec.md`, including Change Surface confirmation/exclusion evidence, are defined in this section and referenced elsewhere by `evidence_id`.

```yaml
evidence_refs:
  - evidence_id: "E-001"
    ref: "<immutable-artifact/source/test-result-reference>"
    revision_or_as_of: "<revision/time>"
    method: "<how the observation was obtained>"
    environment: "<environment-or-N/A>"
    integrity: "<digest/signature/governed-result-ref when applicable>"
    claim_ids:
      - "STATE-001"
      - "CS-001"

current_state_findings:
  - finding_id: "STATE-001"
    statement: "<current-state claim>"
    evidence_refs:
      - "E-001"
    context_refs:
      - "CTX-001"
    limitations: []
```

Current behavior/state claims used materially by T2 MUST have an `EvidenceRef`; Context alone is insufficient when current applicability is material. Any `evidence_id` referenced in §6 or §12 MUST resolve to an `EvidenceRef` defined here or to a governed Evidence record explicitly reachable from this artifact.

### `## 6. Change Surface`

```yaml
change_surface:
  discovery_scope:
    products: []
    systems: []
    relation_types: []
    traversal_budget: "<bounded-selector-summary>"
    exclusions: []

  findings:
    - finding_id: "CS-001"
      repo_id: "<stable-repository-id>"
      status: "CANDIDATE|CONFIRMED|EXCLUDED|UNRESOLVED"
      relevance: "<why this repo may/must matter>"
      relation_types:
        - "api"
      criterion_ids:
        - "C-001"
      requirement_ids:
        - "R-001"
      context_refs:
        - "CTX-001"
      evidence_refs:
        - "E-002"
      owner: "<resolved-owner-or-null>"
      required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE|NOT_APPLICABLE|UNDECIDED"
      planned_change: "<expected change/verification/no-change rationale>"
      blocking: true
```

Rules from Layer 1 L5 are normative:

- `CANDIDATE` / `UNRESOLVED` → `UNDECIDED`
- `CONFIRMED` → `CHANGE | VERIFY_ONLY | NO_CHANGE`
- `EXCLUDED` → `NOT_APPLICABLE`
- only current feature-specific `EvidenceRef` may support `CONFIRMED`

### `## 7. Interface, Data, Security, and Operational Obligations`

This section MUST contain an applicability record:

```yaml
cross_cutting_obligations:
  interfaces:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  data:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  configuration:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  schema:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  security:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  operations:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []

  rollout_rollback:
    applicability: "APPLICABLE|NOT_APPLICABLE"
    requirement_ids: []
    details: []
```

### `## 8. Implementation Tasks and Ownership`

```yaml
tasks:
  - task_id: "T-001"
    requirement_ids:
      - "R-001"
    repo_ids:
      - "<repo-id>"
    owner: "<accountable owner>"
    disposition: "PLANNED|NO_CHANGE|BLOCKED"
```

At `SPEC_READY`, implementation work is normally `PLANNED`; an explicit no-change obligation may use `NO_CHANGE`. `IMPLEMENTED` is not a valid T2 disposition. A `BLOCKED` task prevents `SPEC_READY` when it affects a blocking obligation.

### `## 9. Verification and Validation Plan`

```yaml
vv_dispositions:
  - criterion_id: "C-001"
    evaluation: "REQUIRED|OBSERVE_IF_AVAILABLE"
    method_id: "V-001|null"
    method: "<non-tautological-method-or-N/A>"
    evidence_expectation: "<required-evidence-or-observation-policy>"
    threshold_or_acceptance: "<pass-condition-or-N/A>"
    required_scope: "<scope-that-must-be-observed-or-N/A>"
    independence: "<required-independence-or-N/A>"
```

Every blocking criterion MUST use `REQUIRED` and define a non-tautological method, evidence expectation, threshold/acceptance, and required scope. A non-blocking criterion may use `OBSERVE_IF_AVAILABLE` only when authorized by the active Intention.

### `## 10. Appendix Registry`

```yaml
appendices:
  - appendix_id: "A-001"
    type: "SPEC"
    trigger: "<why separate detail is required>"
    status: "ACTIVE|SUPERSEDED"
    path: "appendices/spec/A-001.md"
    related_ids:
      - "R-001"
    backlink:
      owner_artifact: "spec"
      owner_revision: <this-spec-revision>
```

If no appendices:

```yaml
appendices: []
```

### `## 11. Context Used and Selector Proof`

```yaml
resolved_context_refs:
  - context_ref_id: "CTX-001"
    requirement_id: "<context-requirement-id>"
    ref: "<stable-context-ref>"
    revision_or_as_of: "<revision/time>"
    selected_for: "<purpose/claim>"
    authority_dimension: "<dimension>"
    trust_state: "<state>"
    applicability: "<scope>"
    freshness: "<state>"
    evidence_backlink: "<source/evidence-ref-or-null>"

context_exclusions:
  - requirement_id: "<context-requirement-id>"
    candidate_ref: "<context-candidate-ref>"
    reason: "<why it was excluded>"

selector_proof:
  - selector_id: "<selector-id>"
    purpose: "<purpose>"
    bounded_by: "<scope/budget/rule>"
    excluded_by_rule: []
```

### `## 12. Risks, Gaps, and Deviations`

```yaml
risks_gaps_deviations:
  - item_id: "RGD-001"
    type: "RISK|CONTEXT_GAP|EVIDENCE_GAP|DEVIATION|OWNERSHIP_GAP|DESIGN_GAP"
    statement: "<issue>"
    affected_ids:
      - "R-001"
    blocking: true
    disposition: "RESOLVED|ACCEPTED|BLOCKING|REQUIRES_AUTHORIZATION"
    owner: "<owner>"
```

### `## 13. Gate Record`

```yaml
gate_record:
  gate: "SPEC_READY|BLOCKED"
  intention_revision: <revision>
  blocking_items: []
  unresolved_change_surface_findings: []
  rationale: "<bounded gate rationale>"
```

---

# 4. `implementation.md` Physical Contract

## 4.1 Function

```text
ImplementationBundle
=
f(
  spec.md@exact-active-revision,
  T3-Implementation-Skill@revision
  ;
  ResolvedContextRefs
)
```

## 4.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "implementation"
revision: <positive-integer>

produced_by:
  skill: "T3-Implementation-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T3-owner>"

upstream:
  spec_revision: <exact-active-revision>

gate: "CHANGE_SET_READY|BLOCKED"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<executor>"
  execution_id: "<run-id>"
---
```

## 4.3 Exact body structure

```markdown
# Implementation

## 1. Upstream Spec

## 2. Candidate Summary

## 3. Repository Implementation Dispositions

## 4. Candidate References

## 5. Changed Paths and Migrations

## 6. Requirement, Design, and Task Mapping

## 7. Checks and Observed Results

## 8. Deviations from Spec

## 9. Appendix Registry

## 10. Context Used

## 11. Execution Provenance

## 12. Known Gaps and T4 Handoff

## 13. Gate Record
```

All thirteen H2 sections are `REQUIRED`.

## 4.4 Section contracts

### `## 1. Upstream Spec`

```yaml
upstream_spec:
  feature_id: "<feature-id>"
  revision: <exact-revision>
  gate: "SPEC_READY"
  validity_at_execution: "ACTIVE"
```

### `## 2. Candidate Summary`

```yaml
candidate_summary:
  repositories_confirmed: <integer>
  repositories_change: <integer>
  repositories_verify_only: <integer>
  repositories_no_change: <integer>
  reviewable_candidate_count: <integer>
  blocking_repository_count: <integer>
  summary: "<bounded summary>"
```

### `## 3. Repository Implementation Dispositions`

```yaml
repository_dispositions:
  - repo_id: "<repo-id>"
    required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE"
    disposition: "READY|BLOCKED|SUPERSEDED"
    task_ids:
      - "T-001"
    candidate_ref: "CR-001|null"
    evidence_refs:
      - "E-001"
    notes: "<bounded-disposition-summary>"
```

Every `CONFIRMED` repository from the active Spec MUST have exactly one active disposition.

### `## 4. Candidate References`

`candidate_ref_id` is the physical stable identifier used to instantiate and cross-reference the Layer 1 `candidate_ref` record.

```yaml
candidate_refs:
  - candidate_ref_id: "CR-001"
    repo_id: "<repo-id>"
    base_revision: "<immutable-base>"
    head_revision: "<immutable-head>"
    location: "<branch/PR/commit/candidate-ref>"
    status: "REVIEWABLE|NOT_READY|SUPERSEDED"
    task_ids:
      - "T-001"
```

`CHANGE` requires a candidate ref. `VERIFY_ONLY` and `NO_CHANGE` MUST NOT fabricate one.

### `## 5. Changed Paths and Migrations`

```yaml
changed_paths:
  - repo_id: "<repo-id>"
    candidate_ref_id: "CR-001"
    paths:
      - "<path>"
    change_types:
      - "CODE|CONFIG|SCHEMA|TEST|DOC|MIGRATION|OTHER"

migrations:
  - migration_id: "MIG-001"
    repo_id: "<repo-id>"
    description: "<migration>"
    rollback_ref: "<rollback-plan-ref-or-null>"
```

If no migrations:

```yaml
migrations: []
```

### `## 6. Requirement, Design, and Task Mapping`

```yaml
implementation_mappings:
  - requirement_id: "R-001"
    invariant_ids:
      - "D-001"
    task_ids:
      - "T-001"
    repo_ids:
      - "<repo-id>"
    candidate_ref_ids:
      - "CR-001"
    changed_path_refs:
      - "<repo-id>:<path>"
```

### `## 7. Checks and Observed Results`

All T3 `EvidenceRef` records referenced by repository dispositions, checks, deviations, or the T4 handoff are defined here.

```yaml
evidence_refs:
  - evidence_id: "E-001"
    ref: "<immutable-artifact/source/test-result-reference>"
    revision_or_as_of: "<revision/time>"
    method: "<how the observation was obtained>"
    environment: "<environment-or-N/A>"
    integrity: "<digest/signature/governed-result-ref when applicable>"
    claim_ids:
      - "CHK-001"

checks:
  - check_id: "CHK-001"
    type: "BUILD|TEST|STATIC|MIGRATION|CONFIG|OTHER"
    repo_id: "<repo-id>"
    candidate_ref_id: "CR-001|null"
    method: "<how check was run>"
    result: "PASS|FAIL|NOT_RUN"
    evidence_refs:
      - "E-001"
```

T3 checks are implementation observations, not T4 Correctness verdicts. Every `evidence_id` used elsewhere in `implementation.md` MUST resolve here or to a governed Evidence record explicitly reachable from this artifact.

### `## 8. Deviations from Spec`

```yaml
deviations:
  - deviation_id: "DEV-001"
    statement: "<deviation>"
    affected_ids:
      - "R-001"
    blocking: true
    classification: "IMPLEMENTATION_DEFECT|SPEC_CONFLICT|NEW_SCOPE|OTHER"
    proposed_disposition: "FIX_T3|REENTER_T2|AUTHORIZED_EXCEPTION|BLOCK"
    evidence_refs: []
```

### `## 9. Appendix Registry`

```yaml
appendices:
  - appendix_id: "A-101"
    type: "IMPLEMENTATION_REPOSITORY"
    trigger: "<why repository-local detail is separate>"
    status: "ACTIVE|SUPERSEDED"
    path: "appendices/implementation/<repo-id>.md"
    repo_id: "<repo-id>"
```

If none:

```yaml
appendices: []
```

### `## 10. Context Used`

Use the exact `resolved_context_refs` item schema from `spec.md` §11, including `requirement_id`, immutable/as-of reference, authority dimension, trust, applicability, freshness, and `evidence_backlink`. If no Context was materially influential, emit:

```yaml
resolved_context_refs: []
```

### `## 11. Execution Provenance`

```yaml
execution_provenance:
  root_skill:
    id: "T3-Implementation-Skill"
    revision: "<revision>"

  materially_influential_helpers:
    - kind: "SKILL|AGENT|REVIEWER|WORKER"
      id: "<stable-id>"
      revision: "<revision-or-model/config-ref>"
      execution_id: "<run-id>"
      contribution: "<material contribution>"

  capability_refs:
    - "<permitted-capability-ref>"
```

### `## 12. Known Gaps and T4 Handoff`

```yaml
t4_handoff:
  known_gaps:
    - gap_id: "GAP-001"
      statement: "<gap>"
      blocking_for_t4: true

  exact_candidate_refs:
    - "CR-001"

  planned_vv_method_ids:
    - "V-001"

  evidence_available:
    - "E-001"
```

### `## 13. Gate Record`

```yaml
gate_record:
  gate: "CHANGE_SET_READY|BLOCKED"
  spec_revision: <revision>
  blocking_repository_ids: []
  blocking_deviation_ids: []
  rationale: "<bounded gate rationale>"
```

---

# 5. `correctness.md` Physical Contract

## 5.1 Function

```text
CorrectnessBundle
=
f(
  intention.md@exact-active-revision,
  spec.md@exact-active-revision,
  ImplementationBundle@exact-candidate-revisions,
  T4-Correctness-Skill@revision
  ;
  ResolvedContextRefs
)
```

## 5.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "correctness"
revision: <positive-integer>

produced_by:
  skill: "T4-Correctness-Skill"
  skill_revision: "<revision>"

canonical_owner: "<T4-owner-distinct-from-T3-owner>"

upstream:
  intention_revision: <exact-active-revision>
  spec_revision: <exact-active-revision>
  implementation_revision: <exact-active-revision>
  candidate_refs:
    - "CR-001"

gate: "PASS|FAIL|INCONCLUSIVE"
validity: "ACTIVE|STALE|SUPERSEDED"  # lifecycle snapshot; current lineage remains authoritative
supersedes: <prior-revision-or-null>

executor:
  role_or_agent: "<independent-evaluator>"
  execution_id: "<distinct-evaluation-run-id>"
---
```

## 5.3 Exact body structure

```markdown
# Correctness

## 1. Exact Inputs and Independence

## 2. Evidence Inventory and Integrity

## 3. Verification Findings

## 4. Validation Findings

## 5. Criterion Verdicts

## 6. Coverage

## 7. Deviations, Gaps, Limitations, and Unobserved Scope

## 8. Release and Production Observation

## 9. Earliest Re-entry

## 10. Context Used

## 11. Execution Provenance

## 12. Overall Verdict and Gate Record
```

All twelve H2 sections are `REQUIRED`.

## 5.4 Section contracts

### `## 1. Exact Inputs and Independence`

```yaml
exact_inputs:
  intention_revision: <revision>
  spec_revision: <revision>
  implementation_revision: <revision>
  candidate_refs:
    - candidate_ref_id: "CR-001"
      repo_id: "<repo-id>"
      head_revision: "<immutable-head>"

independence:
  t3_canonical_owner: "<T3-owner>"
  t4_canonical_owner: "<T4-owner>"
  distinct_owner: true
  t3_execution_id: "<T3-run>"
  t4_execution_id: "<T4-run>"
  distinct_evaluation_context: true
  candidate_mutation_authority_during_evaluation: false
```

### `## 2. Evidence Inventory and Integrity`

```yaml
evidence_refs:
  - evidence_id: "E-101"
    ref: "<immutable-evidence-ref>"
    revision_or_as_of: "<revision/time>"
    method: "<observation method>"
    environment: "<environment-or-N/A>"
    integrity: "<digest/signature/governed-ref when applicable>"
    claim_ids:
      - "C-001"

evidence_appendix_registry:
  - appendix_id: "A-201"
    evidence_id: "E-101"
    trigger: "<why a governed evidence file is needed>"
    status: "ACTIVE|SUPERSEDED"
    path: "appendices/evidence/E-101.md"
    backlink:
      owner_artifact: "correctness"
      owner_revision: <this-correctness-revision>
```

### `## 3. Verification Findings`

```yaml
verification_findings:
  - finding_id: "VF-001"
    requirement_id: "R-001"
    result: "PASS|FAIL|INCONCLUSIVE"
    statement: "<Spec conformance finding>"
    evidence_refs:
      - "E-101"
    limitations: []
```

### `## 4. Validation Findings`

```yaml
validation_findings:
  - finding_id: "VAL-001"
    criterion_id: "C-001"
    result: "PASS|FAIL|INCONCLUSIVE"
    intended_use_scenario_ids:
      - "S-001"
    statement: "<fitness-for-Intention finding>"
    evidence_refs:
      - "E-101"
    limitations: []
```

### `## 5. Criterion Verdicts`

```yaml
criterion_verdicts:
  - criterion_id: "C-001"
    blocking: true
    evaluation: "REQUIRED"
    verdict: "PASS|FAIL|INCONCLUSIVE"
    verification_finding: "<verification-summary-or-N/A>"
    validation_finding: "<validation-summary>"
    verification_finding_refs:
      - "VF-001"
    validation_finding_refs:
      - "VAL-001"
    evidence_refs:
      - "E-101"
    limitations: []
    earliest_reentry: "T1|T2|T3|T4|NONE"
```

### `## 6. Coverage`

```yaml
coverage:
  criteria:
    required: ["C-001"]
    observed: ["C-001"]
    missing: []

  requirements:
    required: ["R-001"]
    observed: ["R-001"]
    missing: []

  design_invariants:
    required: ["D-001"]
    observed: ["D-001"]
    missing: []

  tasks:
    required: ["T-001"]
    observed: ["T-001"]
    missing: []

  repositories:
    required: ["<repo-id>"]
    observed: ["<repo-id>"]
    missing: []

  vv_scope:
    - criterion_id: "C-001"
      required_scope: "<from Spec>"
      observed_scope: "<actual>"
      scope_satisfied: true
```

### `## 7. Deviations, Gaps, Limitations, and Unobserved Scope`

```yaml
limitations:
  - limitation_id: "LIM-001"
    type: "EVIDENCE_GAP|SCOPE_GAP|ENVIRONMENT_LIMITATION|DEVIATION|OTHER"
    statement: "<limitation>"
    affected_ids:
      - "C-001"
    blocking: true
```

If none:

```yaml
limitations: []
```

### `## 8. Release and Production Observation`

```yaml
release_observation:
  state: "OBSERVED|NOT_OBSERVED"
  details: "<bounded observation or N/A>"
  evidence_refs: []
```

`NOT_OBSERVED` does not prevent PASS unless release/production observation is an explicit blocking criterion/V&V obligation.

### `## 9. Earliest Re-entry`

```yaml
reentry:
  transition: "T1|T2|T3|T4|NONE"
  owner: "<owner-or-null>"
  cause_ids:
    - "<finding/criterion/limitation-id>"
  required_next_action: "<bounded action>"
```

### `## 10. Context Used`

Use the exact `resolved_context_refs` item schema from `spec.md` §11, including `requirement_id`, immutable/as-of reference, authority dimension, trust, applicability, freshness, and `evidence_backlink`. If no Context was materially influential, emit:

```yaml
resolved_context_refs: []
```

### `## 11. Execution Provenance`

```yaml
execution_provenance:
  root_skill:
    id: "T4-Correctness-Skill"
    revision: "<revision>"

  materially_influential_helpers:
    - kind: "SKILL|AGENT|REVIEWER"
      id: "<id>"
      revision: "<revision/config>"
      execution_id: "<run-id>"
      contribution: "<material contribution>"

  capability_refs:
    - "<capability-ref>"
```

### `## 12. Overall Verdict and Gate Record`

```yaml
overall_verdict:
  gate: "PASS|FAIL|INCONCLUSIVE"
  blocking_criteria:
    total: <integer>
    pass: <integer>
    fail: <integer>
    inconclusive: <integer>
  required_scope_satisfied: true
  rationale: "<bounded verdict rationale>"

gate_record:
  gate: "PASS|FAIL|INCONCLUSIVE"
  exact_lineage:
    intention_revision: <revision>
    spec_revision: <revision>
    implementation_revision: <revision>
    candidate_refs:
      - "CR-001"
```

---

# 6. Spec Appendix Physical Contract

## 6.1 Path pattern

```text
appendices/spec/{appendix-id}.md
```

## 6.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "spec_appendix"
appendix_id: "A-001"
appendix_type: "SPEC"

owner_artifact:
  artifact: "spec"
  revision: <exact-owning-spec-revision>

status: "ACTIVE|SUPERSEDED"
---
```

## 6.3 Exact body structure

```markdown
# Spec Appendix — {appendix-id}

## 1. Purpose and Trigger

## 2. Scope

## 3. Related Canonical IDs

## 4. Detailed Technical Content

## 5. Context and Evidence References

## 6. Risks, Gaps, and Limitations

## 7. Backlink
```

### Required records

```yaml
purpose:
  trigger: "<registry trigger>"
  statement: "<why detail is separated>"

scope:
  included: []
  excluded: []

related_ids:
  criteria: []
  requirements: []
  invariants: []
  repositories: []
  tasks: []

references:
  context_refs: []
  evidence_refs: []

backlink:
  owner_artifact: "spec"
  owner_revision: <revision>
  registry_appendix_id: "A-001"
```

The appendix MUST NOT introduce an unregistered requirement, repository, criterion, or V&V obligation.

---

# 7. Implementation Repository Appendix Physical Contract

## 7.1 Path pattern

```text
appendices/implementation/{repo-id}.md
```

## 7.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "implementation_repository_appendix"
appendix_id: "A-101"
appendix_type: "IMPLEMENTATION_REPOSITORY"

repo_id: "<confirmed-repo-id>"

owner_artifact:
  artifact: "implementation"
  revision: <exact-owning-implementation-revision>

status: "ACTIVE|SUPERSEDED"
---
```

## 7.3 Exact body structure

```markdown
# Implementation Appendix — {repo-id}

## 1. Repository Disposition

## 2. Tasks

## 3. Candidate

## 4. Changed Paths and Migrations

## 5. Checks and Evidence

## 6. Deviations and Gaps

## 7. Backlink
```

### Required records

```yaml
repository_disposition:
  repo_id: "<repo-id>"
  required_action: "CHANGE|VERIFY_ONLY|NO_CHANGE"
  disposition: "READY|BLOCKED|SUPERSEDED"
  task_ids: []
  candidate_ref: "<CR-id-or-null>"
  evidence_refs: []

tasks: []

candidate:
  applicability: "APPLICABLE|NOT_APPLICABLE"
  candidate_ref_id: "<CR-id-or-null>"

changed_paths: []
migrations: []
checks: []
deviations: []
gaps: []

backlink:
  owner_artifact: "implementation"
  owner_revision: <revision>
  registry_appendix_id: "A-101"
```

For `CHANGE`, candidate applicability MUST be `APPLICABLE` and `candidate_ref_id` MUST resolve to the owning `implementation.md`. For `VERIFY_ONLY` / `NO_CHANGE`, candidate applicability MUST be `NOT_APPLICABLE`.

---

# 8. Evidence Appendix Physical Contract

## 8.1 Path pattern

```text
appendices/evidence/{evidence-id}.md
```

## 8.2 Frontmatter

```yaml
---
fdi_version: "0.2"
profile: "layer1-markdown-io-v0.1"

feature_id: "<feature-id>"
artifact: "evidence_appendix"
appendix_id: "A-201"
appendix_type: "EVIDENCE"
evidence_id: "E-101"

owner_artifact:
  artifact: "correctness"
  revision: <exact-owning-correctness-revision>

status: "ACTIVE|SUPERSEDED"
---
```

## 8.3 Exact body structure

```markdown
# Evidence Appendix — {evidence-id}

## 1. Evidence Identity

## 2. Claim Mapping

## 3. Method and Environment

## 4. Observation

## 5. Integrity and Provenance

## 6. Limitations

## 7. Backlink
```

### Required records

```yaml
evidence_identity:
  evidence_id: "E-101"
  ref: "<immutable-evidence-ref>"
  revision_or_as_of: "<revision/time>"

claim_mapping:
  criterion_ids: []
  requirement_ids: []
  finding_ids: []

method_environment:
  method: "<method>"
  environment: "<environment-or-N/A>"

observation:
  statement: "<what was observed>"
  result: "PASS|FAIL|INCONCLUSIVE|OBSERVATION_ONLY"

integrity_provenance:
  integrity: "<digest/signature/governed-ref>"
  producer: "<producer/tool/system>"
  captured_at: "<timestamp>"

limitations: []

backlink:
  owner_artifact: "correctness"
  owner_revision: <revision>
  registry_appendix_id: "A-201"
```

An Evidence appendix records evidence; it MUST be registered in the owning `correctness.md` §2 `evidence_appendix_registry`, and it MUST NOT independently calculate the overall Correctness gate.

---

# 8.4 Cross-file Record Reuse Invariant

The physical profile MUST NOT redefine a Layer 1 shared structured record incompatibly.

The following records reuse the approved Layer 1 semantics:

```text
criterion
requirement
vv_disposition
task
candidate_ref
repository_disposition
EvidenceRef
criterion_verdict
ResolvedContextRef
```

A physical-only identifier such as `candidate_ref_id` or `context_ref_id` MAY be added solely to make cross-references addressable. Such an identifier does not change the semantic authority of the underlying record.

Every referenced `evidence_id`, `candidate_ref_id`, `appendix_id`, criterion ID, requirement ID, invariant ID, and task ID MUST resolve within the active OutputBundle or through an explicitly governed immutable reference.


# 9. Skill Read/Write Contracts

This section fixes what each canonical Skill MUST read and what it MUST produce physically.

## 9.1 T1

```text
AuthenticatedHumanSignal
        +
Resolved Context
        |
        v
T1 procedure
        |
        v
intention.md
```

| T1 reads | T1 uses it for | `intention.md` output |
| --- | --- | --- |
| Human Signal envelope/content | expressed need + authorization | §1 Human Signal |
| Human content | users/stakeholders | §2 Stakeholders |
| Human content | desired result | §3 Desired Outcome |
| Human content | intended use | §4 Intended-Use Scenarios |
| Human content + applicable constraints | boundary | §5 Scope and Non-Goals |
| Human content + Context | constraints/assumptions | §6 Constraints and Assumptions |
| authorized outcomes | measurable acceptance | §7 Success Criteria |
| product/system hints + Context | navigation seeds only | §8 Seeds |
| resolved Context | provenance | §9 Context Used |
| unresolved meaning/authority | blockers | §10 Open Questions |
| all above | gate calculation | §11 Gate Record |

## 9.2 T2

```text
intention.md
        +
Resolved Context
        |
        v
T2 procedure
        |
        +--> gathers/pins current Evidence during execution
        |
        v
spec.md + Spec appendices*
```

| T2 reads | T2 procedure | `spec.md` output |
| --- | --- | --- |
| Intention §7 Criteria | create technical obligations | §2 Mapping + §3 Requirements |
| Intention §3–§6 | preserve outcome/bounds | §3–§4 |
| Intention §8 Seeds | initialize discovery only | §6 Change Surface |
| Context refs | select constraints/navigation | §5, §6, §7, §11 |
| current Evidence | establish current applicability | §5 Current-State + §6 CONFIRMED/EXCLUDED |
| criteria + requirements | create work | §8 Tasks |
| criteria | design V&V | §9 V&V Plan |
| complex bounded design detail | allocate appendix | §10 Registry |
| all unresolved findings | classify/block | §12 Risks/Gaps |
| all above | gate calculation | §13 Gate Record |

## 9.3 T3

```text
spec.md
        +
Resolved Context
        |
        v
T3 procedure
        |
        +--> uses permitted repository capabilities during execution
        |
        v
ImplementationBundle
├── implementation.md
├── repo candidates*
└── implementation appendices*
```

| T3 reads | T3 procedure | `implementation.md` output |
| --- | --- | --- |
| Spec §6 Change Surface | determine per-repo action | §3 Dispositions |
| Spec §8 Tasks | execute approved work | §3, §6 |
| Spec §3–§4 obligations/design | implement | §5–§6 |
| repository state/Context | pin bases and local constraints | §4 Candidate Refs + §10 |
| produced candidates | record exact heads/paths | §4–§5 |
| implementation checks | record observations | §7 Checks |
| mismatch/new scope | classify deviation | §8 Deviations |
| repo-local detail | appendix if triggered | §9 Registry |
| execution topology | provenance only | §11 |
| unresolved evidence/gaps | T4 handoff | §12 |
| all above | gate calculation | §13 Gate Record |

## 9.4 T4

```text
intention.md
+ spec.md
+ implementation.md
+ exact candidate refs
+ Resolved Context
        |
        v
T4 procedure
        |
        +--> gathers/references independent Evidence during execution
        |
        v
correctness.md + evidence appendices*
```

| T4 reads | T4 procedure | `correctness.md` output |
| --- | --- | --- |
| exact lineage | pin evaluation target | §1 Exact Inputs |
| Spec §9 V&V plan | select required methods/scope | §3–§6 |
| Spec requirements | verify candidate conformance | §3 Verification |
| Intention scenarios/criteria | validate outcome | §4 Validation |
| independent Evidence | evaluate claims | §2–§5 |
| requirement/repo/task mappings | calculate coverage | §6 Coverage |
| evidence/scope gaps | limitations | §7 |
| release evidence if applicable | observe, not assume | §8 |
| findings | determine earliest return | §9 |
| Context | interpretation provenance | §10 |
| independent evaluation execution | provenance | §11 |
| all blocking verdicts + scope | gate calculation | §12 |

---

# 10. Canonical End-to-End I/O Matrix

```text
AuthenticatedHumanSignal
        |
        | T1-Intention-Skill
        | ; ResolvedContextRefs
        v
intention.md
        |
        | T2-Delivery-Spec-Skill
        | ; ResolvedContextRefs
        |   (gathers current Evidence during execution)
        v
spec.md
        |
        | T3-Implementation-Skill
        | ; ResolvedContextRefs
        |   (uses permitted repository capabilities)
        v
implementation.md
+ exact repo candidates
        |
        | T4-Correctness-Skill
        | ; ResolvedContextRefs
        |   (gathers/references independent Evidence)
        v
correctness.md
```

The canonical artifact chain remains:

```text
Human Signal
→ intention.md
→ spec.md
→ implementation.md
→ correctness.md
```

Appendices and side effects are subordinate OutputBundle members and do not add stages.

---

# 11. Agent Compliance Rules

A Layer 1 Agent producing a canonical Markdown artifact MUST:

1. use the exact required top-level section order from this profile;
2. preserve exact upstream revisions in frontmatter;
3. preserve stable IDs rather than renumbering for aesthetics;
4. emit required structured records in the declared sections;
5. include empty arrays / explicit `NOT_APPLICABLE` records instead of silently omitting required structure;
6. record materially influential `ResolvedContextRef` and `EvidenceRef` separately;
7. avoid inventing authority absent from the upstream artifact/source;
8. avoid using narrative prose to bypass structured gate fields;
9. allocate appendices only through the owning core artifact registry;
10. calculate only the gate owned by the current canonical transition.

A consumer Agent MUST reject or block on a canonical input when:

- required frontmatter is missing or inconsistent;
- the artifact's upstream reference does not match the expected lineage;
- the artifact is `STALE` or `SUPERSEDED`;
- the required previous gate is not satisfied;
- required structured sections/records necessary for the current transformation are missing;
- narrative and structured records materially conflict.

---

# 12. What This Profile Does Not Define

This profile does not define:

- how Product Assets / Layer 2 Context are physically represented;
- how `ResolvedContextRef` is selected by a runtime;
- actual `SKILL.md` contents for T1–T4;
- physical FDI repository root deployment;
- a Markdown parser or validator implementation;
- raw CI/evidence storage;
- repository branching/PR conventions;
- Agent/model assignment.

Those remain separate contracts.

---

# 13. Contract Review Result

The contract-level review for this profile is complete.

Resolved in this review:

1. Human Signal fragments now have stable physical IDs so criterion traceability is resolvable.
2. T2 and T3 now define exact `EvidenceRef` inventory locations.
3. T4 now registers governed Evidence appendices in the owning `correctness.md`.
4. `ResolvedContextRef` physical records now include the approved `evidence_backlink` field and explicit exclusions where required.
5. V&V disposition fields align with the approved Layer 1 shared record, including nullable/N/A semantics for authorized non-blocking observation.
6. `spec.md` covers configuration separately from data/schema.
7. `correctness.md` coverage now includes design invariants and tasks as required by Layer 1 traceability.
8. Criterion verdict records preserve the approved shared fields while adding physical finding references.
9. Execution-time Evidence and repository capabilities are no longer depicted as additional canonical inputs.
10. Candidate-reference physical identity is explicitly defined as addressability metadata, not new authority.

```text
Contract review: PASS
Open contract blockers: NONE IDENTIFIED
Herman design approval: APPROVED
```

---

# 14. Approval Checklist

Before this profile may be called `Contract-ready`, approve:

- [x] Common physical Markdown rules
- [x] Common canonical frontmatter
- [x] Exact `intention.md` heading order and section schemas
- [x] Exact `spec.md` heading order and section schemas
- [x] Exact `implementation.md` heading order and section schemas
- [x] Exact `correctness.md` heading order and section schemas
- [x] Spec appendix physical profile
- [x] Implementation repository appendix physical profile
- [x] Evidence appendix physical profile
- [x] Stable ID conventions
- [x] Required-section non-omission rule
- [x] Structured-record-over-narrative consistency rule
- [x] T1 input-to-output mapping
- [x] T2 input-to-output mapping
- [x] T3 input-to-output mapping
- [x] T4 multi-input-to-output mapping
- [x] Consumer rejection/blocking rules

Current state:

```text
Layer 1 semantic contract: APPROVED

Layer 1 Markdown I/O Profile v0.1:
Contract-ready: APPROVED
Execution-verified: NOT_CLAIMED
Validator implementation: NOT_AUTHORIZED_BY_THIS_DESIGN
```

---

# 15. Approval Record

```text
Approved by: Herman
Decision: APPROVE
Layer 1 Markdown I/O Profile v0.1: Contract-ready
Execution-verified: NOT_CLAIMED
Implementation authorization: NOT_GRANTED_BY_THIS_APPROVAL
```

This approval freezes the physical Markdown I/O contract unless a later approved revision supersedes it.

---

# 16. Completion Definition

After approval of this profile, Layer 1 will have all three required specification levels:

```text
A. Semantic Contract
   what each artifact means
   → APPROVED

B. Structured Record Contract
   what machine-readable records exist
   → APPROVED through Layer 1 + this profile

C. Physical Markdown I/O Contract
   exact headings, ordering, placement, and required empty-state behavior
   → APPROVED
```

At that point a conforming Agent can determine, without inventing structure:

```text
what canonical input to read
which exact sections/records are authoritative
which Context/Evidence references are dependencies
what procedure the Skill must perform
what exact Markdown structure to write
what gate it may calculate
what the next Skill is allowed to consume
```

## FT-T2 — layer1_ft_t2_helpers

- Semantic version: `LOCKED-HERM-211`
- Approval: `HERM-210:01a0532d-e397-793d-b334-05a4fc8d2560; HERM-211:01a05336-448a-746a-8deb-6dd6968a9ad4`
- Compatibility: `L1-SEM@0.2; sole gate SPEC_READY|BLOCKED`

### Source: `normative/ft-t2/contracts/candidate-repo-set.schema.json`

SHA-256: `b6effd125f6948699d81e0c118367e07fffb231c87be20996a3662a8826f3572`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fdi.local/contracts/candidate-repo-set.schema.json",
  "title": "CandidateRepoSet",
  "type": "object",
  "additionalProperties": false,
  "required": ["contract_name", "contract_version", "record_id", "feature_id", "revision", "created_at", "producer_id", "owner_id", "lifecycle", "intent_spec_ref", "discovery_policy_ref", "candidates", "unknowns", "ordering_rule", "caps"],
  "properties": {
    "contract_name": {"const": "CandidateRepoSet"}, "contract_version": {"type": "string", "pattern": "^1\\.[0-9]+\\.[0-9]+$"},
    "record_id": {"$ref": "#/$defs/id"}, "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"}, "revision": {"type": "integer", "minimum": 1},
    "created_at": {"type": "string", "format": "date-time"}, "producer_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"}, "lifecycle": {"$ref": "#/$defs/lifecycle"},
    "intent_spec_ref": {"$ref": "#/$defs/recordRef"},
    "discovery_policy_ref": {"type": "object", "additionalProperties": false, "required": ["policy_id", "revision", "digest"], "properties": {"policy_id": {"$ref": "#/$defs/id"}, "revision": {"type": "string", "minLength": 1}, "digest": {"$ref": "#/$defs/digest"}}},
    "candidates": {"type": "array", "items": {"$ref": "#/$defs/candidate"}},
    "unknowns": {"type": "array", "items": {"$ref": "#/$defs/unknown"}},
    "ordering_rule": {"type": "object", "additionalProperties": false, "required": ["score_rule", "tie_break"], "properties": {"score_rule": {"type": "string", "minLength": 1}, "tie_break": {"const": "repository_id_ascending"}}},
    "caps": {"type": "object", "additionalProperties": false, "required": ["max_candidate_repositories"], "properties": {"max_candidate_repositories": {"type": "integer", "minimum": 1}}}
  },
  "$defs": {
    "id": {"type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"}, "digest": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "lifecycle": {"type": "string", "enum": ["ACTIVE", "STALE", "SUPERSEDED", "RETIRED"]},
    "recordRef": {"type": "object", "additionalProperties": false, "required": ["contract_name", "contract_version", "record_id", "revision", "digest"], "properties": {"contract_name": {"type": "string", "minLength": 1}, "contract_version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"}, "record_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "digest": {"$ref": "#/$defs/digest"}}},
    "candidate": {
      "type": "object", "additionalProperties": false,
      "required": ["candidate_id", "repository_id", "registry_state", "introduced_by_refs", "rationale", "ordering_score", "state", "evidence_refs", "current_evidence", "limitations"],
      "properties": {"candidate_id": {"$ref": "#/$defs/id"}, "repository_id": {"$ref": "#/$defs/id"}, "registry_state": {"type": "string", "enum": ["REGISTERED", "UNREGISTERED"]}, "introduced_by_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "rationale": {"type": "string", "minLength": 1}, "ordering_score": {"type": ["number", "null"]}, "state": {"type": "string", "enum": ["CANDIDATE", "CONFIRMED", "EXCLUDED", "UNRESOLVED"]}, "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "current_evidence": {"type": "boolean"}, "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}}},
      "allOf": [
        {"if": {"properties": {"state": {"enum": ["CONFIRMED", "EXCLUDED"]}}}, "then": {"properties": {"current_evidence": {"const": true}, "evidence_refs": {"minItems": 1}}}},
        {"if": {"properties": {"registry_state": {"const": "UNREGISTERED"}}}, "then": {"properties": {"state": {"const": "UNRESOLVED"}}}}
      ]
    },
    "unknown": {"type": "object", "additionalProperties": false, "required": ["unknown_id", "affected_ids", "reason", "materiality", "owner_id", "resolution_condition", "earliest_reentry"], "properties": {"unknown_id": {"$ref": "#/$defs/id"}, "affected_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "reason": {"type": "string", "minLength": 1}, "materiality": {"type": "string", "enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "owner_id": {"$ref": "#/$defs/id"}, "resolution_condition": {"type": "string", "minLength": 1}, "earliest_reentry": {"enum": ["CANDIDATE_GENERATION", "SELECTOR_PREFLIGHT"]}}}
  }
}

### Source: `normative/ft-t2/contracts/change-surface-set.schema.json`

SHA-256: `c8301f38fec1fde6fe51e8c1f76ba29c91a700659d33a96728452af0732951c9`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fdi.local/contracts/change-surface-set.schema.json",
  "title": "ChangeSurfaceSet",
  "type": "object",
  "additionalProperties": false,
  "required": ["contract_name", "contract_version", "record_id", "feature_id", "revision", "created_at", "producer_id", "owner_id", "lifecycle", "intent_spec_ref", "candidate_repo_set_ref", "selector_refs", "surfaces", "dependency_edges", "unknowns"],
  "properties": {
    "contract_name": {"const": "ChangeSurfaceSet"}, "contract_version": {"type": "string", "pattern": "^1\\.[0-9]+\\.[0-9]+$"},
    "record_id": {"$ref": "#/$defs/id"}, "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"}, "revision": {"type": "integer", "minimum": 1}, "created_at": {"type": "string", "format": "date-time"},
    "producer_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"}, "lifecycle": {"$ref": "#/$defs/lifecycle"},
    "intent_spec_ref": {"$ref": "#/$defs/recordRef"}, "candidate_repo_set_ref": {"$ref": "#/$defs/recordRef"},
    "selector_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/selectorRef"}},
    "surfaces": {"type": "array", "items": {"$ref": "#/$defs/surface"}},
    "dependency_edges": {"type": "array", "items": {"$ref": "#/$defs/edge"}},
    "unknowns": {"type": "array", "items": {"$ref": "#/$defs/unknown"}}
  },
  "$defs": {
    "id": {"type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"}, "digest": {"type": "string", "pattern": "^[a-f0-9]{64}$"}, "sha": {"type": "string", "pattern": "^[a-f0-9]{40,64}$"},
    "path": {"type": "string", "pattern": "^(?!/)(?!.*(?:^|/)\\.{1,2}(?:/|$))(?!.*\\\\)[^\\u0000]+$"},
    "lifecycle": {"type": "string", "enum": ["ACTIVE", "STALE", "SUPERSEDED", "RETIRED"]},
    "recordRef": {"type": "object", "additionalProperties": false, "required": ["contract_name", "contract_version", "record_id", "revision", "digest"], "properties": {"contract_name": {"type": "string", "minLength": 1}, "contract_version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"}, "record_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "digest": {"$ref": "#/$defs/digest"}}},
    "selectorRef": {"type": "object", "additionalProperties": false, "required": ["selector_id", "revision", "repository_id", "repository_revision", "concrete_matches", "pass_evidence_ref"], "properties": {"selector_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "repository_id": {"$ref": "#/$defs/id"}, "repository_revision": {"$ref": "#/$defs/sha"}, "concrete_matches": {"type": "array", "items": {"$ref": "#/$defs/path"}, "uniqueItems": true}, "pass_evidence_ref": {"$ref": "#/$defs/id"}}},
    "surface": {
      "type": "object", "additionalProperties": false,
      "required": ["surface_id", "repository_id", "repository_revision", "path", "symbol_or_anchor", "anchor_absence_reason", "surface_type", "criterion_ids", "obligation_ids", "disposition", "evidence_refs", "current_evidence", "owner_id", "dependency_refs", "limitations", "materiality"],
      "properties": {"surface_id": {"$ref": "#/$defs/id"}, "repository_id": {"$ref": "#/$defs/id"}, "repository_revision": {"$ref": "#/$defs/sha"}, "path": {"$ref": "#/$defs/path"}, "symbol_or_anchor": {"type": ["string", "null"], "minLength": 1}, "anchor_absence_reason": {"type": ["string", "null"], "minLength": 1}, "surface_type": {"type": "string", "enum": ["SOURCE", "API", "EVENT", "SCHEMA", "DATA", "CONFIG", "TEST", "DEPLOYMENT", "DOCUMENTATION", "OTHER"]}, "criterion_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "obligation_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "disposition": {"type": "string", "enum": ["CANDIDATE", "CONFIRMED", "EXCLUDED", "UNRESOLVED"]}, "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "current_evidence": {"type": "boolean"}, "owner_id": {"anyOf": [{"$ref": "#/$defs/id"}, {"type": "null"}]}, "dependency_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}}, "materiality": {"type": "string", "enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}},
      "allOf": [
        {"if": {"properties": {"symbol_or_anchor": {"type": "null"}}}, "then": {"properties": {"anchor_absence_reason": {"type": "string", "minLength": 1}}}},
        {"if": {"properties": {"disposition": {"enum": ["CONFIRMED", "EXCLUDED"]}}}, "then": {"properties": {"current_evidence": {"const": true}, "evidence_refs": {"minItems": 1}}}},
        {"if": {"properties": {"materiality": {"const": "MATERIAL"}}}, "then": {"properties": {"owner_id": {"$ref": "#/$defs/id"}}}}
      ]
    },
    "edge": {"type": "object", "additionalProperties": false, "required": ["edge_id", "from_id", "to_id", "relation_type", "disposition", "materiality", "evidence_refs", "owner_id", "limitations"], "properties": {"edge_id": {"$ref": "#/$defs/id"}, "from_id": {"$ref": "#/$defs/id"}, "to_id": {"$ref": "#/$defs/id"}, "relation_type": {"type": "string", "enum": ["UPSTREAM", "DOWNSTREAM", "CALLS", "CONSUMES", "PRODUCES", "IMPLEMENTS", "VALIDATES", "DEPLOYS_WITH", "CO_CHANGE_HINT"]}, "disposition": {"type": "string", "enum": ["CANDIDATE", "CONFIRMED", "EXCLUDED", "UNRESOLVED"]}, "materiality": {"type": "string", "enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "owner_id": {"anyOf": [{"$ref": "#/$defs/id"}, {"type": "null"}]}, "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}}}},
    "unknown": {"type": "object", "additionalProperties": false, "required": ["unknown_id", "affected_ids", "reason", "materiality", "owner_id", "resolution_condition", "earliest_reentry"], "properties": {"unknown_id": {"$ref": "#/$defs/id"}, "affected_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "reason": {"type": "string", "minLength": 1}, "materiality": {"type": "string", "enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "owner_id": {"$ref": "#/$defs/id"}, "resolution_condition": {"type": "string", "minLength": 1}, "earliest_reentry": {"enum": ["CANDIDATE_GENERATION", "SELECTOR_PREFLIGHT", "SOURCE_INVESTIGATION", "DEPENDENCY_EXPANSION"]}}}
  }
}

### Source: `normative/ft-t2/contracts/closure-package.schema.json`

SHA-256: `463aa8f26aeb54e0f532ba4d7addc9f7130b333412beed7f83b4b69d558baf8a`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fdi.local/contracts/closure-package.schema.json",
  "title": "ClosurePackage",
  "type": "object",
  "additionalProperties": false,
  "required": ["contract_name", "contract_version", "record_id", "feature_id", "revision", "created_at", "producer_id", "owner_id", "lifecycle", "proposal_state", "intent_spec_ref", "change_surface_set_ref", "repository_pins", "passed_selectors", "finite_caps", "candidate_dispositions", "surface_dispositions", "edge_dispositions", "interfaces", "validation_surfaces", "evidence_refs", "exclusions", "unknowns", "source_versions", "supersedes", "closure_status"],
  "properties": {
    "contract_name": {"const": "ClosurePackage"}, "contract_version": {"type": "string", "pattern": "^1\\.[0-9]+\\.[0-9]+$"}, "record_id": {"$ref": "#/$defs/id"},
    "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"}, "revision": {"type": "integer", "minimum": 1}, "created_at": {"type": "string", "format": "date-time"},
    "producer_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"}, "lifecycle": {"$ref": "#/$defs/lifecycle"}, "proposal_state": {"const": "PROPOSED"},
    "intent_spec_ref": {"$ref": "#/$defs/recordRef"}, "change_surface_set_ref": {"$ref": "#/$defs/recordRef"},
    "repository_pins": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["repository_id", "revision", "owner_id"], "properties": {"repository_id": {"$ref": "#/$defs/id"}, "revision": {"$ref": "#/$defs/sha"}, "owner_id": {"$ref": "#/$defs/id"}}}},
    "passed_selectors": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/selector"}},
    "finite_caps": {"type": "object", "additionalProperties": false, "required": ["max_matches", "max_total_bytes", "max_expansion_depth", "max_nodes", "max_edges", "max_evidence_records"], "properties": {"max_matches": {"type": "integer", "minimum": 1}, "max_total_bytes": {"type": "integer", "minimum": 1}, "max_expansion_depth": {"type": "integer", "minimum": 1}, "max_nodes": {"type": "integer", "minimum": 1}, "max_edges": {"type": "integer", "minimum": 1}, "max_evidence_records": {"type": "integer", "minimum": 1}}},
    "candidate_dispositions": {"type": "array", "items": {"$ref": "#/$defs/disposition"}}, "surface_dispositions": {"type": "array", "items": {"$ref": "#/$defs/disposition"}}, "edge_dispositions": {"type": "array", "items": {"$ref": "#/$defs/disposition"}},
    "interfaces": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["interface_id", "producer_id", "consumer_id", "kind", "version", "compatibility_obligations", "rollout_obligations", "owner_ids", "evidence_refs"], "properties": {"interface_id": {"$ref": "#/$defs/id"}, "producer_id": {"$ref": "#/$defs/id"}, "consumer_id": {"$ref": "#/$defs/id"}, "kind": {"enum": ["API", "EVENT", "SCHEMA", "DATA", "OTHER"]}, "version": {"type": "string", "minLength": 1}, "compatibility_obligations": {"type": "array", "items": {"type": "string", "minLength": 1}}, "rollout_obligations": {"type": "array", "items": {"type": "string", "minLength": 1}}, "owner_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "evidence_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}}}},
    "validation_surfaces": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["validation_id", "criterion_ids", "obligation_ids", "method", "surface_id", "owner_id", "environment", "planned_evidence_destination"], "properties": {"validation_id": {"$ref": "#/$defs/id"}, "criterion_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "obligation_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "method": {"type": "string", "minLength": 1}, "surface_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"}, "environment": {"type": "string", "minLength": 1}, "planned_evidence_destination": {"type": "string", "minLength": 1}}}},
    "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true},
    "exclusions": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["excluded_id", "kind", "reason", "current_evidence_refs", "owner_id"], "properties": {"excluded_id": {"$ref": "#/$defs/id"}, "kind": {"enum": ["REPOSITORY", "PATH", "SURFACE", "EDGE"]}, "reason": {"type": "string", "minLength": 1}, "current_evidence_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "owner_id": {"$ref": "#/$defs/id"}}}},
    "unknowns": {"type": "array", "items": {"$ref": "#/$defs/unknown"}},
    "source_versions": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["source_id", "kind", "version", "digest"], "properties": {"source_id": {"$ref": "#/$defs/id"}, "kind": {"enum": ["CONTRACT", "SKILL", "PRODUCT_ASSET", "REGISTRY", "POLICY", "SOURCE"]}, "version": {"type": "string", "minLength": 1}, "digest": {"$ref": "#/$defs/digest"}}}},
    "supersedes": {"anyOf": [{"type": "null"}, {"$ref": "#/$defs/recordRef"}]},
    "closure_status": {"type": "string", "enum": ["OPEN", "PARTIAL", "CLOSED_WITHIN_DECLARED_SCOPE"]}
  },
  "allOf": [
    {"if": {"properties": {"closure_status": {"const": "CLOSED_WITHIN_DECLARED_SCOPE"}}}, "then": {"properties": {"unknowns": {"not": {"contains": {"properties": {"materiality": {"enum": ["MATERIAL", "UNKNOWN"]}}, "required": ["materiality"]}}}}}}
  ],
  "$defs": {
    "id": {"type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"}, "digest": {"type": "string", "pattern": "^[a-f0-9]{64}$"}, "sha": {"type": "string", "pattern": "^[a-f0-9]{40,64}$"}, "lifecycle": {"type": "string", "enum": ["ACTIVE", "STALE", "SUPERSEDED", "RETIRED"]},
    "recordRef": {"type": "object", "additionalProperties": false, "required": ["contract_name", "contract_version", "record_id", "revision", "digest"], "properties": {"contract_name": {"type": "string", "minLength": 1}, "contract_version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"}, "record_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "digest": {"$ref": "#/$defs/digest"}}},
    "selector": {"type": "object", "additionalProperties": false, "required": ["selector_id", "revision", "repository_id", "repository_revision", "derivation_refs", "path_templates", "root", "extensions", "exclusions", "concrete_matches", "zero_behavior", "excess_behavior", "pass_evidence_ref"], "properties": {"selector_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "repository_id": {"$ref": "#/$defs/id"}, "repository_revision": {"$ref": "#/$defs/sha"}, "derivation_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "path_templates": {"type": "array", "minItems": 1, "items": {"type": "string", "minLength": 1}}, "root": {"type": "string", "minLength": 1}, "extensions": {"type": "array", "minItems": 1, "items": {"type": "string", "pattern": "^\\.[a-z0-9]+$"}}, "exclusions": {"type": "array", "items": {"type": "string", "minLength": 1}}, "concrete_matches": {"type": "array", "items": {"type": "string", "minLength": 1}, "uniqueItems": true}, "zero_behavior": {"enum": ["BLOCK", "RECORD_GAP"]}, "excess_behavior": {"const": "BLOCK"}, "pass_evidence_ref": {"$ref": "#/$defs/id"}}},
    "disposition": {"type": "object", "additionalProperties": false, "required": ["item_id", "disposition", "materiality", "evidence_refs", "owner_id", "limitations"], "properties": {"item_id": {"$ref": "#/$defs/id"}, "disposition": {"enum": ["CANDIDATE", "CONFIRMED", "EXCLUDED", "UNRESOLVED"]}, "materiality": {"enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}}, "owner_id": {"anyOf": [{"$ref": "#/$defs/id"}, {"type": "null"}]}, "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}}}},
    "unknown": {"type": "object", "additionalProperties": false, "required": ["unknown_id", "affected_ids", "reason", "materiality", "owner_id", "resolution_condition", "earliest_reentry"], "properties": {"unknown_id": {"$ref": "#/$defs/id"}, "affected_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "reason": {"type": "string", "minLength": 1}, "materiality": {"enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "owner_id": {"$ref": "#/$defs/id"}, "resolution_condition": {"type": "string", "minLength": 1}, "earliest_reentry": {"enum": ["INTENT_CLARIFICATION", "CANDIDATE_GENERATION", "SELECTOR_PREFLIGHT", "SOURCE_INVESTIGATION", "DEPENDENCY_EXPANSION", "CLOSURE_ASSEMBLY", "SPEC_AUTHORING"]}}}
  }
}

### Source: `normative/ft-t2/contracts/closure-review.schema.json`

SHA-256: `a6ea49e1481b4ad6874d2068081cb1bfe82031d2e16868075495df037b2dfe6f`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fdi.local/contracts/closure-review.schema.json",
  "title": "ClosureReview",
  "type": "object",
  "additionalProperties": false,
  "required": ["contract_name", "contract_version", "record_id", "feature_id", "revision", "created_at", "producer_id", "owner_id", "lifecycle", "reviewed_closure_package_ref", "reviewed_spec_draft_ref", "reviewed_spec_absence_reason", "investigator_identity", "reviewer_identity", "independence", "missing_candidate_ids", "unsupported_claim_ids", "unresolved_material_edge_ids", "selector_failures", "provenance_failures", "evidence_refs", "limitations", "verdict", "required_reentry_point", "required_actions"],
  "properties": {
    "contract_name": {"const": "ClosureReview"}, "contract_version": {"type": "string", "pattern": "^1\\.[0-9]+\\.[0-9]+$"}, "record_id": {"$ref": "#/$defs/id"},
    "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"}, "revision": {"type": "integer", "minimum": 1}, "created_at": {"type": "string", "format": "date-time"}, "producer_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"}, "lifecycle": {"type": "string", "enum": ["ACTIVE", "STALE", "SUPERSEDED", "RETIRED"]},
    "reviewed_closure_package_ref": {"$ref": "#/$defs/recordRef"}, "reviewed_spec_draft_ref": {"anyOf": [{"type": "null"}, {"$ref": "#/$defs/artifactRef"}]}, "reviewed_spec_absence_reason": {"type": ["string", "null"], "minLength": 1},
    "investigator_identity": {"$ref": "#/$defs/identity"}, "reviewer_identity": {"$ref": "#/$defs/identity"},
    "independence": {"type": "object", "additionalProperties": false, "required": ["separate_identity", "separate_context", "conflict_check", "capability_boundary", "declaration"], "properties": {"separate_identity": {"const": true}, "separate_context": {"const": true}, "conflict_check": {"type": "string", "minLength": 1}, "capability_boundary": {"type": "string", "minLength": 1}, "declaration": {"type": "string", "minLength": 1}}},
    "missing_candidate_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "unsupported_claim_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "unresolved_material_edge_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true},
    "selector_failures": {"type": "array", "items": {"$ref": "#/$defs/failure"}}, "provenance_failures": {"type": "array", "items": {"$ref": "#/$defs/failure"}}, "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}},
    "verdict": {"type": "string", "enum": ["PASS", "FAIL", "INCONCLUSIVE"]},
    "required_reentry_point": {"type": ["string", "null"], "enum": ["INTENT_CLARIFICATION", "CANDIDATE_GENERATION", "SELECTOR_PREFLIGHT", "SOURCE_INVESTIGATION", "DEPENDENCY_EXPANSION", "CLOSURE_ASSEMBLY", "SPEC_AUTHORING", null]},
    "required_actions": {"type": "array", "items": {"type": "object", "additionalProperties": false, "required": ["action_id", "owner_id", "affected_ids", "materiality", "evidence_needed", "completion_test"], "properties": {"action_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"}, "affected_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}, "materiality": {"enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "evidence_needed": {"type": "string", "minLength": 1}, "completion_test": {"type": "string", "minLength": 1}}}}
  },
  "allOf": [
    {"if": {"properties": {"reviewed_spec_draft_ref": {"type": "null"}}}, "then": {"properties": {"reviewed_spec_absence_reason": {"type": "string", "minLength": 1}}}},
    {"if": {"properties": {"verdict": {"const": "PASS"}}}, "then": {"properties": {"required_reentry_point": {"type": "null"}, "required_actions": {"maxItems": 0}, "missing_candidate_ids": {"maxItems": 0}, "unsupported_claim_ids": {"maxItems": 0}, "unresolved_material_edge_ids": {"maxItems": 0}, "selector_failures": {"maxItems": 0}, "provenance_failures": {"maxItems": 0}}}},
    {"if": {"properties": {"verdict": {"enum": ["FAIL", "INCONCLUSIVE"]}}}, "then": {"properties": {"required_reentry_point": {"type": "string"}, "required_actions": {"minItems": 1}}}}
  ],
  "$defs": {
    "id": {"type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"}, "digest": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "recordRef": {"type": "object", "additionalProperties": false, "required": ["contract_name", "contract_version", "record_id", "revision", "digest"], "properties": {"contract_name": {"const": "ClosurePackage"}, "contract_version": {"type": "string", "pattern": "^[0-9]+\\.[0-9]+\\.[0-9]+$"}, "record_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "digest": {"$ref": "#/$defs/digest"}}},
    "artifactRef": {"type": "object", "additionalProperties": false, "required": ["path", "revision", "digest", "gate_state"], "properties": {"path": {"const": "spec.md"}, "revision": {"type": "integer", "minimum": 1}, "digest": {"$ref": "#/$defs/digest"}, "gate_state": {"const": "NOT_GATED"}}},
    "identity": {"type": "object", "additionalProperties": false, "required": ["identity_id", "role", "context_id"], "properties": {"identity_id": {"$ref": "#/$defs/id"}, "role": {"enum": ["INVESTIGATOR", "REVIEWER"]}, "context_id": {"$ref": "#/$defs/id"}}},
    "failure": {"type": "object", "additionalProperties": false, "required": ["failure_id", "subject_id", "reason", "evidence_refs"], "properties": {"failure_id": {"$ref": "#/$defs/id"}, "subject_id": {"$ref": "#/$defs/id"}, "reason": {"type": "string", "minLength": 1}, "evidence_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}}}}
  }
}

### Source: `normative/ft-t2/contracts/evidence-record.schema.json`

SHA-256: `85d0eb6c2a4fc72c9ab7fa100f0aa49bbaa67b8feb30688ea4e2e5488e1289c1`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fdi.local/contracts/evidence-record.schema.json",
  "title": "EvidenceRecord",
  "type": "object",
  "additionalProperties": false,
  "required": ["contract_name", "contract_version", "record_id", "evidence_id", "feature_id", "revision", "created_at", "producer_id", "owner_id", "lifecycle", "claim", "claim_effect", "method", "origin", "observed_at", "source_revision", "environment", "integrity", "authority_dimension", "limitations", "review_state", "expires_at", "expiry_reason", "superseded_by", "backlinks"],
  "properties": {
    "contract_name": {"const": "EvidenceRecord"},
    "contract_version": {"type": "string", "pattern": "^1\\.[0-9]+\\.[0-9]+$"},
    "record_id": {"$ref": "#/$defs/id"}, "evidence_id": {"$ref": "#/$defs/id"},
    "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"},
    "revision": {"type": "integer", "minimum": 1}, "created_at": {"type": "string", "format": "date-time"},
    "producer_id": {"$ref": "#/$defs/id"}, "owner_id": {"$ref": "#/$defs/id"},
    "lifecycle": {"type": "string", "enum": ["ACTIVE", "STALE", "SUPERSEDED", "RETIRED"]},
    "claim": {"type": "object", "additionalProperties": false, "required": ["claim_id", "text"], "properties": {"claim_id": {"$ref": "#/$defs/id"}, "text": {"type": "string", "minLength": 1}}},
    "claim_effect": {"type": "string", "enum": ["SUPPORTS", "CONTRADICTS", "LIMITS", "OBSERVES"]},
    "method": {"type": "object", "additionalProperties": false, "required": ["kind", "procedure", "skill_version", "capability_id"], "properties": {"kind": {"type": "string", "enum": ["SEARCH", "INSPECTION", "TEST", "MEASUREMENT", "REVIEW", "OBSERVATION"]}, "procedure": {"type": "string", "minLength": 1}, "skill_version": {"type": "string", "minLength": 1}, "capability_id": {"$ref": "#/$defs/id"}}},
    "origin": {"type": "object", "additionalProperties": false, "required": ["locator", "owner_id", "access_conditions", "origin_type"], "properties": {"locator": {"type": "string", "minLength": 1, "not": {"pattern": "^(file:|/|~|[A-Za-z]:\\\\)"}}, "owner_id": {"$ref": "#/$defs/id"}, "access_conditions": {"type": "string", "minLength": 1}, "origin_type": {"type": "string", "enum": ["IMMUTABLE_CONTENT", "TIMESTAMPED_RUNTIME"]}}},
    "observed_at": {"type": ["string", "null"], "format": "date-time"},
    "source_revision": {"type": "string", "minLength": 1, "not": {"pattern": "^(main|master|HEAD|latest)$"}},
    "environment": {"type": "string", "minLength": 1},
    "integrity": {"type": "object", "additionalProperties": false, "required": ["algorithm", "digest", "coverage", "verified", "verifier_id"], "properties": {"algorithm": {"const": "SHA-256"}, "digest": {"$ref": "#/$defs/digest"}, "coverage": {"type": "string", "minLength": 1}, "verified": {"const": true}, "verifier_id": {"$ref": "#/$defs/id"}}},
    "authority_dimension": {"type": "string", "enum": ["DESIRED_BEHAVIOR", "TECHNICAL_OBLIGATION", "DURABLE_CONSTRAINT", "CURRENT_BEHAVIOR", "PROCEDURE", "RATIONALE_SUPPORT"]},
    "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}},
    "review_state": {"type": "string", "enum": ["CURRENT", "EXPIRED", "INVALIDATED", "SUPERSEDED"]},
    "expires_at": {"type": ["string", "null"], "format": "date-time"},
    "expiry_reason": {"type": "string", "minLength": 1},
    "superseded_by": {"anyOf": [{"type": "null"}, {"$ref": "#/$defs/id"}]},
    "backlinks": {"type": "array", "minItems": 1, "items": {"type": "object", "additionalProperties": false, "required": ["contract_name", "record_id", "revision", "field", "claim_or_criterion_id"], "properties": {"contract_name": {"type": "string", "minLength": 1}, "record_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "field": {"type": "string", "minLength": 1}, "claim_or_criterion_id": {"$ref": "#/$defs/id"}}}}
  },
  "allOf": [
    {"if": {"properties": {"origin": {"properties": {"origin_type": {"const": "TIMESTAMPED_RUNTIME"}}}}}, "then": {"properties": {"observed_at": {"type": "string", "format": "date-time"}, "environment": {"not": {"const": "NOT_APPLICABLE"}}}}},
    {"if": {"properties": {"origin": {"properties": {"origin_type": {"const": "IMMUTABLE_CONTENT"}}}}}, "then": {"properties": {"observed_at": {"type": "null"}}}}
  ],
  "$defs": {
    "id": {"type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"},
    "digest": {"type": "string", "pattern": "^[a-f0-9]{64}$"}
  }
}

### Source: `normative/ft-t2/contracts/intent-spec.schema.json`

SHA-256: `e809f4a030c713312cd1e76bc4b2514bf2787381174a02116cf3a9866900418c`

{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "$id": "https://fdi.local/contracts/intent-spec.schema.json",
  "title": "IntentSpec",
  "type": "object",
  "additionalProperties": false,
  "required": ["contract_name", "contract_version", "record_id", "feature_id", "revision", "created_at", "producer_id", "owner_id", "lifecycle", "feature_identity", "outcome", "expected_behaviors", "criterion_ids", "acceptance_criteria", "authorized_source_refs", "scope", "constraints", "non_goals", "assumptions", "repository_seeds", "unknowns", "source_backlinks", "supersedes"],
  "properties": {
    "contract_name": {"const": "IntentSpec"},
    "contract_version": {"type": "string", "pattern": "^1\\.[0-9]+\\.[0-9]+$"},
    "record_id": {"$ref": "#/$defs/id"},
    "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"},
    "revision": {"type": "integer", "minimum": 1},
    "created_at": {"type": "string", "format": "date-time"},
    "producer_id": {"$ref": "#/$defs/id"},
    "owner_id": {"$ref": "#/$defs/id"},
    "lifecycle": {"$ref": "#/$defs/lifecycle"},
    "feature_identity": {
      "type": "object", "additionalProperties": false,
      "required": ["feature_id", "title", "human_signal_id", "product_ids", "system_ids"],
      "properties": {
        "feature_id": {"type": "string", "pattern": "^[A-Za-z0-9][A-Za-z0-9._-]*$"},
        "title": {"type": "string", "minLength": 1},
        "human_signal_id": {"$ref": "#/$defs/id"},
        "product_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true},
        "system_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}
      }
    },
    "outcome": {"type": "string", "minLength": 1},
    "expected_behaviors": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/behavior"}},
    "criterion_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true},
    "acceptance_criteria": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/criterion"}},
    "authorized_source_refs": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/sourceRef"}},
    "scope": {
      "type": "object", "additionalProperties": false,
      "required": ["product_ids", "system_ids", "user_boundaries"],
      "properties": {
        "product_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true},
        "system_ids": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true},
        "user_boundaries": {"type": "array", "items": {"type": "string", "minLength": 1}, "uniqueItems": true}
      }
    },
    "constraints": {"type": "array", "items": {"$ref": "#/$defs/constraint"}},
    "non_goals": {"type": "array", "items": {"type": "string", "minLength": 1}, "uniqueItems": true},
    "assumptions": {"type": "array", "items": {"$ref": "#/$defs/assumption"}},
    "repository_seeds": {"type": "array", "items": {"$ref": "#/$defs/repositorySeed"}},
    "unknowns": {"type": "array", "items": {"$ref": "#/$defs/unknown"}},
    "source_backlinks": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/backlink"}},
    "supersedes": {"anyOf": [{"type": "null"}, {"$ref": "#/$defs/revisionRef"}]}
  },
  "$defs": {
    "id": {"type": "string", "pattern": "^[a-z0-9]+(?:-[a-z0-9]+)*$"},
    "digest": {"type": "string", "pattern": "^[a-f0-9]{64}$"},
    "lifecycle": {"type": "string", "enum": ["ACTIVE", "STALE", "SUPERSEDED", "RETIRED"]},
    "behavior": {
      "type": "object", "additionalProperties": false,
      "required": ["behavior_id", "actor", "trigger", "preconditions", "observable_result", "priority", "blocking_class", "criterion_ids"],
      "properties": {
        "behavior_id": {"$ref": "#/$defs/id"}, "actor": {"type": "string", "minLength": 1}, "trigger": {"type": "string", "minLength": 1},
        "preconditions": {"type": "array", "items": {"type": "string", "minLength": 1}}, "observable_result": {"type": "string", "minLength": 1},
        "priority": {"type": "string", "enum": ["MUST", "SHOULD", "MAY"]}, "blocking_class": {"type": "string", "enum": ["BLOCKING", "NON_BLOCKING"]},
        "criterion_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}
      }
    },
    "criterion": {
      "type": "object", "additionalProperties": false,
      "required": ["criterion_id", "observable_signal", "expected_evidence", "blocking_class"],
      "properties": {"criterion_id": {"$ref": "#/$defs/id"}, "observable_signal": {"type": "string", "minLength": 1}, "expected_evidence": {"type": "string", "minLength": 1}, "blocking_class": {"type": "string", "enum": ["BLOCKING", "NON_BLOCKING"]}}
    },
    "sourceRef": {
      "type": "object", "additionalProperties": false,
      "required": ["source_id", "origin", "owner_id", "revision", "authority_dimension", "limitations"],
      "properties": {"source_id": {"$ref": "#/$defs/id"}, "origin": {"type": "string", "minLength": 1}, "owner_id": {"$ref": "#/$defs/id"}, "revision": {"type": "string", "minLength": 1}, "authority_dimension": {"type": "string", "enum": ["DESIRED_BEHAVIOR", "DURABLE_CONSTRAINT", "RATIONALE_SUPPORT"]}, "limitations": {"type": "array", "items": {"type": "string", "minLength": 1}}}
    },
    "constraint": {
      "type": "object", "additionalProperties": false, "required": ["constraint_id", "kind", "statement", "authority_ref"],
      "properties": {"constraint_id": {"$ref": "#/$defs/id"}, "kind": {"type": "string", "enum": ["PRODUCT", "ARCHITECTURE", "DOMAIN", "REGULATORY", "TIME", "COMPATIBILITY", "POLICY"]}, "statement": {"type": "string", "minLength": 1}, "authority_ref": {"$ref": "#/$defs/id"}}
    },
    "assumption": {
      "type": "object", "additionalProperties": false, "required": ["assumption_id", "statement", "owner_id", "authority_ref", "evidence_refs", "invalidation_condition"],
      "properties": {"assumption_id": {"$ref": "#/$defs/id"}, "statement": {"type": "string", "minLength": 1}, "owner_id": {"$ref": "#/$defs/id"}, "authority_ref": {"$ref": "#/$defs/id"}, "evidence_refs": {"type": "array", "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "invalidation_condition": {"type": "string", "minLength": 1}}
    },
    "repositorySeed": {
      "type": "object", "additionalProperties": false, "required": ["repository_id", "classification", "source_ref", "reason"],
      "properties": {"repository_id": {"$ref": "#/$defs/id"}, "classification": {"const": "HINT_ONLY"}, "source_ref": {"$ref": "#/$defs/id"}, "reason": {"type": "string", "minLength": 1}}
    },
    "unknown": {
      "type": "object", "additionalProperties": false, "required": ["unknown_id", "affected_ids", "reason", "materiality", "owner_id", "resolution_condition", "earliest_reentry"],
      "properties": {"unknown_id": {"$ref": "#/$defs/id"}, "affected_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}, "reason": {"type": "string", "minLength": 1}, "materiality": {"type": "string", "enum": ["MATERIAL", "NON_MATERIAL", "UNKNOWN"]}, "owner_id": {"$ref": "#/$defs/id"}, "resolution_condition": {"type": "string", "minLength": 1}, "earliest_reentry": {"type": "string", "enum": ["INTENT_CLARIFICATION", "CANDIDATE_GENERATION", "SELECTOR_PREFLIGHT", "SOURCE_INVESTIGATION", "DEPENDENCY_EXPANSION", "CLOSURE_ASSEMBLY", "SPEC_AUTHORING"]}}
    },
    "backlink": {
      "type": "object", "additionalProperties": false, "required": ["source_fragment", "target_ids"],
      "properties": {"source_fragment": {"type": "string", "minLength": 1}, "target_ids": {"type": "array", "minItems": 1, "items": {"$ref": "#/$defs/id"}, "uniqueItems": true}}
    },
    "revisionRef": {
      "type": "object", "additionalProperties": false, "required": ["record_id", "revision", "digest", "reason"],
      "properties": {"record_id": {"$ref": "#/$defs/id"}, "revision": {"type": "integer", "minimum": 1}, "digest": {"$ref": "#/$defs/digest"}, "reason": {"type": "string", "minLength": 1}}
    }
  }
}

### Source: `normative/ft-t2/skills/changesurface-investigation/SKILL.md`

SHA-256: `49d146291f1f45b8aba7513660c62adc5148766ecf5d13554853e60694d9a2a6`

---
name: changesurface-investigation
description: Inspect only passed concrete matches at immutable repository pins and emit ChangeSurfaceSet plus evidence.
version: 1.0.0
digest_algorithm: SHA-256
digest: 453a080bcfea8414f95ef0c6ad97c2898fbaef1c8027d2ed36e1610ed5cc9990
digest_coverage: UTF-8 bytes excluding the digest metadata line
source: HERM-210/HERM-211/HERM-212-v0.3
compatible_runtime: ">=1.0.0 <2.0.0"
owner: fdi-workflow-owner
authority: FT-T2 passed-selector source investigation procedure only
status: ACTIVE
review_state: CONTRACT_REVIEWED
reviewer: fdi-governance-reviewer
last_reviewed: 2026-08-31
next_review: 2027-02-28
supersedes: null
superseded_by: null
---

# Purpose and applicability

Use this Skill after selector preflight to inspect bounded source matches at immutable pins and emit one `ChangeSurfaceSet@1.x` plus claim-linked `EvidenceRecord@1.x` records.

## Transition contract

Inputs are exact active `IntentSpec` and `CandidateRepoSet` refs/digests, registry-qualified repository pins, versioned `SourceScopeSelector` records with positive caps and declared zero/excess behavior, exact concrete-match destinations, source access, and this Skill digest. Extra, mutable, unregistered, or unpassed scope is rejected.

Outputs are one immutable `ChangeSurfaceSet@1.0.0` and ordered evidence records at declared destinations. No source mutation, selector creation, or gate output is permitted.

## Context selection

Read the Codebase registry and exact repository-local instructions before any repository content. Use only pinned source/config/schema/test/interface paths named by passed selectors plus applicable Domain, Operations, and Steering constraints. Exclude unrelated repositories, directory-wide defaults, caches, generated output, vendor trees, secrets, and evaluator-only state. Record every name enumeration, selector proof, concrete match, content read, and exclusion.

## Capability bindings

- `selector-validate` (required): validate repo ID, immutable SHA, root, template, extensions, exclusions, caps, and derivation refs.
- `pinned-name-enumerate` (required): path names only; maximum is the selector's positive cap; no content returned.
- `pinned-file-read` (required): exact frozen concrete matches only; enforce aggregate byte/time limits.
- `bounded-symbol-search` (optional): only within a frozen concrete match; hard result cap and timeout.
- `contract-validate` (required): validate ChangeSurfaceSet and EvidenceRecord outputs.

## Permissions and approvals

Read only registered repositories at declared SHAs and passed concrete matches. Write only contract/evidence destinations. Mutable refs, content before enumeration/cardinality pass, out-of-scope paths, source writes, evaluator-only state, secrets, self-authorized expansion, and gate mutation are prohibited. Repository-local ownership and access controls remain authoritative.

## Procedure

1. Validate fixed inputs, registry state, immutable pins, selectors, capabilities, permissions, and output collision state.
2. Enumerate path names only; record count and freeze deterministic concrete matches.
3. Apply zero behavior; excess always blocks before content reads.
4. Read only frozen matches within byte/time caps and record exact `repo-id@sha:path#symbol` evidence.
5. Map each surface to criteria, obligations, owner, type, dependencies, disposition, limitations, and materiality.
6. Stop before any new repo/path read; record the discovery and earliest re-entry.
7. Sort, validate, and emit immutable outputs.

## Stopping conditions

Succeed when every passed concrete match is dispositioned and every cap held. Zero follows `BLOCK|RECORD_GAP`; excess always blocks. A new repository/path, changed pin, missing required owner, or missing current evidence stops without reading beyond scope.

## Failure, escalation, and idempotency

Invalid selector re-enters `SELECTOR_PREFLIGHT`; new scope re-enters `CANDIDATE_GENERATION` then selector preflight; missing owner/evidence re-enters `SOURCE_INVESTIGATION`; changed pin re-enters fixed-input preflight. Input tuple includes all upstream refs, pins, selectors, frozen matches, caps, and Skill digest. Identical tuples yield the same surface order/digest; changed scope creates a new revision.

## Completion and evidence

Evidence names exact pins, paths/symbols, method, selector/concrete-match backlink, claim, authority, owner, integrity, limitations, and consulted/excluded paths. Completion includes cap accounting and asserts no out-of-scope/evaluator read.

## Fixtures

- Positive `staged-surface`: API, schema, test, config, and deployment surfaces map to criteria.
- Negative `mutable-or-out-of-scope`: mutable pin, unpassed path, missing mapping, or unowned material surface fails.
- Trigger boundary `zero-and-excess`: zero follows policy; excess blocks before content and records cap evidence.

## Version and provenance

SemVer `1.0.0`; governed by HERM-210/211 and HERM-212 v0.3. Digest coverage excludes only its metadata line. Any permission/selector widening requires a major version and new review.

### Source: `normative/ft-t2/skills/closure-review/SKILL.md`

SHA-256: `c24482c750f3e71c8f6cd2ef98b48e25ae3a5aa7804e54765b68b4cab1253fbd`

---
name: closure-review
description: Independently challenge an exact immutable ClosurePackage and emit ClosureReview without mutating proposal, Spec, or gates.
version: 1.0.0
digest_algorithm: SHA-256
digest: 7bdb07e7b8ca3425d995881726d1ede2aed29cb6e6a533d55004b392320634da
digest_coverage: UTF-8 bytes excluding the digest metadata line
source: HERM-210/HERM-211/HERM-212-v0.3
compatible_runtime: ">=1.0.0 <2.0.0"
owner: fdi-workflow-owner
authority: FT-T2 independent closure review evidence procedure only
status: ACTIVE
review_state: CONTRACT_REVIEWED
reviewer: fdi-governance-reviewer
last_reviewed: 2026-08-31
next_review: 2027-02-28
supersedes: null
superseded_by: null
---

# Purpose and applicability

Use this Skill under an identity and working Context distinct from the investigator to challenge one exact immutable closure proposal and optionally one exact non-gated draft Spec. It emits review evidence only.

## Transition contract

Inputs are exact `ClosurePackage` name/version/revision/digest, optional exact non-gated draft `spec.md` revision/digest or an explicit absence reason, read-only upstream/evidence refs, distinct investigator/reviewer identities and contexts, already authorized selectors, and this Skill digest. Unknown inputs, changed refs, or failed independence stop.

Output is one immutable `ClosureReview@1.0.0` with omissions, unsupported claims, material edges, selector/provenance failures, evidence, limitations, `PASS|FAIL|INCONCLUSIVE`, required actions, and earliest re-entry. It cannot rewrite any input or own/recommend a separate gate.

## Context selection

Resolve minimal governing rules and registries independently. Read only declared artifacts and permitted current evidence. Bounded challenge searches stay under already passed selectors. Do not inherit hidden investigator reasoning, session state, prompts, caches, evaluator answers, ground truth, score state, answer-bearing identifiers, or digests. Record every independent Context selection and limitation.

## Capability bindings

- `artifact-validate` (required): validate exact input refs/digests and contract conformance.
- `independence-check` (required): compare identity, context/session, conflicts, capability boundary, and prohibited mounts.
- `bounded-challenge-search` (optional): read-only, passed selectors only, declared timeout/result/byte caps.
- `claim-backlink-check` (required): check required claims, evidence authority/freshness/integrity, selectors, and cap proofs.
- `contract-validate` (required): validate `ClosureReview@1.0.0` and verdict semantics.

## Permissions and approvals

Read-only review of the exact proposal, optional draft, upstream records, and already authorized evidence; write only review/evidence destinations. Same identity/context, proposal rewrite, Spec editing/finalization, scope widening, selector creation, source mutation, hidden omissions, evaluator-only access, and canonical gate mutation are prohibited.

## Procedure

1. Pin the exact reviewed tuple and verify Skill/capability availability.
2. Verify distinct identity/context, conflict status, and evaluator isolation before reviewing claims.
3. Independently validate provenance, registry state, selectors, concrete matches, caps, and source versions.
4. Challenge candidate/surface/interface omissions, false closure, unsupported `REQUIRED` claims, material edges, owner/mapping gaps, and draft incorporation.
5. Record evidence and limitations; choose `PASS`, `FAIL`, or `INCONCLUSIVE` without optimism.
6. For non-pass, name the earliest exact re-entry and owner/action/completion test; validate and emit immutable review.

## Stopping conditions

`PASS` requires no material defect/gap and sufficient independent evidence. An established material defect yields `FAIL`; insufficient independence, access, capability, or evidence yields `INCONCLUSIVE`. A changed proposal/draft stops and requires a new review.

## Failure, escalation, and idempotency

Findings map only to `INTENT_CLARIFICATION|CANDIDATE_GENERATION|SELECTOR_PREFLIGHT|SOURCE_INVESTIGATION|DEPENDENCY_EXPANSION|CLOSURE_ASSEMBLY|SPEC_AUTHORING`. The tuple of reviewed refs, reviewer identity/context, selected Context/caps, and Skill digest fixes output order/digest. Same tuple returns the existing review; a new proposal or draft cannot reuse prior `PASS`.

## Completion and evidence

Evidence includes independence declaration, exact reviewed refs, every claim/selector/provenance challenge, limitations, ordered findings, action owners, and output digest. Completion explicitly confirms proposal/Spec/gates were not mutated and evaluator-only state was inaccessible.

## Fixtures

- Positive `independent-pass`: exact proposal/draft tuple passes without changing either.
- Negative `same-identity-or-unsupported-pass`: same identity, missing ref, widened scope, or unsupported pass fails.
- Trigger boundary `missing-or-insufficient`: likely missing surface yields `FAIL`/`SOURCE_INVESTIGATION`; insufficient evidence yields `INCONCLUSIVE`.

## Version and provenance

SemVer `1.0.0`; governed by HERM-210/211 and HERM-212 v0.3. Digest coverage excludes only its metadata line. Any weakening of independence or gate boundaries requires a major version and new governance approval.

### Source: `normative/ft-t2/skills/dependency-closure/SKILL.md`

SHA-256: `aa62ced44de6e93b81a9fd07267b290f2e98e83969b8727c2997d69f51fc1044`

---
name: dependency-closure
description: Expand dependency and validation edges within finite bounds and emit an immutable ClosurePackage proposal.
version: 1.0.0
digest_algorithm: SHA-256
digest: ddd07de789f0d34eaa2c5df53ec5502275fad614c186e86957c4a3bbd1fe7a38
digest_coverage: UTF-8 bytes excluding the digest metadata line
source: HERM-210/HERM-211/HERM-212-v0.3
compatible_runtime: ">=1.0.0 <2.0.0"
owner: fdi-workflow-owner
authority: FT-T2 bounded dependency closure proposal procedure only
status: ACTIVE
review_state: CONTRACT_REVIEWED
reviewer: fdi-governance-reviewer
last_reviewed: 2026-08-31
next_review: 2027-02-28
supersedes: null
superseded_by: null
---

# Purpose and applicability

Use this Skill to expand dependencies already authorized by passed selectors and emit one immutable `ClosurePackage@1.x` proposal. `CLOSED_WITHIN_DECLARED_SCOPE` is a producer claim, not a gate or review result.

## Transition contract

Inputs are exact active `IntentSpec` and `ChangeSurfaceSet` refs/digests, current EvidenceRecord refs, registry-qualified pins, passed selectors, positive finite caps for matches/bytes/depth/nodes/edges/evidence, exact Skill digest, and declared output destination. Missing or unbounded inputs fail.

Output is one new immutable `ClosurePackage@1.0.0` with `proposal_state: PROPOSED`, all dispositions, interfaces, validation surfaces, evidence, exclusions, unknowns, source versions, cap accounting, and `OPEN|PARTIAL|CLOSED_WITHIN_DECLARED_SCOPE`. It cannot emit a review or gate.

## Context selection

Select only repository projections and applicable interface/event/schema/data/operations/deployment/validation Product Assets for already surfaced IDs. Registry-first checks require active, fresh, non-superseded entries with owner and digest. Current edge claims require pinned feature-specific evidence. Co-change/history remains a hint. New repositories or paths are recorded but unread until registry validation and a new passed selector. Evaluator-only state is inaccessible.

## Capability bindings

- `finite-worklist` (required): deterministic breadth-first traversal by depth then stable ID; enforce depth/node/edge caps.
- `pinned-file-read` (required): only existing passed concrete matches; enforce total match/byte caps.
- `bounded-name-search` (optional): within authorized concrete scope; declared timeout and result cap.
- `edge-deduplicate` (required): stable identity tuple and deterministic sort.
- `contract-validate` (required): validate `ClosurePackage@1.0.0` and cap/status semantics.

## Permissions and approvals

Read only existing passed concrete matches and governed applicable Context; request re-entry for new scope. Write only proposal/evidence destinations. Unbounded recursion, cap bypass, newly discovered reads, upstream rewrite, reviewer invocation, source mutation, evaluator-only access, global state, and `SPEC_READY` mutation/recommendation are prohibited.

## Procedure

1. Verify inputs, pins, selectors, positive caps, Skill digest, capabilities, and collision state.
2. Initialize a deterministic worklist from confirmed surfaces.
3. Expand callers/consumers, interfaces, events, schemas, data, deployments, validation, and labeled co-change hints.
4. Require current evidence before confirming a current edge; deduplicate and account for every node/edge/read/byte.
5. Stop before reading new scope and create an explicit unknown/re-entry.
6. Disposition every candidate, surface, and edge; assemble interfaces, validation, exclusions, unknowns, and source versions.
7. Compute `OPEN`, `PARTIAL`, or `CLOSED_WITHIN_DECLARED_SCOPE`, validate, and emit without rewriting prior proposals.

## Stopping conditions

Use `CLOSED_WITHIN_DECLARED_SCOPE` only when all material items under declared pins/selectors/caps have supported dispositions. Cap exhaustion or material/unknown uncertainty yields `PARTIAL`. Incomplete preflight/investigation yields `OPEN`. No-progress on the same immutable tuple stops idempotently.

## Failure, escalation, and idempotency

New repo/path re-enters registry/selector preflight; unsupported current edge re-enters `SOURCE_INVESTIGATION`; cap exhaustion requires an owner decision on scope/caps before `DEPENDENCY_EXPANSION`; changed inputs create a new proposal. The normalized upstream refs/pins/selectors/caps/Skill tuple fixes worklist order and digest. Existing proposals are never rewritten.

## Completion and evidence

Evidence includes every edge/current-state claim, selector backlink, cap counter, exclusion, material unknown, source version/digest, and planned validation destination. Completion proves bounded traversal and explicitly states no gate/reviewer/evaluator action occurred.

## Fixtures

- Positive `bounded-recursive`: producer/consumer/interface/deployment/validation edges yield an auditable proposal.
- Negative `self-authorizing-closure`: unbounded selector, missing pin, unresolved material edge marked closed, or new-scope read fails.
- Trigger boundary `cap-and-new-repo`: cap exhaustion yields `PARTIAL`; new repository remains unread pending selector re-entry.

## Version and provenance

SemVer `1.0.0`; governed by HERM-210/211 and HERM-212 v0.3. Digest coverage excludes only its metadata line. Any cap bypass or authority widening is a major incompatible change.

### Source: `normative/ft-t2/skills/feature-intent-analysis/SKILL.md`

SHA-256: `174a0eaa54b5a8df9d48ae59059c46bd04f864918117859ed6ca45a7567c28e4`

---
name: feature-intent-analysis
description: Normalize an authenticated Human signal into IntentSpec material without selecting implementation scope.
version: 1.0.0
digest_algorithm: SHA-256
digest: cf34124d6e009be2548307c1eb924d9a24a78360b43a5d943f2c9331c021c7b3
digest_coverage: UTF-8 bytes excluding the digest metadata line
source: HERM-210/HERM-211/HERM-212-v0.3
compatible_runtime: ">=1.0.0 <2.0.0"
owner: fdi-workflow-owner
authority: FT-T1 intent normalization procedure only
status: ACTIVE
review_state: CONTRACT_REVIEWED
reviewer: fdi-governance-reviewer
last_reviewed: 2026-08-31
next_review: 2027-02-28
supersedes: null
superseded_by: null
---

# Purpose and applicability

Use this Skill only to create a new `IntentSpec@1.x` revision owned by `intention.md`. It preserves Human authority and material ambiguity. It never identifies implementation scope or owns `INTENTION_READY`.

## Transition contract

Required inputs are one authenticated Human signal with immutable source ID, exact applicable Product/Architecture/Domain authority records, this Skill version and verified digest, and the declared output destination. Repository names are accepted only when present in authorized input fragments and remain `HINT_ONLY`. Unknown or extra inputs fail preflight.

The only output is one immutable `IntentSpec@1.0.0` revision plus safe source backlinks at the declared `intention.md` appendix destination. The caller, not this Skill, owns the canonical artifact and gate.

## Context selection

Read the Human signal and minimal fixed authority records first. Registry-first selection may add a reviewed Product Asset or Knowledge item only when its `applies_to` intersects an authorized product/system ID, it is `ACTIVE`, fresh, non-superseded, and its authority dimension is appropriate. Record every selected and excluded ID/revision/digest in the `IntentSpec` provenance destination. Steering and authenticated Human intent outrank explanatory Knowledge; conflicts stop for owner resolution.

Never read source repositories, repository content indexes, evaluator-only state, ground truth, replay results, or answer-bearing digests.

## Capability bindings

- `authenticated-signal-read` (required): read one named signal; input is immutable source ID; output is redacted fragments and authentication evidence; fail closed on missing assurance.
- `governed-context-read` (required): read exact selected authority records; maximum 32 records and 2 MiB; fail on stale, superseded, or unregistered content.
- `contract-validate` (required): validate `IntentSpec@1.0.0` against `contracts/intent-spec.schema.json`; fail with ordered JSON pointers.

Availability of all required capabilities and compatible versions is checked before any interpretation.

## Permissions and approvals

Read only named inputs and write only the proposed `IntentSpec` destination. Human/product authority is required for desired behavior. Network access, external-audience actions, destructive operations, source changes, secrets, raw authentication material, canonical gate mutation, and evaluator-only access are prohibited.

## Procedure

1. Verify signal identity, authentication, Skill digest, capabilities, authority, and output collision state.
2. Extract outcome and observable behaviors without adding requirements.
3. Allocate stable behavior and criterion IDs; map every source fragment forward.
4. Separate authorized scope, constraints, non-goals, assumptions, and repository hints.
5. Represent every material ambiguity as an explicit unknown with owner, resolution condition, and `INTENT_CLARIFICATION` re-entry.
6. Sort ID sets, validate the contract, record consulted/excluded Context, and emit a new immutable revision.

## Stopping conditions

Succeed only when outcome, behaviors, criteria, authority, backlinks, and every material ambiguity are represented. Stop blocked when identity, authority, or desired behavior is ambiguous. Never guess to obtain a valid output.

## Failure, escalation, and idempotency

Identity/authority ambiguity re-enters FT-T1 Human clarification; an authority conflict goes to the named owner; schema failure reruns after correction. The input tuple is signal ID/revision/digest + sorted Context revisions/digests + Skill version/digest. The same tuple yields byte-equivalent normalized content. An existing identical output is returned without rewrite; changed authorization creates a new revision and stales dependent records.

## Completion and evidence

Completion evidence includes authentication assurance, exact signal-fragment backlinks, selected/excluded Context proofs, validation result, output digest, and limitations. It must show that no repository was confirmed/excluded and no source/evaluator read occurred.

## Fixtures

- Positive `multi-criterion`: explicit constraints/non-goals produce a valid record with no implementation scope.
- Negative `guessed-ambiguity`: silent guessing or `CONFIRMED` repository state is rejected.
- Trigger boundary `repository-hint-only`: a named repository remains `HINT_ONLY`; any attempted content-read authorization is rejected.

## Version and provenance

SemVer `1.0.0`; source is the approved HERM-210 design, HERM-211 plan, and HERM-212 v0.3 bundle. Digest verification uses the declared coverage rule. Backward-incompatible input/output or authority changes require a major version and supersession record.

### Source: `normative/ft-t2/skills/repo-discovery/SKILL.md`

SHA-256: `502d1c4f63f5fc4e76c87266e9f2aa13c24caa6dae0d1442644ee4904373247f`

---
name: repo-discovery
description: Produce a high-recall CandidateRepoSet from governed registries and Product Intelligence without authorizing source reads.
version: 1.0.0
digest_algorithm: SHA-256
digest: dc3e5ee502151015df912f8fc09d51d89264d079afc43175ec3c60caa3dbe1a8
digest_coverage: UTF-8 bytes excluding the digest metadata line
source: HERM-210/HERM-211/HERM-212-v0.3
compatible_runtime: ">=1.0.0 <2.0.0"
owner: fdi-workflow-owner
authority: FT-T2 candidate repository discovery procedure only
status: ACTIVE
review_state: CONTRACT_REVIEWED
reviewer: fdi-governance-reviewer
last_reviewed: 2026-08-31
next_review: 2027-02-28
supersedes: null
superseded_by: null
---

# Purpose and applicability

Use this Skill to produce one `CandidateRepoSet@1.x` from an exact active `IntentSpec`. It maximizes investigation recall while preserving uncertainty and never grants source-content access.

## Transition contract

Inputs are the exact `IntentSpec` name/version/revision/digest, active repository and Product Intelligence registries, applicable selected assets, a discovery policy with finite `max_candidate_repositories`, and this Skill version/digest. Unknown inputs, stale registries, missing digests, or an inactive Intent fail.

Output is one immutable `CandidateRepoSet@1.0.0` revision with introduction refs, rationale, ordering score, state, current evidence, limitations, unknowns, caps, and stable order. No selector or repository read permission is emitted.

## Context selection

Read repository/Product Asset registries before leaves. Select only entries that are `ACTIVE`, applicable, fresh, non-superseded, owner-attributed, and digest-verified. Product, Architecture, Delivery History, Knowledge, and Reference assets may introduce candidates; stale/draft assets require a declared investigative exception and cannot confirm or exclude. Record registry revision, entry ID, selection reason, trust/freshness, and exclusions in discovery evidence.

Ground truth, validation fixtures, replay outputs, answer-bearing metadata/digests, and repository file contents are inaccessible.

## Capability bindings

- `registry-read` (required): exact registry revision and entry enumeration; maximum 16 registries and 10,000 entries.
- `governed-leaf-read` (required): read selected Product Assets; maximum 128 leaves and 8 MiB.
- `bounded-name-search` (optional): lexical/semantic name-only search when policy permits; hard timeout 60 seconds and declared result cap.
- `contract-validate` (required): validate against `contracts/candidate-repo-set.schema.json` with ordered failures.

## Permissions and approvals

Read-only access to governed discovery inputs; write only candidate/evidence destinations. Source repository content, unregistered repositories, mutable refs, secrets, source writes, gate mutation, evaluator-only state, and external actions are prohibited. An exception to inspect stale discovery context requires the named governance owner and stays non-authoritative.

## Procedure

1. Validate Intent, registry revisions, policy/caps, Skill digest, capabilities, and output collision state.
2. Enumerate authorized hints and registry/Product Asset relationships.
3. Run only declared bounded name searches; record method, caps, and result count.
4. Merge candidates by stable repository ID while preserving every introduction source.
5. Classify `CANDIDATE|CONFIRMED|EXCLUDED|UNRESOLVED`; require current feature-specific evidence for the middle two.
6. Retain plausible uncertain candidates, compute priority scores without granting authority, sort by score then repository ID, validate, and emit.

## Stopping conditions

Succeed after all declared sources/caps are exhausted and every candidate is supported or explicitly unresolved. Missing/stale registry or cap excess blocks. An unregistered repository stops as `UNRESOLVED` without source access.

## Failure, escalation, and idempotency

Missing registry re-enters fixed-input preflight; new/unregistered candidates re-enter candidate generation/registry validation; authority conflicts go to the owner. Input tuple is Intent ref + registry/asset digests + policy/caps + Skill digest. Identical input yields the same de-duplicated order; output collision returns the existing digest; new evidence creates a new revision.

## Completion and evidence

Evidence records all introduction sources, registry states, searches/caps, limitations, and current evidence for `CONFIRMED|EXCLUDED`. Completion explicitly states no repository content was read and scores were not used as authority.

## Fixtures

- Positive `registered-and-unresolved`: registered and unresolved candidates retain stable order.
- Negative `score-as-authority`: score or stale asset alone cannot produce `CONFIRMED`.
- Trigger boundary `unregistered-repository`: record `UNRESOLVED`, deny content access, and re-enter registry/selector preflight.

## Version and provenance

SemVer `1.0.0`; governed by HERM-210/211 and HERM-212 v0.3. Digest verification excludes only the digest metadata line. Any change that widens source access or confirmation authority is backward-incompatible.

### Source: `normative/ft-t2/workflow/feature-closure.md`

SHA-256: `06e8d4794e87c266793369763f952a60cead43ba5e1f669b26b58717caf8e26e`

# Feature Closure manual/agent-driven workflow contract

Version: `1.0.0`
Lifecycle: `ACTIVE`
Owner: `fdi-workflow-owner`
Governing sources: HERM-210, HERM-211, HERM-212 v0.3
Execution-verified: `NOT_CLAIMED`

## Role and canonical boundary

Feature Closure is the bounded ChangeSurface discovery/closure subworkflow inside FT-T2, not an engine, orchestrator, service, scheduler, database, UI, control plane, global state owner, fifth Layer 1 transition, or canonical artifact.

```text
Human -> Intention -> Delivery Spec -> Change Set -> Verification & Validation Report
                     ^
                     FT-T2 internal Feature Closure

intention.md / IntentSpec
  -> CandidateRepoSet
  -> passed SourceScopeSelector[]
  -> ChangeSurfaceSet + EvidenceRecord[]
  -> immutable ClosurePackage proposal
  -> independent ClosureReview
  -> accountable FT-T2 Spec finalization
  -> sole SPEC_READY decision in spec.md
```

`IntentSpec` belongs to `intention.md`. `CandidateRepoSet`, `ChangeSurfaceSet`, and `ClosurePackage` are governed `spec.md` appendices. `EvidenceRecord` is a governed evidence appendix. `ClosureReview` contributes evidence to finalization. Under the adopted `.fdi/` deployment profile, `spec.md` is represented by `.fdi/features/{feature-id}/spec/index.md` plus its fixed bundle members; the sole gate remains `.fdi/features/{feature-id}/spec/index.md#gate-record`.

## Fixed-input preflight envelope

Before Step 1, the accountable Spec agent records and validates all of these as fixed inputs:

- exact active `intention.md` and `IntentSpec` version/revision/digest and the canonical Intention gate result;
- all six contract schema versions/digests and all five Skill versions/digests, owners, `ACTIVE` lifecycle, current review, and compatible runtime;
- exact repository, Product Asset, and Skill registry revisions and applicable authority policies;
- exact capability IDs/versions, availability, permissions, repository owners, independent reviewer requirement, and evidence destinations;
- immutable revision and POSIX-relative path grammar, stable ID grammar, explicit unknown policy, canonical ordering/serialization, supersession, and conflict rules;
- positive finite `max_candidate_repositories`, `max_matches`, `max_total_bytes`, `max_expansion_depth`, `max_nodes`, `max_edges`, `max_evidence_records`, and `max_review_attempts`;
- validation-only access denial for investigators/reviewers and prohibition on source-content reads before selector syntax/authority and cardinality gates pass.

A missing, stale, superseded, unauthorized, mutable, unavailable, or conflicting material input yields `NOT_CONTRACT_READY`, names the owner and exact earliest re-entry, and stops. No hidden runtime state repairs a failed preflight.

## Ordered handoffs

| Step | Responsible agent / exact Skill | Exact inputs | Exact outputs | Completion | Failure and earliest re-entry |
| --- | --- | --- | --- | --- | --- |
| 1. Intent normalization | Intent agent / `skills/feature-intent-analysis/SKILL.md` | Authenticated Human signal; governing desired-behavior records | New `IntentSpec` revision owned by `intention.md`; safe backlinks | Outcome, behavior, criteria, authority, constraints, non-goals, and unknowns explicit; repositories remain hints | Desired-behavior ambiguity -> `INTENT_CLARIFICATION` |
| 2. Candidate generation | Discovery agent / `skills/repo-discovery/SKILL.md` | Exact Intent; exact registries/assets; discovery policy and cap | New `CandidateRepoSet` revision and discovery evidence | Every candidate has origin, rationale, state, evidence/limitations; uncertain candidates retained | Missing registry -> fixed-input preflight; unregistered repo -> `UNRESOLVED`, no content read |
| 3. Selector preflight | Accountable Spec agent with investigation Skill | Completed upstream refs; authorized repository registry/pins; selector policy | Versioned `SourceScopeSelector[]`; syntax/authority result; name enumeration count; cardinality result; concrete-match destination | Each repo/pin/root/template/extension/exclusion/cap/zero/excess rule declared and passed before content | Invalid/zero-blocking/excess -> `SELECTOR_PREFLIGHT`; excess always blocks |
| 4. Investigation | Investigator / `skills/changesurface-investigation/SKILL.md` | Passed selectors, immutable pins, frozen concrete matches | New `ChangeSurfaceSet` and `EvidenceRecord[]` | Every match mapped to criterion/obligation/owner/disposition/current evidence | New repo/path -> stop before read, then `CANDIDATE_GENERATION`/`SELECTOR_PREFLIGHT`; evidence gap -> `SOURCE_INVESTIGATION` |
| 5. Dependency expansion | Closure investigator / `skills/dependency-closure/SKILL.md` | Exact surface/evidence refs; existing passed selectors; finite caps | Immutable `ClosurePackage` with `proposal_state: PROPOSED` | Honest `OPEN|PARTIAL|CLOSED_WITHIN_DECLARED_SCOPE`; all scoped items dispositioned or explicit unknown | New scope -> selector preflight; cap/material gap -> `PARTIAL` and `DEPENDENCY_EXPANSION`; incomplete input -> `OPEN` |
| 6. Independent review | Distinct reviewer / `skills/closure-review/SKILL.md` | Exact immutable proposal; optional exact non-gated Spec draft; permitted evidence only | Immutable `ClosureReview` | `PASS|FAIL|INCONCLUSIVE`, evidence/limitations/actions, exact re-entry | Same identity/context or access gap -> `INCONCLUSIVE`; material defect -> `FAIL`; changed tuple invalidates review |
| 7. FT-T2 finalization | Accountable Spec agent, not reviewer | Active Intent; exact proposal/review; evidence/mappings/owner handshakes; complete draft | Final `spec.md` and registered appendices; canonical gate record | All FT-T2 conditions pass for the exact revision; Spec agent records sole `SPEC_READY` | Any failed condition -> earliest affected step; `FAIL|INCONCLUSIVE` never becomes ready |

Every handoff pins contract name/version/record/revision/digest. The receiver rejects unexpected fields, versions, stale lifecycle, missing evidence, or changed bytes.

## Selector and source boundary

The selector preflight order is fixed:

1. read only fixed artifact/registry inputs;
2. write the selector draft with derivation anchors, repo ID, immutable SHA, root, exact path/template, allowed extensions, exclusions, and positive cap;
3. validate syntax, registry membership, authority, pin, and ownership before repository access;
4. enumerate path names only at the pin;
5. record count and pass cardinality (`zero` follows declared `BLOCK|RECORD_GAP`; excess always blocks);
6. freeze the concrete matches and only then read their content;
7. record exact `repo-id@sha:path#symbol` matches and evidence in the outputs.

New scope discovered at any later step is recorded without reading. It returns to candidate generation and selector preflight. Final surfaces never authorize their own discovery.

## Proposal, review, and finalization independence

`dependency-closure` writes a new proposal revision and never rewrites it. `closure-review` uses a different identity and isolated Context, pins the exact proposal/draft tuple, cannot widen scope, and writes a separate review. Corrections create new upstream/proposal revisions and a new review. A `PASS` review is necessary but insufficient: only the accountable Spec agent finalizes the canonical Spec and owns the existing gate.

Reviewer and investigator cannot access `validation/features/*/evaluator-only/**`, ground truth, answer-bearing metadata/digests, scorer outputs, or hidden prompts/session state. Evaluation tooling enforces this with disjoint input roots; the workflow contract does not rely on an in-memory flag.

## Sole SPEC_READY decision

The Spec agent may record `SPEC_READY` only when the exact finalized revision satisfies all conditions:

- active Intent and every criterion map bidirectionally to requirement, design obligation, task, owner, ChangeSurface/repository, and planned V&V evidence;
- every registry, pin, selector, concrete-match count, and finite cap passed;
- every material candidate/surface/edge/interface/validation obligation has a supported disposition and required current evidence;
- exclusions, conflicts, limitations, and unknowns are explicit, with no hidden material unresolved item;
- proposal is `CLOSED_WITHIN_DECLARED_SCOPE` and independent review is `PASS` for the exact active tuple;
- cross-repository owner handshakes preserve source-repository authority;
- contract/Skill/Product Asset/source versions and supersession state are pinned; and
- re-entry/downstream invalidation rules and evidence destinations are complete.

`OPEN`, material `PARTIAL`, `FAIL`, `INCONCLUSIVE`, invalid selector/provenance, stale review, missing owner/current evidence, or an inaccessible required source forbids `SPEC_READY`. This workflow never emits a competing readiness recommendation.

## Re-entry, invalidation, retries, and idempotency

| Trigger | Earliest re-entry | Invalidated records |
| --- | --- | --- |
| New/revised desired behavior | `INTENT_CLARIFICATION` | All dependent FT-T2 records/finalization |
| New repository | `CANDIDATE_GENERATION`, then selector preflight | Candidate/surface/proposal/review |
| Invalid, zero-blocking, or excess selector | `SELECTOR_PREFLIGHT` | Concrete matches and downstream reads |
| Missing/stale current finding | `SOURCE_INVESTIGATION` | Affected surfaces/edges/proposal/review |
| New/material dependency or cap decision | `DEPENDENCY_EXPANSION` | Proposal/review |
| Assembly/disposition/backlink error | `CLOSURE_ASSEMBLY` | Proposal/review |
| Review incorporation or Spec mapping defect | `SPEC_AUTHORING` | Spec draft/finalization unless evidence changed |
| FT-T3 out-of-scope discovery | Corresponding FT-T2 step before read/write | Exact readiness revision and dependent FT-T3 work |

Retries cannot exceed `max_review_attempts` or other declared caps. A retry must change a named input/evidence/gap. Replaying an identical immutable tuple returns the existing digest and does not count as progress. Exhausted caps stop honestly as `OPEN|PARTIAL` and/or `FAIL|INCONCLUSIVE`.

## Permissions, stopping, and observable evidence

Allowed actions are declared Context reads, name enumeration at pins, reads of passed matches, new contract/evidence revisions at declared destinations, clarification/owner requests, and bounded stop/re-entry.

Prohibited actions are source mutation, unpassed reads, mutable refs, unbounded traversal, self-authorized scope, secrets/unsafe paths, evaluator-answer access, proposal/Spec mutation by reviewer, merge/deploy/release/publication, global workflow state, or service/database/scheduler behavior.

Every step records fixed inputs, selected/excluded Context, capability/permission checks, exact reads, caps, ordered outputs, validation result, retries, limitations, earliest re-entry, and output digest at declared artifact/evidence destinations. No hidden state is required to reconstruct a dry chain.

## Acceptance fixtures

`tests/fixtures/workflow/cases.json` freezes six dry-chain cases:

- `complete`: only declared artifacts traverse all handoffs; the Spec agent alone records a supported `SPEC_READY`.
- `open`, `partial`, review `fail`, and review `inconclusive`: each is barred from readiness.
- `out-of-scope`: source access stops before read and re-enters `SELECTOR_PREFLIGHT`.

Tests also reject reviewer proposal/Spec mutation, widened scope, reused review after proposal revision, hidden-state dependency, or any new gate owner.

## L2-FWK — layer2_framework

- Semantic version: `0.1`
- Approval: `HERM-210; multica-attachment:01a05228-a42d-72fa-b388-558f59430632`
- Compatibility: `L1-SEM@0.2; L2-PROFILE@0.1; L2-MAINT@0.1`

### Source: `normative/layer2/framework/fdi-layer2-product-intelligence-framework-v0.1-approved.md`

SHA-256: `167b0bbe88112fd7a895c10a64be977f2f7dd4ba7678c81818be79e38de1e165`

# FDI Layer 2 — Product Intelligence Asset Framework v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Primary actor:** Frontier Team; Agents may assist under governed maintenance contracts  
> **Scope:** Durable Product Assets that make Layer 1 agent execution more accurate, reusable, and product-aware  
> **Design only:** No crawler, graph engine, builder implementation, validator, repository mutation, or runtime execution claim  
> **Non-goal:** Turn every source into Markdown, build a complete enterprise knowledge graph, or move feature-specific execution state into Layer 2

---

## 0. Purpose

Layer 1 defines **how Agents deliver a feature**:

```text
Human Signal
    |
    v
FT-T1 Intention Skill
    |
    v
intention.md
    |
    v
FT-T2 Delivery Spec Skill
    |
    v
spec.md
    |
    v
FT-T3 Implementation Skill
    |
    v
implementation.md
    |
    v
FT-T4 Correctness Skill
    |
    v
correctness.md
```

Layer 2 defines **what durable Product Intelligence the Frontier Team maintains so those Skills can execute well**.

```text
Distributed Product Sources
        |
        v
Frontier-Team-Maintained Product Assets
        |
        | selectively resolved for one execution
        v
Execution Context
        |
        v
Layer 1 f_skill
```

The central distinction is:

> **Product Asset is durable and product-scoped. Context is an execution-specific view of Product Assets and qualified direct references.**

Layer 2 therefore does not own Layer 1 feature artifacts. It owns reusable product intelligence that persists across many features.

---

# Contract P1 — Layer Boundary

## P1.1 Layer 1 responsibility

Layer 1 owns:

- feature-specific canonical flow;
- `intention.md`, `spec.md`, `implementation.md`, `correctness.md`;
- `f_skill` transformation contracts;
- feature-specific Change Surface findings;
- execution Context requirements and resolved Context provenance;
- feature lifecycle, gates, invalidation, re-entry, traceability, and correctness.

## P1.2 Layer 2 responsibility

Layer 2 owns:

- durable product/system knowledge needed repeatedly across features;
- governed product structure and navigation assets;
- product architecture and domain assets;
- reusable delivery-history intelligence;
- operations and governance knowledge needed by delivery agents;
- provenance, ownership, lifecycle, trust, and maintenance semantics for those assets.

## P1.3 Layer 2 MUST NOT

Layer 2 MUST NOT:

- become a fifth Layer 1 transition;
- own feature-specific Intention, Spec, Implementation, or Correctness authority;
- store feature-specific temporary reasoning as durable Product Intelligence by default;
- treat an inferred or historical relationship as current product truth without qualification;
- require a complete dependency graph before Layer 1 can execute;
- require every Product Asset to be copied into an FDI-owned Markdown file;
- allow an Agent-generated summary to gain organizational authority merely because it was materialized;
- silently mutate a Layer 1 artifact when a Product Asset changes.

---

# Contract P2 — Semantic Model

## P2.1 Core entities

| Entity | Meaning |
| --- | --- |
| **Source** | Existing system of record or evidence source: repositories, service catalogs, ADRs, Feature/Backlog systems, PRs, runbooks, standards, etc. |
| **Product Asset** | Durable, governed, reusable product intelligence maintained for repeated use across features. An Asset may be materialized content or a governed registration of an authoritative external source. |
| **Product Asset Descriptor** | The uniform governed metadata envelope that gives an Asset stable identity, scope, authority, provenance, lifecycle, trust, freshness, and selection metadata independent of storage form. |
| **Product Asset Ref** | Stable reference to one exact Product Asset semantic revision and its descriptor/content or referenced source. |
| **Execution Context** | The bounded execution-specific set of Product Asset Refs and qualified direct references selected to satisfy one Layer 1 Skill's `ContextRequirement`. |
| **EvidenceRef** | Claim-specific evidence used by Layer 1 to establish a finding or verdict; it is not the same as a Product Asset Ref. |
| **Asset Maintainer** | Frontier Team role, delegated product authority, or accountable maintenance role responsible for keeping an Asset semantically useful and appropriately current. |
| **Asset Maintenance Skill** | Governed procedure that may assist creation, extraction, reconciliation, validation, or refresh of a Product Asset. |

## P2.2 Fundamental relation

```text
Product Asset
  = Product Asset Descriptor
    + materialized content OR governed source reference

Execution Context
  = Select(
      Product Asset Refs,
      qualified bounded direct references,
      Layer 1 ContextRequirement
    )
```

Layer 1 may conceptually execute:

```text
OutputBundle = f(
    CanonicalInput(s),
    FT-Skill@revision
    ; ExecutionContext
)
```

Layer 1 does not need to know how an Asset was built or where its content is stored. It depends only on the resolved Asset/reference contract: identity, exact revision/as-of state, authority dimension, provenance, applicability, trust profile, freshness, and lifecycle eligibility.

# Contract P3 — Product Asset Descriptor and Content Contract

Every durable Product Asset MUST have a stable `ProductAssetDescriptor`, regardless of whether the Asset is Markdown, another materialized representation, or a governed reference to an existing authoritative artifact.

A materialized Asset MAY embed this descriptor as frontmatter. A `REFERENCED` Asset MAY keep the descriptor only in the Product Intelligence registry while its semantics remain in the referenced source.

A descriptor MUST expose metadata equivalent to:

```yaml
fdi_asset_version: "0.1"
asset_id: "<stable-id>"
asset_family: "PRODUCT|ARCHITECTURE|CODEBASE|DOMAIN|DELIVERY_HISTORY|OPERATIONS|KNOWLEDGE|REFERENCE"
asset_type: "<specific-type>"
asset_revision: <positive-integer>
content_ref: "<materialized-content-ref-or-governed-source-ref>"

publication_state: "DRAFT|PUBLISHED|RETIRED"
validity_state: "NOT_APPLICABLE|ACTIVE|STALE|SUPERSEDED"

owner: "<frontier-team-role-or-delegated-authority>"
maintenance_mode: "CURATED|DERIVED|REFERENCED"
publication_policy: "HUMAN_APPROVAL|RULE_BASED_AUTO|SOURCE_REFERENCE"

scope:
  products: []
  systems: []
  repositories: []
  environments: []

authority_dimensions: []
trust_profile:
  provenance: "DIRECT|DERIVED|ASSERTED"
  review: "UNREVIEWED|REVIEWED"
  verification: "NOT_VERIFIED|VERIFIED"
  authorization: "NONE|SOURCE_INHERITED|EXPLICIT"

as_of: "<time-or-source-state>"
source_refs: []
dependency_refs: []

freshness_policy:
  mode: "UNTIL_SUPERSEDED|SOURCE_CHANGE|TTL|EVENT_DRIVEN|MANUAL"
  ttl: null

supersedes: null
invalidation_triggers: []
selection_metadata:
  terms: []
  applicability: []
```

## P3.1 Asset revision versus source revision

`asset_revision` identifies the semantic revision of the Product Asset descriptor/content contract. Source versions are pinned independently in `source_refs`.

For a `REFERENCED` Asset, `asset_revision` versions the FDI registration/selection metadata; it does **not** replace the referenced source's own revision/version authority.

Once an Asset revision has been `PUBLISHED`, its semantic content and provenance bindings are immutable. A semantic change creates a new `asset_revision`. Lifecycle changes such as `ACTIVE -> STALE` or `ACTIVE -> SUPERSEDED` do not by themselves create a new semantic revision.

## P3.2 Required Asset semantics

Every durable Asset MUST make reviewable, either in its content or descriptor:

1. what reusable product knowledge it provides;
2. what it explicitly does not claim;
3. source/provenance references with source revision/as-of semantics;
4. dependencies on other Product Assets where materially derived from them;
5. authority dimensions;
6. trust profile;
7. scope and applicability;
8. current Asset revision and as-of semantics;
9. known limitations or incompleteness;
10. freshness policy, invalidation, and supersession rules;
11. ownership and maintenance responsibility;
12. selection metadata sufficient for bounded Layer 1 retrieval;
13. publication state and publication policy.

## P3.3 Authority and trust invariants

> **Asset existence does not create authority.**

Authority derives from the underlying source, organizational authorization, review path, derivation method, scope, and the claim being made.

Trust is **faceted, not a single global ranking**:

- `provenance` distinguishes direct, derived, and unsupported/asserted semantics;
- `review` records whether an accountable review occurred;
- `verification` records whether the represented claim was independently checked against its declared sources/evidence;
- `authorization` records whether an accountable authority adopted the Asset for an applicable authority dimension.

A selector MUST evaluate the facets required by the Layer 1 `ContextRequirement`. These facets do not form one global ranking; for example, `EXPLICIT` authorization and `VERIFIED` source checking answer different questions.

When Layer 2 produces Layer 1 `ResolvedContextRef.trust_state`, it MAY serialize or summarize this trust profile, but the underlying facets remain reviewable.

Examples:

- an approved architecture principle may have `DIRECT + REVIEWED + NOT_VERIFIED + EXPLICIT` and be authoritative for durable architecture constraints;
- a derived repository index may have `DERIVED + UNREVIEWED + VERIFIED + NONE` and be excellent navigation intelligence while still not proving feature-specific impact;
- a historical delivery record may be authoritative about what happened historically but not about what must change now.

## P3.4 Layer 2 authority dimensions

Layer 2 Product Assets MAY declare only support/constraint authority that is compatible with the approved Layer 1 model:

| Layer 2 authority ID | Layer 1 meaning |
| --- | --- |
| `DURABLE_CONSTRAINT` | Applicable governed organizational, architecture, domain, operations, or adopted reference constraint |
| `CURRENT_BEHAVIOR_SUPPORT` | Navigation/current-state support used to guide investigation; current feature truth still requires Layer 1 pinned `EvidenceRef` when material |
| `RATIONALE_SUPPORT` | Historical rationale, patterns, learnings, and supporting knowledge |

A Product Asset MUST NOT claim Layer 1 `DESIRED_OUTCOME`, `TECHNICAL_OBLIGATION`, or `PROCEDURE` authority. Those remain owned respectively by the active Intention, active Spec, and active governed Skill/capability contract.

Asset family does not determine authority automatically; each Asset declares the dimensions justified by its sources, scope, and publication path.

# Contract P4 — Asset Maintenance Modes

Layer 2 defines three durable Asset maintenance modes.

## P4.1 `CURATED`

Used when the Product Asset itself is maintained by an accountable Frontier Team or organizational authority.

Typical examples:

- product boundaries and capability definitions;
- architecture principles;
- approved domain rules;
- technology/governance constraints.

Conceptually:

```text
Authorized product/organization knowledge
        |
        | accountable curation/review
        v
Durable Product Asset
```

Agents MAY assist drafting or diff analysis, but MUST NOT manufacture organizational authority.

## P4.2 `DERIVED`

Used when a durable Product Asset is extracted, normalized, correlated, or summarized from governed sources.

```text
ProductAsset
=
f(
  SourceInputs,
  PA-Maintenance-Skill@revision
  ; SupportingAssetRefs
)
```

Typical examples:

- repository inventory;
- historical delivery records;
- known high-value codebase relations;
- normalized operations inventory.

Derived Assets MUST preserve source backlinks and their derived status.

## P4.3 `REFERENCED`

Used when an existing governed artifact is already the correct durable source and FDI only needs to register/index it.

Examples:

- canonical OpenAPI/protobuf contracts;
- approved ADRs;
- canonical runbooks;
- external standards;
- repository-local engineering instructions.

Layer 2 SHOULD store reference metadata rather than copying the content merely to conform to an FDI directory layout.

## P4.4 `RESOLVED` is not a Product Asset maintenance mode

`RESOLVED` belongs to **Layer 1 Context consumption**, not Layer 2 durable asset maintenance.

An execution may dynamically resolve current source evidence when no durable Asset is sufficient:

```text
Layer 1 ContextRequirement
        |
        v
Product Asset selection
        +
qualified bounded direct source lookup
        |
        v
Execution Context
```

The result may later motivate a new Product Asset, but it does not automatically become one.

---

# Contract P5 — Product Asset Families

Layer 2 recommends seven core Product Intelligence families plus an optional Reference family.

```text
Product Intelligence
├── Product
├── Architecture
├── Codebase
├── Domain
├── Delivery History
├── Operations
├── Knowledge
└── Reference
```

These are semantic families, not mandatory directories or exhaustive file bundles.

---

## P5.1 Product Assets

### Purpose

Describe the product from a persistent capability and boundary perspective.

### Typical reusable knowledge

- product/platform purpose;
- capabilities;
- product/system boundaries;
- users/actors;
- stable terminology;
- product-level constraints;
- ownership at product/system level.

### Typical upstream sources

- approved product/platform definitions;
- capability maps;
- organization/product ownership sources;
- approved product documentation.

### Typical maintenance mode

Primarily `CURATED`, optionally `REFERENCED`.

### Layer 1 consumers

Primarily T1 and T2; T4 where product-level intended-use interpretation matters.

### Example logical assets

```text
product/index.md
product/capabilities.md
product/boundaries.md
```

---

## P5.2 Architecture Assets

### Purpose

Capture durable architecture rules and system-level structure that repeatedly constrain feature delivery.

### Typical reusable knowledge

- architecture principles;
- system boundaries;
- interface conventions;
- approved technology choices;
- integration patterns;
- architecture invariants;
- cross-system ownership rules.

### Typical upstream sources

- approved ADRs;
- architecture principles;
- platform standards;
- architecture review decisions.

### Typical maintenance mode

`CURATED` and `REFERENCED`.

### Layer 1 consumers

T2 and T3 primarily; T4 when architecture constraints are explicit V&V obligations.

### Important authority rule

An Agent MAY infer an architectural observation from code, but it MUST NOT turn that observation into an architecture rule without the appropriate authority/review state.

---

## P5.3 Codebase Assets

### Purpose

Make the product's code estate navigable enough for bounded feature investigation.

### Recommended minimal Asset

```text
codebase/index.md
```

### Minimum useful content

For each known repository/system/component:

```yaml
repo:
  repo_id: "..."
  canonical_ref: "..."
  product_system: []
  owner_refs: []
  languages_platforms: []
  known_entrypoints: []
  known_contract_refs: []
  source_revision_or_as_of: "..."
```

### Typical upstream sources

- repository inventory;
- ownership/CODEOWNERS;
- service catalog;
- build/package manifests;
- deployment metadata;
- repository-local descriptors.

### Typical maintenance mode

Primarily `DERIVED`, optionally augmented with `CURATED` or `REFERENCED` metadata.

### Known Relation Assets

Layer 2 MAY maintain high-value relation indexes such as:

```text
repo-A --API--> repo-B
repo-C --CONSUMES_EVENT--> repo-D
repo-E --OWNS_SCHEMA--> contract-X
```

Every materialized relation MUST preserve:

```yaml
relation:
  relation_id: "..."
  from: "..."
  to: "..."
  relation_type: "API|EVENT|SCHEMA|PACKAGE|CONFIG|DEPLOYMENT|DATA|OTHER"
  source_refs: []
  as_of: "..."
  provenance_state: "DIRECT|DERIVED"
  review_state: "UNREVIEWED|REVIEWED"
  verification_state: "NOT_VERIFIED|VERIFIED"
  completeness: "PARTIAL|BOUNDED|UNKNOWN"
```

### Critical boundary

> **Codebase Asset relations are navigation intelligence, not a promise of a complete current dependency graph.**

They may generate Layer 1 T2 candidates. Feature-specific `CONFIRMED` Change Surface findings still require current applicable evidence under Layer 1.

### Layer 1 consumers

T1 for high-level orientation; primarily T2 and T3; T4 when source ownership or candidate coverage matters.

---

## P5.4 Domain Assets

### Purpose

Represent stable business/domain semantics that should not be rediscovered for every feature.

### Typical reusable knowledge

- vocabulary;
- business rules;
- invariants;
- regulated constraints;
- canonical domain models;
- business ownership.

### Typical upstream sources

- approved domain documentation;
- business policy;
- regulatory rules;
- canonical domain definitions;
- subject-matter authority decisions.

### Typical maintenance mode

`CURATED`, `REFERENCED`, or reviewed `DERIVED`.

### Trust boundary

A derived domain summary MUST remain `DERIVED` until the appropriate authority/review process gives it stronger status.

### Layer 1 consumers

T1/T2/T4 primarily; T3 where requirements map directly to domain invariants.

---

## P5.5 Delivery History Assets

### Purpose

Turn prior product delivery experience into reusable search and change-pattern intelligence.

### Primary upstream sources

```text
Historical Feature / Epic
+ Backlog / Issues
+ PRs
+ Commits
+ Review history
+ CI/Test
+ Release/deployment evidence when available
```

These sources are **upstream of the durable Delivery History Asset**, not Layer 1 canonical inputs.

### Typical maintenance mode

`DERIVED`.

### Conceptual production

```text
HistoricalDeliveryAsset
=
f(
  Historical Feature,
  Backlog,
  PRs,
  Commits,
  Reviews,
  Delivery Evidence,
  PA-Historical-Delivery@revision
)
```

### Recommended shape

```text
delivery-history/
├── index.md
└── records/{historical-feature-id}.md
```

### Minimum historical record

```yaml
historical_delivery:
  historical_feature_id: "..."
  feature_semantics:
    product_system: []
    capability_terms: []
    requirement_terms: []
  delivery:
    repos_touched: []
    paths_touched: []
    change_types: []
    interface_impacts: []
  source_refs:
    feature: []
    backlog: []
    prs: []
    commits: []
    reviews: []
  delivered_as_of: "..."
  trust_profile:
    provenance: "DERIVED"
    review: "UNREVIEWED|REVIEWED"
    verification: "NOT_VERIFIED|VERIFIED"
    authorization: "NONE"
```

### Authority

Delivery History Assets can establish or rank **historical delivery facts/patterns**.

They MAY help T2 generate candidates:

```text
similar historical feature
        -> historically touched repo
        -> T2 candidate
```

They MUST NOT by themselves establish:

```text
historically touched repo
        -> current CONFIRMED impacted repo
```

Current feature-specific applicability remains a Layer 1 responsibility.

### Layer 1 consumers

Primarily T2 candidate discovery and investigation prioritization.

---

## P5.6 Operations Assets

### Purpose

Represent persistent operational constraints that repeatedly affect delivery.

### Typical reusable knowledge

- environments;
- deployment/release controls;
- runtime topology where governed;
- observability conventions;
- SLO/SLA;
- rollback rules;
- operational ownership;
- data/runtime constraints.

### Typical upstream sources

- canonical runbooks;
- environment definitions;
- deployment systems;
- release policy;
- observability/platform standards.

### Typical maintenance mode

Primarily `REFERENCED` and `CURATED`; indexes may be `DERIVED`.

### Boundary

Runtime observations used to establish a feature-specific correctness claim remain Layer 1 `EvidenceRef`s. Durable Operations Assets describe reusable operating constraints; they are not a substitute for execution evidence.

### Layer 1 consumers

T2, T3, T4.

---

## P5.7 Knowledge Assets

### Purpose

Retain reusable engineering rationale and learnings that help future features without redefining current product truth.

### Typical reusable knowledge

- ADR rationale;
- incident learnings;
- retrospectives;
- known failure patterns;
- reviewed engineering patterns;
- lessons from historical delivery.

### Typical upstream sources

- ADRs;
- incidents/postmortems;
- retrospectives;
- reviewed engineering notes;
- qualified historical findings.

### Typical maintenance mode

`CURATED`, `REFERENCED`, or reviewed `DERIVED`.

### Trust profile

Knowledge MUST make provenance, review, verification, and authorization explicit using the common `trust_profile`; these dimensions MUST NOT be collapsed into one implied ranking.

Raw chat, transient scratchpads, and unreviewed agent memory do not automatically become Knowledge Assets. They may remain `ASSERTED + UNREVIEWED + NOT_VERIFIED + NONE` investigative inputs until a governed maintenance path creates a durable Asset revision.

### Scope control

Layer 2 v0.1 defines the Asset contract only. A full knowledge-promotion or organizational-memory workflow is optional future work and is not a prerequisite for initial FDI operation.

---

## P5.8 Reference Assets

### Purpose

Provide a governed registry for external or internal sources that are best referenced rather than duplicated.

Examples:

- external standards;
- vendor/API documentation;
- canonical repository-local instructions;
- external policies/reference material.

### Typical maintenance mode

`REFERENCED`.

### Required metadata

At minimum:

- exact reference;
- version/as-of date;
- applicability;
- authority/trust profile;
- owner/curator;
- expiry or update trigger where applicable.

---

# Contract P6 — Frontier Team Maintenance Model

Layer 2 exists to make Product Intelligence **maintainable by the Frontier Team**, not merely discoverable by an Agent.

## P6.1 Maintenance responsibility

Every durable Asset MUST have an accountable owner or maintenance role.

Ownership means responsibility for:

- semantic usefulness;
- scope correctness;
- source/provenance quality;
- trust profile;
- invalidation and supersession;
- deciding whether an Agent-proposed update should become durable product intelligence.

## P6.2 Agent-assisted maintenance

Agents MAY:

- detect changed sources;
- propose diffs;
- extract structured data;
- correlate Feature/Backlog/PR history;
- identify likely stale Assets;
- draft updates;
- validate backlinks;
- propose new high-value relation Assets.

Agents MUST NOT automatically grant stronger authority than their source/review path supports.

## P6.3 Publication boundary

Producing or editing an Asset revision is not the same as making it available to Layer 1.

Layer 2 separates:

```text
Asset authoring / derivation
        |
        v
DRAFT revision
        |
        | publication policy / review
        v
PUBLISHED revision
        |
        v
eligible for Layer 1 selection when validity_state = ACTIVE
```

A Product Asset MUST NOT satisfy a normal Layer 1 Context requirement unless:

```text
publication_state = PUBLISHED
AND
validity_state = ACTIVE
```

unless the Layer 1 requirement explicitly permits draft/asserted investigative material.

Publication policy is Asset-specific:

| Policy | Meaning | Typical use |
| --- | --- | --- |
| `HUMAN_APPROVAL` | An accountable Human/team must approve the Asset revision before publication | Product, Architecture, authoritative Domain/Governance assets |
| `RULE_BASED_AUTO` | A governed deterministic/derived maintenance process may publish when all declared quality gates pass and authority is not elevated | Repository inventory, some delivery-history/index assets |
| `SOURCE_REFERENCE` | Publication registers a governed reference to an existing authoritative source; the FDI Asset does not re-author its semantics | ADRs, runbooks, standards, canonical interface definitions |

An Agent-proposed change defaults to `DRAFT` unless its Asset contract explicitly allows `RULE_BASED_AUTO`.

`RULE_BASED_AUTO` is permitted only when the Asset contract has fail-closed quality gates, complete required provenance, and no semantic authority elevation. AI-assisted extraction MAY participate, but semantic policy interpretation, unresolved conflict, or organizational adoption that requires judgment MUST fall back to `HUMAN_APPROVAL`.

A derived or automatically published Asset MUST NOT gain stronger review, verification, or authorization claims than its sources, checks, and maintenance policy justify.

## P6.4 Product Asset publication gate

Before a revision becomes `PUBLISHED`, the maintenance contract MUST establish at least:

1. stable Asset identity and scope;
2. valid source/provenance backlinks;
3. authority dimension consistent with the sources and owner;
4. trust profile consistent with the provenance/review/verification/authorization path;
5. known limitations/incompleteness;
6. freshness/as-of semantics;
7. invalidation triggers;
8. selection metadata sufficient for bounded use;
9. dependency backlinks for materially upstream Product Assets;
10. no silent authority, review, verification, or authorization escalation;
11. no unresolved overlapping conflict with another `PUBLISHED + ACTIVE` Asset of the same authority/scope unless the conflict is explicitly represented for Layer 1 resolution;
12. valid supersession linkage when replacing an existing revision.

A failed publication gate leaves the candidate revision `DRAFT`; it does not alter the currently published revision.

## P6.5 Generic Frontier Team maintenance loop

Layer 2 has a durable maintenance loop separate from Layer 1 feature execution:

```text
Source change / Team decision / Repeated Layer 1 miss
        |
        v
Detect maintenance need
        |
        v
Human or PA-* Skill proposes Asset revision
        |
        v
DRAFT
        |
        v
Validate provenance / authority / scope / freshness
        |
        v
Publish according to Asset policy
        |
        v
PUBLISHED + ACTIVE
        |
        +--> supersede prior revision when applicable
        |
        +--> expose updated selection/index metadata
        `--> signal possible downstream dependency impact
```

This is a Product Asset maintenance loop, not a Layer 1 canonical transition and not a feature delivery gate.

## P6.6 Maintenance Skill namespace

Layer 2 MAY use Product Asset maintenance Skills, distinct from Layer 1 Feature Transformation Skills:

```text
FT-*  Feature Transformation Skills — execute Layer 1
PA-*  Product Asset Maintenance Skills — maintain Layer 2
```

A `PA-*` Skill MAY define:

```text
PA-Skill
├── identity / revision
├── Asset family/type
├── accepted source types
├── source selectors
├── transformation/reconciliation procedure
├── authority-preservation rules
├── allowed capabilities
├── output/update contract
├── trust-profile assignment rules
├── source backlink requirements
├── incompleteness rules
├── invalidation detection
└── prohibitions
```

`PA-*` Skills are not T0 and do not enter the Layer 1 canonical feature chain.

---

# Contract P7 — Asset Lifecycle

Layer 2 Assets have a durable lifecycle independent from Layer 1 feature lifecycle.

## P7.1 Publication state and validity state

Publication state and validity state are separate dimensions, but only the following combinations are legal:

| Publication state | Legal validity state | Meaning |
| --- | --- | --- |
| `DRAFT` | `NOT_APPLICABLE` | Candidate revision; not normally selectable |
| `PUBLISHED` | `ACTIVE` | Eligible for normal bounded Layer 1 selection |
| `PUBLISHED` | `STALE` | Retained for provenance; normally fails a fresh/current requirement |
| `PUBLISHED` | `SUPERSEDED` | Historical published revision replaced by a successor |
| `RETIRED` | `NOT_APPLICABLE` | Asset lineage intentionally withdrawn from active selection; successor not required |

Any other combination is invalid.

At most one revision of the same `asset_id` may be `PUBLISHED + ACTIVE` for the same declared scope partition. Publishing an active successor moves the prior active revision to `SUPERSEDED`.

`SUPERSEDED` means "replaced but retained". `RETIRED` means "withdrawn from active use" and does not imply a successor exists.

## P7.2 Published revision immutability

A `PUBLISHED` semantic revision is immutable. Content/provenance changes create a new `asset_revision`; publication and validity transitions are lifecycle metadata and do not rewrite historical semantic content.

A failed proposed revision never mutates the currently active published revision.

## P7.3 Freshness is Asset-specific

Layer 2 MUST NOT impose one universal TTL. Every Asset declares a `freshness_policy` appropriate to its semantics.

Examples:

- an architecture principle may use `UNTIL_SUPERSEDED`;
- a repository index may use `SOURCE_CHANGE`;
- a relation record may use `SOURCE_CHANGE` against its exact supporting sources;
- a closed historical delivery fact generally uses `MANUAL` or event-driven correction;
- an external standard may use `EVENT_DRIVEN`, `TTL`, or explicit supersession.

## P7.4 Invalidation triggers and dependencies

A durable Asset MUST declare the classes of source/dependency change that can invalidate it or require re-review.

```yaml
invalidation_triggers:
  - trigger_type: "SOURCE_CHANGED|DEPENDENCY_CHANGED|POLICY_SUPERSEDED|SCOPE_CHANGED|EXPIRY|MANUAL_REVIEW"
    source_scope: "..."
    effect: "WHOLE_ASSET|SCOPED_RECORD|RECHECK_REQUIRED"
```

`dependency_refs` provide the minimum dependency graph needed for maintenance. Layer 2 does not require a complete organization-wide graph.

An upstream source or Asset change does not silently rewrite dependent Assets. The maintenance policy marks or rechecks affected Assets according to their declared triggers.

## P7.5 Supersession and Layer 1 history

A newer Asset revision may supersede an earlier revision without deleting historical provenance.

Layer 1 artifacts that previously referenced the older Asset remain historical records. Layer 1 decides whether an active feature claim becomes `STALE` according to its own material dependency semantics; Layer 2 MUST NOT silently mutate Layer 1 lifecycle state.

# Contract P8 — Asset Selection into Execution Context

Layer 2 Product Assets become useful to Layer 1 only through bounded, progressive selection.

```text
Layer 1 ContextRequirement
        |
        v
Product Intelligence Index / Registry
        |
        v
Select bounded eligible Product Asset Refs
        |
        + optional bounded direct reference resolution
        |
        v
Execution Context
        |
        v
ResolvedContextRef(s)
```

## P8.1 ProductAssetRef

A selected durable Asset is represented to the resolver with metadata equivalent to:

```yaml
product_asset_ref:
  asset_id: "..."
  asset_revision: 12
  descriptor_ref: "..."
  content_ref: "..."
  publication_state: "PUBLISHED"
  validity_state: "ACTIVE"
  as_of: "..."
  authority_dimensions: []
  trust_profile: {}
  scope_match: "..."
```

The Layer 1 resolver maps the selected Asset/reference into its approved `ResolvedContextRef` contract. Layer 2 does not change Layer 1's canonical Context interface.

## P8.2 Selection eligibility

Normal selection MUST evaluate:

1. Asset family/type compatibility;
2. authority dimension;
3. scope/applicability;
4. required trust-profile facets;
5. revision/as-of/freshness;
6. publication/validity eligibility;
7. selector bounds;
8. known supersession/conflicts.

The default eligible state is:

```text
publication_state = PUBLISHED
AND validity_state = ACTIVE
```

A `DRAFT` Asset may be selected only when the Layer 1 requirement/selector explicitly permits unpublished or asserted investigative material. It MUST NOT satisfy a requirement that demands published/authorized Context.

## P8.3 Progressive resolution

Selection SHOULD return a bounded, low-redundancy initial set sufficient to begin the Skill's declared task. It MAY expand on demand under the same `ContextRequirement` and selector bounds as new findings require.

Layer 2 MUST NOT require exhaustive preloading or claim that a globally smallest sufficient set can always be known before execution.

Selection MUST NOT silently weaken a Layer 1 Context requirement.

## P8.4 Conflicts and outcomes

A selector MUST NOT silently choose a convenient Asset when materially applicable eligible Assets conflict. It returns the conflict and the relevant refs so Layer 1 can apply its approved conflict/gap semantics.

Possible resolution outcomes:

```text
RESOLVED
NOT_FOUND
STALE_ONLY
INSUFFICIENT_TRUST
CONFLICTING
NOT_APPLICABLE
```

The Layer 1 Skill then applies claim-local blocking, investigation, or gap semantics.

# Contract P9 — Product Intelligence Index

Layer 2 SHOULD expose a compact navigation registry. The recommended logical root is:

```text
fdi/product-intelligence/index.md
```

The index is a navigation and selection surface, not a product knowledge dump.

Example registry entry:

```yaml
assets:
  - asset_id: "codebase-index"
    asset_family: "CODEBASE"
    asset_type: "REPOSITORY_INDEX"
    ref: "..."
    asset_revision: 12
    scope:
      products: ["..."]
    authority_dimensions: ["CURRENT_BEHAVIOR_SUPPORT"]
    trust_profile:
      provenance: "DERIVED"
      review: "UNREVIEWED"
      verification: "VERIFIED"
      authorization: "NONE"
    publication_state: "PUBLISHED"
    validity_state: "ACTIVE"
    as_of: "..."
    selection_metadata:
      terms: []
      applicability: []
```

The index MAY be split by Asset family when scale requires it.

The index is a navigation/selection projection, not an independent authority for the underlying product claim. Index entries MUST backlink to their Asset descriptors. The index itself MAY be maintained as a derived Asset and may use `RULE_BASED_AUTO` when its registry integrity checks pass.

---

# Contract P10 — Product Intelligence vs Evidence

Layer 2 Product Assets and Layer 1 Evidence MUST remain distinct.

```text
Product Asset
= reusable product intelligence

EvidenceRef
= evidence establishing a specific feature claim
```

Examples:

### Codebase relation Asset

```text
"repo A commonly calls service B"
```

can help T2 investigate.

### T2 EvidenceRef

```text
repo-A@sha:path
+ repo-B@sha:contract
```

establishes that the relation is currently relevant to the feature-specific finding.

Likewise:

```text
Delivery History Asset
→ suggests repo-C

Current feature-specific EvidenceRef
→ CONFIRMS or EXCLUDES repo-C
```

This boundary prevents Product Intelligence from becoming stale hidden truth.

---

# Contract P11 — Recommended Product Intelligence Structure

The following logical structure is recommended, not mandatory as a fixed exhaustive bundle:

```text
fdi/product-intelligence/
├── index.md
│
├── product/
│   ├── index.md
│   ├── capabilities.md
│   └── boundaries.md
│
├── architecture/
│   ├── index.md
│   └── principles.md
│
├── codebase/
│   ├── index.md
│   ├── repos/
│   └── relations/
│
├── domain/
│   └── index.md
│
├── delivery-history/
│   ├── index.md
│   └── records/
│
├── operations/
│   └── index.md
│
├── knowledge/
│   └── index.md
│
└── references/
    └── index.md
```

Only useful Assets SHOULD be materialized. Empty placeholder files are not required.

---

# Contract P12 — Layer 1 Consumption Map

| Product Asset family | T1 Intention | T2 Delivery Spec | T3 Implementation | T4 Correctness |
| --- | --- | --- | --- | --- |
| Product | Primary | Primary | Occasional | Applicable validation |
| Architecture | Occasional | Primary | Primary | Applicable verification |
| Codebase | Orientation | **Primary** | **Primary** | Candidate/source coverage |
| Domain | Primary when applicable | Primary | Mapped constraints | **Primary validation when applicable** |
| Delivery History | Rare | **Candidate discovery / prioritization** | Rare | Rare |
| Operations | Rare | Primary when applicable | Primary | Primary when applicable |
| Knowledge | On demand | On demand | On demand | On demand |
| Reference | On demand | On demand | On demand | On demand |

This table is a default consumption profile, not a rule to preload every family.

---

# Contract P13 — Bootstrap Principle

Layer 2 MUST grow according to demonstrated Layer 1 reuse value.

It MUST NOT begin by building a complete enterprise graph or full organizational memory system.

Recommended bootstrap order:

```text
P0  Product / architecture curated core already available to the team
P0  Minimal Codebase Index
P0  Delivery History Assets from Feature + Backlog + PR/Commit
P1  High-value Codebase relation Assets discovered as repeated T2 needs
P1  Operations Assets required by pilot product
P1  Domain Assets required by pilot product
P2  Additional Product Intelligence driven by repeated Layer 1 misses
P3  Broader Knowledge lifecycle / promotion only when justified
```

The governing rule is:

> **Materialize an Asset when maintaining it once is cheaper and more reliable than repeatedly rediscovering the same product knowledge during Layer 1 execution.**

---

# Contract P14 — Layer 2 Success Criteria

Layer 2 is successful only if maintained Product Assets measurably improve Layer 1 delivery.

Recommended evaluation dimensions:

| Dimension | Example measure |
| --- | --- |
| Reuse | How often an Asset is materially reused across features |
| Discovery quality | Improvement in T2 candidate/critical repo recall |
| Context efficiency | Reduction in unnecessary repository/context loading |
| Freshness | Rate of materially stale Asset use |
| Human maintenance burden | Time required to keep high-value Assets useful |
| Agent correction rate | How often Agents require Human correction because Product Intelligence was missing/wrong |
| Traceability | % of materially used Assets with valid source/provenance backlinks |
| Asset ROI | Maintenance cost versus repeated investigation effort avoided |

Layer 2 SHOULD remove or demote Assets that are expensive to maintain and rarely improve Layer 1 outcomes.

---

# Contract P15 — Contract Review Invariants

Before Layer 2 can be implemented, the following invariants are normative:

1. **Descriptor is universal; storage is not.** Every Product Asset has a governed descriptor, but Asset content may be Markdown, another materialized representation, or a registered authoritative reference.
2. **Published semantic revisions are immutable.** Lifecycle state may change without rewriting historical Asset content.
3. **Trust is faceted.** Provenance, review, verification, and authorization are evaluated separately; no global trust ranking is implied.
4. **One active lineage.** One `asset_id` has at most one `PUBLISHED + ACTIVE` revision per scope partition.
5. **Derived intelligence does not create current feature truth.** Historical/indexed relations may guide discovery; Layer 1 current `EvidenceRef`s establish feature-specific findings.
6. **No silent publication.** Agent-generated semantic changes default to `DRAFT`; auto-publication is fail-closed and cannot elevate authority.
7. **No silent conflict resolution.** Materially conflicting eligible Assets are surfaced to Layer 1.
8. **No complete graph prerequisite.** Only useful dependency/backlink metadata is maintained; feature execution may resolve bounded current evidence directly.
9. **Layer 2 never mutates Layer 1 authority.** Asset updates may trigger re-evaluation signals, but Layer 1 owns feature validity/invalidation.
10. **Maintenance is ROI-driven.** Frontier Teams materialize and maintain Assets when reuse value exceeds repeated rediscovery cost.

# Layer 2 Design Review Checklist

Layer 2 v0.1 design approval is complete:

- [x] Layer 2 purpose: Frontier-Team-maintained durable Product Intelligence, not execution workflow
- [x] Product Asset vs Execution Context distinction
- [x] Source vs Product Asset vs Evidence boundary
- [x] Product Asset Descriptor/content contract and semantic revision rules
- [x] `CURATED`, `DERIVED`, `REFERENCED` maintenance modes
- [x] `RESOLVED` moved to Layer 1 Context consumption rather than durable Asset maintenance
- [x] Product / Architecture / Codebase / Domain / Delivery History / Operations / Knowledge / Reference families
- [x] Frontier Team ownership and Agent-assisted maintenance boundary
- [x] Faceted trust profile: provenance / review / verification / authorization
- [x] Draft/publication boundary and Asset-specific publication policies
- [x] Product Asset publication gate and generic maintenance loop
- [x] `PA-*` Product Asset Maintenance Skill namespace separated from `FT-*`
- [x] Asset lifecycle legal states, published revision immutability, freshness, dependencies, invalidation, supersession
- [x] Product Intelligence Index / ProductAssetRef / bounded progressive selection contract
- [x] Product Asset vs feature-specific EvidenceRef boundary
- [x] Layer 1 consumption map
- [x] Incremental bootstrap principle based on reuse/ROI
- [x] Layer 2 success metrics tied to Layer 1 quality and maintenance cost

Current state:

```text
Layer 1 Contract-ready: APPROVED
Layer 2 Product Intelligence Contract-ready: APPROVED
Layer 2 Execution-verified: NOT_CLAIMED
Product Asset maintenance implementation: NOT_AUTHORIZED_BY_THIS_DESIGN
```

Approval of this framework authorizes the Product Asset **contract model** only. It does not by itself authorize creation, refresh, publication, or migration of Product Assets in any repository or source system.

## L2-PROFILE — layer2_product_asset_profiles

- Semantic version: `0.1`
- Approval: `HERM-210; multica-attachment:01a05228-a42d-72fa-b388-558f59430632`
- Compatibility: `L2-FWK@0.1; scope fully specifies PA-03 and PA-05 only`

### Source: `normative/layer2/profiles/fdi-product-asset-profile-specification-v0.1-approved.md`

SHA-256: `d43cfc258b36a020c65382a4929c98067599c832b52d63235fd860ff311753ea`

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

## L2-MAINT — layer2_maintenance_skills

- Semantic version: `0.1`
- Approval: `HERM-210; multica-attachment:01a05228-a42d-72fa-b388-558f59430632`
- Compatibility: `L2-FWK@0.1; L2-PROFILE@0.1`

### Source: `normative/layer2/maintenance/fdi-product-asset-maintenance-skill-contracts-v0.1-approved.md`

SHA-256: `471614685929d17334e3d1faad4373c8a03a934731c2c17d7a8fef875dbd304a`

# FDI Product Asset Maintenance Skill Contracts v0.1

> **Status:** APPROVED — Contract-ready  
> **Depends on:** FDI Layer 1 — Feature Transformation Specification v0.2 (`Contract-ready: APPROVED`)  
> **Depends on:** FDI Layer 2 — Product Intelligence Asset Framework v0.1 (`Contract-ready: APPROVED`)  
> **Depends on:** FDI Product Asset Profile Specification v0.1 (`Contract-ready: APPROVED`)  
> **Scope:** Generic `PA-*` maintenance Skill contract plus `PA-Codebase-Inventory` and `PA-Historical-Delivery`  
> **Primary actor:** Frontier Team; Agents/Squads execute approved `PA-*` Skills under delegated capabilities  
> **Design only:** No crawler, correlator, indexer, asset migration, source-system mutation, validator, or publication execution is authorized by this specification

---

# 0. Purpose

Layer 2 defines **what durable Product Assets a Frontier Team maintains**. Product Asset Profiles define the minimum semantics of those Assets. This specification defines the next level down:

> **How an Agent may assist the Frontier Team in creating, refreshing, reconciling, and proposing revisions to those Product Assets without silently changing product authority.**

`PA-*` Skills are not Layer 1 feature transitions and are not T0.

```text
Frontier Team maintenance need
        |
        v
Approved PA-* Skill
        |
        +--> reads governed source snapshots
        +--> refers to supporting Product Assets
        +--> compares active Asset revision
        |
        v
Maintenance Bundle
        |
        +--> NO_CHANGE
        |
        +--> Asset revision proposal (DRAFT)
        |
        +--> publication recommendation
        |
        `--> gaps / conflicts / invalidation findings
```

The Frontier Team remains accountable for the Product Asset family and its publication policy. An Agent executes the Skill; it does not acquire the authority of the Asset owner merely by executing the Skill.

---

# 1. Core Maintenance Function

The common Product Asset maintenance abstraction is:

```text
MaintenanceBundle
=
f(
  MaintenanceRequest,
  SourceSnapshot(s),
  ExistingActiveAsset?,
  PA-Skill@revision
  ;
  SupportingProductAssetRefs
)
```

where:

- `MaintenanceRequest` defines why and within what scope maintenance is being performed;
- `SourceSnapshot(s)` are exact source identities plus immutable revisions or declared as-of states;
- `ExistingActiveAsset?` is the currently active Asset revision when this is a refresh/reconciliation run;
- `PA-Skill@revision` defines the governed maintenance procedure;
- `SupportingProductAssetRefs` are optional durable Assets referenced to interpret or classify source data;
- `MaintenanceBundle` contains the proposed result and provenance but does not by itself create Layer 1 feature truth.

The maintenance function is **governed and traceable**, not required to be byte-identical deterministic when semantic reasoning is involved.

---

# 2. Generic `PA-*` Skill Contract

Every `PA-*` Skill MUST define the following.

| Field | Required meaning |
| --- | --- |
| `skill_id` | Stable maintenance Skill identity |
| `skill_revision` | Exact governed Skill revision |
| `asset_profile` | Product Asset Profile the Skill is allowed to maintain |
| `asset_types` | Specific Asset types the Skill can produce or refresh |
| `maintenance_actions` | `CREATE`, `REFRESH`, `RECONCILE`, `CORRECT`, or a declared subset |
| `accepted_source_types` | Source classes the Skill may read |
| `source_selectors` | Bounded rules for selecting source records |
| `supporting_asset_requirements` | Product Assets that may/must be referenced |
| `procedure` | Required maintenance steps |
| `authority_preservation` | Rules preventing derivation from gaining unsupported authority |
| `trust_assignment` | How provenance/review/verification/authorization facets are assigned |
| `capabilities` | Permitted tools/actions |
| `side_effects` | External changes the Skill may propose or perform |
| `output_contract` | Required Maintenance Bundle structure |
| `publication_eligibility` | Rules for auto-publish eligibility vs Human approval |
| `invalidation_detection` | Source/dependency changes the Skill must identify |
| `idempotence` | Rules preventing duplicate semantic revisions for unchanged source state |
| `failure_classes` | Named blocking/gap/conflict outcomes |
| `prohibitions` | Actions the Skill may not perform |

A helper Skill may be called internally, but materially influential helper identity/revision MUST be recorded in maintenance provenance.

`trust_assignment` MUST populate the Layer 2 faceted `trust_profile` (`provenance`, `review`, `verification`, `authorization`) from observed source/review/check paths. It MUST NOT collapse them into one confidence score or infer organizational authorization from model confidence.

---

# 3. Maintenance Request Contract

A maintenance run MUST begin with a bounded `MaintenanceRequest`.

Minimum semantics:

```yaml
maintenance_request:
  request_id: "<stable-run-request-id>"
  action: "CREATE|REFRESH|RECONCILE|CORRECT"
  trigger: "HUMAN_REQUEST|SOURCE_CHANGE|SCHEDULED_REFRESH|INVALIDATION|LAYER1_FEEDBACK|MANUAL_REVIEW"
  target_profile: "PA-03|PA-05"
  target_asset_type: "<asset-type>"
  target_asset_id: "<asset-id-or-null-for-create>"
  scope:
    products: []
    systems: []
    repositories: []
    source_records: []
    time_range: null
  requested_as_of: "<time-or-source-state>"
  requested_by: "<frontier-team-role-or-system-trigger>"
```

The request scope is a **maintenance boundary**, not permission to infer completeness beyond that scope.

A Layer 1 miss may create a maintenance request or feedback record, but MUST NOT directly mutate a Product Asset.

---

# 4. Source Snapshot Contract

Every materially used source MUST be represented as a reviewable snapshot/reference:

```yaml
source_snapshot:
  source_ref: "<canonical-source-ref>"
  source_type: "<provider/work-item/pr/commit/catalog/manifest/etc>"
  revision_or_as_of: "<immutable-revision-or-as-of>"
  selected_for: "<maintenance-purpose>"
  authority_for: ["DURABLE_CONSTRAINT|CURRENT_BEHAVIOR_SUPPORT|RATIONALE_SUPPORT"]
  source_trust:
    provenance: "DIRECT|DERIVED|ASSERTED"
    review: "UNREVIEWED|REVIEWED"
    verification: "NOT_VERIFIED|VERIFIED"
    authorization: "NONE|SOURCE_INHERITED|EXPLICIT"
  retrieval_state: "AVAILABLE|PARTIAL|UNAVAILABLE|CONFLICTING"
```

Rules:

1. source identity and revision/as-of state MUST be explicit;
2. mutable "latest" references are insufficient for published derivation unless the as-of state is captured;
3. `authority_for` MUST use only approved Layer 2 authority dimensions and the Skill MUST preserve source-specific authority instead of flattening all sources into one trust level;
4. source trust facets MUST be preserved separately; a maintenance Skill MUST NOT manufacture `REVIEWED`, `VERIFIED`, or `EXPLICIT` status that the source/review path did not establish;
5. unavailable or conflicting sources create explicit gaps/conflicts rather than silent substitution;
6. source selection MUST remain bounded by the Maintenance Request and Skill selectors.

---

## 4.1 Supporting Product Asset eligibility

A supporting Product Asset reference MUST pin exact `asset_id` and `asset_revision`. Normal maintenance uses only `PUBLISHED + ACTIVE` supporting Assets. A `DRAFT` or `STALE` Asset may be used only when the specific PA-Skill declares an investigative exception, and that exception MUST be recorded as a limitation; it cannot satisfy an authoritative dependency requirement.

# 5. Maintenance Bundle Contract

Every `PA-*` Skill run returns one `MaintenanceBundle`.

```yaml
maintenance_bundle:
  request_id: "<request-id>"
  skill:
    id: "<PA-skill-id>"
    revision: "<skill-revision>"

  result: "NO_CHANGE|REVISION_PROPOSED|LIFECYCLE_UPDATE_PROPOSED|BLOCKED"

  target:
    asset_id: "<asset-id>"
    asset_profile: "<profile-id>"
    asset_type: "<asset-type>"
    prior_active_revision: "<revision-or-null>"
    prior_validity_state: "<ACTIVE|STALE|SUPERSEDED|NOT_APPLICABLE-or-null>"

  proposal:
    proposed_asset_revision: "<revision-or-null>"
    proposed_publication_state: "DRAFT|NONE"
    semantic_diff_ref: "<diff-ref-or-null>"
    proposed_validity_state: "ACTIVE|STALE|SUPERSEDED|NOT_APPLICABLE|NONE"
    lifecycle_reason: "<reason-or-null>"

  publication:
    eligibility: "RULE_BASED_AUTO_ELIGIBLE|HUMAN_APPROVAL_REQUIRED|NOT_PUBLISHABLE"
    reasons: []

  sources_used: []
  supporting_assets_used: []
  helper_skills_used: []

  findings:
    source_gaps: []
    conflicts: []
    invalidation_findings: []
    limitations: []

  maintenance_provenance:
    executor: "<agent/role>"
    execution_id: "<run-id>"
    executed_at: "<timestamp>"
```

## 5.1 Result semantics

### `NO_CHANGE`

The active Asset remains semantically correct for the evaluated maintenance scope and source state. No new semantic Asset revision is created.

### `REVISION_PROPOSED`

A semantic Asset revision is proposed. It is `DRAFT` until publication occurs according to the Asset policy.

### `LIFECYCLE_UPDATE_PROPOSED`

The semantic Asset revision remains unchanged, but lifecycle validity should change, for example `ACTIVE -> STALE`, `STALE -> ACTIVE` after successful revalidation, or `ACTIVE -> SUPERSEDED`. The Maintenance Bundle MUST state the exact prior/proposed validity states and reason. Lifecycle metadata changes do not create a new semantic `asset_revision`.

### `BLOCKED`

The Skill cannot safely determine the required Asset state because a required source, identity, authority, or conflict condition is unresolved.

`BLOCKED` MUST NOT mutate the currently active published Asset.

## 5.2 Publication eligibility is not publication

The Skill may classify a proposal as:

```text
RULE_BASED_AUTO_ELIGIBLE
HUMAN_APPROVAL_REQUIRED
NOT_PUBLISHABLE
```

This is a recommendation under the approved Asset contract. It is **not itself the publication state transition**.

Actual publication is governed by the Layer 2 Asset publication policy and accountable authority.

---

# 6. Common Maintenance Invariants

## 6.1 Published Asset immutability

A `PUBLISHED` semantic revision MUST NOT be rewritten.

Any semantic/provenance change produces a new `asset_revision`.

## 6.2 Lifecycle revalidation

Semantic revision and lifecycle validity are separate. A refresh MAY return `LIFECYCLE_UPDATE_PROPOSED` without creating a new Asset revision when the content/provenance binding is unchanged but validity changes. In particular, a previously `STALE` revision MAY return to `ACTIVE` only after the invalidation condition has been re-evaluated against qualified current sources.

## 6.3 Idempotence

For the same:

```text
MaintenanceRequest scope
+ exact SourceSnapshot set
+ exact supporting ProductAssetRefs
+ PA-Skill revision
+ existing active Asset revision
```

a repeated run SHOULD produce `NO_CHANGE` rather than an unnecessary new semantic revision when no material semantic difference exists.

## 6.4 Authority preservation

A derived output MUST NOT gain authority merely because it is normalized, summarized, indexed, or generated by a powerful model.

For example:

```text
source says "owner unknown"
        ↓
PA-Skill
        ↓
MUST NOT become "Team A owns this repo"
```

unless a qualified source supports that claim.

## 6.5 Scope-qualified completeness

Every completeness claim MUST identify the scope it covers.

```text
"complete repository inventory"
```

is invalid without a declared product/system/provider/source boundary.

## 6.6 No Layer 1 mutation

`PA-*` Skills MUST NOT:

- change an active Intention;
- change an active Delivery Spec;
- alter a Layer 1 gate or validity state;
- convert a Product Asset relation into a feature-specific `CONFIRMED` Change Surface finding;
- modify Layer 1 artifacts automatically because an Asset changed.

They MAY emit a downstream-impact signal for Layer 1 to evaluate.

## 6.6a Default side-effect boundary

Unless a specific approved PA-Skill explicitly declares otherwise, maintenance execution is read-only against upstream source systems. Permitted outputs are Maintenance Bundles, DRAFT Asset revision proposals, lifecycle-update proposals, index deltas, and review/publication recommendations. Source-system mutation and publication are separate governed actions.

## 6.7 Frontier Team accountability

The Frontier Team owns:

- Asset scope;
- publication policy;
- semantic review requirements;
- authority delegation;
- acceptable incompleteness;
- retirement/supersession decisions when not deterministic.

The Agent/Squad owns execution trace and adherence to the approved Skill contract.

---

# 7. `PA-Codebase-Inventory` Skill Contract

## 7.1 Identity

```yaml
skill_id: "PA-Codebase-Inventory"
asset_profile: "PA-03"
asset_types:
  - "CB-01_REPOSITORY_INVENTORY"
maintenance_actions:
  - "CREATE"
  - "REFRESH"
  - "RECONCILE"
  - "CORRECT"
```

## 7.2 Purpose

Maintain a bounded, stable, provenance-backed inventory of repositories relevant to declared Product/System scope so Layer 1 Agents can navigate the current product codebase without assuming a complete enterprise dependency graph.

The Skill answers:

> **What repositories currently exist in the declared scope, what stable identities/ownership/product mappings are known, and what navigation metadata can safely be reused?**

It does **not** answer:

> **Which repositories must change for a specific feature?**

That remains FT-T2 responsibility.

## 7.3 Accepted source types

The Skill MAY read, according to declared source authority:

- canonical Git/repository provider metadata;
- repository registry;
- CODEOWNERS or approved ownership system;
- product/service catalog;
- deployment/service descriptors;
- package/build manifests;
- repository-level metadata/configuration;
- approved product/system mapping assets;
- explicitly approved manual correction records.

The Skill MUST NOT treat:

- README prose alone as authoritative ownership;
- repository naming convention alone as product membership;
- semantic similarity alone as stable repository lineage;
- branch names or transient development metadata as canonical repository identity.

## 7.4 Supporting Product Assets

Optional/conditional supporting Assets may include:

```text
Product Asset
Architecture Asset
existing Codebase Asset
approved Reference Asset
```

These are used for classification/navigation only within their declared authority dimensions.

## 7.5 Required procedure

`PA-Codebase-Inventory` MUST:

1. pin the Maintenance Request scope and requested as-of state;
2. enumerate repositories from the declared canonical repository source(s);
3. establish or recover stable `repo_id`;
4. resolve canonical repository reference;
5. preserve aliases and known identity lineage;
6. classify repository lifecycle state;
7. resolve ownership from the approved ownership source, or record an ownership gap;
8. resolve product/system membership from qualified sources, or record `UNKNOWN`;
9. derive bounded technical fingerprint fields where supported:
   - language/platform;
   - build/package manifests;
   - primary entry points;
   - declared contracts;
   - deployment/service descriptors;
10. retain field-level provenance/authority;
11. compare against the active CB-01 revision;
12. detect create/archive/rename/move/replacement/split/merge signals;
13. distinguish rename/move from replacement/split/merge when evidence permits;
14. expose unresolved identity collisions rather than merging them heuristically;
15. calculate scope-qualified completeness/limitations;
16. calculate semantic diff;
17. assign publication eligibility;
18. return the Maintenance Bundle.

## 7.6 Repository identity continuity rules

Stable `repo_id` is not the repository display name.

A rename/move MAY retain the same `repo_id` when repository continuity is established.

```text
repo-old-name
      ↓ rename
repo-new-name
```

may remain one identity.

By contrast:

```text
repo-A
  ↓ split
repo-B + repo-C
```

or:

```text
repo-A + repo-B
  ↓ merge
repo-C
```

MUST be represented through lineage/replacement semantics rather than silently reusing one identity.

When continuity cannot be established confidently, the Skill MUST surface `IDENTITY_CONFLICT` or an explicit unknown lineage state.

## 7.7 Minimum CB-01 output semantics

Each repository record MUST expose the PA-03 profile fields, including semantics equivalent to:

```yaml
repo_id: "<stable-id>"
canonical_ref: "<repo-provider-ref>"
repository_state: "ACTIVE|ARCHIVED|REPLACED|UNKNOWN"
aliases: []
lineage_refs: []

product_system_refs: []
owner_refs: []

role_summary: "<bounded-reusable-description-or-unknown>"
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
```

Field-level provenance MAY be normalized into a supporting provenance table rather than repeated inline, provided backward traceability is preserved.

## 7.8 Publication eligibility

### `RULE_BASED_AUTO_ELIGIBLE`

Allowed only when all materially changed fields are deterministic/source-backed under an approved rule, such as:

- repository creation/archive state from canonical provider;
- exact repository reference;
- stable identity continuity established by approved deterministic identity rule;
- ownership from approved ownership source;
- manifest-derived language/platform fields;
- source/as-of metadata.

### `HUMAN_APPROVAL_REQUIRED`

Required when material publication depends on judgment, including:

- ambiguous repository identity continuity;
- conflicting ownership sources;
- ambiguous product/system membership;
- semantic `role_summary` that materially affects selection;
- split/merge/replacement interpretation not covered by approved deterministic rule.

### `NOT_PUBLISHABLE`

Required when:

- canonical repository identity cannot be established;
- required source provenance is missing;
- unresolved collision would create duplicate/incorrect repository identity;
- requested completeness claim cannot be supported.

## 7.9 Failure classes

```text
SOURCE_UNAVAILABLE
SOURCE_PARTIAL
IDENTITY_CONFLICT
OWNERSHIP_CONFLICT
PRODUCT_SCOPE_CONFLICT
LINEAGE_UNRESOLVED
COMPLETENESS_UNSUPPORTED
PUBLICATION_POLICY_BLOCK
```

Each failure is claim/scope-specific when possible; a gap in one repository record need not block unrelated valid records unless the requested publication scope requires atomic completeness.

## 7.10 Prohibitions

The Skill MUST NOT:

- create or delete source repositories;
- rewrite CODEOWNERS/service catalogs;
- invent ownership;
- infer architecture policy;
- claim a complete organization graph;
- publish a high-confidence current feature impact;
- mark an indexed repository as required for a particular feature;
- rewrite historical CB-01 revisions.

## 7.11 Quality measures

Recommended maintenance quality indicators:

```text
repository identity collision rate
ownership coverage within declared scope
product/system mapping coverage
source freshness lag
manual reconciliation rate
unnecessary revision rate
stale active Asset rate
```

These are Layer 2 maintenance measures, not Layer 1 Feature Delivery KPIs.

---

# 8. `PA-Historical-Delivery` Skill Contract

## 8.1 Identity

```yaml
skill_id: "PA-Historical-Delivery"
asset_profile: "PA-05"
asset_types:
  - "DH-01_HISTORICAL_DELIVERY_RECORD"
maintenance_actions:
  - "CREATE"
  - "REFRESH"
  - "RECONCILE"
  - "CORRECT"
```

`DH-02 Delivery History Index` is a derived navigation projection over published DH-01 records. v0.1 does not require a separate semantic correlation Skill for DH-02; the maintenance run MUST emit enough stable selection metadata for the Layer 2 index to be refreshed deterministically.

## 8.2 Purpose

Transform bounded historical delivery sources into reusable, provenance-backed records of what was requested and what was observed to change historically.

The Skill answers:

> **For this historical delivery unit, what product-change semantics, delivery sources, repositories, paths, and change types are supported by historical evidence?**

It does not answer:

> **What must change for a current feature?**

## 8.3 Accepted source types

The Skill MAY read:

- historical Feature/Epic records;
- backlog/work items/issues;
- requirement and acceptance-criteria records;
- linked design/review records;
- PRs;
- commits;
- code-review records;
- CI/build/test records;
- release/deployment evidence where relevant;
- approved manual correlation/correction records.

Every source must retain original identity and revision/as-of semantics where available.

## 8.4 Historical delivery unit identity

The Skill MUST establish:

```yaml
delivery_unit_id: "<stable-fdi-history-id>"
primary_work_item_ref: "<feature/backlog/source-ref>"
```

`delivery_unit_id` is the stable FDI Asset identity. It is not required to equal the upstream tracker ID.

Multiple historical work items may participate in one delivery unit, but the grouping rationale and source linkage MUST be explicit.

The Skill MUST NOT merge work items into one delivery unit merely because their text is semantically similar.

## 8.5 Required procedure

`PA-Historical-Delivery` MUST:

1. pin Maintenance Request scope and historical source boundary;
2. identify the primary historical work item;
3. collect declared linked backlog/issues;
4. collect PR/commit/review/CI/release sources through bounded link traversal;
5. preserve a correlation record for every materially used source;
6. classify correlation method and strength;
7. extract historical product-change semantics with provenance;
8. identify observed repositories and paths;
9. identify observed change types such as:
   - API;
   - EVENT;
   - SCHEMA;
   - CONFIG;
   - PACKAGE;
   - DEPLOYMENT;
   - DATA;
   - TEST;
   - OPERATIONS;
10. create one or more source-backed historical change facts;
11. map each fact to its supporting evidence;
12. classify delivery relevance:
   - `FEATURE_DELIVERY`;
   - `CO_DELIVERED`;
   - `INCIDENTAL`;
   - `UNKNOWN`;
13. default ambiguous relevance to `UNKNOWN`;
14. record delivery outcome where supported:
   - `EFFECTIVE`;
   - `PARTIALLY_EFFECTIVE`;
   - `REVERTED`;
   - `SUPERSEDED`;
   - `UNKNOWN`;
15. establish `delivered_as_of` plus its basis;
16. represent conflicts, reverts, replacements, missing links, and incompleteness;
17. compare against active DH-01 revision;
18. calculate semantic diff;
19. assign publication eligibility;
20. emit stable selection metadata for DH-02 navigation;
21. return the Maintenance Bundle.

## 8.6 Correlation contract

Every materially influential linked source MUST have a correlation record.

Conceptually:

```yaml
correlation:
  source_ref: "<PR/commit/work-item/etc>"
  method: "<method-id>"
  derivation: "EXPLICIT|DERIVED|MANUAL"
  strength: "STRONG|AMBIGUOUS"
  review: "UNREVIEWED|REVIEWED"
  evidence_refs: []
  limitations: []
```

Examples of strong explicit linkage:

```text
EXPLICIT_FEATURE_LINK
EXPLICIT_BACKLOG_LINK
EXPLICIT_PR_WORKITEM_LINK
EXPLICIT_COMMIT_WORKITEM_LINK
RELEASE_LINK
```

Derived methods may include:

```text
BRANCH_OR_PR_METADATA_LINK
DERIVED_SEMANTIC_LINK
DERIVED_TEMPORAL_LINK
```

A derived link MAY be useful for candidate investigation but MUST NOT be silently upgraded to explicit linkage.

## 8.7 Historical change fact contract

Each materially reusable fact MUST preserve:

```yaml
historical_change_fact:
  fact_id: "<stable-within-delivery-unit>"
  kind: "REPOSITORY|PATH|API|EVENT|SCHEMA_DATA|CONFIG|OPERATIONS|TEST_VALIDATION|OTHER"
  subject_ref: "<historical-repo-path-contract-or-other-ref>"
  current_repo_id: "<optional-current-PA-03-navigation-mapping>"
  detail: "<bounded-historical-observation>"
  evidence_refs: []
  delivery_relevance: "FEATURE_DELIVERY|CO_DELIVERED|INCIDENTAL|UNKNOWN"
  confidence_basis: "<source/correlation-basis>"
  limitations: []
```

Historical identity is preserved in `subject_ref`. `current_repo_id`, when present, is navigation support derived from PA-03 identity/lineage evidence and MUST NOT rewrite the historical identity.

The critical invariant is:

```text
historical fact
    -> historical evidence
    -> declared delivery relevance
```

A linked PR touching repo X does not by itself prove that repo X was necessary for the feature.

## 8.8 Feature semantics contract

The Skill MAY derive reusable feature terms/capability labels for retrieval, but MUST preserve derivation.

Examples:

```text
product area
capability
feature family
domain terms
change intent terms
```

Derived feature semantics support search/navigation. They do not become Product/Domain/Architecture authority.

## 8.9 Delivery outcome and temporal semantics

`delivered_as_of` MUST state both value and basis.

Examples:

```text
MERGE
RELEASE
WORK_ITEM_DONE
OTHER
UNKNOWN
```

A later correction, newly discovered PR, or newly discovered revert may require a new DH-01 semantic revision.

Historical records generally do not become stale because the current codebase changed; they become incomplete/incorrect only when the representation of what happened historically is corrected or expanded.

## 8.10 Publication eligibility

### `RULE_BASED_AUTO_ELIGIBLE`

May be used when:

- historical source correlation is based entirely on declared strong/deterministic links;
- extraction is source-backed;
- delivery relevance remains `UNKNOWN` where semantic judgment would otherwise be required;
- no material historical conflict is unresolved;
- delivered-as-of basis is mechanically supported.

### `HUMAN_APPROVAL_REQUIRED`

Required when a material reusable conclusion depends on:

- ambiguous semantic/temporal linkage;
- manual reconstruction;
- classifying a material change as `FEATURE_DELIVERY`, `CO_DELIVERED`, or `INCIDENTAL` without an approved deterministic rule;
- resolving conflicting/reverted sources;
- grouping multiple work items into one delivery unit through judgment;
- excluding a material linked change from the reusable history pattern.

### `NOT_PUBLISHABLE`

Required when:

- primary delivery-unit identity cannot be established;
- material historical evidence has no recoverable provenance;
- conflict could materially change the represented repo/change surface and cannot be exposed safely;
- correlation is too weak to support even the bounded historical claim being published.

## 8.11 DH-02 index delta

The Skill SHOULD emit selection/index metadata such as:

```text
product/system terms
capability/feature-family terms
repo IDs
change types
delivered-as-of
delivery outcome
correlation-quality indicators
```

DH-02 aggregates MUST be calculated only from eligible published DH-01 records and MUST expose:

```text
support_count
denominator
source_record_refs
aggregation_as_of
aggregation_rule_revision
```

The index is navigation intelligence, not authority.

## 8.12 Failure classes

```text
PRIMARY_WORK_ITEM_UNRESOLVED
SOURCE_LINK_CONFLICT
SOURCE_UNAVAILABLE
CORRELATION_AMBIGUOUS
DELIVERY_UNIT_GROUPING_AMBIGUOUS
HISTORICAL_FACT_UNSUPPORTED
DELIVERY_RELEVANCE_REVIEW_REQUIRED
DELIVERY_OUTCOME_UNRESOLVED
PUBLICATION_POLICY_BLOCK
```

Ambiguity MAY result in a publishable record with explicit `UNKNOWN` fields when the Asset Profile permits that bounded claim. It need not always block the entire historical record.

## 8.13 Prohibitions

The Skill MUST NOT:

- infer current repo applicability;
- label historical repo touch as a current feature requirement;
- fabricate links between Feature/Backlog/PR/Commit;
- hide a revert or conflicting delivery path when material;
- convert historical patterns into Architecture or Domain policy;
- use future historical replay truth to rewrite what sources were actually linked;
- rewrite published DH-01 revisions.

## 8.14 Quality measures

Recommended maintenance quality indicators:

```text
source-link provenance coverage
historical fact evidence coverage
explicit-vs-derived correlation mix
UNKNOWN delivery-relevance rate
manual review rate
late-discovered linked-source rate
duplicate delivery-unit rate
index support/denominator integrity
```

High `UNKNOWN` rate is not automatically poor quality; it can be preferable to false semantic certainty.

---

# 9. Frontier Team Operating Boundary

For both Skills:

```text
Frontier Team
├── owns Asset profile/policy
├── approves semantic authority delegation
├── resolves material ambiguity
└── publishes/retire/supersedes according to policy

PA-* Agent/Squad
├── executes maintenance procedure
├── preserves evidence/provenance
├── proposes semantic revision
├── identifies gaps/conflicts
└── recommends publication disposition

Layer 2 governance
├── validates legal Asset lifecycle transition
├── preserves immutable published revisions
└── exposes eligible Asset refs to Layer 1

Layer 1
└── selectively resolves Product Assets as execution Context
```

A maintenance Agent may be highly autonomous for deterministic refresh work while publication policy remains stricter for semantic judgments.

---

# 10. First Implementation Boundary

This specification deliberately stops before physical implementation.

After approval, the first implementation design SHOULD define only:

1. the physical `SKILL.md` contract for `PA-Codebase-Inventory`;
2. the physical `SKILL.md` contract for `PA-Historical-Delivery`;
3. source adapters/selectors required by a chosen pilot product;
4. Product Asset descriptor/materialization layout;
5. dry-run mode that emits Maintenance Bundles without publishing;
6. validator checks for the contracts in this specification.

It SHOULD NOT start with:

- complete enterprise repository graph extraction;
- generic knowledge graph infrastructure;
- automatic semantic publication;
- every Product Asset family;
- organization-wide historical backfill.

---

# 11. Design Approval Checklist

Approved decisions:

- [x] Generic `PA-*` maintenance function and Skill interface
- [x] Maintenance Request and Source Snapshot contracts
- [x] Maintenance Bundle result, lifecycle-update, and publication-eligibility semantics
- [x] Published-Asset immutability, lifecycle revalidation, and maintenance idempotence
- [x] Authority-preservation, faceted trust, and scope-qualified completeness invariants
- [x] No automatic Layer 1 mutation and default upstream read-only boundary
- [x] `PA-Codebase-Inventory` source classes and bounded maintenance procedure
- [x] Stable repository identity / rename / split / merge semantics
- [x] CB-01 Profile enum/schema alignment and deterministic vs Human-reviewed publication boundary
- [x] `PA-Historical-Delivery` historical source and delivery-unit identity model
- [x] Per-source correlation and historical-change-fact contracts with preserved historical identity
- [x] `UNKNOWN` as safe default for ambiguous delivery relevance
- [x] Historical delivery outcome and delivered-as-of semantics aligned to PA-05 Profile
- [x] DH-01 deterministic vs Human-reviewed publication boundary
- [x] DH-02 index delta is navigation only and exposes support/denominator
- [x] Frontier Team accountability vs Agent execution boundary
- [x] First implementation boundary and non-goals

Current state:

```text
Layer 1 Contract-ready: APPROVED
Layer 2 Product Intelligence Contract-ready: APPROVED
Product Asset Profile v0.1 Contract-ready: APPROVED

Product Asset Maintenance Skill Contracts v0.1:
Contract review: PASS
Contract-ready: APPROVED
Herman design approval: APPROVED
Execution-verified: NOT_CLAIMED
Physical SKILL.md validation: NOT_CLAIMED
Implementation/publication: NOT_AUTHORIZED_BY_THIS_DESIGN
```

---

# 12. Compact Model

```text
                  FRONTIER TEAM

         maintenance request / source change
                       |
                       v
       +----------------------------------+
       |       PA-* Maintenance Skill     |
       |                                  |
       |  sources + current Asset         |
       |  + supporting Product Assets     |
       +----------------+-----------------+
                        |
                        v
                Maintenance Bundle
              /          |          \
             /           |           \
       NO_CHANGE   REVISION/LIFECYCLE   BLOCKED
                         |
                         v
              publication eligibility
                /             \
       RULE_BASED_AUTO      HUMAN_APPROVAL
                         |
                         v
                  PUBLISHED + ACTIVE
                         |
                         v
                 Product Asset Ref
                         |
                         v
─────────────────────────┼────────────────────────
                         |
                    LAYER 1 Context
                         |
                         v
                     FT-* Skill
```

The central invariant is:

> **PA-* Skills maintain durable Product Assets for the Frontier Team; FT-* Skills consume selected Product Assets as Context to deliver a specific feature. Neither layer silently acquires the authority of the other.**
