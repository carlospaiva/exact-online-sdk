from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Project(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_contact: Optional[UUID] = Field(None, alias="AccountContact")
    account_name: Optional[str] = Field(None, alias="AccountName")
    allow_additional_invoicing: Optional[bool] = Field(
        None, alias="AllowAdditionalInvoicing"
    )
    block_entry: Optional[bool] = Field(None, alias="BlockEntry")
    block_rebilling: Optional[bool] = Field(None, alias="BlockRebilling")
    budget_costs: Optional[float] = Field(None, alias="BudgetCosts")
    budget_revenue: Optional[float] = Field(None, alias="BudgetRevenue")
    budget_type: Optional[int] = Field(None, alias="BudgetType")
    budget_type_description: Optional[str] = Field(None, alias="BudgetTypeDescription")
    classification: Optional[UUID] = Field(None, alias="Classification")
    classification_description: Optional[str] = Field(
        None, alias="ClassificationDescription"
    )
    code: Optional[str] = Field(None, alias="Code")
    costs_amount_fc: Optional[float] = Field(None, alias="CostsAmountFC")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    fixed_price_item: Optional[UUID] = Field(None, alias="FixedPriceItem")
    fixed_price_item_description: Optional[str] = Field(
        None, alias="FixedPriceItemDescription"
    )
    invoice_as_quoted: Optional[bool] = Field(None, alias="InvoiceAsQuoted")
    manager: Optional[UUID] = Field(None, alias="Manager")
    manager_full_name: Optional[str] = Field(None, alias="ManagerFullname")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    prepaid_item: Optional[UUID] = Field(None, alias="PrepaidItem")
    prepaid_item_description: Optional[str] = Field(
        None, alias="PrepaidItemDescription"
    )
    prepaid_type: Optional[int] = Field(None, alias="PrepaidType")
    prepaid_type_description: Optional[str] = Field(
        None, alias="PrepaidTypeDescription"
    )
    sales_time_quantity: Optional[float] = Field(None, alias="SalesTimeQuantity")
    source_quotation: Optional[UUID] = Field(None, alias="SourceQuotation")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    status: Optional[int] = Field(None, alias="Status")
    time_quantity_to_alert: Optional[float] = Field(None, alias="TimeQuantityToAlert")
    type: Optional[int] = Field(None, alias="Type")
    type_description: Optional[str] = Field(None, alias="TypeDescription")
    use_billing_milestones: Optional[bool] = Field(None, alias="UseBillingMilestones")
