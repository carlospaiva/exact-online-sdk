from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import SupplierItem


def test_supplier_item_parses_aliases_and_dates() -> None:
    now = datetime.now(timezone.utc)
    item_id = uuid4()
    item_unit_id = uuid4()
    supplier_id = uuid4()

    supplier_item = SupplierItem.model_validate(
        {
            "ID": str(uuid4()),
            "Item": str(item_id),
            "ItemUnit": str(item_unit_id),
            "PurchasePrice": 12.5,
            "PurchaseUnit": "PCS",
            "Supplier": str(supplier_id),
            "Created": now.isoformat(),
            "Modified": now.isoformat(),
            "MainSupplier": True,
            "StartDate": now.isoformat(),
        }
    )

    assert supplier_item.item == item_id
    assert supplier_item.item_unit == item_unit_id
    assert supplier_item.supplier == supplier_id
    assert supplier_item.created == now
    assert supplier_item.modified == now
    assert supplier_item.main_supplier is True
    assert supplier_item.start_date == now


def test_supplier_item_requires_core_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        SupplierItem.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("item",) in error_fields
    assert ("item_unit",) in error_fields
    assert ("purchase_price",) in error_fields
    assert ("purchase_unit",) in error_fields
    assert ("supplier",) in error_fields


def test_supplier_item_rejects_invalid_purchase_price() -> None:
    with pytest.raises(ValidationError) as exc:
        SupplierItem.model_validate(
            {
                "Item": str(uuid4()),
                "ItemUnit": str(uuid4()),
                "PurchasePrice": "not-a-number",
                "PurchaseUnit": "PCS",
                "Supplier": str(uuid4()),
            }
        )

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("purchase_price",) in error_fields
