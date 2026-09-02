# NON-NORMATIVE PHYSICALIZATION CANDIDATE / STORE IMPLEMENTATION SCAFFOLD

# Product Intelligence Store

Durable Product Knowledge accumulates in a Product-owned Layer 2 `ProductIntelligenceStore`.

## MVP backend

```text
ProductIntelligenceStore
        ↓
GitStoreAdapter
        ↓
<product>-product-intelligence.git
```

The store contains governed Product Assets and immutable published semantic revisions. It does not contain raw Agent scratchpads, the full Grafel graph, arbitrary embeddings, or unqualified observations.

## Lifecycle

```text
ProductAssetProposal
      ↓
DRAFT revision
      ↓
validation / publication policy
      ↓
review when required
      ↓
PUBLISHED + ACTIVE
```

Git merge is not itself semantic authority; merge is only the physical publication event after the FDI publication gate succeeds.

## Registry

Registry/indexes are derived selection views. Loss of Registry should be recoverable from Product Assets. Loss of Product Intelligence Store means durable organizational PK is lost.
