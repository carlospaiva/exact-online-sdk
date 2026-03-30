from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import GLAccount, SelectionCode, Unit


def test_gl_account_parses_alias_fields() -> None:
    account_id = uuid4()
    created = datetime.now(timezone.utc)

    account = GLAccount.model_validate(
        {
            "ID": str(account_id),
            "Code": "1400",
            "Description": "Inventory",
            "AllowCostsInSales": True,
            "Created": created.isoformat(),
        }
    )

    assert account.id == account_id
    assert account.code == "1400"
    assert account.description == "Inventory"
    assert account.allow_costs_in_sales is True
    assert account.created == created


def test_unit_parses_optional_fields() -> None:
    unit = Unit.model_validate({"ID": str(uuid4()), "Code": "PCS", "Active": True})

    assert unit.code == "PCS"
    assert unit.active is True
    assert unit.description is None


def test_unit_rejects_invalid_active_value() -> None:
    with pytest.raises(ValidationError) as exc:
        Unit.model_validate({"Code": "PCS", "Active": "yes"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("active",) in error_fields


def test_selection_code_parses_dates_and_aliases() -> None:
    code_id = uuid4()
    created = datetime.now(timezone.utc)

    selection_code = SelectionCode.model_validate(
        {
            "ID": str(code_id),
            "Code": "LOYAL",
            "Description": "Loyal Customers",
            "Active": 1,
            "Created": created.isoformat(),
        }
    )

    assert selection_code.id == code_id
    assert selection_code.code == "LOYAL"
    assert selection_code.description == "Loyal Customers"
    assert selection_code.active == 1
    assert selection_code.created == created


def test_selection_code_rejects_invalid_active() -> None:
    with pytest.raises(ValidationError) as exc:
        SelectionCode.model_validate({"Code": "LOYAL", "Active": "yes"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("active",) in error_fields
