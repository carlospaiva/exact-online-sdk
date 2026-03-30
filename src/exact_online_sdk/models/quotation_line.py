from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class QuotationLine(StrictModel):
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
    customer_item_code: Optional[str] = Field(default=None, alias="CustomerItemCode")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    description: Optional[str] = Field(default=None, alias="Description")
    discount: Optional[float] = Field(default=None, alias="Discount")
    division: Optional[int] = Field(default=None, alias="Division")
    item: UUID = Field(alias="Item")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    net_price: Optional[float] = Field(default=None, alias="NetPrice")
    notes: Optional[str] = Field(default=None, alias="Notes")
    optional: Optional[bool] = Field(default=None, alias="Optional")
    quantity: Optional[float] = Field(default=None, alias="Quantity")
    quotation_id: UUID = Field(alias="QuotationID")
    quotation_number: Optional[int] = Field(default=None, alias="QuotationNumber")
    unit_code: Optional[str] = Field(default=None, alias="UnitCode")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    unit_price: Optional[float] = Field(default=None, alias="UnitPrice")
    vat_amount_fc: Optional[float] = Field(default=None, alias="VATAmountFC")
    vat_code: Optional[str] = Field(default=None, alias="VATCode")
    vat_description: Optional[str] = Field(default=None, alias="VATDescription")
    vat_percentage: Optional[float] = Field(default=None, alias="VATPercentage")
    version_number: Optional[int] = Field(default=None, alias="VersionNumber")
