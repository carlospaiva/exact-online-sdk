from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Journal(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    allow_variable_currency: Optional[bool] = Field(None, alias="AllowVariableCurrency")
    allow_variable_exchange_rate: Optional[bool] = Field(
        None, alias="AllowVariableExchangeRate"
    )
    allow_vat: Optional[bool] = Field(None, alias="AllowVAT")
    auto_save: Optional[bool] = Field(None, alias="AutoSave")
    bank: Optional[UUID] = Field(None, alias="Bank")
    bank_account_bic_code: Optional[str] = Field(None, alias="BankAccountBICCode")
    bank_account_country: Optional[str] = Field(None, alias="BankAccountCountry")
    bank_account_description: Optional[str] = Field(
        None, alias="BankAccountDescription"
    )
    bank_account_iban: Optional[str] = Field(None, alias="BankAccountIBAN")
    bank_account_id: Optional[UUID] = Field(None, alias="BankAccountID")
    bank_account_including_mask: Optional[str] = Field(
        None, alias="BankAccountIncludingMask"
    )
    bank_account_use_sepa: Optional[bool] = Field(None, alias="BankAccountUseSEPA")
    bank_account_use_sepa_direct_debit: Optional[bool] = Field(
        None, alias="BankAccountUseSepaDirectDebit"
    )
    bank_name: Optional[str] = Field(None, alias="BankName")
    code: Optional[str] = Field(None, alias="Code")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    currency_description: Optional[str] = Field(None, alias="CurrencyDescription")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    gl_account_type: Optional[int] = Field(None, alias="GLAccountType")
    is_blocked: Optional[bool] = Field(None, alias="IsBlocked")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    payment_in_transit_account: Optional[UUID] = Field(
        None, alias="PaymentInTransitAccount"
    )
    payment_service_account_identifier: Optional[str] = Field(
        None, alias="PaymentServiceAccountIdentifier"
    )
    payment_service_provider: Optional[int] = Field(
        None, alias="PaymentServiceProvider"
    )
    payment_service_provider_name: Optional[str] = Field(
        None, alias="PaymentServiceProviderName"
    )
    type: Optional[int] = Field(None, alias="Type")
