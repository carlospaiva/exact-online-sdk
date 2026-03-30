from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import PurchaseOrder, PurchaseOrderLine


def test_purchase_order_parses_alias_payload() -> None:
    order_id = uuid4()
    supplier_id = uuid4()
    line_id = uuid4()
    item_id = uuid4()
    delivery_date = datetime.now(timezone.utc)

    payload = {
        "PurchaseOrderID": str(order_id),
        "Supplier": str(supplier_id),
        "OrderDate": delivery_date.isoformat(),
        "PurchaseOrderLines": [
            {
                "ID": str(line_id),
                "PurchaseOrderID": str(order_id),
                "Item": str(item_id),
                "QuantityInPurchaseUnits": 5,
            }
        ],
    }

    order = PurchaseOrder.model_validate(payload)

    assert order.purchase_order_id == order_id
    assert order.supplier == supplier_id
    assert order.order_date == delivery_date
    assert len(order.purchase_order_lines) == 1

    line = order.purchase_order_lines[0]
    assert line.id == line_id
    assert line.item == item_id
    assert line.quantity_in_purchase_units == 5


def test_purchase_order_defaults_lines() -> None:
    supplier_id = uuid4()

    order = PurchaseOrder(supplier=supplier_id)

    assert order.purchase_order_lines == []


def test_purchase_order_requires_supplier() -> None:
    with pytest.raises(ValidationError) as exc:
        PurchaseOrder.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("supplier",) in error_fields


def test_purchase_order_line_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        PurchaseOrderLine.model_validate({"QuantityInPurchaseUnits": 1})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("purchase_order_id",) in error_fields
    assert ("item",) in error_fields


def test_purchase_order_line_alias_input() -> None:
    order_id = uuid4()
    item_id = uuid4()

    line = PurchaseOrderLine.model_validate(
        {
            "PurchaseOrderID": str(order_id),
            "Item": str(item_id),
            "QuantityInPurchaseUnits": 8,
            "UnitPrice": 12.5,
        }
    )

    assert line.purchase_order_id == order_id
    assert line.item == item_id
    assert line.quantity_in_purchase_units == 8
    assert line.unit_price == 12.5
