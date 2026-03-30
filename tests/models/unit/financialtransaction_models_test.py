from __future__ import annotations

import pytest
from pydantic import ValidationError

from exact_online_sdk.models.bank_entry import BankEntry
from exact_online_sdk.models.bank_entry_line import BankEntryLine
from exact_online_sdk.models.cash_entry import CashEntry
from exact_online_sdk.models.cash_entry_line import CashEntryLine


class TestBankEntry:
    def test_parses_aliases(self) -> None:
        data = {
            "EntryID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Currency": "EUR",
            "Division": 100,
            "EntryNumber": 1,
            "FinancialPeriod": 1,
            "FinancialYear": 2024,
            "JournalCode": "70",
            "Status": 5,
            "ClosingBalanceFC": 1000.50,
        }
        obj = BankEntry.model_validate(data)
        assert str(obj.entry_id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.currency == "EUR"
        assert obj.entry_number == 1
        assert obj.closing_balance_fc == 1000.50

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            BankEntry.model_validate({"UnknownField": "value"})


class TestBankEntryLine:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "AmountDC": 100.0,
            "AmountFC": 100.0,
            "Description": "Payment",
            "GLAccount": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "LineNumber": 1,
            "VATCode": "1",
        }
        obj = BankEntryLine.model_validate(data)
        assert obj.amount_dc == 100.0
        assert obj.description == "Payment"
        assert obj.line_number == 1
        assert obj.vat_code == "1"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            BankEntryLine.model_validate({"UnknownField": "value"})


class TestCashEntry:
    def test_parses_aliases(self) -> None:
        data = {
            "EntryID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Currency": "EUR",
            "Division": 100,
            "EntryNumber": 5,
            "FinancialPeriod": 3,
            "FinancialYear": 2024,
            "JournalCode": "80",
            "Status": 5,
            "OpeningBalanceFC": 500.0,
        }
        obj = CashEntry.model_validate(data)
        assert str(obj.entry_id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.journal_code == "80"
        assert obj.opening_balance_fc == 500.0

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            CashEntry.model_validate({"UnknownField": "value"})


class TestCashEntryLine:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "AmountDC": 200.0,
            "AmountFC": 200.0,
            "Description": "Cash payment",
            "GLAccount": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "LineNumber": 1,
            "VATPercentage": 21.0,
        }
        obj = CashEntryLine.model_validate(data)
        assert obj.amount_dc == 200.0
        assert obj.description == "Cash payment"
        assert obj.vat_percentage == 21.0

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            CashEntryLine.model_validate({"UnknownField": "value"})
