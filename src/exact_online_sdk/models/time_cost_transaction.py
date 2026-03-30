from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class TimeCostTransaction(StrictModel):
    timestamp: Optional[int] = Field(None, alias="Timestamp")
    id: Optional[UUID] = Field(None, alias="ID")
    account: Optional[UUID] = Field(None, alias="Account")
    account_name: Optional[str] = Field(None, alias="AccountName")
    amount_fc: Optional[float] = Field(None, alias="AmountFC")
    attachment: Optional[UUID] = Field(None, alias="Attachment")
    created: Optional[datetime] = Field(None, alias="Created")
    creator: Optional[UUID] = Field(None, alias="Creator")
    creator_full_name: Optional[str] = Field(None, alias="CreatorFullName")
    currency: Optional[str] = Field(None, alias="Currency")
    custom_field: Optional[str] = Field(None, alias="CustomField")
    date: Optional[datetime] = Field(None, alias="Date")
    division: Optional[int] = Field(None, alias="Division")
    employee: Optional[UUID] = Field(None, alias="Employee")
    end_time: Optional[datetime] = Field(None, alias="EndTime")
    entry_number: Optional[int] = Field(None, alias="EntryNumber")
    error_text: Optional[str] = Field(None, alias="ErrorText")
    hour_status: Optional[int] = Field(None, alias="HourStatus")
    item: Optional[UUID] = Field(None, alias="Item")
    item_code: Optional[str] = Field(None, alias="ItemCode")
    item_description: Optional[str] = Field(None, alias="ItemDescription")
    item_divisable: Optional[bool] = Field(None, alias="ItemDivisable")
    modified: Optional[datetime] = Field(None, alias="Modified")
    modifier: Optional[UUID] = Field(None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(None, alias="ModifierFullName")
    notes: Optional[str] = Field(None, alias="Notes")
    price_fc: Optional[float] = Field(None, alias="PriceFC")
    project: Optional[UUID] = Field(None, alias="Project")
    project_account: Optional[UUID] = Field(None, alias="ProjectAccount")
    project_account_code: Optional[str] = Field(None, alias="ProjectAccountCode")
    project_account_name: Optional[str] = Field(None, alias="ProjectAccountName")
    project_code: Optional[str] = Field(None, alias="ProjectCode")
    project_description: Optional[str] = Field(None, alias="ProjectDescription")
    quantity: Optional[float] = Field(None, alias="Quantity")
    skip_validation: Optional[bool] = Field(None, alias="SkipValidation")
    start_time: Optional[datetime] = Field(None, alias="StartTime")
    subscription: Optional[UUID] = Field(None, alias="Subscription")
    subscription_account: Optional[UUID] = Field(None, alias="SubscriptionAccount")
    subscription_account_code: Optional[str] = Field(
        None, alias="SubscriptionAccountCode"
    )
    subscription_account_name: Optional[str] = Field(
        None, alias="SubscriptionAccountName"
    )
    subscription_description: Optional[str] = Field(
        None, alias="SubscriptionDescription"
    )
    subscription_number: Optional[int] = Field(None, alias="SubscriptionNumber")
    type: Optional[int] = Field(None, alias="Type")
