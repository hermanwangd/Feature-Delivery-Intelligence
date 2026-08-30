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
