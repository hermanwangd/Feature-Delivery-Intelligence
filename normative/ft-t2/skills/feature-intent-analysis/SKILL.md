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
