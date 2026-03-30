from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Asset(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    already_depreciated: Optional[int] = Field(None, alias="AlreadyDepreciated")
    asset_from: Optional[UUID] = Field(None, alias="AssetFrom")
    asset_from_description: Optional[str] = Field(None, alias="AssetFromDescription")
    asset_group: Optional[UUID] = Field(None, alias="AssetGroup")
    asset_group_code: Optional[str] = Field(None, alias="AssetGroupCode")
    asset_group_description: Optional[str] = Field(None, alias="AssetGroupDescription")
    catalogue_value: Optional[float] = Field(None, alias="CatalogueValue")
    code: Optional[str] = Field(None, alias="Code")
    commercial_building_values: Optional[Any] = Field(
        None, alias="CommercialBuildingValues"
    )
    costcenter: Optional[str] = Field(None, alias="Costcenter")
    costcenter_description: Optional[str] = Field(None, alias="CostcenterDescription")
    costunit: Optional[str] = Field(None, alias="Costunit")
    costunit_description: Optional[str] = Field(None, alias="CostunitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    deduction_percentage: Optional[float] = Field(None, alias="DeductionPercentage")
    depreciated_amount: Optional[float] = Field(None, alias="DepreciatedAmount")
    depreciated_periods: Optional[int] = Field(None, alias="DepreciatedPeriods")
    depreciated_start_date: Optional[datetime] = Field(
        None, alias="DepreciatedStartDate"
    )
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    engine_emission: Optional[int] = Field(None, alias="EngineEmission")
    engine_type: Optional[int] = Field(None, alias="EngineType")
    gl_transaction_line: Optional[UUID] = Field(None, alias="GLTransactionLine")
    gl_transaction_line_description: Optional[str] = Field(
        None, alias="GLTransactionLineDescription"
    )
    investment_account: Optional[UUID] = Field(None, alias="InvestmentAccount")
    investment_account_code: Optional[str] = Field(None, alias="InvestmentAccountCode")
    investment_account_name: Optional[str] = Field(None, alias="InvestmentAccountName")
    investment_amount_dc: Optional[float] = Field(None, alias="InvestmentAmountDC")
    investment_amount_fc: Optional[float] = Field(None, alias="InvestmentAmountFC")
    investment_currency: Optional[str] = Field(None, alias="InvestmentCurrency")
    investment_currency_description: Optional[str] = Field(
        None, alias="InvestmentCurrencyDescription"
    )
    investment_date: Optional[datetime] = Field(None, alias="InvestmentDate")
    investment_deduction: Optional[int] = Field(None, alias="InvestmentDeduction")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    parent: Optional[UUID] = Field(None, alias="Parent")
    parent_code: Optional[str] = Field(None, alias="ParentCode")
    parent_description: Optional[str] = Field(None, alias="ParentDescription")
    picture: Optional[str] = Field(None, alias="Picture")
    picture_file_name: Optional[str] = Field(None, alias="PictureFileName")
    primary_method: Optional[UUID] = Field(None, alias="PrimaryMethod")
    primary_method_code: Optional[str] = Field(None, alias="PrimaryMethodCode")
    primary_method_description: Optional[str] = Field(
        None, alias="PrimaryMethodDescription"
    )
    residual_value: Optional[float] = Field(None, alias="ResidualValue")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    status: Optional[int] = Field(None, alias="Status")
    transaction_entry_id: Optional[UUID] = Field(None, alias="TransactionEntryID")
    transaction_entry_no: Optional[int] = Field(None, alias="TransactionEntryNo")
    type: Optional[str] = Field(None, alias="Type")
