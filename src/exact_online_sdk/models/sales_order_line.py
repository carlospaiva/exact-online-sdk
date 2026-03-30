from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SalesOrderLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    cost_center: Optional[str] = Field(default=None, alias="CostCenter")
    cost_center_description: Optional[str] = Field(
        default=None, alias="CostCenterDescription"
    )
    cost_price_fc: Optional[float] = Field(default=None, alias="CostPriceFC")
    cost_unit: Optional[str] = Field(default=None, alias="CostUnit")
    cost_unit_description: Optional[str] = Field(
        default=None, alias="CostUnitDescription"
    )
    customer_item_code: Optional[str] = Field(default=None, alias="CustomerItemCode")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    delivery_date: Optional[datetime] = Field(default=None, alias="DeliveryDate")
    delivery_status: Optional[int] = Field(default=None, alias="DeliveryStatus")
    description: Optional[str] = Field(default=None, alias="Description")
    discount: Optional[float] = Field(default=None, alias="Discount")
    division: Optional[int] = Field(default=None, alias="Division")
    invoice_status: Optional[int] = Field(default=None, alias="InvoiceStatus")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_version: Optional[UUID] = Field(default=None, alias="ItemVersion")
    item_version_description: Optional[str] = Field(
        default=None, alias="ItemVersionDescription"
    )
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    margin: Optional[float] = Field(default=None, alias="Margin")
    net_price: Optional[float] = Field(default=None, alias="NetPrice")
    notes: Optional[str] = Field(default=None, alias="Notes")
    order_id: UUID = Field(alias="OrderID")
    order_number: Optional[int] = Field(default=None, alias="OrderNumber")
    order_status: Optional[int] = Field(default=None, alias="OrderStatus")
    pricelist: Optional[UUID] = Field(default=None, alias="Pricelist")
    pricelist_description: Optional[str] = Field(
        default=None, alias="PricelistDescription"
    )
    project: Optional[UUID] = Field(default=None, alias="Project")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    purchase_order: Optional[UUID] = Field(default=None, alias="PurchaseOrder")
    purchase_order_line: Optional[UUID] = Field(default=None, alias="PurchaseOrderLine")
    purchase_order_line_number: Optional[int] = Field(
        default=None, alias="PurchaseOrderLineNumber"
    )
    purchase_order_number: Optional[int] = Field(
        default=None, alias="PurchaseOrderNumber"
    )
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    quantity_delivered: Optional[float] = Field(default=None, alias="QuantityDelivered")
    quantity_invoiced: Optional[float] = Field(default=None, alias="QuantityInvoiced")
    shop_order: Optional[UUID] = Field(default=None, alias="ShopOrder")
    tax_schedule: Optional[UUID] = Field(default=None, alias="TaxSchedule")
    tax_schedule_code: Optional[str] = Field(default=None, alias="TaxScheduleCode")
    tax_schedule_description: Optional[str] = Field(
        default=None, alias="TaxScheduleDescription"
    )
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    unit_price: Optional[float] = Field(default=None, alias="UnitPrice")
    use_drop_shipment: Optional[int] = Field(default=None, alias="UseDropShipment")
    vat_amount: Optional[float] = Field(default=None, alias="VATAmount")
    vat_code: Optional[str] = Field(default=None, alias="VATCode")
    vat_code_description: Optional[str] = Field(
        default=None, alias="VATCodeDescription"
    )
    vat_percentage: Optional[float] = Field(default=None, alias="VATPercentage")
