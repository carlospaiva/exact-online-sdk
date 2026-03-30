from __future__ import annotations

import time
from uuid import uuid4

import pytest

from exact_online_sdk.models import (
    SalesInvoice,
    SalesInvoiceLine,
    SalesInvoiceOrderChargeLine,
)

pytestmark = pytest.mark.performance


def test_sales_invoice_dump_with_many_lines_is_fast() -> None:
    invoice_id = uuid4()
    ordered_by = uuid4()

    lines = [SalesInvoiceLine(invoice_id=invoice_id, amount_dc=i) for i in range(50)]
    charges = [
        SalesInvoiceOrderChargeLine(invoice_id=invoice_id, amount_fc_incl_vat=1.0)
        for _ in range(10)
    ]

    invoice = SalesInvoice(
        ordered_by=ordered_by,
        journal="80",
        sales_invoice_lines=lines,
        sales_invoice_order_charge_lines=charges,
    )

    start = time.perf_counter()
    for _ in range(20):
        dumped = invoice.model_dump(by_alias=True)
        assert dumped["Journal"] == "80"
    elapsed = time.perf_counter() - start

    assert elapsed < 1.0
