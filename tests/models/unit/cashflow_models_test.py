from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    AllocationRule,
    Bank,
    DirectDebitMandate,
    Payment,
    PaymentCondition,
    Receivable,
)


def test_allocation_rule_parses_aliases() -> None:
    uid = uuid4()

    obj = AllocationRule.model_validate(
        {
            "ID": str(uid),
            "Account": str(uuid4()),
            "GLAccount": str(uuid4()),
            "Words": "invoice rent",
            "VATCode": "21",
        }
    )

    assert obj.id == uid
    assert obj.words == "invoice rent"
    assert obj.vat_code == "21"


def test_allocation_rule_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        AllocationRule.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_bank_parses_aliases() -> None:
    uid = uuid4()

    obj = Bank.model_validate(
        {
            "ID": str(uid),
            "BankName": "ING Bank",
            "BICCode": "INGBNL2A",
            "Country": "NL",
            "Status": "A",
        }
    )

    assert obj.id == uid
    assert obj.bank_name == "ING Bank"
    assert obj.bic_code == "INGBNL2A"
    assert obj.country == "NL"


def test_bank_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Bank.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_direct_debit_mandate_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        DirectDebitMandate.model_validate({})


def test_direct_debit_mandate_parses_aliases() -> None:
    uid = uuid4()
    account_id = uuid4()
    bank_id = uuid4()

    obj = DirectDebitMandate.model_validate(
        {
            "ID": str(uid),
            "Account": str(account_id),
            "BankAccount": str(bank_id),
            "Reference": "MNDT-001",
            "PaymentType": 1,
            "Type": 0,
        }
    )

    assert obj.id == uid
    assert obj.account == account_id
    assert obj.bank_account == bank_id
    assert obj.reference == "MNDT-001"


def test_direct_debit_mandate_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        DirectDebitMandate.model_validate(
            {
                "Account": str(uuid4()),
                "BankAccount": str(uuid4()),
                "UnknownField": "value",
            }
        )

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_payment_condition_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        PaymentCondition.model_validate({})


def test_payment_condition_parses_aliases() -> None:
    uid = uuid4()

    obj = PaymentCondition.model_validate(
        {
            "ID": str(uid),
            "Code": "30D",
            "Description": "30 days net",
            "PaymentDays": 30,
            "DiscountPercentage": 2.0,
            "PaymentMethod": "B",
        }
    )

    assert obj.id == uid
    assert obj.code == "30D"
    assert obj.payment_days == 30
    assert obj.discount_percentage == 2.0


def test_payment_condition_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        PaymentCondition.model_validate(
            {"Code": "X", "Description": "X", "UnknownField": "value"}
        )

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_payment_parses_aliases() -> None:
    uid = uuid4()
    due = datetime.now(timezone.utc)

    obj = Payment.model_validate(
        {
            "ID": str(uid),
            "Account": str(uuid4()),
            "AmountDC": 1500.50,
            "AmountFC": 1500.50,
            "Currency": "EUR",
            "DueDate": due.isoformat(),
            "Status": 20,
            "YourRef": "INV-001",
        }
    )

    assert obj.id == uid
    assert obj.amount_dc == 1500.50
    assert obj.currency == "EUR"
    assert obj.due_date == due
    assert obj.status == 20
    assert obj.your_ref == "INV-001"


def test_payment_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Payment.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_receivable_parses_aliases() -> None:
    uid = uuid4()
    due = datetime.now(timezone.utc)

    obj = Receivable.model_validate(
        {
            "ID": str(uid),
            "Account": str(uuid4()),
            "AmountDC": 2000.0,
            "AmountFC": 2000.0,
            "Currency": "USD",
            "DueDate": due.isoformat(),
            "Status": 20,
            "IsFullyPaid": False,
            "PaymentMethod": "B",
        }
    )

    assert obj.id == uid
    assert obj.amount_dc == 2000.0
    assert obj.is_fully_paid is False
    assert obj.payment_method == "B"


def test_receivable_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Receivable.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"
