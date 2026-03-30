from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Employee(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    accountant: Optional[UUID] = Field(None, alias="Accountant")
    active_employment: Optional[int] = Field(None, alias="ActiveEmployment")
    address: Optional[UUID] = Field(None, alias="Address")
    address_line2: Optional[str] = Field(None, alias="AddressLine2")
    address_line3: Optional[str] = Field(None, alias="AddressLine3")
    address_street: Optional[str] = Field(None, alias="AddressStreet")
    address_street_number: Optional[str] = Field(None, alias="AddressStreetNumber")
    address_street_number_suffix: Optional[str] = Field(
        None, alias="AddressStreetNumberSuffix"
    )
    birth_date: Optional[datetime] = Field(None, alias="BirthDate")
    birth_name: Optional[str] = Field(None, alias="BirthName")
    birth_name_prefix: Optional[str] = Field(None, alias="BirthNamePrefix")
    birth_place: Optional[str] = Field(None, alias="BirthPlace")
    business_email: Optional[str] = Field(None, alias="BusinessEmail")
    business_fax: Optional[str] = Field(None, alias="BusinessFax")
    business_mobile: Optional[str] = Field(None, alias="BusinessMobile")
    business_phone: Optional[str] = Field(None, alias="BusinessPhone")
    business_phone_extension: Optional[str] = Field(
        None, alias="BusinessPhoneExtension"
    )
    city: Optional[str] = Field(None, alias="City")
    code: Optional[str] = Field(None, alias="Code")
    country: Optional[str] = Field(None, alias="Country")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    customer: Optional[UUID] = Field(None, alias="Customer")
    division: Optional[int] = Field(None, alias="Division")
    email: Optional[str] = Field(None, alias="Email")
    employee_hid: Optional[int] = Field(None, alias="EmployeeHID")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    first_name: Optional[str] = Field(None, alias="FirstName")
    full_name: Optional[str] = Field(None, alias="FullName")
    gender: Optional[str] = Field(None, alias="Gender")
    hid: Optional[int] = Field(None, alias="HID")
    initials: Optional[str] = Field(None, alias="Initials")
    is_active: Optional[int] = Field(None, alias="IsActive")
    language: Optional[str] = Field(None, alias="Language")
    last_name: Optional[str] = Field(None, alias="LastName")
    location_description: Optional[str] = Field(None, alias="LocationDescription")
    manager: Optional[UUID] = Field(None, alias="Manager")
    marital_date: Optional[datetime] = Field(None, alias="MaritalDate")
    marital_status: Optional[int] = Field(None, alias="MaritalStatus")
    middle_name: Optional[str] = Field(None, alias="MiddleName")
    mobile: Optional[str] = Field(None, alias="Mobile")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    municipality: Optional[str] = Field(None, alias="Municipality")
    nationality: Optional[str] = Field(None, alias="Nationality")
    nick_name: Optional[str] = Field(None, alias="NickName")
    notes: Optional[str] = Field(None, alias="Notes")
    partner_name: Optional[str] = Field(None, alias="PartnerName")
    partner_name_prefix: Optional[str] = Field(None, alias="PartnerNamePrefix")
    person: Optional[UUID] = Field(None, alias="Person")
    phone: Optional[str] = Field(None, alias="Phone")
    phone_extension: Optional[str] = Field(None, alias="PhoneExtension")
    picture_file_name: Optional[str] = Field(None, alias="PictureFileName")
    picture_url: Optional[str] = Field(None, alias="PictureUrl")
    postcode: Optional[str] = Field(None, alias="Postcode")
    private_email: Optional[str] = Field(None, alias="PrivateEmail")
    social_security_number: Optional[str] = Field(None, alias="SocialSecurityNumber")
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    state: Optional[str] = Field(None, alias="State")
    title: Optional[str] = Field(None, alias="Title")
    user: Optional[UUID] = Field(None, alias="User")
    user_full_name: Optional[str] = Field(None, alias="UserFullName")
