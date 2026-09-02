# Layer 1 Semantic v0.2 ↔ Markdown I/O v0.1 Compatibility

## Result

`PASS`

The selected semantic module remains compatible with the approved Markdown I/O
profile. No L1-I/O successor is required.

## Evidence

| Check | Semantic v0.2 | I/O v0.1 | Result |
| --- | --- | --- | --- |
| Dependency identity | Layer 1 v0.2 | Explicitly depends on Layer 1 v0.2 | PASS |
| Canonical flow | T1 → T2 → T3 → T4 | Same four files/transitions | PASS |
| Core artifacts | `intention.md`, `spec.md`, `implementation.md`, `correctness.md` | Same exact core files | PASS |
| Gates | `INTENTION_READY`, `SPEC_READY`, `CHANGE_SET_READY`, `PASS|FAIL|INCONCLUSIVE`, each with fail-closed behavior | Same gate fields and legal values | PASS |
| Artifact envelope | Identity, revision, upstream, producer Skill, owner, gate, validity, supersession | Frontmatter and required sections encode the same fields | PASS |
| Appendices | Conditional, bounded, registered, no independent gate | Three governed appendix profiles preserve those rules | PASS |
| Multi-repository authority | Coordination owns aggregate; source repositories own source/review/release | Same ownership/backlink boundary | PASS |
| Evidence | Exact claim/method/origin/revision/environment/integrity/limits/backlinks | Same evidence table/appendix requirements | PASS |
| Validity/re-entry | Gate and validity distinct; deterministic invalidation and earliest re-entry | Same lifecycle and re-entry sections | PASS |

Exact inputs:

- L1 semantic SHA-256: `9442f7ad788d4ffa59f9b1d5ef77de9b119550846df1e09df77737aa3fc7307d`
- L1 I/O SHA-256: `9793619861bf0745914746a2909a195131d318426f74d0eace6caabf34ac4c45`

The v0.3 candidate's extra physical paths are not used to alter this result.

