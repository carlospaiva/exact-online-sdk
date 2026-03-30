from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import AccountClassification, AccountClassificationName


def test_account_classification_parses_aliases_and_dates() -> None:
    created = datetime.now(timezone.utc)
    classification = AccountClassification.model_validate(
        {
            "ID": str(uuid4()),
            "Code": "A",
            "Description": "Priority client",
            "Created": created.isoformat(),
            "AccountClassificationName": str(uuid4()),
        }
    )

    assert classification.code == "A"
    assert classification.description == "Priority client"
    assert classification.created == created


def test_account_classification_forbids_extra_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        AccountClassification.model_validate({"Code": "A", "Extra": "nope"})

    errors = exc.value.errors()
    assert errors[0]["type"] == "extra_forbidden"


def test_account_classification_name_parses_aliases() -> None:
    created = datetime.now(timezone.utc)

    name = AccountClassificationName.model_validate(
        {
            "ID": str(uuid4()),
            "Description": "Strategic",
            "Created": created.isoformat(),
            "SequenceNumber": 10,
        }
    )

    assert name.description == "Strategic"
    assert name.created == created
    assert name.sequence_number == 10
