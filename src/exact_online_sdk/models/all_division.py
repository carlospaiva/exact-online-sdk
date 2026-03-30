from __future__ import annotations

from datetime import datetime
from typing import Any, Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class AllDivision(StrictModel):
    code: Optional[int] = Field(None, alias="Code")
    address_line1: Optional[str] = Field(None, alias="AddressLine1")
    address_line2: Optional[str] = Field(None, alias="AddressLine2")
    address_line3: Optional[str] = Field(None, alias="AddressLine3")
    archive_date: Optional[datetime] = Field(None, alias="ArchiveDate")
    blocking_status: Optional[int] = Field(None, alias="BlockingStatus")
    business_type_code: Optional[str] = Field(None, alias="BusinessTypeCode")
    business_type_description: Optional[str] = Field(
        None, alias="BusinessTypeDescription"
    )
    chamber_of_commerce_establishment: Optional[str] = Field(
        None, alias="ChamberOfCommerceEstablishment"
    )
    chamber_of_commerce_number: Optional[str] = Field(
        None, alias="ChamberOfCommerceNumber"
    )
    city: Optional[str] = Field(None, alias="City")
    class_01: Optional[Any] = Field(None, alias="Class_01")
    class_02: Optional[Any] = Field(None, alias="Class_02")
    class_03: Optional[Any] = Field(None, alias="Class_03")
    class_04: Optional[Any] = Field(None, alias="Class_04")
    class_05: Optional[Any] = Field(None, alias="Class_05")
    company_size_code: Optional[str] = Field(None, alias="CompanySizeCode")
    company_size_description: Optional[str] = Field(
        None, alias="CompanySizeDescription"
    )
    country: Optional[str] = Field(None, alias="Country")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    current: Optional[bool] = Field(None, alias="Current")
    customer: Optional[UUID] = Field(None, alias="Customer")
    customer_code: Optional[str] = Field(None, alias="CustomerCode")
    customer_name: Optional[str] = Field(None, alias="CustomerName")
    datev_accountant_number: Optional[str] = Field(None, alias="DatevAccountantNumber")
    datev_client_number: Optional[str] = Field(None, alias="DatevClientNumber")
    description: Optional[str] = Field(None, alias="Description")
    division_hr_link_unlink_date: Optional[datetime] = Field(
        None, alias="DivisionHRLinkUnlinkDate"
    )
    division_move_date: Optional[datetime] = Field(None, alias="DivisionMoveDate")
    email: Optional[str] = Field(None, alias="Email")
    fax: Optional[str] = Field(None, alias="Fax")
    hid: Optional[int] = Field(None, alias="Hid")
    is_dossier_division: Optional[bool] = Field(None, alias="IsDossierDivision")
    is_hr_division: Optional[bool] = Field(None, alias="IsHRDivision")
    is_main_division: Optional[bool] = Field(None, alias="IsMainDivision")
    is_practice_division: Optional[bool] = Field(None, alias="IsPracticeDivision")
    legislation: Optional[str] = Field(None, alias="Legislation")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    ob_number: Optional[str] = Field(None, alias="OBNumber")
    phone: Optional[str] = Field(None, alias="Phone")
    postcode: Optional[str] = Field(None, alias="Postcode")
    sbi_code: Optional[str] = Field(None, alias="SbiCode")
    sbi_description: Optional[str] = Field(None, alias="SbiDescription")
    sector_code: Optional[str] = Field(None, alias="SectorCode")
    sector_description: Optional[str] = Field(None, alias="SectorDescription")
    share_capital: Optional[float] = Field(None, alias="ShareCapital")
    siret_number: Optional[str] = Field(None, alias="SiretNumber")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    state: Optional[str] = Field(None, alias="State")
    status: Optional[int] = Field(None, alias="Status")
    subsector_code: Optional[str] = Field(None, alias="SubsectorCode")
    subsector_description: Optional[str] = Field(None, alias="SubsectorDescription")
    tax_office_number: Optional[str] = Field(None, alias="TaxOfficeNumber")
    tax_reference_number: Optional[str] = Field(None, alias="TaxReferenceNumber")
    template_code: Optional[str] = Field(None, alias="TemplateCode")
    vat_number: Optional[str] = Field(None, alias="VATNumber")
    website: Optional[str] = Field(None, alias="Website")
