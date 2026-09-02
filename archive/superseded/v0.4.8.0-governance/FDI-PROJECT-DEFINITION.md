# Feature Delivery Intelligence — Recovery Project Definition

FDI is a reusable agentic product-development workflow package intended to run on Multica.

It exposes two product workflows:

- **Maintain Product** — acquire evidence, derive observations, synthesize proposals, govern durable Layer 2 Product Intelligence.
- **Develop Feature** — consume selectively resolved Product Intelligence plus current evidence through Layer 1 T1–T4.

## Architecture

```text
                         Product Owner
                              │
                 ┌────────────┴────────────┐
                 │                         │
          Maintain Product          Develop Feature
                 │                         │
                 ▼                         ▼
     ┌──────────────────────┐   ┌─────────────────────────┐
     │ Layer 2              │   │ Layer 1                 │
     │ Product Intelligence │──▶│ Feature Execution       │
     │                      │   │ T1 → T2 → T3 → T4       │
     └──────────┬───────────┘   └────────────┬────────────┘
                ▲                            │
                │ Product Asset Update       │
                │ Proposal                   │
                └────────────────────────────┘

              ─────────────────────────────────
                    Multica Execution Plane
              ─────────────────────────────────
```

Layer 2 acquisition outputs Evidence/Observations, not Product truth. Agent synthesis creates `ProductAssetProposal`. Publication governance creates durable Product Assets.

MVP proof target remains downstream value: better multi-repository candidate and Change Surface discovery quality/efficiency with bounded Product/Structural Intelligence, not graph size or contract-test success alone.
