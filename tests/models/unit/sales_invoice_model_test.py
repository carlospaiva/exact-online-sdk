from __future__ import annotations

from datetime import datetime, timezone
from decimal import Decimal
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    SalesInvoice,
    SalesInvoiceLine,
    SalesInvoiceOrderChargeLine,
    SalesInvoiceStatus,
)


def test_sales_invoice_parses_alias_payload() -> None:
    invoice_id = uuid4()
    ordered_by = uuid4()
    journal = "80"
    line_id = uuid4()
    item_id = uuid4()
    charge_line_id = uuid4()
    invoice_date = datetime.now(timezone.utc)

    payload = {
        "InvoiceID": str(invoice_id),
        "OrderedBy": str(ordered_by),
        "Journal": journal,
        "InvoiceDate": invoice_date.isoformat(),
        "SalesInvoiceLines": [
            {
                "ID": str(line_id),
                "InvoiceID": str(invoice_id),
                "Item": str(item_id),
            }
        ],
        "SalesInvoiceOrderChargeLines": [
            {
                "ID": str(charge_line_id),
                "InvoiceID": str(invoice_id),
                "AmountFCInclVAT": 12.0,
            }
        ],
        "Status": SalesInvoiceStatus.DRAFT.value,
    }

    invoice = SalesInvoice.model_validate(payload)

    assert invoice.invoice_id == invoice_id
    assert invoice.ordered_by == ordered_by
    assert invoice.journal == journal
    assert invoice.invoice_date == invoice_date
    assert invoice.status == SalesInvoiceStatus.DRAFT
    assert len(invoice.sales_invoice_lines) == 1
    assert invoice.sales_invoice_order_charge_lines is not None
    assert len(invoice.sales_invoice_order_charge_lines) == 1

    line = invoice.sales_invoice_lines[0]
    assert line.id == line_id
    assert line.invoice_id == invoice_id
    assert line.item == item_id

    charge_line = invoice.sales_invoice_order_charge_lines[0]
    assert charge_line.id == charge_line_id
    assert charge_line.invoice_id == invoice_id
    assert charge_line.amount_fc_incl_vat == 12.0


def test_sales_invoice_defaults_lists() -> None:
    ordered_by = uuid4()

    invoice = SalesInvoice.model_validate(
        {"OrderedBy": str(ordered_by), "Journal": "82"}
    )

    assert invoice.sales_invoice_lines == []
    assert invoice.sales_invoice_order_charge_lines is None


def test_sales_invoice_requires_ordered_by_and_journal() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesInvoice.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("ordered_by",) in error_fields
    assert ("journal",) in error_fields


def test_sales_invoice_line_requires_invoice_id() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesInvoiceLine.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("invoice_id",) in error_fields


def test_sales_invoice_line_alias_input() -> None:
    invoice_id = uuid4()

    line = SalesInvoiceLine.model_validate({"InvoiceID": str(invoice_id)})

    assert line.invoice_id == invoice_id


def test_sales_invoice_order_charge_line_requires_invoice_id() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesInvoiceOrderChargeLine.model_validate({"AmountFCInclVAT": 5})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("invoice_id",) in error_fields


def test_sales_invoice_order_charge_line_alias_input() -> None:
    invoice_id = uuid4()

    charge_line = SalesInvoiceOrderChargeLine.model_validate(
        {
            "InvoiceID": str(invoice_id),
            "AmountFCInclVAT": 9,
            "VATPercentage": 21,
        }
    )

    assert charge_line.invoice_id == invoice_id
    assert charge_line.amount_fc_incl_vat == 9
    assert charge_line.vat_percentage == 21


def test_sales_invoice_line_decimal_precision() -> None:
    line = SalesInvoiceLine.model_validate(
        {
            "ID": str(uuid4()),
            "InvoiceID": str(uuid4()),
            "AmountDC": "12.345",
        }
    )

    assert isinstance(line.amount_dc, Decimal)
    assert line.amount_dc == Decimal("12.345")


def test_sales_invoice_line_rejects_invalid_decimal() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesInvoiceLine.model_validate(
            {"InvoiceID": str(uuid4()), "AmountDC": "not-a-number"}
        )

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("amount_dc",) in error_fields


def test_sales_invoice_requires_list_for_lines() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesInvoice.model_validate(
            {
                "OrderedBy": str(uuid4()),
                "Journal": "80",
                "SalesInvoiceLines": "not-a-list",
            }
        )

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("sales_invoice_lines",) in error_fields
