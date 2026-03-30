from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

from exact_online_sdk.models import Address


def test_address_parses_alias_fields_and_dates() -> None:
    address_id = uuid4()
    created = datetime.now(timezone.utc)

    address = Address.model_validate(
        {
            "ID": str(address_id),
            "Account": str(uuid4()),
            "AddressLine1": "Main Street 1",
            "City": "Amsterdam",
            "Country": "NL",
            "Created": created.isoformat(),
        }
    )

    assert address.id == address_id
    assert address.address_line_1 == "Main Street 1"
    assert address.city == "Amsterdam"
    assert address.country == "NL"
    assert address.created == created


def test_address_optional_geo_fields_default_to_none() -> None:
    address = Address.model_validate({"Account": str(uuid4())})

    assert address.city is None
    assert address.country is None
    assert address.address_line_1 is None
