from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    SalesOrder,
    SalesOrderLine,
    SalesOrderOrderChargeLine,
)


def test_sales_order_parses_alias_payload() -> None:
    order_id = uuid4()
    ordered_by = uuid4()
    line_id = uuid4()
    item_id = uuid4()
    charge_line_id = uuid4()
    delivery_date = datetime.now(timezone.utc)

    payload = {
        "OrderID": str(order_id),
        "OrderedBy": str(ordered_by),
        "DeliveryDate": delivery_date.isoformat(),
        "SalesOrderLines": [
            {
                "ID": str(line_id),
                "OrderID": str(order_id),
                "Item": str(item_id),
                "Quantity": 10,
            }
        ],
        "SalesOrderOrderChargeLines": [
            {
                "ID": str(charge_line_id),
                "OrderID": str(order_id),
                "AmountFCInclVAT": 5.0,
            }
        ],
    }

    order = SalesOrder.model_validate(payload)

    assert order.order_id == order_id
    assert order.ordered_by == ordered_by
    assert order.delivery_date == delivery_date
    assert len(order.sales_order_lines) == 1
    assert len(order.sales_order_order_charge_lines) == 1

    line = order.sales_order_lines[0]
    assert line.id == line_id
    assert line.item == item_id
    assert line.quantity == 10

    charge_line = order.sales_order_order_charge_lines[0]
    assert charge_line.id == charge_line_id
    assert charge_line.amount_fc_incl_vat == 5.0


def test_sales_order_defaults_lists() -> None:
    ordered_by = uuid4()

    order = SalesOrder(ordered_by=ordered_by)

    assert order.sales_order_lines == []
    assert order.sales_order_order_charge_lines == []


def test_sales_order_requires_ordered_by() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesOrder.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("ordered_by",) in error_fields


def test_sales_order_line_requires_order_id_and_item() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesOrderLine.model_validate({"Quantity": 1})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("order_id",) in error_fields
    assert ("item",) in error_fields


def test_sales_order_line_alias_input() -> None:
    order_id = uuid4()
    item_id = uuid4()

    line = SalesOrderLine.model_validate(
        {
            "OrderID": str(order_id),
            "Item": str(item_id),
            "Quantity": 2,
            "UnitPrice": 12.5,
        }
    )

    assert line.order_id == order_id
    assert line.item == item_id
    assert line.quantity == 2
    assert line.unit_price == 12.5


def test_sales_order_order_charge_line_requires_order_id() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesOrderOrderChargeLine.model_validate({"AmountFCInclVAT": 10})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("order_id",) in error_fields


def test_sales_order_order_charge_line_alias_input() -> None:
    order_id = uuid4()

    charge_line = SalesOrderOrderChargeLine.model_validate(
        {
            "OrderID": str(order_id),
            "AmountFCInclVAT": 7.5,
            "VATPercentage": 21,
        }
    )

    assert charge_line.order_id == order_id
    assert charge_line.amount_fc_incl_vat == 7.5
    assert charge_line.vat_percentage == 21
