from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import Opportunity


def test_opportunity_parses_optional_dates() -> None:
    opportunity_id = uuid4()
    close_date = datetime(2025, 1, 15, 9, 0, tzinfo=timezone.utc)

    opportunity = Opportunity.model_validate(
        {
            "ID": str(opportunity_id),
            "Name": "Renewal",
            "CloseDate": close_date.isoformat(),
        }
    )

    assert opportunity.id == opportunity_id
    assert opportunity.name == "Renewal"
    assert opportunity.close_date == close_date


def test_opportunity_missing_optional_fields_defaults() -> None:
    opportunity = Opportunity.model_validate({})

    assert opportunity.account is None
    assert opportunity.close_date is None


def test_opportunity_validates_numeric_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Opportunity.model_validate({"Probability": "not-a-number"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("probability",) in error_fields
