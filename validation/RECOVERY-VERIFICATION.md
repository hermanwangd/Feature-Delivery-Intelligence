# Recovery Verification

Before continuing development:

1. Verify bundle manifest.
2. Validate JSON Schemas.
3. Run unit tests.
4. Validate Azure Repos source configuration without credentials in repo.
5. Resolve every selected source to full Git commit ID.
6. Build frozen local worktrees.
7. Bind Grafel exact scope/ref to per-repository revisions and persist machine-readable attestation evidence.
8. Only then run DEV-204 fresh-context behavior validation.
9. Only after DEV-204 success run F001 four-arm calibration.

Do not promote contract/unit-test success into empirical FDI effectiveness claims.
