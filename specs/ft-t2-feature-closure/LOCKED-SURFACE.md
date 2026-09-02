# HERM-211 FT-T2 Locked Surface

FT-T2 Feature Closure is subordinate to `T2-Delivery-Spec-Skill`.

## Six helper contracts

1. IntentSpec
2. CandidateRepoSet
3. ChangeSurfaceSet
4. EvidenceRecord
5. ClosurePackage
6. ClosureReview

## Five helper Skills

1. feature-intent-analysis
2. repo-discovery
3. changesurface-investigation
4. dependency-closure
5. closure-review

Helper closure status is only `OPEN | PARTIAL | CLOSED_WITHIN_DECLARED_SCOPE`.
The sole canonical T2 gate is `SPEC_READY | BLOCKED`.
`CLOSED_WITHIN_DECLARED_SCOPE != SPEC_READY`.
