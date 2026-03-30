from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import Budget, BudgetScenario


def test_budget_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        Budget.model_validate({})


def test_budget_parses_aliases() -> None:
    uid = uuid4()

    obj = Budget.model_validate(
        {
            "ID": str(uid),
            "AmountDC": 10000.0,
            "BudgetScenario": str(uuid4()),
            "Costcenter": "CC01",
            "ReportingPeriod": 6,
            "ReportingYear": 2024,
        }
    )

    assert obj.id == uid
    assert obj.amount_dc == 10000.0
    assert obj.costcenter == "CC01"
    assert obj.reporting_period == 6
    assert obj.reporting_year == 2024


def test_budget_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Budget.model_validate({"AmountDC": 1.0, "UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_budget_scenario_parses_aliases() -> None:
    uid = uuid4()
    created = datetime.now(timezone.utc)

    obj = BudgetScenario.model_validate(
        {
            "ID": str(uid),
            "Code": "BS2024",
            "Description": "Budget 2024",
            "FromYear": 2024,
            "ToYear": 2024,
            "Created": created.isoformat(),
        }
    )

    assert obj.id == uid
    assert obj.code == "BS2024"
    assert obj.from_year == 2024
    assert obj.to_year == 2024


def test_budget_scenario_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        BudgetScenario.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"
