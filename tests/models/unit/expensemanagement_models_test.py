from __future__ import annotations

import pytest
from pydantic import ValidationError

from exact_online_sdk.models.expense import Expense
from exact_online_sdk.models.expense_report import ExpenseReport


class TestExpenseReport:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Currency": "EUR",
            "Description": "Travel expenses",
            "Division": 100,
            "Status": 1,
            "TotalAmountDC": 250.50,
            "ReportNumber": 42,
        }
        obj = ExpenseReport.model_validate(data)
        assert str(obj.id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.currency == "EUR"
        assert obj.description == "Travel expenses"
        assert obj.division == 100
        assert obj.status == 1
        assert obj.total_amount_dc == 250.50
        assert obj.report_number == 42

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            ExpenseReport.model_validate({"UnknownField": "value"})


class TestExpense:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Currency": "USD",
            "Description": "Taxi fare",
            "Division": 200,
            "ExpenseType": 1,
            "TotalAmountDC": 35.00,
            "TotalAmountFC": 35.00,
            "Quantity": 1.0,
        }
        obj = Expense.model_validate(data)
        assert str(obj.id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.currency == "USD"
        assert obj.description == "Taxi fare"
        assert obj.expense_type == 1
        assert obj.total_amount_dc == 35.00
        assert obj.quantity == 1.0

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Expense.model_validate({"UnknownField": "value"})
