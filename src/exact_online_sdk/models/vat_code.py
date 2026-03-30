from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class VATCode(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_name: Optional[str] = Field(None, alias="AccountName")
    calculation_basis: Optional[int] = Field(None, alias="CalculationBasis")
    charged: Optional[bool] = Field(None, alias="Charged")
    code: Optional[str] = Field(None, alias="Code")
    country: Optional[str] = Field(None, alias="Country")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    eu_sales_listing: Optional[str] = Field(None, alias="EUSalesListing")
    exclude_vat_listing: Optional[int] = Field(None, alias="ExcludeVATListing")
    gl_discount_purchase: Optional[UUID] = Field(None, alias="GLDiscountPurchase")
    gl_discount_purchase_code: Optional[str] = Field(
        None, alias="GLDiscountPurchaseCode"
    )
    gl_discount_purchase_description: Optional[str] = Field(
        None, alias="GLDiscountPurchaseDescription"
    )
    gl_discount_sales: Optional[UUID] = Field(None, alias="GLDiscountSales")
    gl_discount_sales_code: Optional[str] = Field(None, alias="GLDiscountSalesCode")
    gl_discount_sales_description: Optional[str] = Field(
        None, alias="GLDiscountSalesDescription"
    )
    gl_to_claim: Optional[UUID] = Field(None, alias="GLToClaim")
    gl_to_claim_code: Optional[str] = Field(None, alias="GLToClaimCode")
    gl_to_claim_description: Optional[str] = Field(None, alias="GLToClaimDescription")
    gl_to_pay: Optional[UUID] = Field(None, alias="GLToPay")
    gl_to_pay_code: Optional[str] = Field(None, alias="GLToPayCode")
    gl_to_pay_description: Optional[str] = Field(None, alias="GLToPayDescription")
    intra_stat: Optional[bool] = Field(None, alias="IntraStat")
    intrastat_type: Optional[str] = Field(None, alias="IntrastatType")
    is_blocked: Optional[bool] = Field(None, alias="IsBlocked")
    legal_text: Optional[str] = Field(None, alias="LegalText")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    oss_country: Optional[str] = Field(None, alias="OssCountry")
    percentage: Optional[float] = Field(None, alias="Percentage")
    tax_return_type: Optional[int] = Field(None, alias="TaxReturnType")
    type: Optional[str] = Field(None, alias="Type")
    vat_doc_type: Optional[str] = Field(None, alias="VatDocType")
    vat_margin: Optional[int] = Field(None, alias="VatMargin")
    vat_partial_ratio: Optional[int] = Field(None, alias="VATPartialRatio")
    vat_percentages: Optional[list] = Field(  # type: ignore[type-arg]
        None, alias="VATPercentages"
    )
    vat_transaction_type: Optional[str] = Field(None, alias="VATTransactionType")
