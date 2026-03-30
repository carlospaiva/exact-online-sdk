from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Receivable(StrictModel):
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_bank_account_id: Optional[UUID] = Field(None, alias="AccountBankAccountID")
    account_bank_account_number: Optional[str] = Field(
        None, alias="AccountBankAccountNumber"
    )
    account_code: Optional[str] = Field(None, alias="AccountCode")
    account_contact: Optional[UUID] = Field(None, alias="AccountContact")
    account_contact_name: Optional[str] = Field(None, alias="AccountContactName")
    account_country: Optional[str] = Field(None, alias="AccountCountry")
    account_name: Optional[str] = Field(None, alias="AccountName")
    amount_dc: Optional[float] = Field(None, alias="AmountDC")
    amount_discount_dc: Optional[float] = Field(None, alias="AmountDiscountDC")
    amount_discount_fc: Optional[float] = Field(None, alias="AmountDiscountFC")
    amount_fc: Optional[float] = Field(None, alias="AmountFC")
    bank_account_id: Optional[UUID] = Field(None, alias="BankAccountID")
    bank_account_number: Optional[str] = Field(None, alias="BankAccountNumber")
    cashflow_transaction_batch_code: Optional[str] = Field(
        None, alias="CashflowTransactionBatchCode"
    )
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    description: Optional[str] = Field(None, alias="Description")
    direct_debit_mandate: Optional[UUID] = Field(None, alias="DirectDebitMandate")
    direct_debit_mandate_description: Optional[str] = Field(
        None, alias="DirectDebitMandateDescription"
    )
    direct_debit_mandate_payment_type: Optional[int] = Field(
        None, alias="DirectDebitMandatePaymentType"
    )
    direct_debit_mandate_reference: Optional[str] = Field(
        None, alias="DirectDebitMandateReference"
    )
    direct_debit_mandate_type: Optional[int] = Field(
        None, alias="DirectDebitMandateType"
    )
    discount_due_date: Optional[datetime] = Field(None, alias="DiscountDueDate")
    division: Optional[int] = Field(None, alias="Division")
    document: Optional[UUID] = Field(None, alias="Document")
    document_number: Optional[int] = Field(None, alias="DocumentNumber")
    document_subject: Optional[str] = Field(None, alias="DocumentSubject")
    due_date: Optional[datetime] = Field(None, alias="DueDate")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    end_period: Optional[int] = Field(None, alias="EndPeriod")
    end_to_end_id: Optional[str] = Field(None, alias="EndToEndID")
    end_year: Optional[int] = Field(None, alias="EndYear")
    entry_date: Optional[datetime] = Field(None, alias="EntryDate")
    entry_id: Optional[UUID] = Field(None, alias="EntryID")
    entry_number: Optional[int] = Field(None, alias="EntryNumber")
    gl_account: Optional[UUID] = Field(None, alias="GLAccount")
    gl_account_code: Optional[str] = Field(None, alias="GLAccountCode")
    gl_account_description: Optional[str] = Field(None, alias="GLAccountDescription")
    invoice_date: Optional[datetime] = Field(None, alias="InvoiceDate")
    invoice_number: Optional[int] = Field(None, alias="InvoiceNumber")
    is_batch_booking: Optional[int] = Field(None, alias="IsBatchBooking")
    is_fully_paid: Optional[bool] = Field(None, alias="IsFullyPaid")
    journal: Optional[str] = Field(None, alias="Journal")
    journal_description: Optional[str] = Field(None, alias="JournalDescription")
    last_payment_date: Optional[datetime] = Field(None, alias="LastPaymentDate")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    order_number: Optional[int] = Field(None, alias="OrderNumber")
    payment_condition: Optional[str] = Field(None, alias="PaymentCondition")
    payment_condition_description: Optional[str] = Field(
        None, alias="PaymentConditionDescription"
    )
    payment_days: Optional[int] = Field(None, alias="PaymentDays")
    payment_days_discount: Optional[int] = Field(None, alias="PaymentDaysDiscount")
    payment_discount_percentage: Optional[float] = Field(
        None, alias="PaymentDiscountPercentage"
    )
    payment_information_id: Optional[str] = Field(None, alias="PaymentInformationID")
    payment_method: Optional[str] = Field(None, alias="PaymentMethod")
    payment_reference: Optional[str] = Field(None, alias="PaymentReference")
    rate_fc: Optional[float] = Field(None, alias="RateFC")
    receivable_batch_number: Optional[int] = Field(None, alias="ReceivableBatchNumber")
    receivable_selected: Optional[datetime] = Field(None, alias="ReceivableSelected")
    receivable_selector: Optional[UUID] = Field(None, alias="ReceivableSelector")
    receivable_selector_full_name: Optional[str] = Field(
        None, alias="ReceivableSelectorFullName"
    )
    source: Optional[int] = Field(None, alias="Source")
    status: Optional[int] = Field(None, alias="Status")
    transaction_amount_dc: Optional[float] = Field(None, alias="TransactionAmountDC")
    transaction_amount_fc: Optional[float] = Field(None, alias="TransactionAmountFC")
    transaction_due_date: Optional[datetime] = Field(None, alias="TransactionDueDate")
    transaction_entry_id: Optional[UUID] = Field(None, alias="TransactionEntryID")
    transaction_id: Optional[UUID] = Field(None, alias="TransactionID")
    transaction_is_reversal: Optional[bool] = Field(None, alias="TransactionIsReversal")
    transaction_reporting_period: Optional[int] = Field(
        None, alias="TransactionReportingPeriod"
    )
    transaction_reporting_year: Optional[int] = Field(
        None, alias="TransactionReportingYear"
    )
    transaction_status: Optional[int] = Field(None, alias="TransactionStatus")
    transaction_type: Optional[int] = Field(None, alias="TransactionType")
    your_ref: Optional[str] = Field(None, alias="YourRef")
