from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class ItemGroup(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    code: Optional[str] = Field(default=None, alias="Code")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    description: Optional[str] = Field(default=None, alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    gl_costs: Optional[UUID] = Field(default=None, alias="GLCosts")
    gl_costs_code: Optional[str] = Field(default=None, alias="GLCostsCode")
    gl_costs_description: Optional[str] = Field(
        default=None, alias="GLCostsDescription"
    )
    gl_costs_work_in_progress: Optional[UUID] = Field(
        default=None, alias="GLCostsWorkInProgress"
    )
    gl_costs_work_in_progress_code: Optional[str] = Field(
        default=None, alias="GLCostsWorkInProgressCode"
    )
    gl_costs_work_in_progress_description: Optional[str] = Field(
        default=None, alias="GLCostsWorkInProgressDescription"
    )
    gl_purchase_account: Optional[UUID] = Field(default=None, alias="GLPurchaseAccount")
    gl_purchase_account_code: Optional[str] = Field(
        default=None, alias="GLPurchaseAccountCode"
    )
    gl_purchase_account_description: Optional[str] = Field(
        default=None, alias="GLPurchaseAccountDescription"
    )
    gl_purchase_price_difference: Optional[UUID] = Field(
        default=None, alias="GLPurchasePriceDifference"
    )
    gl_purchase_price_difference_code: Optional[str] = Field(
        default=None, alias="GLPurchasePriceDifferenceCode"
    )
    gl_purchase_price_difference_descr: Optional[str] = Field(
        default=None, alias="GLPurchasePriceDifferenceDescr"
    )
    gl_revenue: Optional[UUID] = Field(default=None, alias="GLRevenue")
    gl_revenue_code: Optional[str] = Field(default=None, alias="GLRevenueCode")
    gl_revenue_description: Optional[str] = Field(
        default=None, alias="GLRevenueDescription"
    )
    gl_revenue_work_in_progress: Optional[UUID] = Field(
        default=None, alias="GLRevenueWorkInProgress"
    )
    gl_revenue_work_in_progress_code: Optional[str] = Field(
        default=None, alias="GLRevenueWorkInProgressCode"
    )
    gl_revenue_work_in_progress_description: Optional[str] = Field(
        default=None, alias="GLRevenueWorkInProgressDescription"
    )
    gl_stock: Optional[UUID] = Field(default=None, alias="GLStock")
    gl_stock_code: Optional[str] = Field(default=None, alias="GLStockCode")
    gl_stock_description: Optional[str] = Field(
        default=None, alias="GLStockDescription"
    )
    gl_stock_variance: Optional[UUID] = Field(default=None, alias="GLStockVariance")
    gl_stock_variance_code: Optional[str] = Field(
        default=None, alias="GLStockVarianceCode"
    )
    gl_stock_variance_description: Optional[str] = Field(
        default=None, alias="GLStockVarianceDescription"
    )
    is_default: Optional[int] = Field(default=None, alias="IsDefault")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    notes: Optional[str] = Field(default=None, alias="Notes")
