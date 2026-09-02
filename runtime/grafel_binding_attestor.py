"""Concrete Grafel snapshot-binding attestation for FDI Structural Intelligence.

This module is provider-specific on purpose.  It combines two independent
Grafel surfaces:

* MCP ``grafel_orient`` at an explicit ``group`` + ``ref`` proves that the
  routed graph is queryable and not still warming/indexing.
* The Grafel dashboard group metadata endpoint exposes each repo graph header's
  ``indexed_ref`` + ``indexed_sha``.  Those values are compared with the
  canonical revisions in ``StructuralSnapshotRef``.

The returned object is provider-independent binding state consumed by
``validate_snapshot_binding``.  It does not publish Product Intelligence and it
never establishes current Feature truth.
"""
from __future__ import annotations

from copy import deepcopy
import json
import re
from urllib.parse import quote
from urllib.request import Request, urlopen

from runtime.structural_intelligence import StructuralIntelligenceError, validate_snapshot_ref


class GrafelBindingAttestorError(ValueError):
    """Raised when live Grafel provenance cannot prove an exact snapshot."""


_HEX_RE = re.compile(r"^[0-9a-fA-F]+$")
_ALLOWED_FRESHNESS = {"LIVE_CURRENT", "FROZEN_INDEXED"}


def _unwrap_mapping(value):
    """Accept common HTTP/MCP envelopes without leaking them into FDI."""
    if isinstance(value, str):
        try:
            return _unwrap_mapping(json.loads(value))
        except json.JSONDecodeError as exc:
            raise GrafelBindingAttestorError("Grafel text response is not JSON") from exc
    if not isinstance(value, dict):
        raise GrafelBindingAttestorError("Grafel response must be an object")
    if isinstance(value.get("structuredContent"), dict):
        return _unwrap_mapping(value["structuredContent"])
    if isinstance(value.get("data"), dict):
        return _unwrap_mapping(value["data"])
    if isinstance(value.get("result"), dict):
        return _unwrap_mapping(value["result"])
    content = value.get("content")
    if isinstance(content, list) and content:
        text_parts = [item.get("text") for item in content if isinstance(item, dict) and isinstance(item.get("text"), str)]
        if text_parts:
            try:
                return _unwrap_mapping(json.loads("".join(text_parts)))
            except json.JSONDecodeError as exc:
                raise GrafelBindingAttestorError("Grafel MCP text content is not JSON") from exc
    return value


def _git_sha_matches(provider_sha: str, canonical_revision: str) -> bool:
    """Match Grafel's abbreviated indexed SHA to a canonical Git revision.

    Grafel persists an abbreviated SHA in graph metadata.  FDI keeps the full
    canonical revision when available.  We accept only hexadecimal prefix
    equivalence with at least 12 provider SHA characters; branch names or
    arbitrary string equality are not accepted as revision proof.
    """
    if not isinstance(provider_sha, str) or not isinstance(canonical_revision, str):
        return False
    provider_sha = provider_sha.strip().lower()
    canonical_revision = canonical_revision.strip().lower()
    if len(provider_sha) < 12 or len(canonical_revision) < 12:
        return False
    if not _HEX_RE.fullmatch(provider_sha) or not _HEX_RE.fullmatch(canonical_revision):
        return False
    return canonical_revision.startswith(provider_sha) or provider_sha.startswith(canonical_revision)


class StaticGrafelSnapshotRouteResolver:
    """Explicit snapshot-id -> Grafel route binding used by an execution plan.

    The resolver deliberately requires an explicit repository identity map.
    FDI repository identities and Grafel repo slugs are separate namespaces and
    must not be guessed during attestation.
    """

    def __init__(self, routes: dict):
        if not isinstance(routes, dict) or not routes:
            raise GrafelBindingAttestorError("routes must be a non-empty mapping")
        self._routes = deepcopy(routes)

    def __call__(self, snapshot_ref: dict) -> dict:
        snapshot_id = snapshot_ref.get("snapshot_id") if isinstance(snapshot_ref, dict) else None
        route = self._routes.get(snapshot_id)
        if not isinstance(route, dict):
            raise GrafelBindingAttestorError(f"no Grafel route for snapshot: {snapshot_id}")
        return deepcopy(route)


class GrafelDashboardGroupMetadataClient:
    """Read per-repository graph provenance from Grafel's dashboard API."""

    def __init__(self, base_url: str, *, opener=None, timeout_seconds: float = 5.0):
        if not isinstance(base_url, str) or not base_url.strip():
            raise GrafelBindingAttestorError("Grafel dashboard base_url is required")
        if not isinstance(timeout_seconds, (int, float)) or timeout_seconds <= 0:
            raise GrafelBindingAttestorError("timeout_seconds must be positive")
        self._base_url = base_url.rstrip("/")
        self._opener = opener or urlopen
        self._timeout = float(timeout_seconds)

    def get_group(self, group_id: str) -> dict:
        if not isinstance(group_id, str) or not group_id:
            raise GrafelBindingAttestorError("Grafel group_id is required")
        url = f"{self._base_url}/api/v2/groups/{quote(group_id, safe='')}"
        request = Request(url, method="GET", headers={"Accept": "application/json"})
        try:
            with self._opener(request, timeout=self._timeout) as response:
                raw = response.read()
        except Exception as exc:  # exact HTTP/client type is environment-specific
            raise GrafelBindingAttestorError(f"Grafel group metadata request failed: {exc}") from exc
        try:
            decoded = json.loads(raw.decode("utf-8"))
        except Exception as exc:
            raise GrafelBindingAttestorError("Grafel group metadata is not valid UTF-8 JSON") from exc
        return deepcopy(_unwrap_mapping(decoded))


class GrafelSnapshotBindingAttestor:
    """Provider-specific live implementation of ``SnapshotBindingAttestor``."""

    def __init__(
        self,
        transport,
        *,
        route_resolver,
        group_metadata_client,
        orient_tool: str = "grafel_orient",
    ):
        if transport is None or not callable(getattr(transport, "invoke", None)):
            raise GrafelBindingAttestorError("transport must provide invoke(tool_name, payload)")
        if not callable(route_resolver):
            raise GrafelBindingAttestorError("route_resolver must be callable")
        if group_metadata_client is None or not callable(getattr(group_metadata_client, "get_group", None)):
            raise GrafelBindingAttestorError("group_metadata_client must provide get_group(group_id)")
        if not isinstance(orient_tool, str) or not orient_tool:
            raise GrafelBindingAttestorError("orient_tool is required")
        self._transport = transport
        self._route_resolver = route_resolver
        self._metadata = group_metadata_client
        self._orient_tool = orient_tool

    def _route(self, snapshot: dict) -> dict:
        try:
            route = self._route_resolver(deepcopy(snapshot))
        except Exception as exc:
            if isinstance(exc, GrafelBindingAttestorError):
                raise
            raise GrafelBindingAttestorError(f"Grafel route resolution failed: {exc}") from exc
        if not isinstance(route, dict):
            raise GrafelBindingAttestorError("Grafel route must be an object")
        scope_id = route.get("provider_scope_id")
        provider_ref = route.get("provider_ref")
        freshness = route.get("freshness")
        repository_map = route.get("repository_map")
        if not isinstance(scope_id, str) or not scope_id:
            raise GrafelBindingAttestorError("provider_scope_id is required")
        if not isinstance(provider_ref, str) or not provider_ref:
            raise GrafelBindingAttestorError("provider_ref is required")
        if freshness not in _ALLOWED_FRESHNESS:
            raise GrafelBindingAttestorError("freshness must be LIVE_CURRENT or FROZEN_INDEXED")
        if not isinstance(repository_map, dict) or not repository_map:
            raise GrafelBindingAttestorError("repository_map must be a non-empty mapping")

        expected_repos = {item["repository"] for item in snapshot["source_snapshots"]}
        if set(repository_map) != expected_repos:
            raise GrafelBindingAttestorError("repository_map must exactly cover StructuralSnapshotRef repositories")
        if any(not isinstance(slug, str) or not slug for slug in repository_map.values()):
            raise GrafelBindingAttestorError("repository_map values must be non-empty Grafel repo slugs")
        if len(set(repository_map.values())) != len(repository_map):
            raise GrafelBindingAttestorError("repository_map Grafel repo slugs must be unique")

        return {
            "provider_scope_id": scope_id,
            "provider_ref": provider_ref,
            "freshness": freshness,
            "repository_map": deepcopy(repository_map),
        }

    def _probe_route(self, route: dict) -> dict:
        payload = {
            "view": "me",
            "group": route["provider_scope_id"],
            "ref": route["provider_ref"],
        }
        try:
            raw = self._transport.invoke(self._orient_tool, payload)
        except Exception as exc:
            raise GrafelBindingAttestorError(f"Grafel explicit route is not queryable: {exc}") from exc
        result = _unwrap_mapping(raw)
        if result.get("error"):
            raise GrafelBindingAttestorError(f"Grafel explicit route is not queryable: {result['error']}")
        if not result:
            raise GrafelBindingAttestorError("Grafel orient response is incomplete")
        if result.get("group") != route["provider_scope_id"]:
            raise GrafelBindingAttestorError("Grafel orient provider scope is missing or does not match")
        if result.get("indexed_ref") != route["provider_ref"]:
            raise GrafelBindingAttestorError("Grafel orient resolved a different provider ref or omitted provider ref")
        # Grafel v0.3.0 does not emit ``queryable``. Exact route identity plus
        # explicit idle booleans is its affirmative queryability evidence. If a
        # provider does emit the field, contradictory evidence still fails closed.
        if "queryable" in result and result["queryable"] is not True:
            raise GrafelBindingAttestorError("Grafel explicit route reports non-queryable state")
        if result.get("warming") is not False:
            raise GrafelBindingAttestorError("Grafel explicit route warming state is not explicitly false")
        if result.get("indexing") is not False:
            raise GrafelBindingAttestorError("Grafel explicit route indexing state is not explicitly complete")
        return result

    def __call__(self, snapshot_ref: dict) -> dict:
        try:
            snapshot = validate_snapshot_ref(snapshot_ref)
        except StructuralIntelligenceError as exc:
            raise GrafelBindingAttestorError(str(exc)) from exc
        if snapshot["provider"]["name"] != "GRAFEL":
            raise GrafelBindingAttestorError("GrafelSnapshotBindingAttestor requires provider.name=GRAFEL")

        route = self._route(snapshot)
        self._probe_route(route)
        group = _unwrap_mapping(self._metadata.get_group(route["provider_scope_id"]))
        if group.get("id") != route["provider_scope_id"]:
            raise GrafelBindingAttestorError("Grafel group metadata scope identity is missing or does not match")
        repos = group.get("repos")
        if not isinstance(repos, list):
            raise GrafelBindingAttestorError("Grafel group metadata repos must be a list")
        by_slug = {}
        for repo in repos:
            if not isinstance(repo, dict) or not isinstance(repo.get("slug"), str) or not repo.get("slug"):
                raise GrafelBindingAttestorError("Grafel group metadata repo requires slug")
            if repo["slug"] in by_slug:
                raise GrafelBindingAttestorError(f"duplicate Grafel repo slug: {repo['slug']}")
            by_slug[repo["slug"]] = repo

        expected_slugs = set(route["repository_map"].values())
        if set(by_slug) != expected_slugs:
            raise GrafelBindingAttestorError("Grafel group metadata repository set does not match repository_map")

        canonical = {item["repository"]: item["revision"] for item in snapshot["source_snapshots"]}
        normalized = []
        for repository in sorted(canonical):
            slug = route["repository_map"][repository]
            provider_repo = by_slug.get(slug)
            if provider_repo is None:
                raise GrafelBindingAttestorError(f"Grafel group metadata missing repository: {slug}")
            if provider_repo.get("indexed_ref") != route["provider_ref"]:
                raise GrafelBindingAttestorError(f"Grafel repository indexed_ref does not match provider_ref: {repository}")
            provider_sha = provider_repo.get("indexed_sha")
            if not _git_sha_matches(provider_sha, canonical[repository]):
                raise GrafelBindingAttestorError(f"Grafel repository indexed SHA does not match canonical revision: {repository}")
            normalized.append(
                {
                    "repository": repository,
                    "provider_repository": slug,
                    # Normalize the provider's abbreviated SHA back to the exact
                    # canonical revision expected by provider-neutral validation.
                    "indexed_revision": canonical[repository],
                    "queryable": True,
                    "head_revision": provider_repo.get("head_revision"),
                }
            )

        return {
            "provider_scope_id": route["provider_scope_id"],
            "provider_ref": route["provider_ref"],
            "queryability": "QUERYABLE",
            "freshness": route["freshness"],
            "repositories": normalized,
        }
