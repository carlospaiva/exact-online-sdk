from __future__ import annotations

import pytest

from exact_online_sdk.exceptions import (
    APIError,
    BadRequestError,
    ClientError,
    ConflictError,
    ForbiddenError,
    NotFoundError,
    ServerError,
    UnauthorizedError,
    UnprocessableEntityError,
    api_error_from_status,
)


@pytest.mark.parametrize(
    ("status", "expected_type"),
    [
        (400, BadRequestError),
        (401, UnauthorizedError),
        (403, ForbiddenError),
        (404, NotFoundError),
        (409, ConflictError),
        (422, UnprocessableEntityError),
    ],
)
def test_api_error_from_status_specific_mappings(
    status: int, expected_type: type[APIError]
) -> None:
    err = api_error_from_status(status, "msg")
    assert isinstance(err, expected_type)
    assert err.status_code == status


def test_api_error_from_status_client_and_server_ranges() -> None:
    client_err = api_error_from_status(418, "teapot")
    server_err = api_error_from_status(503, "down")

    assert isinstance(client_err, ClientError)
    assert isinstance(server_err, ServerError)


def test_api_error_from_status_fallback_to_generic() -> None:
    err = api_error_from_status(0, "oops")

    assert isinstance(err, APIError)
    assert not isinstance(err, ClientError)
    assert not isinstance(err, ServerError)
