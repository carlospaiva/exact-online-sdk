from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    Asset,
    AssetGroup,
    CommercialBuildingValue,
    DepreciationMethod,
)


def test_asset_group_parses_aliases() -> None:
    uid = uuid4()
    created = datetime.now(timezone.utc)

    obj = AssetGroup.model_validate(
        {
            "ID": str(uid),
            "Code": "AG001",
            "Description": "Vehicles",
            "Created": created.isoformat(),
            "Division": 1,
            "Notes": "Fleet",
        }
    )

    assert obj.id == uid
    assert obj.code == "AG001"
    assert obj.description == "Vehicles"
    assert obj.created == created


def test_asset_group_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        AssetGroup.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_asset_parses_aliases() -> None:
    uid = uuid4()

    obj = Asset.model_validate(
        {
            "ID": str(uid),
            "Code": "A001",
            "Description": "Company car",
            "CatalogueValue": 25000.0,
            "ResidualValue": 5000.0,
            "Status": 1,
            "Type": "10",
            "InvestmentAmountDC": 25000.0,
        }
    )

    assert obj.id == uid
    assert obj.code == "A001"
    assert obj.catalogue_value == 25000.0
    assert obj.residual_value == 5000.0
    assert obj.investment_amount_dc == 25000.0


def test_asset_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Asset.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_commercial_building_value_parses_aliases() -> None:
    uid = uuid4()
    start = datetime.now(timezone.utc)

    obj = CommercialBuildingValue.model_validate(
        {
            "ID": str(uid),
            "Asset": str(uuid4()),
            "LineNumber": 1,
            "PropertyValue": 500000.0,
            "MinimumValue": 300000.0,
            "StartDate": start.isoformat(),
        }
    )

    assert obj.id == uid
    assert obj.line_number == 1
    assert obj.property_value == 500000.0
    assert obj.minimum_value == 300000.0


def test_commercial_building_value_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        CommercialBuildingValue.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_depreciation_method_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        DepreciationMethod.model_validate({})


def test_depreciation_method_parses_aliases() -> None:
    uid = uuid4()

    obj = DepreciationMethod.model_validate(
        {
            "ID": str(uid),
            "Code": "SL",
            "Description": "Straight line",
            "Percentage": 20.0,
            "Years": 5,
            "Type": 1,
        }
    )

    assert obj.id == uid
    assert obj.code == "SL"
    assert obj.description == "Straight line"
    assert obj.percentage == 20.0
    assert obj.years == 5


def test_depreciation_method_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        DepreciationMethod.model_validate(
            {"Code": "SL", "Description": "X", "UnknownField": "value"}
        )

    assert exc.value.errors()[0]["type"] == "extra_forbidden"
