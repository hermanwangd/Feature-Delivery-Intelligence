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
