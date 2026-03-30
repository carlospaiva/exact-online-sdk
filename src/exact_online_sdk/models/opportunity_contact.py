from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field, model_validator

from .base import StrictModel


class OpportunityContact(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: UUID = Field(alias="Account")
    account_is_customer: Optional[bool] = Field(default=None, alias="AccountIsCustomer")
    account_is_supplier: Optional[bool] = Field(default=None, alias="AccountIsSupplier")
    account_main_contact: Optional[UUID] = Field(
        default=None, alias="AccountMainContact"
    )
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    address_line_2: Optional[str] = Field(default=None, alias="AddressLine2")
    address_street: Optional[str] = Field(default=None, alias="AddressStreet")
    address_street_number: Optional[str] = Field(
        default=None, alias="AddressStreetNumber"
    )
    address_street_number_suffix: Optional[str] = Field(
        default=None, alias="AddressStreetNumberSuffix"
    )
    allow_mailing: Optional[int] = Field(default=None, alias="AllowMailing")
    birth_date: Optional[datetime] = Field(default=None, alias="BirthDate")
    birth_name: Optional[str] = Field(default=None, alias="BirthName")
    birth_name_prefix: Optional[str] = Field(default=None, alias="BirthNamePrefix")
    birth_place: Optional[str] = Field(default=None, alias="BirthPlace")
    business_email: Optional[str] = Field(default=None, alias="BusinessEmail")
    business_fax: Optional[str] = Field(default=None, alias="BusinessFax")
    business_mobile: Optional[str] = Field(default=None, alias="BusinessMobile")
    business_phone: Optional[str] = Field(default=None, alias="BusinessPhone")
    business_phone_extension: Optional[str] = Field(
        default=None, alias="BusinessPhoneExtension"
    )
    city: Optional[str] = Field(default=None, alias="City")
    code: Optional[str] = Field(default=None, alias="Code")
    contact: Optional[UUID] = Field(default=None, alias="Contact")
    country: Optional[str] = Field(default=None, alias="Country")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    division: Optional[int] = Field(default=None, alias="Division")
    email: Optional[str] = Field(default=None, alias="Email")
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    first_name: Optional[str] = Field(default=None, alias="FirstName")
    full_name: Optional[str] = Field(default=None, alias="FullName")
    gender: Optional[str] = Field(default=None, alias="Gender")
    hid: Optional[int] = Field(default=None, alias="HID")
    identification_date: Optional[datetime] = Field(
        default=None, alias="IdentificationDate"
    )
    identification_document: Optional[UUID] = Field(
        default=None, alias="IdentificationDocument"
    )
    identification_user: Optional[UUID] = Field(
        default=None, alias="IdentificationUser"
    )
    initials: Optional[str] = Field(default=None, alias="Initials")
    is_anonymised: Optional[int] = Field(default=None, alias="IsAnonymised")
    is_mailing_excluded: Optional[bool] = Field(default=None, alias="IsMailingExcluded")
    is_main_contact: Optional[bool] = Field(default=None, alias="IsMainContact")
    job_title_description: Optional[str] = Field(
        default=None, alias="JobTitleDescription"
    )
    language: Optional[str] = Field(default=None, alias="Language")
    last_name: Optional[str] = Field(default=None, alias="LastName")
    lead_purpose: Optional[UUID] = Field(default=None, alias="LeadPurpose")
    lead_source: Optional[UUID] = Field(default=None, alias="LeadSource")
    marketing_notes: Optional[str] = Field(default=None, alias="MarketingNotes")
    middle_name: Optional[str] = Field(default=None, alias="MiddleName")
    mobile: Optional[str] = Field(default=None, alias="Mobile")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    nationality: Optional[str] = Field(default=None, alias="Nationality")
    notes: Optional[str] = Field(default=None, alias="Notes")
    opportunity: Optional[UUID] = Field(default=None, alias="Opportunity")
    partner_name: Optional[str] = Field(default=None, alias="PartnerName")
    partner_name_prefix: Optional[str] = Field(default=None, alias="PartnerNamePrefix")
    person: Optional[UUID] = Field(default=None, alias="Person")
    phone: Optional[str] = Field(default=None, alias="Phone")
    phone_extension: Optional[str] = Field(default=None, alias="PhoneExtension")
    picture: Optional[bytes] = Field(default=None, alias="Picture")
    picture_name: Optional[str] = Field(default=None, alias="PictureName")
    picture_thumbnail_url: Optional[str] = Field(
        default=None, alias="PictureThumbnailUrl"
    )
    picture_url: Optional[str] = Field(default=None, alias="PictureUrl")
    postcode: Optional[str] = Field(default=None, alias="Postcode")
    social_security_number: Optional[str] = Field(
        default=None, alias="SocialSecurityNumber"
    )
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    state: Optional[str] = Field(default=None, alias="State")
    title: Optional[str] = Field(default=None, alias="Title")
    title_abbreviation: Optional[str] = Field(default=None, alias="TitleAbbreviation")
    title_description: Optional[str] = Field(default=None, alias="TitleDescription")

    @model_validator(mode="after")
    def _validate_name_components(self) -> "OpportunityContact":
        if not (self.first_name or self.last_name):
            msg = "Either `FirstName` or `LastName` must be provided."
            raise ValueError(msg)
        return self
