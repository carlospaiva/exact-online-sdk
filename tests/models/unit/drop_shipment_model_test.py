from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import DropShipment, DropShipmentLine


def test_drop_shipment_parses_alias_payload() -> None:
    entry_id = uuid4()
    line_id = uuid4()
    purchase_order_line_id = uuid4()
    sales_order_line_id = uuid4()
    delivery_date = datetime.now(timezone.utc)

    payload = {
        "EntryID": str(entry_id),
        "DeliveryDate": delivery_date.isoformat(),
        "DropShipmentLines": [
            {
                "ID": str(line_id),
                "PurchaseOrderLineID": str(purchase_order_line_id),
                "QuantityDelivered": 2.5,
                "SalesOrderLineID": str(sales_order_line_id),
            }
        ],
    }

    shipment = DropShipment.model_validate(payload)

    assert shipment.entry_id == entry_id
    assert shipment.delivery_date == delivery_date
    assert len(shipment.drop_shipment_lines) == 1
    line = shipment.drop_shipment_lines[0]
    assert line.id == line_id
    assert line.purchase_order_line_id == purchase_order_line_id
    assert line.quantity_delivered == 2.5
    assert line.sales_order_line_id == sales_order_line_id


def test_drop_shipment_lines_default_to_empty_list() -> None:
    delivery_date = datetime.now(timezone.utc)

    shipment = DropShipment(delivery_date=delivery_date)

    assert shipment.drop_shipment_lines == []


def test_drop_shipment_line_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        DropShipmentLine(  # type: ignore[call-arg]
            purchase_order_line_id=uuid4(),
            quantity_delivered=1,
        )

    errors = exc.value.errors()
    error_fields = {err["loc"][0] for err in errors}
    assert "sales_order_line_id" in error_fields


def test_drop_shipment_line_accepts_alias_input() -> None:
    purchase_order_line_id = uuid4()
    sales_order_line_id = uuid4()

    model = DropShipmentLine.model_validate(
        {
            "PurchaseOrderLineID": str(purchase_order_line_id),
            "QuantityDelivered": 3,
            "SalesOrderLineID": str(sales_order_line_id),
        }
    )

    assert model.purchase_order_line_id == purchase_order_line_id
    assert model.sales_order_line_id == sales_order_line_id
    assert model.quantity_delivered == 3
