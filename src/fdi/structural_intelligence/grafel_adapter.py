from __future__ import annotations
from dataclasses import dataclass
from typing import Protocol
import json

class GrafelTransport(Protocol):
    def invoke(self, tool: str, payload: dict) -> dict: ...

class UnsupportedBoundError(ValueError):
    pass

@dataclass
class GrafelAdapter:
    transport: GrafelTransport
    adapter_version: str = "fdi-0.4.8.2"

    # Provider-specific names live only here.
    tool_map = {
        "ORIENT": "grafel_orient",
        "FIND": "grafel_find",
        "EXPAND": "grafel_subgraph",
        "TRACE": "grafel_find_paths",
        "DIFF": "grafel_diff",
    }

    def _provider_payload(self, snapshot: dict, query: dict) -> dict:
        # FDI-owned bounds are passed mechanically to the provider adapter. A live
        # Grafel binding must verify that the concrete provider/tool revision honors
        # these fields; otherwise compatibility verification must fail closed.
        payload = dict(query.get("payload", {}))
        payload.update({
            "group": snapshot["provider_scope_id"],
            "ref": snapshot["provider_ref"],
            "repository_scope": list(query["repository_scope"]),
            "relation_allowlist": list(query["relation_allowlist"]),
            "max_depth": int(query["max_depth"]),
            "max_nodes": int(query["max_nodes"]),
            "max_edges": int(query["max_edges"]),
            "max_paths": int(query["max_paths"]),
            "max_result_bytes": int(query["max_result_bytes"]),
        })
        return payload

    def _enforce_bounds(self, result: dict, query: dict) -> None:
        nodes = result.get("nodes", []) or []
        edges = result.get("edges", []) or []
        paths = result.get("paths", []) or []
        if len(nodes) > query["max_nodes"]: raise ValueError("max_nodes exceeded")
        if len(edges) > query["max_edges"]: raise ValueError("max_edges exceeded")
        if len(paths) > query["max_paths"]: raise ValueError("max_paths exceeded")
        if len(json.dumps(result, ensure_ascii=False).encode("utf-8")) > query["max_result_bytes"]:
            raise ValueError("max_result_bytes exceeded")

    def query(self, snapshot: dict, query: dict) -> dict:
        if query["snapshot_id"] != snapshot["snapshot_id"]:
            raise ValueError("query snapshot mismatch")
        if query["operation"] not in self.tool_map:
            raise ValueError("unsupported operation")
        payload = self._provider_payload(snapshot, query)
        raw = self.transport.invoke(self.tool_map[query["operation"]], payload)
        self._enforce_bounds(raw, query)
        return raw
