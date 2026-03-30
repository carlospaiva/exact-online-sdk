from __future__ import annotations

import pytest
from pydantic import ValidationError

from exact_online_sdk.models.general_journal_entry import GeneralJournalEntry
from exact_online_sdk.models.general_journal_entry_line import (
    GeneralJournalEntryLine,
)


class TestGeneralJournalEntry:
    def test_parses_aliases(self) -> None:
        data = {
            "EntryID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Currency": "EUR",
            "Division": 100,
            "EntryNumber": 1,
            "FinancialPeriod": 1,
            "FinancialYear": 2024,
            "JournalCode": "90",
            "Status": 5,
            "Reversal": False,
        }
        obj = GeneralJournalEntry.model_validate(data)
        assert str(obj.entry_id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.currency == "EUR"
        assert obj.journal_code == "90"
        assert obj.reversal is False

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            GeneralJournalEntry.model_validate({"UnknownField": "value"})


class TestGeneralJournalEntryLine:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "AmountDC": 500.0,
            "AmountFC": 500.0,
            "AmountVATDC": 105.0,
            "AmountVATFC": 105.0,
            "Description": "Manual posting",
            "EntryID": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "GLAccount": "c1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "LineNumber": 1,
            "VATCode": "1",
            "VATPercentage": 21.0,
        }
        obj = GeneralJournalEntryLine.model_validate(data)
        assert obj.amount_dc == 500.0
        assert obj.amount_vat_dc == 105.0
        assert obj.description == "Manual posting"
        assert obj.line_number == 1
        assert obj.vat_percentage == 21.0

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            GeneralJournalEntryLine.model_validate({"UnknownField": "value"})
