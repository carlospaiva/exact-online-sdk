from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .sales_invoice_line import SalesInvoiceLine
from .sales_invoice_order_charge_line import SalesInvoiceOrderChargeLine
from .sales_invoice_status import SalesInvoiceStatus


class SalesInvoice(StrictModel):
    invoice_id: Optional[UUID] = Field(default=None, alias="InvoiceID")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_discount: Optional[float] = Field(default=None, alias="AmountDiscount")
    amount_discount_excl_vat: Optional[float] = Field(
        default=None, alias="AmountDiscountExclVat"
    )
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    amount_fc_excl_vat: Optional[float] = Field(default=None, alias="AmountFCExclVat")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    deliver_to: Optional[UUID] = Field(default=None, alias="DeliverTo")
    deliver_to_address: Optional[UUID] = Field(default=None, alias="DeliverToAddress")
    deliver_to_contact_person: Optional[UUID] = Field(
        default=None, alias="DeliverToContactPerson"
    )
    deliver_to_contact_person_full_name: Optional[str] = Field(
        default=None, alias="DeliverToContactPersonFullName"
    )
    deliver_to_name: Optional[str] = Field(default=None, alias="DeliverToName")
    description: Optional[str] = Field(default=None, alias="Description")
    discount: Optional[float] = Field(default=None, alias="Discount")
    discount_type: Optional[int] = Field(default=None, alias="DiscountType")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    document_number: Optional[int] = Field(default=None, alias="DocumentNumber")
    document_subject: Optional[str] = Field(default=None, alias="DocumentSubject")
    due_date: Optional[datetime] = Field(default=None, alias="DueDate")
    extra_duty_amount_fc: Optional[float] = Field(
        default=None, alias="ExtraDutyAmountFC"
    )
    g_account_amount_fc: Optional[float] = Field(default=None, alias="GAccountAmountFC")
    id: Optional[UUID] = Field(default=None, alias="ID")
    incoterm_address: Optional[str] = Field(default=None, alias="IncotermAddress")
    incoterm_code: Optional[str] = Field(default=None, alias="IncotermCode")
    incoterm_version: Optional[int] = Field(default=None, alias="IncotermVersion")
    invoice_date: Optional[datetime] = Field(default=None, alias="InvoiceDate")
    invoice_number: Optional[int] = Field(default=None, alias="InvoiceNumber")
    invoice_to: Optional[UUID] = Field(default=None, alias="InvoiceTo")
    invoice_to_contact_person: Optional[UUID] = Field(
        default=None, alias="InvoiceToContactPerson"
    )
    invoice_to_contact_person_full_name: Optional[str] = Field(
        default=None, alias="InvoiceToContactPersonFullName"
    )
    invoice_to_name: Optional[str] = Field(default=None, alias="InvoiceToName")
    is_extra_duty: Optional[bool] = Field(default=None, alias="IsExtraDuty")
    journal: str = Field(alias="Journal")
    journal_description: Optional[str] = Field(default=None, alias="JournalDescription")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    order_date: Optional[datetime] = Field(default=None, alias="OrderDate")
    ordered_by: UUID = Field(alias="OrderedBy")
    ordered_by_contact_person: Optional[UUID] = Field(
        default=None, alias="OrderedByContactPerson"
    )
    ordered_by_contact_person_full_name: Optional[str] = Field(
        default=None, alias="OrderedByContactPersonFullName"
    )
    ordered_by_name: Optional[str] = Field(default=None, alias="OrderedByName")
    order_number: Optional[int] = Field(default=None, alias="OrderNumber")
    payment_condition: Optional[str] = Field(default=None, alias="PaymentCondition")
    payment_condition_description: Optional[str] = Field(
        default=None, alias="PaymentConditionDescription"
    )
    payment_reference: Optional[str] = Field(default=None, alias="PaymentReference")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    sales_channel: Optional[UUID] = Field(default=None, alias="SalesChannel")
    sales_channel_code: Optional[str] = Field(default=None, alias="SalesChannelCode")
    sales_channel_description: Optional[str] = Field(
        default=None, alias="SalesChannelDescription"
    )
    sales_invoice_lines: list[SalesInvoiceLine] = Field(
        default_factory=list, alias="SalesInvoiceLines"
    )
    sales_invoice_order_charge_lines: Optional[list[SalesInvoiceOrderChargeLine]] = (
        Field(default=None, alias="SalesInvoiceOrderChargeLines")
    )
    salesperson: Optional[UUID] = Field(default=None, alias="Salesperson")
    salesperson_full_name: Optional[str] = Field(
        default=None, alias="SalespersonFullName"
    )
    selection_code: Optional[UUID] = Field(default=None, alias="SelectionCode")
    selection_code_code: Optional[str] = Field(default=None, alias="SelectionCodeCode")
    selection_code_description: Optional[str] = Field(
        default=None, alias="SelectionCodeDescription"
    )
    shipping_method: Optional[UUID] = Field(default=None, alias="ShippingMethod")
    shipping_method_code: Optional[str] = Field(
        default=None, alias="ShippingMethodCode"
    )
    shipping_method_description: Optional[str] = Field(
        default=None, alias="ShippingMethodDescription"
    )
    starter_sales_invoice_status: Optional[int] = Field(
        default=None, alias="StarterSalesInvoiceStatus"
    )
    starter_sales_invoice_status_description: Optional[str] = Field(
        default=None, alias="StarterSalesInvoiceStatusDescription"
    )
    status: Optional[SalesInvoiceStatus] = Field(default=None, alias="Status")
    status_description: Optional[str] = Field(default=None, alias="StatusDescription")
    tax_schedule: Optional[UUID] = Field(default=None, alias="TaxSchedule")
    tax_schedule_code: Optional[str] = Field(default=None, alias="TaxScheduleCode")
    tax_schedule_description: Optional[str] = Field(
        default=None, alias="TaxScheduleDescription"
    )
    type: Optional[int] = Field(default=None, alias="Type")
    type_description: Optional[str] = Field(default=None, alias="TypeDescription")
    vat_amount_dc: Optional[float] = Field(default=None, alias="VATAmountDC")
    vat_amount_fc: Optional[float] = Field(default=None, alias="VATAmountFC")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    withholding_tax_amount_fc: Optional[float] = Field(
        default=None, alias="WithholdingTaxAmountFC"
    )
    withholding_tax_base_amount: Optional[float] = Field(
        default=None, alias="WithholdingTaxBaseAmount"
    )
    withholding_tax_percentage: Optional[float] = Field(
        default=None, alias="WithholdingTaxPercentage"
    )
    your_ref: Optional[str] = Field(default=None, alias="YourRef")
