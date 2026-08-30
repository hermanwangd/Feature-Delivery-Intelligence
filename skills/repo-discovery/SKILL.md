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
