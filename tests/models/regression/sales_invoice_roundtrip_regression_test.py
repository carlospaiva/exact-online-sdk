from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest

from exact_online_sdk.models import (
    SalesInvoice,
    SalesInvoiceLine,
    SalesInvoiceOrderChargeLine,
    SalesInvoiceStatus,
)

pytestmark = pytest.mark.regression


def test_sales_invoice_roundtrip_preserves_core_fields() -> None:
    invoice_id = uuid4()
    ordered_by = uuid4()
    invoice_date = datetime.now(timezone.utc)

    line = SalesInvoiceLine(invoice_id=invoice_id)
    charge_line = SalesInvoiceOrderChargeLine(
        invoice_id=invoice_id,
        amount_fc_incl_vat=10.0,
    )

    original = SalesInvoice(
        invoice_id=invoice_id,
        ordered_by=ordered_by,
        journal="80",
        invoice_date=invoice_date,
        status=SalesInvoiceStatus.DRAFT,
        sales_invoice_lines=[line],
        sales_invoice_order_charge_lines=[charge_line],
    )

    dumped = original.model_dump(by_alias=True)
    restored = SalesInvoice.model_validate(dumped)

    assert restored.invoice_id == original.invoice_id
    assert restored.ordered_by == original.ordered_by
    assert restored.journal == original.journal
    assert restored.invoice_date == original.invoice_date
    assert restored.status == original.status
    assert len(restored.sales_invoice_lines) == 1
    assert restored.sales_invoice_order_charge_lines is not None
    assert len(restored.sales_invoice_order_charge_lines) == 1
