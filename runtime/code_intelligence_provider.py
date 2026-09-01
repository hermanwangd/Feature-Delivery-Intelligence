"""Provider-independent Structural Intelligence capability contract.

The Protocol is intentionally storage/provider neutral. Grafel is only the
reference MVP implementation; Layer 1 and Layer 2 contracts depend on this
surface, not on Grafel MCP names or response schemas.
"""
from __future__ import annotations

from typing import Protocol, runtime_checkable


@runtime_checkable
class SnapshotBindingAttestor(Protocol):
    """Provider/version-specific proof that an exact provider route is queryable.

    Implementations may consult provider provenance, source control, or a frozen
    replay workspace. They return provider-independent binding state consumed by
    ``validate_snapshot_binding``.
    """

    def __call__(self, snapshot_ref: dict) -> dict: ...


@runtime_checkable
class CodeIntelligenceProvider(Protocol):
    def orient(self, request: dict, snapshot_ref: dict): ...
    def find(self, structural_query: dict, snapshot_ref: dict) -> dict: ...
    def expand(self, structural_query: dict, snapshot_ref: dict) -> dict: ...
    def trace(self, structural_query: dict, snapshot_ref: dict) -> dict: ...
    def diff(self, request: dict, before_snapshot_ref: dict, after_snapshot_ref: dict) -> dict: ...
