from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import SalesItemPrice


def test_sales_item_price_parses_aliases_and_dates() -> None:
    now = datetime.now(timezone.utc)
    item_id = uuid4()

    sales_item_price = SalesItemPrice.model_validate(
        {
            "ID": str(uuid4()),
            "Item": str(item_id),
            "Price": 42.5,
            "StartDate": now.isoformat(),
            "EndDate": now.isoformat(),
            "NumberOfItemsPerUnit": 1.5,
        }
    )

    assert sales_item_price.item == item_id
    assert sales_item_price.price == 42.5
    assert sales_item_price.start_date == now
    assert sales_item_price.end_date == now
    assert sales_item_price.number_of_items_per_unit == 1.5


def test_sales_item_price_defaults_optional_fields_to_none() -> None:
    sales_item_price = SalesItemPrice.model_validate({})

    assert sales_item_price.price is None
    assert sales_item_price.start_date is None
    assert sales_item_price.account is None


def test_sales_item_price_rejects_invalid_price_type() -> None:
    with pytest.raises(ValidationError) as exc:
        SalesItemPrice.model_validate({"Price": "invalid"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("price",) in error_fields
