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
