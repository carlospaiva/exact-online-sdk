from __future__ import annotations

from datetime import datetime
from typing import Optional
from uuid import UUID

from pydantic import Field

from .base import StrictModel
from .document_attachment_info import DocumentAttachmentInfo


class Document(StrictModel):
    id: Optional[UUID] = Field(default=None, alias="ID")
    account: Optional[UUID] = Field(default=None, alias="Account")
    account_code: Optional[str] = Field(default=None, alias="AccountCode")
    account_name: Optional[str] = Field(default=None, alias="AccountName")
    amount_fc: Optional[float] = Field(default=None, alias="AmountFC")
    attachments: Optional[list[DocumentAttachmentInfo]] = Field(
        default=None, alias="Attachments"
    )
    body: Optional[str] = Field(default=None, alias="Body")
    category: Optional[UUID] = Field(default=None, alias="Category")
    category_description: Optional[str] = Field(
        default=None, alias="CategoryDescription"
    )
    contact: Optional[UUID] = Field(default=None, alias="Contact")
    contact_full_name: Optional[str] = Field(default=None, alias="ContactFullName")
    contract_id: Optional[UUID] = Field(default=None, alias="ContractID")
    contract_number: Optional[str] = Field(default=None, alias="ContractNumber")
    created: Optional[datetime] = Field(default=None, alias="Created")
    creator: Optional[UUID] = Field(default=None, alias="Creator")
    creator_full_name: Optional[str] = Field(default=None, alias="CreatorFullName")
    currency: Optional[str] = Field(default=None, alias="Currency")
    division: Optional[int] = Field(default=None, alias="Division")
    document_date: Optional[datetime] = Field(default=None, alias="DocumentDate")
    document_folder: Optional[UUID] = Field(default=None, alias="DocumentFolder")
    document_folder_code: Optional[str] = Field(
        default=None, alias="DocumentFolderCode"
    )
    document_folder_description: Optional[str] = Field(
        default=None, alias="DocumentFolderDescription"
    )
    document_view_url: Optional[str] = Field(default=None, alias="DocumentViewUrl")
    entry_status_description: Optional[str] = Field(
        default=None, alias="EntryStatusDescription"
    )
    expiry_date: Optional[datetime] = Field(default=None, alias="ExpiryDate")
    financial_transaction_entry_id: Optional[UUID] = Field(
        default=None, alias="FinancialTransactionEntryID"
    )
    has_empty_body: Optional[bool] = Field(default=None, alias="HasEmptyBody")
    hid: Optional[int] = Field(default=None, alias="HID")
    inherit_share: Optional[bool] = Field(default=None, alias="InheritShare")
    item: Optional[UUID] = Field(default=None, alias="Item")
    item_code: Optional[str] = Field(default=None, alias="ItemCode")
    item_description: Optional[str] = Field(default=None, alias="ItemDescription")
    language: Optional[str] = Field(default=None, alias="Language")
    modified: Optional[datetime] = Field(default=None, alias="Modified")
    modifier: Optional[UUID] = Field(default=None, alias="Modifier")
    modifier_full_name: Optional[str] = Field(default=None, alias="ModifierFullName")
    opportunity: Optional[UUID] = Field(default=None, alias="Opportunity")
    project: Optional[UUID] = Field(default=None, alias="Project")
    project_code: Optional[str] = Field(default=None, alias="ProjectCode")
    project_description: Optional[str] = Field(default=None, alias="ProjectDescription")
    proposed_entry_status: Optional[int] = Field(
        default=None, alias="ProposedEntryStatus"
    )
    purchase_invoice_number: Optional[int] = Field(
        default=None, alias="PurchaseInvoiceNumber"
    )
    purchase_order_number: Optional[int] = Field(
        default=None, alias="PurchaseOrderNumber"
    )
    sales_invoice_number: Optional[int] = Field(
        default=None, alias="SalesInvoiceNumber"
    )
    sales_order_number: Optional[int] = Field(default=None, alias="SalesOrderNumber")
    scan_service_status: Optional[int] = Field(default=None, alias="ScanServiceStatus")
    send_method: Optional[int] = Field(default=None, alias="SendMethod")
    share: Optional[int] = Field(default=None, alias="Share")
    share_point_connection_status: Optional[int] = Field(
        default=None, alias="SharePointConnectionStatus"
    )
    share_point_id: Optional[str] = Field(default=None, alias="SharePointID")
    shop_order_number: Optional[int] = Field(default=None, alias="ShopOrderNumber")
    source: Optional[int] = Field(default=None, alias="Source")
    source_description: Optional[str] = Field(default=None, alias="SourceDescription")
    subject: str = Field(alias="Subject")
    teams_meeting_id: Optional[str] = Field(default=None, alias="TeamsMeetingId")
    type: int = Field(alias="Type")
    type_description: Optional[str] = Field(default=None, alias="TypeDescription")
