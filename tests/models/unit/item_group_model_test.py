from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import ItemGroup


def test_item_group_parses_aliases_and_datetimes() -> None:
    created = datetime.now(timezone.utc)
    modified = created.replace(hour=(created.hour + 1) % 24)

    item_group = ItemGroup.model_validate(
        {
            "ID": str(uuid4()),
            "Code": "FG",
            "Description": "Finished goods",
            "Created": created.isoformat(),
            "Modified": modified.isoformat(),
            "GLRevenue": str(uuid4()),
        }
    )

    assert item_group.code == "FG"
    assert item_group.description == "Finished goods"
    assert item_group.created == created
    assert item_group.modified == modified


def test_item_group_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        ItemGroup.model_validate({"Code": "FG", "UnknownField": "value"})

    errors = exc.value.errors()
    assert errors[0]["type"] == "extra_forbidden"
