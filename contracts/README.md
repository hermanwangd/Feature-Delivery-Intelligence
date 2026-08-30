# Phase 1 contract conventions

These six files are the complete Phase 1 framework/agent contract set. They use JSON Schema Draft 2020-12 and validate JSON or YAML-decoded instances. `make validate` is the repository-native validation command.

## Identity and compatibility

- Contract versions use SemVer. Backward-incompatible changes increment the major version; compatible required-field additions are not permitted within a major version unless a default-free migration is documented.
- Stable IDs match `^[a-z0-9]+(?:-[a-z0-9]+)*$`, except case-preserving delivery `feature_id` values. IDs are never derived from array positions.
- Revisions are positive and monotonic. Historical revisions are immutable; changes create a new revision and use `supersedes` or `superseded_by`.
- SHA-256 digests are lowercase 64-character hexadecimal strings and cover the exact referenced bytes.

## Provenance, unknowns, and ordering

- Source references are immutable. Runtime observations must name `environment` and `observed_at`.
- Unknowns are explicit records with materiality, owner, resolution condition, and earliest re-entry. Absence, empty strings, and `null` never silently mean unknown.
- Schemas reject undeclared fields. Nullable fields are explicitly typed and require a reason where the contract demands one.
- Arrays that represent sets are serialized in ascending stable-ID order. Paths are POSIX-relative, Unicode NFC, have no `.` or `..` segments, and are compared case-sensitively.
- Canonical JSON uses UTF-8, sorted keys, compact separators, and a trailing newline. Semantic digests exclude observational timing/cost fields only where the scorer contract says so.

## Authority and isolation

Scores and historical patterns order investigation only. `CONFIRMED` and `EXCLUDED` require current feature-specific evidence. None of the six records owns `INTENTION_READY`, `SPEC_READY`, or another canonical gate.

`validation/**/evaluator-only/` is unavailable to investigation and closure-review agents. Ground truth, answer-bearing identities, adjudication, and replay score state never become execution Context.
