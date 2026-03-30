from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import ItemVersion


def test_item_version_parses_aliases_and_required_fields() -> None:
    created = datetime.now(timezone.utc)
    item_id = uuid4()

    item_version = ItemVersion.model_validate(
        {
            "ID": str(uuid4()),
            "Description": "Initial build",
            "Item": str(item_id),
            "Created": created.isoformat(),
            "VersionNumber": 3,
        }
    )

    assert item_version.description == "Initial build"
    assert item_version.item == item_id
    assert item_version.created == created
    assert item_version.version_number == 3


def test_item_version_requires_description_and_item() -> None:
    with pytest.raises(ValidationError) as exc:
        ItemVersion.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("description",) in error_fields
    assert ("item",) in error_fields
