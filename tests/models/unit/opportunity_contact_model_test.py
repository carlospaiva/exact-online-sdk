from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import OpportunityContact


def test_opportunity_contact_parses_aliases() -> None:
    account_id = uuid4()
    contact_id = uuid4()
    opportunity_id = uuid4()
    birth_date = datetime(1988, 7, 3, 12, tzinfo=timezone.utc)

    opportunity_contact = OpportunityContact.model_validate(
        {
            "Account": str(account_id),
            "Contact": str(contact_id),
            "Opportunity": str(opportunity_id),
            "FirstName": "Grace",
            "LastName": "Hopper",
            "BirthDate": birth_date.isoformat(),
        }
    )

    assert opportunity_contact.account == account_id
    assert opportunity_contact.contact == contact_id
    assert opportunity_contact.opportunity == opportunity_id
    assert opportunity_contact.birth_date == birth_date
    assert opportunity_contact.first_name == "Grace"
    assert opportunity_contact.last_name == "Hopper"


def test_opportunity_contact_requires_name_component() -> None:
    with pytest.raises(ValidationError) as exc:
        OpportunityContact.model_validate({"Account": str(uuid4())})

    errors = exc.value.errors()
    assert errors[0]["type"] == "value_error"
    assert "FirstName" in errors[0]["msg"] or "LastName" in errors[0]["msg"]


def test_opportunity_contact_requires_account() -> None:
    with pytest.raises(ValidationError) as exc:
        OpportunityContact.model_validate({"FirstName": "Alan"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("account",) in error_fields
