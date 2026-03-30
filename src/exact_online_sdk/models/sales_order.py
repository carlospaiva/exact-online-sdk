from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .sales_order_line import SalesOrderLine
from .sales_order_order_charge_line import SalesOrderOrderChargeLine


class SalesOrder(StrictModel):
    order_id: Optional[UUID] = Field(default=None, alias="OrderID")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_discount: Optional[float] = Field(default=None, alias="AmountDiscount")
    amount_discount_excl_vat: Optional[float] = Field(
        default=None, alias="AmountDiscountExclVat"
    )
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    amount_fc_excl_vat: Optional[float] = Field(default=None, alias="AmountFCExclVat")
    approval_status: Optional[int] = Field(default=None, alias="ApprovalStatus")
    approval_status_description: Optional[str] = Field(
        default=None, alias="ApprovalStatusDescription"
    )
    approved: Optional[datetime] = Field(default=None, alias="Approved")
    approver: Optional[UUID] = Field(default=None, alias="Approver")
    approver_full_name: Optional[str] = Field(default=None, alias="ApproverFullName")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    deliver_to: Optional[UUID] = Field(default=None, alias="DeliverTo")
    deliver_to_contact_person: Optional[UUID] = Field(
        default=None, alias="DeliverToContactPerson"
    )
    deliver_to_contact_person_full_name: Optional[str] = Field(
        default=None, alias="DeliverToContactPersonFullName"
    )
    deliver_to_name: Optional[str] = Field(default=None, alias="DeliverToName")
    delivery_address: Optional[UUID] = Field(default=None, alias="DeliveryAddress")
    delivery_date: Optional[datetime] = Field(default=None, alias="DeliveryDate")
    delivery_status: Optional[int] = Field(default=None, alias="DeliveryStatus")
    delivery_status_description: Optional[str] = Field(
        default=None, alias="DeliveryStatusDescription"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    discount: Optional[float] = Field(default=None, alias="Discount")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    document_number: Optional[int] = Field(default=None, alias="DocumentNumber")
    document_subject: Optional[str] = Field(default=None, alias="DocumentSubject")
    incoterm_address: Optional[str] = Field(default=None, alias="IncotermAddress")
    incoterm_code: Optional[str] = Field(default=None, alias="IncotermCode")
    incoterm_version: Optional[int] = Field(default=None, alias="IncotermVersion")
    invoice_status: Optional[int] = Field(default=None, alias="InvoiceStatus")
    invoice_status_description: Optional[str] = Field(
        default=None, alias="InvoiceStatusDescription"
    )
    invoice_to: Optional[UUID] = Field(default=None, alias="InvoiceTo")
    invoice_to_contact_person: Optional[UUID] = Field(
        default=None, alias="InvoiceToContactPerson"
    )
    invoice_to_contact_person_full_name: Optional[str] = Field(
        default=None, alias="InvoiceToContactPersonFullName"
    )
    invoice_to_name: Optional[str] = Field(default=None, alias="InvoiceToName")
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
    sales_order_lines: list[SalesOrderLine] = Field(
        default_factory=list, alias="SalesOrderLines"
    )
    sales_order_order_charge_lines: list[SalesOrderOrderChargeLine] = Field(
        default_factory=list, alias="SalesOrderOrderChargeLines"
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
    shipping_method_description: Optional[str] = Field(
        default=None, alias="ShippingMethodDescription"
    )
    status: Optional[int] = Field(default=None, alias="Status")
    status_description: Optional[str] = Field(default=None, alias="StatusDescription")
    tax_schedule: Optional[UUID] = Field(default=None, alias="TaxSchedule")
    tax_schedule_code: Optional[str] = Field(default=None, alias="TaxScheduleCode")
    tax_schedule_description: Optional[str] = Field(
        default=None, alias="TaxScheduleDescription"
    )
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
    warehouse_id: Optional[UUID] = Field(default=None, alias="WarehouseID")
    your_ref: Optional[str] = Field(default=None, alias="YourRef")
