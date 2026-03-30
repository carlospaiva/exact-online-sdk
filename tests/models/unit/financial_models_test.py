from __future__ import annotations

import pytest
from pydantic import ValidationError

from exact_online_sdk.models.deductibility_percentage import DeductibilityPercentage
from exact_online_sdk.models.exchange_rate import ExchangeRate
from exact_online_sdk.models.financial_period import FinancialPeriod
from exact_online_sdk.models.gl_account_classification_mapping import (
    GLAccountClassificationMapping,
)
from exact_online_sdk.models.gl_scheme import GLScheme
from exact_online_sdk.models.gl_transaction_source import GLTransactionSource
from exact_online_sdk.models.gl_transaction_type import GLTransactionType
from exact_online_sdk.models.journal import Journal
from exact_online_sdk.models.official_return import OfficialReturn
from exact_online_sdk.models.reporting_balance import ReportingBalance


class TestDeductibilityPercentage:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Division": 100,
            "LineNumber": 1,
            "PrivateUsePercentage": 25.5,
            "VATNonDeductiblePercentage": 10.0,
        }
        obj = DeductibilityPercentage.model_validate(data)
        assert str(obj.id) == "a1b2c3d4-e5f6-7890-abcd-ef1234567890"
        assert obj.division == 100
        assert obj.line_number == 1
        assert obj.private_use_percentage == 25.5

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            DeductibilityPercentage.model_validate({"UnknownField": "x"})


class TestExchangeRate:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Rate": 1.2345,
            "SourceCurrency": "USD",
            "TargetCurrency": "EUR",
            "Division": 100,
        }
        obj = ExchangeRate.model_validate(data)
        assert obj.rate == 1.2345
        assert obj.source_currency == "USD"
        assert obj.target_currency == "EUR"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            ExchangeRate.model_validate({"UnknownField": "x"})


class TestFinancialPeriod:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "FinPeriod": 1,
            "FinYear": 2024,
            "Division": 100,
        }
        obj = FinancialPeriod.model_validate(data)
        assert obj.fin_period == 1
        assert obj.fin_year == 2024

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            FinancialPeriod.model_validate({"UnknownField": "x"})


class TestGLAccountClassificationMapping:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Classification": "b1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "ClassificationCode": "C001",
            "GLAccountCode": "1000",
            "Division": 100,
        }
        obj = GLAccountClassificationMapping.model_validate(data)
        assert obj.classification_code == "C001"
        assert obj.gl_account_code == "1000"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            GLAccountClassificationMapping.model_validate({"UnknownField": "x"})


class TestGLScheme:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "S001",
            "Description": "Main scheme",
            "Main": 1,
            "Division": 100,
        }
        obj = GLScheme.model_validate(data)
        assert obj.code == "S001"
        assert obj.description == "Main scheme"
        assert obj.main == 1

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            GLScheme.model_validate({"UnknownField": "x"})


class TestGLTransactionSource:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": 1,
            "Description": "Manual entry",
            "DescriptionSuffix": "suffix",
        }
        obj = GLTransactionSource.model_validate(data)
        assert obj.id == 1
        assert obj.description == "Manual entry"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            GLTransactionSource.model_validate({"UnknownField": "x"})


class TestGLTransactionType:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": 10,
            "Description": "Sales entry",
            "DescriptionSuffix": "suffix",
        }
        obj = GLTransactionType.model_validate(data)
        assert obj.id == 10
        assert obj.description == "Sales entry"

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            GLTransactionType.model_validate({"UnknownField": "x"})


class TestJournal:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Code": "70",
            "Description": "Bank journal",
            "Type": 12,
            "AllowVAT": True,
            "Division": 100,
        }
        obj = Journal.model_validate(data)
        assert obj.code == "70"
        assert obj.description == "Bank journal"
        assert obj.type == 12
        assert obj.allow_vat is True

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            Journal.model_validate({"UnknownField": "x"})


class TestOfficialReturn:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
            "Amount": 1000.0,
            "Description": "VAT return",
            "Status": 1,
            "Type": 2,
            "Year": 2024,
            "Period": 1,
        }
        obj = OfficialReturn.model_validate(data)
        assert obj.amount == 1000.0
        assert obj.description == "VAT return"
        assert obj.year == 2024

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            OfficialReturn.model_validate({"UnknownField": "x"})


class TestReportingBalance:
    def test_parses_aliases(self) -> None:
        data = {
            "ID": 1,
            "Amount": 5000.0,
            "AmountCredit": 2000.0,
            "AmountDebit": 3000.0,
            "BalanceType": "W",
            "GLAccountCode": "1000",
            "ReportingPeriod": 1,
            "ReportingYear": 2024,
            "Division": 100,
        }
        obj = ReportingBalance.model_validate(data)
        assert obj.id == 1
        assert obj.amount == 5000.0
        assert obj.balance_type == "W"
        assert obj.reporting_year == 2024

    def test_forbids_unknown_fields(self) -> None:
        with pytest.raises(ValidationError):
            ReportingBalance.model_validate({"UnknownField": "x"})
