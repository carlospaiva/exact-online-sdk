from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import GoodsDelivery, GoodsDeliveryLine


def test_goods_delivery_parses_alias_payload() -> None:
    entry_id = uuid4()
    line_id = uuid4()
    sales_order_line_id = uuid4()
    delivery_date = datetime.now(timezone.utc)

    payload = {
        "EntryID": str(entry_id),
        "DeliveryDate": delivery_date.isoformat(),
        "GoodsDeliveryLines": [
            {
                "ID": str(line_id),
                "QuantityDelivered": 1.0,
                "SalesOrderLineID": str(sales_order_line_id),
            }
        ],
    }

    delivery = GoodsDelivery.model_validate(payload)

    assert delivery.entry_id == entry_id
    assert delivery.delivery_date == delivery_date
    assert len(delivery.goods_delivery_lines) == 1
    line = delivery.goods_delivery_lines[0]
    assert line.id == line_id
    assert line.sales_order_line_id == sales_order_line_id
    assert line.quantity_delivered == 1.0


def test_goods_delivery_lines_default_to_empty_list() -> None:
    delivery_date = datetime.now(timezone.utc)

    delivery = GoodsDelivery(delivery_date=delivery_date)

    assert delivery.goods_delivery_lines == []


def test_goods_delivery_line_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        GoodsDeliveryLine(quantity_delivered=1.5)  # type: ignore[call-arg]

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("sales_order_line_id",) in error_fields


def test_goods_delivery_line_accepts_alias_input() -> None:
    sales_order_line_id = uuid4()
    model = GoodsDeliveryLine.model_validate(
        {
            "QuantityDelivered": 4,
            "SalesOrderLineID": str(sales_order_line_id),
        }
    )

    assert model.sales_order_line_id == sales_order_line_id
    assert model.quantity_delivered == 4


def test_goods_delivery_line_optional_alias_fields() -> None:
    payload = {
        "QuantityDelivered": 2,
        "SalesOrderLineID": str(uuid4()),
        "StorageLocationCode": "A-01",
        "Unitcode": "PCS",
    }

    line = GoodsDeliveryLine.model_validate(payload)

    assert line.storage_location_code == "A-01"
    assert line.unit_code == "PCS"
