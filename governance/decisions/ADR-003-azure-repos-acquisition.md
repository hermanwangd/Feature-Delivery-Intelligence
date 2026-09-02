# ADR-003 — Azure Repos Acquisition

**Decision:** Azure Repos is a source provider. FDI clones/fetches and materializes exact local worktrees at full Git revisions; Grafel analyzes those frozen worktrees. Credentials remain external to FDI files.
