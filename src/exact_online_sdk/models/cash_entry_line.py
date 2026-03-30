from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class CashEntryLine(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_name: Optional[str] = Field(None, alias="AccountName")
    amount_dc: Optional[float] = Field(None, alias="AmountDC")
    amount_fc: Optional[float] = Field(None, alias="AmountFC")
    amount_vat_fc: Optional[float] = Field(None, alias="AmountVATFC")
    asset: Optional[UUID] = Field(None, alias="Asset")
    asset_code: Optional[str] = Field(None, alias="AssetCode")
    asset_description: Optional[str] = Field(None, alias="AssetDescription")
    cost_center: Optional[str] = Field(None, alias="CostCenter")
    cost_center_description: Optional[str] = Field(None, alias="CostCenterDescription")
    cost_unit: Optional[str] = Field(None, alias="CostUnit")
    cost_unit_description: Optional[str] = Field(None, alias="CostUnitDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    date: Optional[datetime] = Field(None, alias="Date")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_number: Optional[int] = Field(None, alias="DocumentNumber")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    entry_id: Optional[UUID] = Field(None, alias="EntryID")
    entry_number: Optional[int] = Field(None, alias="EntryNumber")
    exchange_rate: Optional[float] = Field(None, alias="ExchangeRate")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    offset_id: Optional[UUID] = Field(None, alias="OffsetID")
    our_ref: Optional[int] = Field(None, alias="OurRef")
    project: Optional[UUID] = Field(None, alias="Project")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    project_wbs: Optional[UUID] = Field(None, alias="ProjectWBS")
    project_wbs_description: Optional[str] = Field(None, alias="ProjectWBSDescription")
    quantity: Optional[float] = Field(None, alias="Quantity")
    vat_code: Optional[str] = Field(None, alias="VATCode")
    vat_code_description: Optional[str] = Field(None, alias="VATCodeDescription")
    vat_percentage: Optional[float] = Field(None, alias="VATPercentage")
    vat_type: Optional[str] = Field(None, alias="VATType")
