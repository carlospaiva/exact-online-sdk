from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    AccountInvolvedAccount,
    AccountOwner,
    InvolvedUser,
    InvolvedUserRole,
    SolutionLink,
    TaskType,
)


def test_account_involved_account_parses_aliases() -> None:
    uid = uuid4()
    created = datetime.now(timezone.utc)

    obj = AccountInvolvedAccount.model_validate(
        {
            "ID": str(uid),
            "Account": str(uuid4()),
            "AccountName": "Acme Corp",
            "Created": created.isoformat(),
            "Division": 123,
            "Notes": "test note",
        }
    )

    assert obj.id == uid
    assert obj.account_name == "Acme Corp"
    assert obj.created == created
    assert obj.division == 123
    assert obj.notes == "test note"


def test_account_involved_account_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        AccountInvolvedAccount.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_account_owner_parses_aliases() -> None:
    uid = uuid4()

    obj = AccountOwner.model_validate(
        {
            "ID": str(uid),
            "Account": str(uuid4()),
            "AccountCode": "AC001",
            "AccountName": "Test Account",
            "Shares": 50.5,
        }
    )

    assert obj.id == uid
    assert obj.account_code == "AC001"
    assert obj.shares == 50.5


def test_account_owner_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        AccountOwner.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_involved_user_role_parses_aliases() -> None:
    uid = uuid4()

    obj = InvolvedUserRole.model_validate(
        {
            "ID": str(uid),
            "Code": "MGR",
            "Description": "Manager",
            "DescriptionTermID": 42,
        }
    )

    assert obj.id == uid
    assert obj.code == "MGR"
    assert obj.description == "Manager"
    assert obj.description_term_id == 42


def test_involved_user_role_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        InvolvedUserRole.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_involved_user_parses_aliases() -> None:
    uid = uuid4()
    account_id = uuid4()

    obj = InvolvedUser.model_validate(
        {
            "ID": str(uid),
            "Account": str(account_id),
            "AccountName": "Test Corp",
            "AccountIsSupplier": True,
            "IsMainContact": False,
            "UserFullName": "John Doe",
        }
    )

    assert obj.id == uid
    assert obj.account == account_id
    assert obj.account_is_supplier is True
    assert obj.is_main_contact is False
    assert obj.user_full_name == "John Doe"


def test_involved_user_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        InvolvedUser.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_solution_link_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        SolutionLink.model_validate({})


def test_solution_link_parses_aliases() -> None:
    uid = uuid4()
    account_id = uuid4()

    obj = SolutionLink.model_validate(
        {
            "ID": str(uid),
            "Account": str(account_id),
            "SolutionType": 1,
            "Name": "My Solution",
            "Status": 0,
        }
    )

    assert obj.id == uid
    assert obj.account == account_id
    assert obj.solution_type == 1
    assert obj.name == "My Solution"


def test_solution_link_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        SolutionLink.model_validate(
            {
                "Account": str(uuid4()),
                "SolutionType": 1,
                "UnknownField": "value",
            }
        )

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_task_type_parses_aliases() -> None:
    uid = uuid4()

    obj = TaskType.model_validate(
        {
            "ID": str(uid),
            "Description": "Follow-up",
            "DescriptionTermID": 10,
            "Division": 456,
        }
    )

    assert obj.id == uid
    assert obj.description == "Follow-up"
    assert obj.description_term_id == 10


def test_task_type_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        TaskType.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"
