from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel


class Opportunity(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: Optional[UUID] = Field(default=None, alias="Account")
    accountant: Optional[UUID] = Field(default=None, alias="Accountant")
    accountant_code: Optional[str] = Field(default=None, alias="AccountantCode")
    accountant_name: Optional[str] = Field(default=None, alias="AccountantName")
    account_code: Optional[str] = Field(default=None, alias="AccountCode")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    action_date: Optional[datetime] = Field(default=None, alias="ActionDate")
    amount_dc: Optional[float] = Field(default=None, alias="AmountDC")
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    campaign: Optional[UUID] = Field(default=None, alias="Campaign")
    campaign_description: Optional[str] = Field(
        default=None, alias="CampaignDescription"
    )
    channel: Optional[int] = Field(default=None, alias="Channel")
    channel_description: Optional[str] = Field(default=None, alias="ChannelDescription")
    close_date: Optional[datetime] = Field(default=None, alias="CloseDate")
    contact: Optional[UUID] = Field(default=None, alias="Contact")
    contact_full_name: Optional[str] = Field(default=None, alias="ContactFullName")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    custom_field: Optional[str] = Field(default=None, alias="CustomField")
    division: Optional[int] = Field(default=None, alias="Division")
    lead_source: Optional[UUID] = Field(default=None, alias="LeadSource")
    lead_source_description: Optional[str] = Field(
        default=None, alias="LeadSourceDescription"
    )
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    name: Optional[str] = Field(default=None, alias="Name")
    next_action: Optional[str] = Field(default=None, alias="NextAction")
    notes: Optional[str] = Field(default=None, alias="Notes")
    number: Optional[int] = Field(default=None, alias="Number")
    opportunity_department_code: Optional[int] = Field(
        default=None, alias="OpportunityDepartmentCode"
    )
    opportunity_department_description: Optional[str] = Field(
        default=None, alias="OpportunityDepartmentDescription"
    )
    opportunity_stage: Optional[UUID] = Field(default=None, alias="OpportunityStage")
    opportunity_stage_description: Optional[str] = Field(
        default=None, alias="OpportunityStageDescription"
    )
    opportunity_status: Optional[int] = Field(default=None, alias="OpportunityStatus")
    opportunity_type: Optional[int] = Field(default=None, alias="OpportunityType")
    opportunity_type_description: Optional[str] = Field(
        default=None, alias="OpportunityTypeDescription"
    )
    owner: Optional[UUID] = Field(default=None, alias="Owner")
    owner_full_name: Optional[str] = Field(default=None, alias="OwnerFullName")
    probability: Optional[float] = Field(default=None, alias="Probability")
    project: Optional[UUID] = Field(default=None, alias="Project")
    project_code: Optional[str] = Field(default=None, alias="ProjectCode")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    rate_fc: Optional[float] = Field(default=None, alias="RateFC")
    reason_code: Optional[UUID] = Field(default=None, alias="ReasonCode")
    reason_code_description: Optional[str] = Field(
        default=None, alias="ReasonCodeDescription"
    )
    reseller: Optional[UUID] = Field(default=None, alias="Reseller")
    reseller_code: Optional[str] = Field(default=None, alias="ResellerCode")
    reseller_name: Optional[str] = Field(default=None, alias="ResellerName")
    sales_type: Optional[UUID] = Field(default=None, alias="SalesType")
    sales_type_description: Optional[str] = Field(
        default=None, alias="SalesTypeDescription"
    )
