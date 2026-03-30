from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Item(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    assembled_lead_days: Optional[int] = Field(default=None, alias="AssembledLeadDays")
    average_cost: Optional[float] = Field(default=None, alias="AverageCost")
    barcode: Optional[str] = Field(default=None, alias="Barcode")
    batch_quantity: Optional[float] = Field(default=None, alias="BatchQuantity")
    class_01: Optional[str] = Field(default=None, alias="Class_01")
    class_02: Optional[str] = Field(default=None, alias="Class_02")
    class_03: Optional[str] = Field(default=None, alias="Class_03")
    class_04: Optional[str] = Field(default=None, alias="Class_04")
    class_05: Optional[str] = Field(default=None, alias="Class_05")
    class_06: Optional[str] = Field(default=None, alias="Class_06")
    class_07: Optional[str] = Field(default=None, alias="Class_07")
    class_08: Optional[str] = Field(default=None, alias="Class_08")
    class_09: Optional[str] = Field(default=None, alias="Class_09")
    class_10: Optional[str] = Field(default=None, alias="Class_10")
    code: str = Field(alias="Code")
    copy_remarks: Optional[int] = Field(default=None, alias="CopyRemarks")
    cost_price_currency: Optional[str] = Field(default=None, alias="CostPriceCurrency")
    cost_price_new: Optional[float] = Field(default=None, alias="CostPriceNew")
    cost_price_standard: Optional[float] = Field(
        default=None, alias="CostPriceStandard"
    )
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    description: str = Field(alias="Description")
    division: Optional[int] = Field(default=None, alias="Division")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    extra_description: Optional[str] = Field(default=None, alias="ExtraDescription")
    free_bool_field_01: Optional[bool] = Field(default=None, alias="FreeBoolField_01")
    free_bool_field_02: Optional[bool] = Field(default=None, alias="FreeBoolField_02")
    free_bool_field_03: Optional[bool] = Field(default=None, alias="FreeBoolField_03")
    free_bool_field_04: Optional[bool] = Field(default=None, alias="FreeBoolField_04")
    free_bool_field_05: Optional[bool] = Field(default=None, alias="FreeBoolField_05")
    free_date_field_01: Optional[datetime] = Field(
        default=None, alias="FreeDateField_01"
    )
    free_date_field_02: Optional[datetime] = Field(
        default=None, alias="FreeDateField_02"
    )
    free_date_field_03: Optional[datetime] = Field(
        default=None, alias="FreeDateField_03"
    )
    free_date_field_04: Optional[datetime] = Field(
        default=None, alias="FreeDateField_04"
    )
    free_date_field_05: Optional[datetime] = Field(
        default=None, alias="FreeDateField_05"
    )
    free_number_field_01: Optional[float] = Field(
        default=None, alias="FreeNumberField_01"
    )
    free_number_field_02: Optional[float] = Field(
        default=None, alias="FreeNumberField_02"
    )
    free_number_field_03: Optional[float] = Field(
        default=None, alias="FreeNumberField_03"
    )
    free_number_field_04: Optional[float] = Field(
        default=None, alias="FreeNumberField_04"
    )
    free_number_field_05: Optional[float] = Field(
        default=None, alias="FreeNumberField_05"
    )
    free_number_field_06: Optional[float] = Field(
        default=None, alias="FreeNumberField_06"
    )
    free_number_field_07: Optional[float] = Field(
        default=None, alias="FreeNumberField_07"
    )
    free_number_field_08: Optional[float] = Field(
        default=None, alias="FreeNumberField_08"
    )
    free_text_field_01: Optional[str] = Field(default=None, alias="FreeTextField_01")
    free_text_field_02: Optional[str] = Field(default=None, alias="FreeTextField_02")
    free_text_field_03: Optional[str] = Field(default=None, alias="FreeTextField_03")
    free_text_field_04: Optional[str] = Field(default=None, alias="FreeTextField_04")
    free_text_field_05: Optional[str] = Field(default=None, alias="FreeTextField_05")
    free_text_field_06: Optional[str] = Field(default=None, alias="FreeTextField_06")
    free_text_field_07: Optional[str] = Field(default=None, alias="FreeTextField_07")
    free_text_field_08: Optional[str] = Field(default=None, alias="FreeTextField_08")
    free_text_field_09: Optional[str] = Field(default=None, alias="FreeTextField_09")
    free_text_field_10: Optional[str] = Field(default=None, alias="FreeTextField_10")
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
    gross_weight: Optional[float] = Field(default=None, alias="GrossWeight")
    is_batch_item: Optional[int] = Field(default=None, alias="IsBatchItem")
    is_fraction_allowed_item: Optional[bool] = Field(
        default=None, alias="IsFractionAllowedItem"
    )
    is_make_item: Optional[int] = Field(default=None, alias="IsMakeItem")
    is_new_contract: Optional[int] = Field(default=None, alias="IsNewContract")
    is_on_demand_item: Optional[int] = Field(default=None, alias="IsOnDemandItem")
    is_package_item: Optional[bool] = Field(default=None, alias="IsPackageItem")
    is_purchase_item: Optional[bool] = Field(default=None, alias="IsPurchaseItem")
    is_registration_code_item: Optional[int] = Field(
        default=None, alias="IsRegistrationCodeItem"
    )
    is_sales_item: Optional[bool] = Field(default=None, alias="IsSalesItem")
    is_serial_item: Optional[bool] = Field(default=None, alias="IsSerialItem")
    is_stock_item: Optional[bool] = Field(default=None, alias="IsStockItem")
    is_subcontracted_item: Optional[bool] = Field(
        default=None, alias="IsSubcontractedItem"
    )
    is_taxable_item: Optional[int] = Field(default=None, alias="IsTaxableItem")
    is_time: Optional[int] = Field(default=None, alias="IsTime")
    is_webshop_item: Optional[int] = Field(default=None, alias="IsWebshopItem")
    item_group: Optional[UUID] = Field(default=None, alias="ItemGroup")
    item_group_code: Optional[str] = Field(default=None, alias="ItemGroupCode")
    item_group_description: Optional[str] = Field(
        default=None, alias="ItemGroupDescription"
    )
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    net_weight: Optional[float] = Field(default=None, alias="NetWeight")
    net_weight_unit: Optional[str] = Field(default=None, alias="NetWeightUnit")
    notes: Optional[str] = Field(default=None, alias="Notes")
    picture: Optional[bytes] = Field(default=None, alias="Picture")
    picture_name: Optional[str] = Field(default=None, alias="PictureName")
    picture_thumbnail_url: Optional[str] = Field(
        default=None, alias="PictureThumbnailUrl"
    )
    picture_url: Optional[str] = Field(default=None, alias="PictureUrl")
    sales_vat_code: Optional[str] = Field(default=None, alias="SalesVatCode")
    sales_vat_code_description: Optional[str] = Field(
        default=None, alias="SalesVatCodeDescription"
    )
    search_code: Optional[str] = Field(default=None, alias="SearchCode")
    security_level: Optional[int] = Field(default=None, alias="SecurityLevel")
    standard_sales_price: Optional[float] = Field(
        default=None, alias="StandardSalesPrice"
    )
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    statistical_code: Optional[str] = Field(default=None, alias="StatisticalCode")
    statistical_net_weight: Optional[float] = Field(
        default=None, alias="StatisticalNetWeight"
    )
    statistical_units: Optional[float] = Field(default=None, alias="StatisticalUnits")
    statistical_value: Optional[float] = Field(default=None, alias="StatisticalValue")
    stock: Optional[float] = Field(default=None, alias="Stock")
    unit: Optional[str] = Field(default=None, alias="Unit")
    unit_description: Optional[str] = Field(default=None, alias="UnitDescription")
    unit_type: Optional[str] = Field(default=None, alias="UnitType")
    use_explosion: Optional[int] = Field(default=None, alias="UseExplosion")
