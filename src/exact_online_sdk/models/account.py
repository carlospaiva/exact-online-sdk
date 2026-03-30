from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .account_status import AccountStatus
from .bank_account import BankAccount
from .base import StrictModel


class Account(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    accountant: Optional[UUID] = Field(default=None, alias="Accountant")
    account_manager: Optional[UUID] = Field(default=None, alias="AccountManager")
    account_manager_full_name: Optional[str] = Field(
        default=None, alias="AccountManagerFullName"
    )
    account_manager_hid: Optional[int] = Field(default=None, alias="AccountManagerHID")
    activity_sector: Optional[UUID] = Field(default=None, alias="ActivitySector")
    activity_sub_sector: Optional[UUID] = Field(default=None, alias="ActivitySubSector")
    address_line_1: Optional[str] = Field(default=None, alias="AddressLine1")
    address_line_2: Optional[str] = Field(default=None, alias="AddressLine2")
    address_line_3: Optional[str] = Field(default=None, alias="AddressLine3")
    address_source: Optional[int] = Field(default=None, alias="AddressSource")
    automatic_process_proposed_entry: Optional[int] = Field(
        default=None, alias="AutomaticProcessProposedEntry"
    )
    bank_accounts: Optional[list[BankAccount]] = Field(
        default=None, alias="BankAccounts"
    )
    blocked: Optional[bool] = Field(default=None, alias="Blocked")
    bsn: Optional[str] = Field(default=None, alias="BSN")
    brin: Optional[UUID] = Field(default=None, alias="BRIN")
    business_type: Optional[UUID] = Field(default=None, alias="BusinessType")
    can_drop_ship: Optional[bool] = Field(default=None, alias="CanDropShip")
    chamber_of_commerce: Optional[str] = Field(default=None, alias="ChamberOfCommerce")
    city: Optional[str] = Field(default=None, alias="City")
    classification1: Optional[UUID] = Field(default=None, alias="Classification1")
    classification2: Optional[UUID] = Field(default=None, alias="Classification2")
    classification3: Optional[UUID] = Field(default=None, alias="Classification3")
    classification4: Optional[UUID] = Field(default=None, alias="Classification4")
    classification5: Optional[UUID] = Field(default=None, alias="Classification5")
    classification6: Optional[UUID] = Field(default=None, alias="Classification6")
    classification7: Optional[UUID] = Field(default=None, alias="Classification7")
    classification8: Optional[UUID] = Field(default=None, alias="Classification8")
    classification_description: Optional[str] = Field(
        default=None, alias="ClassificationDescription"
    )
    code: Optional[str] = None
    code_at_supplier: Optional[str] = Field(default=None, alias="CodeAtSupplier")
    company_size: Optional[UUID] = Field(default=None, alias="CompanySize")
    consolidation_scenario: Optional[int] = Field(
        default=None, alias="ConsolidationScenario"
    )
    controlled_date: Optional[datetime] = Field(default=None, alias="ControlledDate")
    costcenter: Optional[str] = None
    costcenter_description: Optional[str] = Field(
        default=None, alias="CostcenterDescription"
    )
    cost_paid: Optional[int] = Field(default=None, alias="CostPaid")
    country: Optional[str] = Field(default=None, alias="Country")
    country_name: Optional[str] = Field(default=None, alias="CountryName")
    name: str
    email: Optional[str] = None
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    credit_line_purchase: Optional[float] = Field(
        default=None, alias="CreditLinePurchase"
    )
    credit_line_sales: Optional[float] = Field(default=None, alias="CreditLineSales")
    currency: Optional[str] = None
    customer_since: Optional[datetime] = Field(default=None, alias="CustomerSince")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    datev_creditor_code: Optional[str] = Field(default=None, alias="DatevCreditorCode")
    datev_debtor_code: Optional[str] = Field(default=None, alias="DatevDebtorCode")
    delivery_advice: Optional[int] = Field(default=None, alias="DeliveryAdvice")
    discount_purchase: Optional[float] = Field(default=None, alias="DiscountPurchase")
    discount_sales: Optional[float] = Field(default=None, alias="DiscountSales")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    division: Optional[int] = Field(default=None, alias="Division")
    document: Optional[UUID] = Field(default=None, alias="Document")
    duns_number: Optional[str] = Field(default=None, alias="DunsNumber")
    enable_sales_payment_link: Optional[bool] = Field(
        default=None, alias="EnableSalesPaymentLink"
    )
    end_date: Optional[datetime] = Field(default=None, alias="EndDate")
    eori_number: Optional[str] = Field(default=None, alias="EORINumber")
    established_date: Optional[datetime] = Field(default=None, alias="EstablishedDate")
    fax: Optional[str] = Field(default=None, alias="Fax")
    gl_account_purchase: Optional[UUID] = Field(default=None, alias="GLAccountPurchase")
    gl_account_sales: Optional[UUID] = Field(default=None, alias="GLAccountSales")
    gl_ar: Optional[UUID] = Field(default=None, alias="GLAR")
    gl_ap: Optional[UUID] = Field(default=None, alias="GLAP")
    gln_number: Optional[str] = Field(default=None, alias="GlnNumber")
    has_withholding_tax_sales: Optional[bool] = Field(
        default=None, alias="HasWithholdingTaxSales"
    )
    ignore_datev_warning_message: Optional[bool] = Field(
        default=None, alias="IgnoreDatevWarningMessage"
    )
    incoterm_address_purchase: Optional[str] = Field(
        default=None, alias="IncotermAddressPurchase"
    )
    incoterm_address_sales: Optional[str] = Field(
        default=None, alias="IncotermAddressSales"
    )
    incoterm_code_purchase: Optional[str] = Field(
        default=None, alias="IncotermCodePurchase"
    )
    incoterm_code_sales: Optional[str] = Field(default=None, alias="IncotermCodeSales")
    incoterm_version_purchase: Optional[int] = Field(
        default=None, alias="IncotermVersionPurchase"
    )
    incoterm_version_sales: Optional[int] = Field(
        default=None, alias="IncotermVersionSales"
    )
    intrastat_area: Optional[str] = Field(default=None, alias="IntraStatArea")
    intrastat_delivery_term: Optional[str] = Field(
        default=None, alias="IntraStatDeliveryTerm"
    )
    intrastat_system: Optional[str] = Field(default=None, alias="IntraStatSystem")
    intrastat_transaction_a: Optional[str] = Field(
        default=None, alias="IntraStatTransactionA"
    )
    intrastat_transaction_b: Optional[str] = Field(
        default=None, alias="IntraStatTransactionB"
    )
    intrastat_transport_method: Optional[str] = Field(
        default=None, alias="IntraStatTransportMethod"
    )
    invoice_account: Optional[UUID] = Field(default=None, alias="InvoiceAccount")
    invoice_account_code: Optional[str] = Field(
        default=None, alias="InvoiceAccountCode"
    )
    invoice_account_name: Optional[str] = Field(
        default=None, alias="InvoiceAccountName"
    )
    invoice_attachment_type: Optional[int] = Field(
        default=None, alias="InvoiceAttachmentType"
    )
    invoicing_method: Optional[int] = Field(default=None, alias="InvoicingMethod")
    is_accountant: Optional[int] = Field(default=None, alias="IsAccountant")
    is_agency: Optional[int] = Field(default=None, alias="IsAgency")
    is_anonymised: Optional[int] = Field(default=None, alias="IsAnonymised")
    is_competitor: Optional[int] = Field(default=None, alias="IsCompetitor")
    is_extra_duty: Optional[bool] = Field(default=None, alias="IsExtraDuty")
    is_mailing: Optional[int] = Field(default=None, alias="IsMailing")
    is_pilot: Optional[bool] = Field(default=None, alias="IsPilot")
    is_reseller: Optional[bool] = Field(default=None, alias="IsReseller")
    is_sales: Optional[bool] = Field(default=None, alias="IsSales")
    is_supplier: Optional[bool] = Field(default=None, alias="IsSupplier")
    language: Optional[str] = Field(default=None, alias="Language")
    language_description: Optional[str] = Field(
        default=None, alias="LanguageDescription"
    )
    latitude: Optional[float] = Field(default=None, alias="Latitude")
    lead_purpose: Optional[UUID] = Field(default=None, alias="LeadPurpose")
    lead_source: Optional[UUID] = Field(default=None, alias="LeadSource")
    is_bank: Optional[bool] = Field(default=None, alias="IsBank")
    is_member: Optional[bool] = Field(default=None, alias="IsMember")
    is_purchase: Optional[bool] = Field(default=None, alias="IsPurchase")
    logo: Optional[bytes] = Field(default=None, alias="Logo")
    logo_file_name: Optional[str] = Field(default=None, alias="LogoFileName")
    logo_thumbnail_url: Optional[str] = Field(default=None, alias="LogoThumbnailUrl")
    logo_url: Optional[str] = Field(default=None, alias="LogoUrl")
    longitude: Optional[float] = Field(default=None, alias="Longitude")
    main_contact: Optional[UUID] = Field(default=None, alias="MainContact")
    oin_number: Optional[str] = Field(default=None, alias="OINNumber")
    parent: Optional[UUID] = Field(default=None, alias="Parent")
    pay_as_you_earn: Optional[str] = Field(default=None, alias="PayAsYouEarn")
    payment_condition_purchase: Optional[str] = Field(
        default=None, alias="PaymentConditionPurchase"
    )
    payment_condition_purchase_description: Optional[str] = Field(
        default=None, alias="PaymentConditionPurchaseDescription"
    )
    payment_condition_sales: Optional[str] = Field(
        default=None, alias="PaymentConditionSales"
    )
    payment_condition_sales_description: Optional[str] = Field(
        default=None, alias="PaymentConditionSalesDescription"
    )
    peppol_identifier: Optional[str] = Field(default=None, alias="PeppolIdentifier")
    peppol_identifier_type: Optional[int] = Field(
        default=None, alias="PeppolIdentifierType"
    )
    phone: Optional[str] = Field(default=None, alias="Phone")
    phone_extension: Optional[str] = Field(default=None, alias="PhoneExtension")
    postcode: Optional[str] = Field(default=None, alias="Postcode")
    pricelist: Optional[UUID] = Field(default=None, alias="PriceList")
    purchase_currency: Optional[str] = Field(default=None, alias="PurchaseCurrency")
    purchase_currency_description: Optional[str] = Field(
        default=None, alias="PurchaseCurrencyDescription"
    )
    purchase_lead_days: Optional[int] = Field(default=None, alias="PurchaseLeadDays")
    purchase_vat_code: Optional[str] = Field(default=None, alias="PurchaseVATCode")
    purchase_vat_code_description: Optional[str] = Field(
        default=None, alias="PurchaseVATCodeDescription"
    )
    recepient_of_commissions: Optional[bool] = Field(
        default=None, alias="RecepientOfCommissions"
    )
    remarks: Optional[str] = Field(default=None, alias="Remarks")
    reseller: Optional[UUID] = Field(default=None, alias="Reseller")
    reseller_code: Optional[str] = Field(default=None, alias="ResellerCode")
    reseller_name: Optional[str] = Field(default=None, alias="ResellerName")
    rsin: Optional[str] = Field(default=None, alias="RSIN")
    sales_currency: Optional[str] = Field(default=None, alias="SalesCurrency")
    sales_currency_description: Optional[str] = Field(
        default=None, alias="SalesCurrencyDescription"
    )
    sales_tax_schedule: Optional[UUID] = Field(default=None, alias="SalesTaxSchedule")
    sales_tax_schedule_code: Optional[str] = Field(
        default=None, alias="SalesTaxScheduleCode"
    )
    sales_tax_schedule_description: Optional[str] = Field(
        default=None, alias="SalesTaxScheduleDescription"
    )
    sales_vat_code: Optional[str] = Field(default=None, alias="SalesVATCode")
    sales_vat_code_description: Optional[str] = Field(
        default=None, alias="SalesVATCodeDescription"
    )
    search_code: Optional[str] = Field(default=None, alias="SearchCode")
    security_level: Optional[int] = Field(default=None, alias="SecurityLevel")
    separate_inv_per_project: Optional[int] = Field(
        default=None, alias="SeparateInvPerProject"
    )
    separate_inv_per_subscription: Optional[int] = Field(
        default=None, alias="SeparateInvPerSubscription"
    )
    shipping_lead_days: Optional[int] = Field(default=None, alias="ShippingLeadDays")
    shipping_method: Optional[UUID] = Field(default=None, alias="ShippingMethod")
    show_remark_for_sales: Optional[bool] = Field(
        default=None, alias="ShowRemarkForSales"
    )
    source: Optional[int] = Field(default=None, alias="Source")
    start_date: Optional[datetime] = Field(default=None, alias="StartDate")
    state: Optional[str] = Field(default=None, alias="State")
    state_name: Optional[str] = Field(default=None, alias="StateName")
    status: Optional[AccountStatus] = Field(default=None, alias="Status")
    status_since: Optional[datetime] = Field(default=None, alias="StatusSince")
    trade_name: Optional[str] = Field(default=None, alias="TradeName")
    type: Optional[str] = Field(default=None, alias="Type")
    unique_taxpayer_reference: Optional[str] = Field(
        default=None, alias="UniqueTaxpayerReference"
    )
    vat_liability: Optional[str] = Field(default=None, alias="VATLiability")
    vat_number: Optional[str] = Field(default=None, alias="VATNumber")
    website: Optional[str] = Field(default=None, alias="Website")
