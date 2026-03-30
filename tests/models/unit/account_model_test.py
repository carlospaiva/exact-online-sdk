from __future__ import annotations

from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import Account, BankAccount


def test_bank_account_accepts_alias_input() -> None:
    account_id = uuid4()
    payload = {
        "Account": str(account_id),
        "BankAccount": "NL26RABO0123456789",
        "BankName": "Rabobank",
    }

    bank_account = BankAccount.model_validate(payload)

    assert bank_account.account == account_id
    assert bank_account.bank_account == "NL26RABO0123456789"
    assert bank_account.bank_name == "Rabobank"


def test_bank_account_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        BankAccount.model_validate({"BankAccount": "NL00TEST"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("account",) in error_fields


def test_account_requires_name() -> None:
    with pytest.raises(ValidationError) as exc:
        Account.model_validate({"Code": "ACC001"})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("name",) in error_fields


def test_account_parses_nested_bank_accounts() -> None:
    account_id = uuid4()
    bank_account_id = uuid4()

    payload = {
        "Name": "Example BV",
        "ID": str(account_id),
        "BankAccounts": [
            {
                "ID": str(bank_account_id),
                "Account": str(account_id),
                "BankAccount": "NL94ABNA1000000001",
            }
        ],
    }

    account = Account.model_validate(payload)

    assert account.name == "Example BV"
    assert account.id == account_id
    assert account.bank_accounts is not None
    bank_account = account.bank_accounts[0]
    assert bank_account.id == bank_account_id
    assert bank_account.bank_account == "NL94ABNA1000000001"
