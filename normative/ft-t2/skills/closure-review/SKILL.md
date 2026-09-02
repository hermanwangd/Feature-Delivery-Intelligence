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
