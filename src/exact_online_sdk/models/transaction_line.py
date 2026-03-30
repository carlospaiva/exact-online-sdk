from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class TransactionLine(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_name: Optional[str] = Field(None, alias="AccountName")
    amount_dc: Optional[float] = Field(None, alias="AmountDC")
    amount_fc: Optional[float] = Field(None, alias="AmountFC")
    amount_vat_base_fc: Optional[float] = Field(None, alias="AmountVATBaseFC")
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
    currency: Optional[str] = Field(None, alias="Currency")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    date: Optional[datetime] = Field(None, alias="Date")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_number: Optional[int] = Field(None, alias="DocumentNumber")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    due_date: Optional[datetime] = Field(None, alias="DueDate")
    entry_id: UUID = Field(..., alias="EntryID")
    entry_number: Optional[int] = Field(None, alias="EntryNumber")
    exchange_rate: Optional[float] = Field(None, alias="ExchangeRate")
    external_link_description: Optional[str] = Field(
        None, alias="ExternalLinkDescription"
    )
    external_link_reference: Optional[str] = Field(None, alias="ExternalLinkReference")
    extra_duty_amount_fc: Optional[float] = Field(None, alias="ExtraDutyAmountFC")
    extra_duty_percentage: Optional[float] = Field(None, alias="ExtraDutyPercentage")
    financial_period: Optional[int] = Field(None, alias="FinancialPeriod")
    financial_year: Optional[int] = Field(None, alias="FinancialYear")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    invoice_number: Optional[int] = Field(None, alias="InvoiceNumber")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    journal_code: Optional[str] = Field(None, alias="JournalCode")
    journal_description: Optional[str] = Field(None, alias="JournalDescription")
    line_number: Optional[int] = Field(None, alias="LineNumber")
    line_type: Optional[int] = Field(None, alias="LineType")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    offset_id: Optional[UUID] = Field(None, alias="OffsetID")
    order_number: Optional[int] = Field(None, alias="OrderNumber")
    payment_discount_amount: Optional[float] = Field(
        None, alias="PaymentDiscountAmount"
    )
    payment_reference: Optional[str] = Field(None, alias="PaymentReference")
    project: Optional[UUID] = Field(None, alias="Project")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    project_wbs: Optional[UUID] = Field(None, alias="ProjectWBS")
    project_wbs_description: Optional[str] = Field(None, alias="ProjectWBSDescription")
    quantity: Optional[float] = Field(None, alias="Quantity")
    serial_number: Optional[str] = Field(None, alias="SerialNumber")
    shop_order: Optional[UUID] = Field(None, alias="ShopOrder")
    status: Optional[int] = Field(None, alias="Status")
    subscription: Optional[UUID] = Field(None, alias="Subscription")
    subscription_description: Optional[str] = Field(
        None, alias="SubscriptionDescription"
    )
    tracking_number: Optional[str] = Field(None, alias="TrackingNumber")
    tracking_number_description: Optional[str] = Field(
        None, alias="TrackingNumberDescription"
    )
    type: Optional[int] = Field(None, alias="Type")
    vat_code: Optional[str] = Field(None, alias="VATCode")
    vat_code_description: Optional[str] = Field(None, alias="VATCodeDescription")
    vat_percentage: Optional[float] = Field(None, alias="VATPercentage")
    vat_type: Optional[str] = Field(None, alias="VATType")
    your_ref: Optional[str] = Field(None, alias="YourRef")
