# Architecture Decisions — Recovery Baseline

## ADR-001 — Grafel behind provider abstraction

FDI depends on `CodeIntelligenceProvider`, not Grafel schema/tool names.

```text
FDI Contract
    ↓
CodeIntelligenceProvider
    ↓
GrafelAdapter
    ↓
Grafel
```

Grafel produces rebuildable Structural Intelligence and normalized observations/hints/deltas. It is non-authoritative.

## ADR-002 — Product Knowledge physical home

Durable PK lives in a Product-owned `ProductIntelligenceStore`.

MVP reference backend: Git repository.

```text
ProductIntelligenceStore
        ↓
GitStoreAdapter
        ↓
<product>-product-intelligence.git
```

Git is storage/versioning, not semantic authority. Published revision semantics are governed by Product Asset descriptors and publication policy.

## ADR-003 — Registry is derived

Registry/indexes are navigation/selection projections and must backlink to exact Product Asset revisions. They are rebuildable from stored assets.

## ADR-004 — Azure Repos boundary

Azure Repos supplies Git sources. FDI acquires/clones/fetches into local frozen worktrees. Grafel indexes those worktrees. Authentication is external to FDI repository content.

## ADR-005 — No second canonical graph in MVP

Do not introduce TerminusDB, Graphiti, Neo4j or GitNexus in the MVP recovery baseline. Reconsider only after measured Git/index/traversal bottlenecks.

## ADR-006 — Structural vs semantic confidence lanes

Deterministic structural observations may become rule-based proposals when fully pinned and policy-eligible. Capability/domain/business-rule interpretations are semantic proposals and default to human review.
