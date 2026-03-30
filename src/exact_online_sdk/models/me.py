from __future__ import annotations

from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Me(StrictModel):
    user_id: Optional[UUID] = Field(None, alias="UserID")
    accounting_division: Optional[int] = Field(None, alias="AccountingDivision")
    current_division: Optional[int] = Field(None, alias="CurrentDivision")
    customer_code: Optional[str] = Field(None, alias="CustomerCode")
    division_customer: Optional[UUID] = Field(None, alias="DivisionCustomer")
    division_customer_code: Optional[str] = Field(None, alias="DivisionCustomerCode")
    division_customer_name: Optional[str] = Field(None, alias="DivisionCustomerName")
    division_customer_siret_number: Optional[str] = Field(
        None, alias="DivisionCustomerSiretNumber"
    )
    division_customer_vat_number: Optional[str] = Field(
        None, alias="DivisionCustomerVatNumber"
    )
    dossier_division: Optional[int] = Field(None, alias="DossierDivision")
    email: Optional[str] = Field(None, alias="Email")
    employee_id: Optional[UUID] = Field(None, alias="EmployeeID")
    first_name: Optional[str] = Field(None, alias="FirstName")
    full_name: Optional[str] = Field(None, alias="FullName")
    gender: Optional[str] = Field(None, alias="Gender")
    initials: Optional[str] = Field(None, alias="Initials")
    is_client_user: Optional[bool] = Field(None, alias="IsClientUser")
    is_employee_self_service_user: Optional[bool] = Field(
        None, alias="IsEmployeeSelfServiceUser"
    )
    is_my_firm_lite_user: Optional[bool] = Field(None, alias="IsMyFirmLiteUser")
    is_my_firm_portal_user: Optional[bool] = Field(None, alias="IsMyFirmPortalUser")
    is_oei_migration_mandatory: Optional[bool] = Field(
        None, alias="IsOEIMigrationMandatory"
    )
    is_starter_user: Optional[bool] = Field(None, alias="IsStarterUser")
    language: Optional[str] = Field(None, alias="Language")
    language_code: Optional[str] = Field(None, alias="LanguageCode")
    last_name: Optional[str] = Field(None, alias="LastName")
    legislation: Optional[int] = Field(None, alias="Legislation")
    middle_name: Optional[str] = Field(None, alias="MiddleName")
    mobile: Optional[str] = Field(None, alias="Mobile")
    nationality: Optional[str] = Field(None, alias="Nationality")
    package_code: Optional[str] = Field(None, alias="PackageCode")
    phone: Optional[str] = Field(None, alias="Phone")
    phone_extension: Optional[str] = Field(None, alias="PhoneExtension")
    picture_url: Optional[str] = Field(None, alias="PictureUrl")
    server_time: Optional[str] = Field(None, alias="ServerTime")
    server_utc_offset: Optional[float] = Field(None, alias="ServerUtcOffset")
    thumbnail_picture: Optional[str] = Field(None, alias="ThumbnailPicture")
    thumbnail_picture_format: Optional[str] = Field(
        None, alias="ThumbnailPictureFormat"
    )
    title: Optional[str] = Field(None, alias="Title")
    user_name: Optional[str] = Field(None, alias="UserName")
