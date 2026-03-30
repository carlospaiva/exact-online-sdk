from __future__ import annotations

import pytest
from pydantic import ValidationError

from exact_online_sdk.models.currency import Currency
from exact_online_sdk.models.layout import Layout


class TestCurrency:
    def test_parses_aliases(self) -> None:
        data = {
            "Code": "EUR",
            "AmountPrecision": 0.01,
            "Description": "Euro",
            "PricePrecision": 0.0001,
        }
        obj = Currency.model_validate(data)
        assert obj.code == "EUR"
        assert obj.amount_precision == 0.01
        assert obj.description == "Euro"
        assert obj.price_precision == 0.0001

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Currency.model_validate({"UnknownField": "value"})


class TestLayout:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Category": 1,
            "CategoryName": "Sales",
            "Division": 100,
            "Subject": "Invoice layout",
            "Type": 2,
            "Status": 1,
        }
        obj = Layout.model_validate(data)
        assert str(obj.id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.category == 1
        assert obj.category_name == "Sales"
        assert obj.subject == "Invoice layout"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Layout.model_validate({"UnknownField": "value"})
