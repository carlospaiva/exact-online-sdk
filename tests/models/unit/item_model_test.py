from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import Item


def test_item_parses_aliases_and_dates() -> None:
    item_id = uuid4()
    created = datetime.now(timezone.utc)

    item = Item.model_validate(
        {
            "ID": str(item_id),
            "Code": "ITEM-001",
            "Description": "Demo Item",
            "Created": created.isoformat(),
            "FreeDateField_01": created.isoformat(),
        }
    )

    assert item.id == item_id
    assert item.code == "ITEM-001"
    assert item.description == "Demo Item"
    assert item.created == created
    assert item.free_date_field_01 == created


def test_item_requires_code_and_description() -> None:
    with pytest.raises(ValidationError) as exc:
        Item.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("code",) in error_fields
    assert ("description",) in error_fields


def test_item_optional_numeric_fields_default_none() -> None:
    item = Item.model_validate({"Code": "ITEM-002", "Description": "Sample"})

    assert item.average_cost is None
    assert item.stock is None
