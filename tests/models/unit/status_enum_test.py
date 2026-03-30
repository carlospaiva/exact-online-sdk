from __future__ import annotations

from enum import Enum

import pytest

from exact_online_sdk.models import (
    AccountStatus,
    QuotationStatus,
    SalesInvoiceStatus,
    SalesOrderStatus,
)


@pytest.mark.parametrize(
    ("enum_cls", "value"),
    [
        (AccountStatus, "Active"),
        (AccountStatus, "Inactive"),
        (SalesInvoiceStatus, "Draft"),
        (SalesInvoiceStatus, "Final"),
        (SalesOrderStatus, "Open"),
        (SalesOrderStatus, "Closed"),
    ],
)
def test_string_enums_match_expected_value(enum_cls: type[Enum], value: str) -> None:
    enum_member = enum_cls(value)
    assert enum_member.value == value
    assert str(enum_member) == value


@pytest.mark.parametrize(
    ("enum_cls", "value"),
    [
        (AccountStatus, "Disabled"),
        (SalesInvoiceStatus, "Cancelled"),
        (SalesOrderStatus, "Pending"),
    ],
)
def test_string_enums_reject_invalid_values(enum_cls: type[Enum], value: str) -> None:
    with pytest.raises(ValueError):
        enum_cls(value)


@pytest.mark.parametrize(
    "status_value",
    [
        QuotationStatus.REJECTED,
        QuotationStatus.REVIEWED_AND_CLOSED,
        QuotationStatus.RECOVERY,
        QuotationStatus.DRAFT,
        QuotationStatus.OPEN,
        QuotationStatus.PROCESSING,
        QuotationStatus.PRINTED,
        QuotationStatus.ACCEPTED,
        QuotationStatus.AWAITING_ONLINE_ACCEPTANCE,
        QuotationStatus.ACCEPTED_WITH_PROCESSING_ERROR,
    ],
)
def test_int_enum_values_roundtrip(status_value: QuotationStatus) -> None:
    recreated = QuotationStatus(status_value.value)
    assert recreated is status_value


@pytest.mark.parametrize("invalid_value", [-1, 0, 999])
def test_int_enum_rejects_invalid_values(invalid_value: int) -> None:
    with pytest.raises(ValueError):
        QuotationStatus(invalid_value)
