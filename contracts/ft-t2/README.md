# FT-T2 / HERM-211 Locked Helper Contract Surface

This directory binds the exact helper identities. It does not invent replacement schemas for unavailable approved bytes.

Exactly six helper contracts:

1. `IntentSpec`
2. `CandidateRepoSet`
3. `ChangeSurfaceSet`
4. `EvidenceRecord`
5. `ClosurePackage`
6. `ClosureReview`

Exactly five helper Skills:

1. `feature-intent-analysis`
2. `repo-discovery`
3. `changesurface-investigation`
4. `dependency-closure`
5. `closure-review`

Helper closure status is only `OPEN | PARTIAL | CLOSED_WITHIN_DECLARED_SCOPE`.
The sole canonical T2 gate remains `SPEC_READY | BLOCKED`.

If exact approved helper contract files are rehydrated, place them under `specs/approved/ft-t2/` and update the source lock/digests without renaming identities.
