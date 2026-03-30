from __future__ import annotations

from typing import Any, Optional, Type


class ExactOnlineSDKError(Exception):
    """Base exception for the SDK."""

    def __init__(
        self, message: str, *, context: Optional[dict[str, Any]] = None
    ) -> None:
        super().__init__(message)
        self.context = context or {}


class ValidationError(ExactOnlineSDKError):
    """Raised on data validation errors."""


class AuthenticationError(ExactOnlineSDKError):
    """Raised when OAuth2 authentication fails."""


class RateLimitError(ExactOnlineSDKError):
    """Raised when the API rate limit is exceeded."""

    def __init__(
        self,
        message: str,
        *,
        retry_after: Optional[float] = None,
        context: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, context=context)
        self.retry_after = retry_after


class APIError(ExactOnlineSDKError):
    """Raised for non-success HTTP responses."""

    def __init__(
        self,
        status_code: int,
        message: str,
        *,
        context: Optional[dict[str, Any]] = None,
    ) -> None:
        super().__init__(message, context=context)
        self.status_code = status_code


class ClientError(APIError):
    """Base class for 4xx HTTP responses."""


class BadRequestError(ClientError):
    """Raised for HTTP 400 responses."""


class UnauthorizedError(ClientError):
    """Raised for HTTP 401 responses."""


class ForbiddenError(ClientError):
    """Raised for HTTP 403 responses."""


class NotFoundError(ClientError):
    """Raised for HTTP 404 responses."""


class ConflictError(ClientError):
    """Raised for HTTP 409 responses."""


class UnprocessableEntityError(ClientError):
    """Raised for HTTP 422 responses."""


class ServerError(APIError):
    """Raised for 5xx HTTP responses."""


_STATUS_EXCEPTION_MAP: dict[int, Type[APIError]] = {
    400: BadRequestError,
    401: UnauthorizedError,
    403: ForbiddenError,
    404: NotFoundError,
    409: ConflictError,
    422: UnprocessableEntityError,
}


def api_error_from_status(
    status_code: int, message: str, *, context: Optional[dict[str, Any]] = None
) -> APIError:
    """Map an HTTP status code to the most specific APIError subclass."""

    if status_code in _STATUS_EXCEPTION_MAP:
        exc_type = _STATUS_EXCEPTION_MAP[status_code]
        return exc_type(status_code, message, context=context)
    if 400 <= status_code < 500:
        return ClientError(status_code, message, context=context)
    if 500 <= status_code < 600:
        return ServerError(status_code, message, context=context)
    return APIError(status_code, message, context=context)
