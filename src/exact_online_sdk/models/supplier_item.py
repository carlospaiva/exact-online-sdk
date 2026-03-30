from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class SupplierItem(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    barcode: Optional[str] = Field(default=None, alias="Barcode")
    copy_remarks: Optional[int] = Field(default=None, alias="CopyRemarks")
    country_of_origin: Optional[str] = Field(default=None, alias="CountryOfOrigin")
    country_of_origin_description: Optional[str] = Field(
        default=None, alias="CountryOfOriginDescription"
    )
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    currency_description: Optional[str] = Field(
        default=None, alias="CurrencyDescription"
    )
    division: Optional[int] = Field(default=None, alias="Division")
    drop_shipment: Optional[int] = Field(default=None, alias="DropShipment")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    item: UUID = Field(alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    item_unit: UUID = Field(alias="ItemUnit")
    item_unit_code: Optional[str] = Field(default=None, alias="ItemUnitCode")
    item_unit_description: Optional[str] = Field(
        default=None, alias="ItemUnitDescription"
    )
    main_supplier: Optional[bool] = Field(default=None, alias="MainSupplier")
    minimum_quantity: Optional[float] = Field(default=None, alias="MinimumQuantity")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    notes: Optional[str] = Field(default=None, alias="Notes")
    purchase_lead_time: Optional[int] = Field(default=None, alias="PurchaseLeadTime")
    purchase_lot_size: Optional[int] = Field(default=None, alias="PurchaseLotSize")
    purchase_price: float = Field(alias="PurchasePrice")
    purchase_unit: str = Field(alias="PurchaseUnit")
    purchase_unit_description: Optional[str] = Field(
        default=None, alias="PurchaseUnitDescription"
    )
    purchase_unit_factor: Optional[float] = Field(
        default=None, alias="PurchaseUnitFactor"
    )
    purchase_vat_code: Optional[str] = Field(default=None, alias="PurchaseVATCode")
    purchase_vat_code_description: Optional[str] = Field(
        default=None, alias="PurchaseVATCodeDescription"
    )
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    supplier: UUID = Field(alias="Supplier")
    supplier_code: Optional[str] = Field(default=None, alias="SupplierCode")
    supplier_description: Optional[str] = Field(
        default=None, alias="SupplierDescription"
    )
    supplier_item_code: Optional[str] = Field(default=None, alias="SupplierItemCode")
