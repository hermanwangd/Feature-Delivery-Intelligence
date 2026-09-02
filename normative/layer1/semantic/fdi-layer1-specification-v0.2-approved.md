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
