from __future__ import annotations

import asyncio
import json as json_module
import threading
import time
from types import TracebackType
from typing import Any, AsyncGenerator, Dict, Generator, Optional, Type

import httpx
from tenacity import (
    AsyncRetrying,
    Retrying,
    retry_if_exception,
    stop_after_attempt,
    wait_exponential,
)

from .auth import AsyncAuthProtocol, ExactOnlineAuth, SyncAuthProtocol
from .config import Settings
from .exceptions import APIError, RateLimitError, api_error_from_status
from .utils.logger import get_logger

_REQUEST_ID_HEADER_CANDIDATES: tuple[str, ...] = (
    "Exact-Request-ID",
    "Exact-Request-Id",
    "X-Request-ID",
    "Request-Id",
    "X-Correlation-ID",
)


def _extract_request_id(headers: httpx.Headers) -> Optional[str]:
    """Return the first matching request id found in the response headers."""

    for header in _REQUEST_ID_HEADER_CANDIDATES:
        value = headers.get(header)
        if value:
            return str(value)
    return None


def _is_retryable(exc: BaseException) -> bool:
    if isinstance(exc, RateLimitError):
        return True
    if isinstance(exc, APIError) and 500 <= exc.status_code < 600:
        return True
    if isinstance(exc, httpx.HTTPError):
        return True
    return False


def _response_context(resp: httpx.Response) -> dict[str, Any]:
    context: dict[str, Any] = {"url": str(resp.request.url)}
    request_id = _extract_request_id(resp.headers)
    if request_id:
        context["request_id"] = request_id
    content_type = resp.headers.get("Content-Type")
    if content_type:
        context["content_type"] = content_type
    return context


def _json_request_headers(headers: dict[str, str]) -> dict[str, str]:
    request_headers = dict(headers)
    request_headers.setdefault("Accept", "application/json")
    return request_headers


def _copy_request_params(
    params: Optional[Dict[str, Any]],
) -> Optional[Dict[str, Any]]:
    if params is None:
        return None
    return dict(params)


def _content_type_looks_json(content_type: Optional[str]) -> bool:
    if not content_type:
        return False
    lowered = content_type.lower()
    return "json" in lowered


def _parse_json_response(resp: httpx.Response) -> Any:
    if not resp.content:
        return None

    context = _response_context(resp)
    content_type = context.get("content_type")
    try:
        return resp.json()
    except (ValueError, json_module.JSONDecodeError) as exc:
        if _content_type_looks_json(content_type):
            message = (
                f"Failed to parse JSON response from {context['url']} "
                f"(content-type: {content_type})"
            )
        else:
            message = (
                f"Expected JSON response from {context['url']} but received "
                f"content-type {content_type or 'unknown'}"
            )
        raise api_error_from_status(resp.status_code, message, context=context) from exc


def _normalize_response_payload(data: Any) -> Any:
    if isinstance(data, dict):
        envelope = data.get("d")
        if isinstance(envelope, dict) and isinstance(envelope.get("results"), list):
            return list(envelope["results"])
        if "value" in data:
            return data["value"]
    return data


def _extract_page_items_and_next_link(
    data: Any,
) -> tuple[list[Any], Optional[str]]:
    next_link: Optional[str] = None
    items: list[Any] = []

    if isinstance(data, dict):
        envelope = data.get("d")
        if isinstance(envelope, dict):
            if isinstance(envelope.get("results"), list):
                items = list(envelope["results"])
            next_link = envelope.get("__next") or envelope.get("@odata.nextLink")
        if not items and isinstance(data.get("value"), list):
            items = list(data["value"])
            next_link = data.get("@odata.nextLink")
    elif isinstance(data, list):
        items = list(data)

    return items, next_link


class ExactOnlineClient:
    """Synchronous HTTP client for Exact Online.

    Thread-safe: all HTTP calls are serialised via an internal lock.
    For higher throughput from multiple threads, use one client per thread
    or switch to :class:`AsyncExactOnlineClient`.
    """

    def __init__(
        self, settings: Settings, *, auth: Optional[SyncAuthProtocol] = None
    ) -> None:
        self._settings = settings
        self._auth: SyncAuthProtocol = auth or ExactOnlineAuth(settings)
        self._logger = get_logger(__name__)
        self._http_lock = threading.Lock()
        self._client = httpx.Client(
            timeout=settings.timeout,
            headers={"User-Agent": settings.user_agent, "Accept": "application/json"},
        )

    def close(self) -> None:
        self._client.close()

    def _resolve_path(self, path: str) -> str:
        if path.startswith("!"):
            return path[1:]
        division = self._settings.division
        if division is None:
            return path
        if "{division}" in path:
            return path.format(division=division)
        return f"{division}/{path.lstrip('/')}"

    def _auth_header(self) -> dict[str, str]:
        token = self._auth.get_access_token()
        return {"Authorization": f"Bearer {token}"}

    def _request_headers(self) -> dict[str, str]:
        return _json_request_headers(self._auth_header())

    def _handle_response(self, resp: httpx.Response) -> Any:
        context = _response_context(resp)
        if resp.status_code == 429:
            retry_after = float(resp.headers.get("Retry-After", "0") or 0)
            raise RateLimitError(
                "Rate limit exceeded", retry_after=retry_after, context=context
            )
        if not 200 <= resp.status_code < 300:
            message = resp.text
            raise api_error_from_status(resp.status_code, message, context=context)
        # Parse common payload shapes
        data = _parse_json_response(resp)
        return _normalize_response_payload(data)

    def _request_impl(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        headers = self._request_headers()
        request_params = _copy_request_params(params)
        resolved = self._resolve_path(path)
        url = f"{self._settings.base_url}/api/v1/{resolved.lstrip('/')}"
        with self._http_lock:
            try:
                resp = self._client.request(
                    method, url, params=request_params, json=json, headers=headers
                )
            except httpx.HTTPError as exc:
                raise api_error_from_status(0, f"HTTP error: {exc}") from exc

        try:
            return self._handle_response(resp)
        except RateLimitError as rle:
            if rle.retry_after and rle.retry_after > 0:
                time.sleep(rle.retry_after)
            raise

    def _request(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        for attempt in Retrying(
            retry=retry_if_exception(_is_retryable),
            wait=wait_exponential(multiplier=1, min=1, max=30),
            stop=stop_after_attempt(5),
            reraise=True,
        ):
            with attempt:
                return self._request_impl(method, path, params=params, json=json)

    # Public API
    def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("GET", path, params=params)

    def post(self, path: str, *, json: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("POST", path, json=json)

    def patch(self, path: str, *, json: Optional[Dict[str, Any]] = None) -> Any:
        return self._request("PATCH", path, json=json)

    def delete(self, path: str) -> Any:
        return self._request("DELETE", path)

    def iter_pages(
        self, path: str, *, params: Optional[Dict[str, Any]] = None
    ) -> Generator[list[Any], None, None]:
        def _build_url(p: str) -> str:
            if p.startswith("http"):
                return p
            resolved = self._resolve_path(p)
            return f"{self._settings.base_url}/api/v1/{resolved.lstrip('/')}"

        url = _build_url(path)
        next_params = _copy_request_params(params)
        while True:
            # Retry each page independently
            for attempt in Retrying(
                retry=retry_if_exception(_is_retryable),
                wait=wait_exponential(multiplier=1, min=1, max=30),
                stop=stop_after_attempt(5),
                reraise=True,
            ):
                with attempt:
                    headers = self._request_headers()
                    with self._http_lock:
                        try:
                            resp = self._client.request(
                                "GET", url, params=next_params, headers=headers
                            )
                        except httpx.HTTPError as exc:
                            raise api_error_from_status(
                                0, f"HTTP error: {exc}"
                            ) from exc

                    if resp.status_code == 429:
                        retry_after = float(resp.headers.get("Retry-After", "0") or 0)
                        if retry_after > 0:
                            time.sleep(retry_after)
                        raise RateLimitError(
                            "Rate limit exceeded",
                            retry_after=retry_after,
                            context=_response_context(resp),
                        )
                    if not 200 <= resp.status_code < 300:
                        raise api_error_from_status(
                            resp.status_code,
                            resp.text,
                            context=_response_context(resp),
                        )

                    items, next_link = _extract_page_items_and_next_link(
                        _parse_json_response(resp)
                    )
                    yield items
                    if next_link:
                        url = _build_url(next_link)
                        next_params = None
                    else:
                        return

    # Context manager
    def __enter__(self) -> "ExactOnlineClient":
        return self

    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        self.close()


class AsyncExactOnlineClient:
    """Asynchronous HTTP client for Exact Online.

    Safe for concurrent use from multiple asyncio tasks within a single
    event loop. Token refresh is serialised via an ``asyncio.Lock``.
    """

    def __init__(
        self, settings: Settings, *, auth: Optional[AsyncAuthProtocol] = None
    ) -> None:
        self._settings = settings
        self._auth: AsyncAuthProtocol = auth or ExactOnlineAuth(settings)
        self._logger = get_logger(__name__)
        self._client = httpx.AsyncClient(
            timeout=settings.timeout,
            headers={"User-Agent": settings.user_agent, "Accept": "application/json"},
        )

    async def aclose(self) -> None:
        await self._client.aclose()

    def _resolve_path(self, path: str) -> str:
        if path.startswith("!"):
            return path[1:]
        division = self._settings.division
        if division is None:
            return path
        if "{division}" in path:
            return path.format(division=division)
        return f"{division}/{path.lstrip('/')}"

    async def _auth_header(self) -> dict[str, str]:
        token = await self._auth.aget_access_token()
        return {"Authorization": f"Bearer {token}"}

    async def _request_headers(self) -> dict[str, str]:
        return _json_request_headers(await self._auth_header())

    def _handle_response(self, resp: httpx.Response) -> Any:
        context = _response_context(resp)
        if resp.status_code == 429:
            retry_after = float(resp.headers.get("Retry-After", "0") or 0)
            raise RateLimitError(
                "Rate limit exceeded", retry_after=retry_after, context=context
            )
        if not 200 <= resp.status_code < 300:
            message = resp.text
            raise api_error_from_status(resp.status_code, message, context=context)
        data = _parse_json_response(resp)
        return _normalize_response_payload(data)

    async def _arequest_impl(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        headers = await self._request_headers()
        request_params = _copy_request_params(params)
        resolved = self._resolve_path(path)
        url = f"{self._settings.base_url}/api/v1/{resolved.lstrip('/')}"
        try:
            resp = await self._client.request(
                method, url, params=request_params, json=json, headers=headers
            )
        except httpx.HTTPError as exc:
            raise api_error_from_status(0, f"HTTP error: {exc}") from exc

        try:
            return self._handle_response(resp)
        except RateLimitError as rle:
            if rle.retry_after and rle.retry_after > 0:
                await asyncio.sleep(rle.retry_after)
            raise

    async def _arequest(
        self,
        method: str,
        path: str,
        *,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None,
    ) -> Any:
        async for attempt in AsyncRetrying(
            retry=retry_if_exception(_is_retryable),
            wait=wait_exponential(multiplier=1, min=1, max=30),
            stop=stop_after_attempt(5),
            reraise=True,
        ):
            with attempt:
                return await self._arequest_impl(method, path, params=params, json=json)

    async def get(self, path: str, *, params: Optional[Dict[str, Any]] = None) -> Any:
        return await self._arequest("GET", path, params=params)

    async def post(self, path: str, *, json: Optional[Dict[str, Any]] = None) -> Any:
        return await self._arequest("POST", path, json=json)

    async def patch(self, path: str, *, json: Optional[Dict[str, Any]] = None) -> Any:
        return await self._arequest("PATCH", path, json=json)

    async def delete(self, path: str) -> Any:
        return await self._arequest("DELETE", path)

    async def __aenter__(self) -> "AsyncExactOnlineClient":
        return self

    async def __aexit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc: Optional[BaseException],
        tb: Optional[TracebackType],
    ) -> None:
        await self.aclose()

    async def aiter_pages(
        self, path: str, *, params: Optional[Dict[str, Any]] = None
    ) -> AsyncGenerator[list[Any], None]:
        def _build_url(p: str) -> str:
            if p.startswith("http"):
                return p
            resolved = self._resolve_path(p)
            return f"{self._settings.base_url}/api/v1/{resolved.lstrip('/')}"

        url = _build_url(path)
        next_params = _copy_request_params(params)
        while True:
            async for attempt in AsyncRetrying(
                retry=retry_if_exception(_is_retryable),
                wait=wait_exponential(multiplier=1, min=1, max=30),
                stop=stop_after_attempt(5),
                reraise=True,
            ):
                with attempt:
                    headers = await self._request_headers()
                    try:
                        resp = await self._client.request(
                            "GET", url, params=next_params, headers=headers
                        )
                    except httpx.HTTPError as exc:
                        raise api_error_from_status(0, f"HTTP error: {exc}") from exc

                    if resp.status_code == 429:
                        retry_after = float(resp.headers.get("Retry-After", "0") or 0)
                        if retry_after > 0:
                            await asyncio.sleep(retry_after)
                        raise RateLimitError(
                            "Rate limit exceeded",
                            retry_after=retry_after,
                            context=_response_context(resp),
                        )
                    if not 200 <= resp.status_code < 300:
                        raise api_error_from_status(
                            resp.status_code,
                            resp.text,
                            context=_response_context(resp),
                        )

                    items, next_link = _extract_page_items_and_next_link(
                        _parse_json_response(resp)
                    )
                    yield items
                    if next_link:
                        url = _build_url(next_link)
                        next_params = None
                    else:
                        return
