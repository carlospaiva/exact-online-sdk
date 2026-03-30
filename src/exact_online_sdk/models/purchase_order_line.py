from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class PurchaseOrderLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    cost_center: Optional[str] = Field(default=None, alias="CostCenter")
    cost_center_description: Optional[str] = Field(
        default=None, alias="CostCenterDescription"
    )
    cost_unit: Optional[str] = Field(default=None, alias="CostUnit")
    cost_unit_description: Optional[str] = Field(
        default=None, alias="CostUnitDescription"
    )
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    description: Optional[str] = Field(default=None, alias="Description")
    discount: Optional[float] = Field(default=None, alias="Discount")
    division: Optional[int] = Field(default=None, alias="Division")
    expense: Optional[UUID] = Field(default=None, alias="Expense")
    expense_description: Optional[str] = Field(default=None, alias="ExpenseDescription")
    in_stock: Optional[float] = Field(default=None, alias="InStock")
    invoiced_quantity: Optional[float] = Field(default=None, alias="InvoicedQuantity")
    is_batch_number_item: Optional[int] = Field(default=None, alias="IsBatchNumberItem")
    is_serial_number_item: Optional[int] = Field(
        default=None, alias="IsSerialNumberItem"
    )
    item: UUID = Field(alias="Item")
    item_barcode: Optional[str] = Field(default=None, alias="ItemBarcode")
    item_barcode_additional: Optional[str] = Field(
        default=None, alias="ItemBarcodeAdditional"
    )
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_divisable: Optional[bool] = Field(default=None, alias="ItemDivisable")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    net_price: Optional[float] = Field(default=None, alias="NetPrice")
    notes: Optional[str] = Field(default=None, alias="Notes")
    project: Optional[UUID] = Field(default=None, alias="Project")
    project_code: Optional[str] = Field(default=None, alias="ProjectCode")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    projected_stock: Optional[float] = Field(default=None, alias="ProjectedStock")
    purchase_order_id: UUID = Field(alias="PurchaseOrderID")
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    quantity_in_purchase_units: float = Field(alias="QuantityInPurchaseUnits")
    rebill: Optional[bool] = Field(default=None, alias="Rebill")
    receipt_date: Optional[datetime] = Field(default=None, alias="ReceiptDate")
    received_quantity: Optional[float] = Field(default=None, alias="ReceivedQuantity")
    sales_order: Optional[UUID] = Field(default=None, alias="SalesOrder")
    sales_order_line: Optional[UUID] = Field(default=None, alias="SalesOrderLine")
    sales_order_line_number: Optional[int] = Field(
        default=None, alias="SalesOrderLineNumber"
    )
    sales_order_number: Optional[int] = Field(default=None, alias="SalesOrderNumber")
    shop_order_material_plans: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="ShopOrderMaterialPlans"
    )
    shop_order_routing_step_plans: Optional[list[dict[str, Any]]] = Field(
        default=None, alias="ShopOrderRoutingStepPlans"
    )
    supplier_item_code: Optional[str] = Field(default=None, alias="SupplierItemCode")
    supplier_item_copy_remarks: Optional[int] = Field(
        default=None, alias="SupplierItemCopyRemarks"
    )
    unit: Optional[str] = Field(default=None, alias="Unit")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    unit_price: Optional[float] = Field(default=None, alias="UnitPrice")
    vat_amount: Optional[float] = Field(default=None, alias="VATAmount")
    vat_code: Optional[str] = Field(default=None, alias="VATCode")
    vat_description: Optional[str] = Field(default=None, alias="VATDescription")
    vat_percentage: Optional[float] = Field(default=None, alias="VATPercentage")
