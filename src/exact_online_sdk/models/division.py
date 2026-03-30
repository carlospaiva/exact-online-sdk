from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Division(StrictModel):
    code: Optional[int] = Field(None, alias="Code")
    archive_date: Optional[datetime] = Field(None, alias="ArchiveDate")
    blocking_status: Optional[int] = Field(None, alias="BlockingStatus")
    country: Optional[str] = Field(None, alias="Country")
    country_description: Optional[str] = Field(None, alias="CountryDescription")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    currency_description: Optional[str] = Field(None, alias="CurrencyDescription")
    customer: Optional[UUID] = Field(None, alias="Customer")
    customer_code: Optional[str] = Field(None, alias="CustomerCode")
    customer_name: Optional[str] = Field(None, alias="CustomerName")
    description: Optional[str] = Field(None, alias="Description")
    hid: Optional[int] = Field(None, alias="HID")
    main: Optional[bool] = Field(None, alias="Main")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    ob_number: Optional[str] = Field(None, alias="OBNumber")
    siret_number: Optional[str] = Field(None, alias="SiretNumber")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    status: Optional[int] = Field(None, alias="Status")
    tax_office_number: Optional[str] = Field(None, alias="TaxOfficeNumber")
    tax_reference_number: Optional[str] = Field(None, alias="TaxReferenceNumber")
    template_code: Optional[str] = Field(None, alias="TemplateCode")
    vat_number: Optional[str] = Field(None, alias="VATNumber")
    website: Optional[str] = Field(None, alias="Website")
