# NON-NORMATIVE SOURCE-INTEGRATION IMPLEMENTATION GUIDE

# Azure Repos Source Integration

Azure DevOps / Azure Repos is treated as a Git source provider, not a Grafel authority.

```text
Azure Repos
    ↓ clone/fetch
FDI Source Acquisition
    ↓ exact commit resolution
Frozen local worktrees
    ↓
Grafel indexing
```

Authentication (PAT, SSH key, credential helper, enterprise SSO) stays outside committed project files.

For reproducible Layer 2 maintenance/evaluation, each repository entry must resolve to an exact full Git commit ID. Branch names alone are not sufficient provenance.

The same local-worktree approach works whether the origin is Azure Repos, GitHub, GitLab or another Git server.
