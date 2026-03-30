from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SalesInvoiceOrderChargeLine(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_fc_excl_vat: Optional[float] = Field(default=None, alias="AmountFCExclVAT")
    amount_fc_incl_vat: Optional[float] = Field(default=None, alias="AmountFCInclVAT")
    amount_vat_fc: Optional[float] = Field(default=None, alias="AmountVATFC")
    division: Optional[int] = Field(default=None, alias="Division")
    gl_account: Optional[UUID] = Field(default=None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(default=None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(
        default=None, alias="GLAccountDescription"
    )
    invoice_id: UUID = Field(alias="InvoiceID")
    is_shipping_cost: Optional[bool] = Field(default=None, alias="IsShippingCost")
    line_number: Optional[int] = Field(default=None, alias="LineNumber")
    order_charge: Optional[UUID] = Field(default=None, alias="OrderCharge")
    order_charge_code: Optional[str] = Field(default=None, alias="OrderChargeCode")
    order_charge_description: Optional[str] = Field(
        default=None, alias="OrderChargeDescription"
    )
    order_charges_line_description: Optional[str] = Field(
        default=None, alias="OrderChargesLineDescription"
    )
    vat_code: Optional[str] = Field(default=None, alias="VATCode")
    vat_description: Optional[str] = Field(default=None, alias="VATDescription")
    vat_percentage: Optional[float] = Field(default=None, alias="VATPercentage")
