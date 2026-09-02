# Grafel Adapter Contract v0.1

**FDI release:** v0.4.7.0<br>
**Classification:** reference provider adapter; not a governing Layer 1 or Product Asset contract.

## Boundary

FDI calls provider-independent operations:

```text
orient
find
expand
trace
diff
```

The reference Grafel binding currently maps these to the provider's MCP surface:

```text
orient  -> grafel_orient
find    -> grafel_find
expand  -> grafel_subgraph
trace   -> grafel_find_paths
diff    -> grafel_diff (aspect=refs)
```

Grafel is v0.x and provider MCP names/response schemas may change. Therefore:

1. provider tool names live only in `runtime/grafel_adapter.py`;
2. provider responses pass through an injected response mapper before FDI normalization;
3. normalized FDI observations use `StructuralObservationSet` and remain non-authoritative;
4. the adapter does not establish current Feature truth or Product Asset publication authority;
5. this overlay does not claim a live Grafel daemon/MCP integration test.

A future Grafel version change should modify the adapter/mapper, not Layer 1 contracts, Product Asset contracts, or FDI Feature semantics.
