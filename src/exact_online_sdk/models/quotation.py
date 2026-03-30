from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .quotation_line import QuotationLine
from .quotation_order_charge_line import QuotationOrderChargeLine
from .quotation_status import QuotationStatus


class Quotation(StrictModel):
    quotation_id: Optional[UUID] = Field(default=None, alias="QuotationID")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_discount: Optional[float] = Field(default=None, alias="AmountDiscount")
    amount_discount_excl_vat: Optional[float] = Field(
        default=None, alias="AmountDiscountExclVat"
    )
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    close_date: Optional[datetime] = Field(default=None, alias="CloseDate")
    closing_date: Optional[datetime] = Field(default=None, alias="ClosingDate")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    delivery_account: Optional[UUID] = Field(default=None, alias="DeliveryAccount")
    delivery_account_code: Optional[str] = Field(
        default=None, alias="DeliveryAccountCode"
    )
    delivery_account_contact: Optional[UUID] = Field(
        default=None, alias="DeliveryAccountContact"
    )
    delivery_account_contact_full_name: Optional[str] = Field(
        default=None, alias="DeliveryAccountContactFullName"
    )
    delivery_account_name: Optional[str] = Field(
        default=None, alias="DeliveryAccountName"
    )
    delivery_address: Optional[UUID] = Field(default=None, alias="DeliveryAddress")
    delivery_date: Optional[datetime] = Field(default=None, alias="DeliveryDate")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    document_subject: Optional[str] = Field(default=None, alias="DocumentSubject")
    due_date: Optional[datetime] = Field(default=None, alias="DueDate")
    incoterm_address: Optional[str] = Field(default=None, alias="IncotermAddress")
    incoterm_code: Optional[str] = Field(default=None, alias="IncotermCode")
    incoterm_version: Optional[int] = Field(default=None, alias="IncotermVersion")
    invoice_account: Optional[UUID] = Field(default=None, alias="InvoiceAccount")
    invoice_account_code: Optional[str] = Field(
        default=None, alias="InvoiceAccountCode"
    )
    invoice_account_contact: Optional[UUID] = Field(
        default=None, alias="InvoiceAccountContact"
    )
    invoice_account_contact_full_name: Optional[str] = Field(
        default=None, alias="InvoiceAccountContactFullName"
    )
    invoice_account_name: Optional[str] = Field(
        default=None, alias="InvoiceAccountName"
    )
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    opportunity: Optional[UUID] = Field(default=None, alias="Opportunity")
    opportunity_name: Optional[str] = Field(default=None, alias="OpportunityName")
    order_account: UUID = Field(alias="OrderAccount")
    order_account_code: Optional[str] = Field(default=None, alias="OrderAccountCode")
    order_account_contact: Optional[UUID] = Field(
        default=None, alias="OrderAccountContact"
    )
    order_account_contact_full_name: Optional[str] = Field(
        default=None, alias="OrderAccountContactFullName"
    )
    order_account_name: Optional[str] = Field(default=None, alias="OrderAccountName")
    payment_condition: Optional[str] = Field(default=None, alias="PaymentCondition")
    payment_condition_description: Optional[str] = Field(
        default=None, alias="PaymentConditionDescription"
    )
    project: Optional[UUID] = Field(default=None, alias="Project")
    project_code: Optional[str] = Field(default=None, alias="ProjectCode")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    quotation_date: Optional[datetime] = Field(default=None, alias="QuotationDate")
    quotation_lines: list[QuotationLine] = Field(
        default_factory=list, alias="QuotationLines"
    )
    quotation_number: Optional[int] = Field(default=None, alias="QuotationNumber")
    quotation_order_charge_lines: Optional[list[QuotationOrderChargeLine]] = Field(
        default=None, alias="QuotationOrderChargeLines"
    )
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    sales_channel: Optional[UUID] = Field(default=None, alias="SalesChannel")
    sales_channel_code: Optional[str] = Field(default=None, alias="SalesChannelCode")
    sales_channel_description: Optional[str] = Field(
        default=None, alias="SalesChannelDescription"
    )
    sales_person: Optional[UUID] = Field(default=None, alias="SalesPerson")
    sales_person_full_name: Optional[str] = Field(
        default=None, alias="SalesPersonFullName"
    )
    selection_code: Optional[UUID] = Field(default=None, alias="SelectionCode")
    selection_code_code: Optional[str] = Field(default=None, alias="SelectionCodeCode")
    selection_code_description: Optional[str] = Field(
        default=None, alias="SelectionCodeDescription"
    )
    shipping_method: Optional[UUID] = Field(default=None, alias="ShippingMethod")
    shipping_method_description: Optional[str] = Field(
        default=None, alias="ShippingMethodDescription"
    )
    status: Optional[QuotationStatus] = Field(default=None, alias="Status")
    status_description: Optional[str] = Field(default=None, alias="StatusDescription")
    vat_amount_fc: Optional[float] = Field(default=None, alias="VATAmountFC")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
    warehouse_id: Optional[UUID] = Field(default=None, alias="WarehouseID")
    your_ref: Optional[str] = Field(default=None, alias="YourRef")
