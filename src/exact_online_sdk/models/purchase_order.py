from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .purchase_order_line import PurchaseOrderLine


class PurchaseOrder(StrictModel):
    purchase_order_id: Optional[UUID] = Field(default=None, alias="PurchaseOrderID")
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
    delivery_account: Optional[UUID] = Field(default=None, alias="DeliveryAccount")
    delivery_account_code: Optional[str] = Field(
        default=None, alias="DeliveryAccountCode"
    )
    delivery_account_name: Optional[str] = Field(
        default=None, alias="DeliveryAccountName"
    )
    delivery_address: Optional[UUID] = Field(default=None, alias="DeliveryAddress")
    delivery_contact: Optional[UUID] = Field(default=None, alias="DeliveryContact")
    delivery_contact_person_full_name: Optional[str] = Field(
        default=None, alias="DeliveryContactPersonFullName"
    )
    description: Optional[str] = Field(default=None, alias="Description")
    discount: Optional[float] = Field(default=None, alias="Discount")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    document_subject: Optional[str] = Field(default=None, alias="DocumentSubject")
    drop_shipment: Optional[bool] = Field(default=None, alias="DropShipment")
    exchange_rate: Optional[float] = Field(default=None, alias="ExchangeRate")
    incoterm_address: Optional[str] = Field(default=None, alias="IncotermAddress")
    incoterm_code: Optional[str] = Field(default=None, alias="IncotermCode")
    incoterm_version: Optional[int] = Field(default=None, alias="IncotermVersion")
    invoice_status: Optional[int] = Field(default=None, alias="InvoiceStatus")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    order_date: Optional[datetime] = Field(default=None, alias="OrderDate")
    order_number: Optional[int] = Field(default=None, alias="OrderNumber")
    order_status: Optional[int] = Field(default=None, alias="OrderStatus")
    payment_condition: Optional[str] = Field(default=None, alias="PaymentCondition")
    payment_condition_description: Optional[str] = Field(
        default=None, alias="PaymentConditionDescription"
    )
    purchase_agent: Optional[UUID] = Field(default=None, alias="PurchaseAgent")
    purchase_agent_full_name: Optional[str] = Field(
        default=None, alias="PurchaseAgentFullName"
    )
    purchase_order_line_count: Optional[int] = Field(
        default=None, alias="PurchaseOrderLineCount"
    )
    purchase_order_lines: list[PurchaseOrderLine] = Field(
        default_factory=list, alias="PurchaseOrderLines"
    )
    receipt_date: Optional[datetime] = Field(default=None, alias="ReceiptDate")
    receipt_status: Optional[int] = Field(default=None, alias="ReceiptStatus")
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    sales_order: Optional[UUID] = Field(default=None, alias="SalesOrder")
    sales_order_number: Optional[int] = Field(default=None, alias="SalesOrderNumber")
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
    source: Optional[int] = Field(default=None, alias="Source")
    supplier: UUID = Field(alias="Supplier")
    supplier_code: Optional[str] = Field(default=None, alias="SupplierCode")
    supplier_contact: Optional[UUID] = Field(default=None, alias="SupplierContact")
    supplier_contact_person_full_name: Optional[str] = Field(
        default=None, alias="SupplierContactPersonFullName"
    )
    supplier_name: Optional[str] = Field(default=None, alias="SupplierName")
    vat_amount: Optional[float] = Field(default=None, alias="VATAmount")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
    your_ref: Optional[str] = Field(default=None, alias="YourRef")
