from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import Contact


def test_contact_parses_alias_and_dates() -> None:
    account_id = uuid4()
    birth_date = datetime(1990, 5, 12, 8, 30, tzinfo=timezone.utc)

    contact = Contact.model_validate(
        {
            "Account": str(account_id),
            "FirstName": "Ada",
            "LastName": "Lovelace",
            "BirthDate": birth_date.isoformat(),
        }
    )

    assert contact.account_id == account_id
    assert contact.first_name == "Ada"
    assert contact.last_name == "Lovelace"
    assert contact.birth_date == birth_date


def test_contact_validator_requires_name_components() -> None:
    account_id = uuid4()

    with pytest.raises(ValidationError) as exc:
        Contact.model_validate({"Account": str(account_id)})

    errors = exc.value.errors()
    assert errors[0]["type"] == "value_error"
    assert "FirstName" in errors[0]["msg"] or "LastName" in errors[0]["msg"]


def test_contact_optional_fields_default_to_none() -> None:
    contact = Contact.model_validate({"Account": str(uuid4()), "LastName": "Turing"})

    assert contact.birth_date is None
    assert contact.business_email is None
