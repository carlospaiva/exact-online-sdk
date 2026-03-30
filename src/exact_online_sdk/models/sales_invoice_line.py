from __future__ import annotations

from decimal import Decimal
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SalesInvoiceLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    invoice_id: UUID = Field(alias="InvoiceID")
    item: Optional[UUID] = Field(default=None, alias="Item")
    gl_account: Optional[UUID] = Field(default=None, alias="GLAccount")
    amount_dc: Optional[Decimal] = Field(default=None, alias="AmountDC")
    division: Optional[int] = Field(default=None, alias="Division")
    cost_center: Optional[str] = Field(default=None, alias="CostCenter")
    cost_unit: Optional[str] = Field(default=None, alias="CostUnit")
    customer_item_code: Optional[str] = Field(default=None, alias="CustomerItemCode")
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    vat_code: Optional[str] = Field(default=None, alias="VATCode")
    employee: Optional[UUID] = Field(default=None, alias="Employee")
    pricelist: Optional[UUID] = Field(default=None, alias="Pricelist")
    project: Optional[UUID] = Field(default=None, alias="Project")
    sales_order: Optional[UUID] = Field(default=None, alias="SalesOrder")
    sales_order_line: Optional[UUID] = Field(default=None, alias="SalesOrderLine")
    subscription: Optional[UUID] = Field(default=None, alias="Subscription")
