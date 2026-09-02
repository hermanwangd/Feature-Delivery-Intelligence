# Maintain Product Intelligence

Incremental maintenance should operate on bounded deltas and avoid mandatory whole-product rescans.

```text
source delta
   ↓
pinned evidence
   ↓
affected Asset resolution
   ↓
structural/semantic delta analysis
   ↓
MaintenanceSignal / ProductAssetProposal
   ↓
review/publication policy
   ↓
new immutable Asset revision
```

Layer 1 reusable findings may create maintenance signals but cannot silently publish Product Assets.
