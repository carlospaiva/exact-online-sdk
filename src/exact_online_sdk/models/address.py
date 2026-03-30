from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Address(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: Optional[UUID] = Field(default=None, alias="Account")
    account_is_supplier: Optional[bool] = Field(default=None, alias="AccountIsSupplier")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    address_line_1: Optional[str] = Field(default=None, alias="AddressLine1")
    address_line_2: Optional[str] = Field(default=None, alias="AddressLine2")
    address_line_3: Optional[str] = Field(default=None, alias="AddressLine3")
    city: Optional[str] = Field(default=None, alias="City")
    contact: Optional[UUID] = Field(default=None, alias="Contact")
    contact_name: Optional[str] = Field(default=None, alias="ContactName")
    country: Optional[str] = Field(default=None, alias="Country")
    country_name: Optional[str] = Field(default=None, alias="CountryName")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    fax: Optional[str] = Field(default=None, alias="Fax")
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
    free_text_field_01: Optional[str] = Field(default=None, alias="FreeTextField_01")
    free_text_field_02: Optional[str] = Field(default=None, alias="FreeTextField_02")
    free_text_field_03: Optional[str] = Field(default=None, alias="FreeTextField_03")
    free_text_field_04: Optional[str] = Field(default=None, alias="FreeTextField_04")
    free_text_field_05: Optional[str] = Field(default=None, alias="FreeTextField_05")
    mailbox: Optional[str] = Field(default=None, alias="Mailbox")
    main: Optional[bool] = Field(default=None, alias="Main")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    nic_number: Optional[str] = Field(default=None, alias="NicNumber")
    notes: Optional[str] = Field(default=None, alias="Notes")
    phone: Optional[str] = Field(default=None, alias="Phone")
    phone_extension: Optional[str] = Field(default=None, alias="PhoneExtension")
    postcode: Optional[str] = Field(default=None, alias="Postcode")
    state: Optional[str] = Field(default=None, alias="State")
    state_description: Optional[str] = Field(default=None, alias="StateDescription")
    type: Optional[int] = Field(default=None, alias="Type")
    warehouse: Optional[UUID] = Field(default=None, alias="Warehouse")
    warehouse_code: Optional[str] = Field(default=None, alias="WarehouseCode")
    warehouse_description: Optional[str] = Field(
        default=None, alias="WarehouseDescription"
    )
