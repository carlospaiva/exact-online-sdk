from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Subscription(StrictModel):
    id: Optional[UUID] = Field(None, alias="EntryID")
    blocked: Optional[bool] = Field(None, alias="Blocked")
    cancellation_date: Optional[datetime] = Field(None, alias="CancellationDate")
    classification: Optional[UUID] = Field(None, alias="Classification")
    classification_code: Optional[str] = Field(None, alias="ClassificationCode")
    classification_description: Optional[str] = Field(
        None, alias="ClassificationDescription"
    )
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    description: Optional[str] = Field(None, alias="Description")
    division: Optional[int] = Field(None, alias="Division")
    end_date: Optional[datetime] = Field(None, alias="EndDate")
    invoiced_to: Optional[datetime] = Field(None, alias="InvoicedTo")
    invoicing_start_date: Optional[datetime] = Field(None, alias="InvoicingStartDate")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    number: Optional[int] = Field(None, alias="Number")
    order_date: Optional[datetime] = Field(None, alias="OrderDate")
    payable_by: Optional[UUID] = Field(None, alias="PayableBy")
    payable_by_account_code: Optional[str] = Field(None, alias="PayableByAccountCode")
    payable_by_account_name: Optional[str] = Field(None, alias="PayableByAccountName")
    payment_condition: Optional[str] = Field(None, alias="PaymentCondition")
    payment_condition_description: Optional[str] = Field(
        None, alias="PaymentConditionDescription"
    )
    printed: Optional[bool] = Field(None, alias="Printed")
    reason_cancelled: Optional[UUID] = Field(None, alias="ReasonCancelled")
    reason_cancelled_code: Optional[str] = Field(None, alias="ReasonCancelledCode")
    reason_cancelled_reason_code: Optional[str] = Field(
        None, alias="ReasonCancelledReasonCode"
    )
    start_date: Optional[datetime] = Field(None, alias="StartDate")
    subscription_lines: Optional[list] = Field(  # type: ignore[type-arg]
        None, alias="SubscriptionLines"
    )
    subscription_type: Optional[UUID] = Field(None, alias="SubscriptionType")
    subscription_type_code: Optional[str] = Field(None, alias="SubscriptionTypeCode")
    subscription_type_description: Optional[str] = Field(
        None, alias="SubscriptionTypeDescription"
    )
