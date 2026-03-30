from __future__ import annotations

from datetime import date, datetime
from typing import Any, Iterable, Iterator, List, Mapping, Optional
from uuid import UUID

from pydantic import ValidationError as PydanticValidationError

from ..client import ExactOnlineClient
from ..exceptions import ValidationError
from ..models import (
    AbsenceRegistration,
    AbsenceRegistrationTransaction,
    Account,
    AccountantInfo,
    AccountClass,
    AccountClassification,
    AccountClassificationName,
    AccountInvolvedAccount,
    AccountOwner,
    Address,
    AddressState,
    AllDivision,
    AllocationRule,
    AssemblyBillOfMaterialHeader,
    AssemblyBillOfMaterialMaterial,
    AssemblyOrder,
    Asset,
    AssetGroup,
    AvailableFeature,
    Bank,
    BankAccount,
    BankEntry,
    BankEntryLine,
    BatchNumber,
    BillOfMaterialMaterial,
    BillOfMaterialVersion,
    BlockedProjectPurchase,
    BlockedProjectSale,
    Budget,
    BudgetScenario,
    BulkCRMAccount,
    BulkCRMAddress,
    BulkCRMContact,
    BulkCRMQuotation,
    BulkCRMQuotationLine,
    BulkDocument,
    BulkDocumentAttachment,
    ByProduct,
    CashEntry,
    CashEntryLine,
    CommercialBuildingValue,
    CommunicationNote,
    Complaint,
    Contact,
    CostByDate,
    CostById,
    Costcenter,
    CostType,
    Costunit,
    Currency,
    CustomerItem,
    DeductibilityPercentage,
    Department,
    DepreciationMethod,
    DirectDebitMandate,
    Division,
    DivisionClass,
    DivisionClassName,
    DivisionClassValue,
    Document,
    DocumentAttachment,
    DocumentCategory,
    DocumentFolder,
    DocumentType,
    DocumentTypeCategory,
    DocumentTypeFolder,
    DropShipment,
    DropShipmentLine,
    Employee,
    Employment,
    EmploymentActiveEmployment,
    EmploymentCLA,
    EmploymentConditionGroup,
    EmploymentContract,
    EmploymentInternalRate,
    EmploymentOrganization,
    EmploymentOrganizationalUnit,
    EmploymentSalary,
    EmploymentStep,
    EmploymentTaxAuthoritiesGeneral,
    EmploymentTerm,
    EmploymentWorkingHour,
    Event,
    ExchangeRate,
    Expense,
    ExpenseReport,
    FinancialPeriod,
    GeneralJournalEntry,
    GeneralJournalEntryLine,
    GetMostRecentlyUsedDivision,
    GLAccount,
    GLAccountClassificationMapping,
    GLClassification,
    GLScheme,
    GLTransactionSource,
    GLTransactionType,
    GoodsDelivery,
    GoodsDeliveryLine,
    HourCostType,
    HoursByDate,
    HourType,
    HourTypeBudget,
    Incoterm,
    InventoryItemStorageLocation,
    InventoryItemWarehouse,
    InventorySerialBatchNumber,
    InventoryStockPosition,
    InventoryStockSerialBatchNumber,
    InventoryStorageLocationStockPosition,
    InvolvedUser,
    InvolvedUserRole,
    Item,
    ItemAssortment,
    ItemAssortmentProperty,
    ItemChargeRelation,
    ItemGroup,
    ItemMaterialsPlanning,
    ItemVersion,
    ItemWarehouse,
    ItemWarehousePlanningDetail,
    ItemWarehouseStorageLocation,
    JobGroup,
    JobTitle,
    Journal,
    Layout,
    LeadPurpose,
    LeadSource,
    LeaveAbsenceHoursByDay,
    LeaveBuildUpRegistration,
    LeaveRegistration,
    Mailbox,
    MailMessageAttachment,
    MailMessagesSent,
    MaterialIssue,
    MaterialReversal,
    Me,
    OfficialReturn,
    Operation,
    OperationResource,
    Opportunity,
    OpportunityContact,
    Payment,
    PaymentCondition,
    PlannedSalesReturn,
    PlannedSalesReturnLine,
    PlannedShopOrder,
    PlanningRelease,
    ProductionArea,
    ProductionOrder,
    Project,
    ProjectClassification,
    ProjectHourBudget,
    ProjectPlanning,
    ProjectPlanningRecurring,
    ProjectWBS,
    PurchaseItemPrice,
    PurchaseOrder,
    PurchaseOrderLine,
    Quotation,
    QuotationLine,
    QuotationOrderChargeLine,
    ReasonCode,
    ReasonCodesLinkType,
    Receivable,
    ReportingBalance,
    RequestAttachment,
    SalesInvoice,
    SalesInvoiceLine,
    SalesInvoiceOrderChargeLine,
    SalesItemPrice,
    SalesOrder,
    SalesOrderLine,
    SalesOrderOrderChargeLine,
    SalesPriceListVolumeDiscount,
    Schedule,
    ScheduleEntry,
    SelectionCode,
    ServiceRequest,
    ShopOrder,
    ShopOrderMaterialPlan,
    ShopOrderPurchasePlanning,
    ShopOrderRoutingStepPlan,
    ShopOrderSubOrder,
    SolutionLink,
    StockBatchNumber,
    StockCount,
    StockCountLine,
    StockSerialNumber,
    StorageLocation,
    SubOrderReversal,
    Subscription,
    SubscriptionLine,
    SubscriptionLineType,
    SubscriptionReasonCode,
    SubscriptionRestrictionEmployee,
    SubscriptionRestrictionItem,
    SubscriptionType,
    SupplierItem,
    Task,
    TaskType,
    TimeAndBillingEntryAccount,
    TimeCostTransaction,
    TransactionLine,
    Unit,
    UserRole,
    UserRolesPerDivision,
    VATCode,
    VatPercentage,
    Warehouse,
    WarehouseTransfer,
    WarehouseTransferLine,
    WebhookSubscription,
)
from ..models.base import StrictModel

FilterValue = Any


class BaseAPI:
    model_cls: type[StrictModel] | None = None
    _skip_division: bool = False

    def __init__(self, client: ExactOnlineClient) -> None:
        self.client = client

    def _resource(self) -> str:  # pragma: no cover - interface
        raise NotImplementedError

    def _get_resource_path(self) -> str:
        resource = self._resource()
        if self._skip_division:
            return f"!{resource}"
        return resource

    def list(
        self,
        *,
        params: Optional[dict[str, Any]] = None,
        filters: Optional[Mapping[str, FilterValue]] = None,
        select: Optional[Iterable[str]] = None,
        order_by: Optional[str] = None,
        top: Optional[int] = None,
        skip: Optional[int] = None,
        raw: bool = False,
    ) -> list[Any]:
        query_params = self._build_params(params, filters, select, order_by, top, skip)
        data = self.client.get(self._get_resource_path(), params=query_params)
        return self._deserialize_many(data, raw=raw)

    def get(self, entity_id: str, *, raw: bool = False) -> Any:
        data = self.client.get(f"{self._get_resource_path()}(guid'{entity_id}')")
        return self._deserialize_item(data, raw=raw)

    def create(
        self, payload: dict[str, Any] | StrictModel, *, raw: bool = False
    ) -> Any:
        body = self._serialize_payload(payload)
        data = self.client.post(self._get_resource_path(), json=body)
        return self._deserialize_item(data, raw=raw)

    def update(
        self,
        entity_id: str,
        payload: dict[str, Any] | StrictModel,
        *,
        raw: bool = False,
    ) -> Any:
        body = self._serialize_payload(payload)
        data = self.client.patch(
            f"{self._get_resource_path()}(guid'{entity_id}')", json=body
        )
        return self._deserialize_item(data, raw=raw)

    def delete(self, entity_id: str) -> Any:
        return self.client.delete(f"{self._get_resource_path()}(guid'{entity_id}')")

    def iter_pages(
        self,
        *,
        params: Optional[dict[str, Any]] = None,
        filters: Optional[Mapping[str, FilterValue]] = None,
        select: Optional[Iterable[str]] = None,
        order_by: Optional[str] = None,
        page_size: Optional[int] = 100,
        raw: bool = False,
    ) -> Iterator[List[Any]]:
        query_params = self._build_params(
            params,
            filters,
            select,
            order_by,
            top=page_size,
            skip=None,
        )
        for page in self.client.iter_pages(
            self._get_resource_path(), params=query_params
        ):
            yield [self._deserialize_item(item, raw=raw) for item in page]

    def iter_all(
        self,
        *,
        params: Optional[dict[str, Any]] = None,
        filters: Optional[Mapping[str, FilterValue]] = None,
        select: Optional[Iterable[str]] = None,
        order_by: Optional[str] = None,
        page_size: Optional[int] = 100,
        raw: bool = False,
    ) -> Iterator[Any]:
        for page in self.iter_pages(
            params=params,
            filters=filters,
            select=select,
            order_by=order_by,
            page_size=page_size,
            raw=raw,
        ):
            for item in page:
                yield item

    def _build_params(
        self,
        params: Optional[dict[str, Any]],
        filters: Optional[Mapping[str, FilterValue]],
        select: Optional[Iterable[str]],
        order_by: Optional[str],
        top: Optional[int],
        skip: Optional[int],
    ) -> Optional[dict[str, Any]]:
        final: dict[str, Any] = dict(params or {})
        if filters:
            if "$filter" in final:
                raise ValidationError(
                    "Provide filters or $filter param, not both",
                    context={"filters": filters},
                )
            final["$filter"] = self._build_filter(filters)
        if select:
            final["$select"] = ",".join(select)
        if order_by:
            final["$orderby"] = order_by
        if top is not None:
            final["$top"] = top
        if skip is not None:
            final["$skip"] = skip
        return final or None

    def _build_filter(self, filters: Mapping[str, FilterValue]) -> str:
        expressions: list[str] = []
        for field, value in filters.items():
            operator = "eq"
            actual = value
            if isinstance(value, tuple) and len(value) == 2:
                operator = str(value[0])
                actual = value[1]
            if isinstance(actual, (list, tuple, set)) and operator.lower() == "in":
                formatted_values = ", ".join(
                    self._format_filter_value(v) for v in actual
                )
                expressions.append(f"{field} in ({formatted_values})")
                continue
            formatted = self._format_filter_value(actual)
            expressions.append(f"{field} {operator} {formatted}")
        return " and ".join(expressions)

    def _format_filter_value(self, value: Any) -> str:
        if value is None:
            return "null"
        if isinstance(value, bool):
            return str(value).lower()
        if isinstance(value, UUID):
            return f"guid'{value}'"
        if isinstance(value, datetime):
            return f"datetimeoffset'{value.isoformat()}'"
        if isinstance(value, date):
            return f"'{value.isoformat()}'"
        if isinstance(value, (int, float)):
            return str(value)
        escaped = str(value).replace("'", "''")
        return f"'{escaped}'"

    def _serialize_payload(
        self, payload: dict[str, Any] | StrictModel
    ) -> dict[str, Any]:
        if isinstance(payload, StrictModel):
            return payload.model_dump()
        if not isinstance(payload, dict):
            raise ValidationError(
                "Payload must be a dict or StrictModel instance",
                context={"payload_type": type(payload).__name__},
            )
        if self.model_cls is None:
            return payload
        try:
            model = self.model_cls.model_validate(payload)
        except (
            PydanticValidationError
        ) as exc:  # pragma: no cover - exercised via api tests
            raise ValidationError(
                "Payload validation failed", context={"errors": exc.errors()}
            ) from exc
        return model.model_dump()

    def _deserialize_item(self, data: Any, *, raw: bool) -> Any:
        if raw or self.model_cls is None or data is None:
            return data
        try:
            return self.model_cls.model_validate(data)
        except PydanticValidationError as exc:
            raise ValidationError(
                "Response validation failed", context={"errors": exc.errors()}
            ) from exc

    def _deserialize_many(self, data: Any, *, raw: bool) -> List[Any]:
        if data is None:
            return []
        if not isinstance(data, list):
            data = [data]
        return [self._deserialize_item(item, raw=raw) for item in data]


class AccountsAPI(BaseAPI):
    model_cls = Account

    def _resource(self) -> str:
        return "crm/Accounts"


class ContactsAPI(BaseAPI):
    model_cls = Contact

    def _resource(self) -> str:
        return "crm/Contacts"


class SyncCRMContactsAPI(BaseAPI):
    model_cls = Contact

    def _resource(self) -> str:
        return "sync/CRM/Contacts"


class SalesOrdersAPI(BaseAPI):
    model_cls = SalesOrder

    def _resource(self) -> str:
        return "salesorder/SalesOrders"


class ItemsAPI(BaseAPI):
    model_cls = Item

    def _resource(self) -> str:
        return "logistics/Items"


class SalesInvoicesAPI(BaseAPI):
    model_cls = SalesInvoice

    def _resource(self) -> str:
        return "salesinvoice/SalesInvoices"


class BulkCRMAccountsAPI(BaseAPI):
    model_cls = BulkCRMAccount

    def _resource(self) -> str:
        return "bulk/CRM/Accounts"


class BulkCRMAddressesAPI(BaseAPI):
    model_cls = BulkCRMAddress

    def _resource(self) -> str:
        return "bulk/CRM/Addresses"


class BulkCRMContactsAPI(BaseAPI):
    model_cls = BulkCRMContact

    def _resource(self) -> str:
        return "bulk/CRM/Contacts"


class BulkCRMQuotationLinesAPI(BaseAPI):
    model_cls = BulkCRMQuotationLine

    def _resource(self) -> str:
        return "bulk/CRM/QuotationLines"


class BulkCRMQuotationsAPI(BaseAPI):
    model_cls = BulkCRMQuotation

    def _resource(self) -> str:
        return "bulk/CRM/Quotations"


class BulkDocumentAttachmentsAPI(BaseAPI):
    model_cls = BulkDocumentAttachment

    def _resource(self) -> str:
        return "bulk/Documents/DocumentAttachments"


class BulkDocumentsAPI(BaseAPI):
    model_cls = BulkDocument

    def _resource(self) -> str:
        return "bulk/Documents/Documents"


class AccountClassesAPI(BaseAPI):
    model_cls = AccountClass

    def _resource(self) -> str:
        return "crm/AccountClasses"


class AccountClassificationNamesAPI(BaseAPI):
    model_cls = AccountClassificationName

    def _resource(self) -> str:
        return "crm/AccountClassificationNames"


class AccountClassificationsAPI(BaseAPI):
    model_cls = AccountClassification

    def _resource(self) -> str:
        return "crm/AccountClassifications"


class AddressesAPI(BaseAPI):
    model_cls = Address

    def _resource(self) -> str:
        return "crm/Addresses"


class SyncCRMAddressesAPI(BaseAPI):
    model_cls = Address

    def _resource(self) -> str:
        return "sync/CRM/Addresses"


class AddressStatesAPI(BaseAPI):
    model_cls = AddressState

    def _resource(self) -> str:
        return "crm/AddressStates"


class BankAccountsAPI(BaseAPI):
    model_cls = BankAccount

    def _resource(self) -> str:
        return "crm/BankAccounts"


class LeadPurposesAPI(BaseAPI):
    model_cls = LeadPurpose

    def _resource(self) -> str:
        return "crm/LeadPurposes"


class LeadSourcesAPI(BaseAPI):
    model_cls = LeadSource

    def _resource(self) -> str:
        return "crm/LeadSources"


class CRMOpportunitiesAPI(BaseAPI):
    model_cls = Opportunity

    def _resource(self) -> str:
        return "crm/Opportunities"


class CRMQuotationLinesAPI(BaseAPI):
    model_cls = QuotationLine

    def _resource(self) -> str:
        return "crm/QuotationLines"


class CRMQuotationOrderChargeLinesAPI(BaseAPI):
    model_cls = QuotationOrderChargeLine

    def _resource(self) -> str:
        return "crm/QuotationOrderChargeLines"


class CRMQuotationsAPI(BaseAPI):
    model_cls = Quotation

    def _resource(self) -> str:
        return "crm/Quotations"


class CRMReasonCodesAPI(BaseAPI):
    model_cls = ReasonCode

    def _resource(self) -> str:
        return "crm/ReasonCodes"


class DocumentAttachmentsAPI(BaseAPI):
    model_cls = DocumentAttachment

    def _resource(self) -> str:
        return "documents/DocumentAttachments"


class DocumentCategoriesAPI(BaseAPI):
    model_cls = DocumentCategory

    def _resource(self) -> str:
        return "documents/DocumentCategories"


class DocumentFoldersAPI(BaseAPI):
    model_cls = DocumentFolder

    def _resource(self) -> str:
        return "documents/DocumentFolders"


class DocumentTypeCategoriesAPI(BaseAPI):
    model_cls = DocumentTypeCategory

    def _resource(self) -> str:
        return "documents/DocumentTypeCategories"


class DocumentTypeFoldersAPI(BaseAPI):
    model_cls = DocumentTypeFolder

    def _resource(self) -> str:
        return "documents/DocumentTypeFolders"


class DocumentTypesAPI(BaseAPI):
    model_cls = DocumentType

    def _resource(self) -> str:
        return "documents/DocumentTypes"


class DocumentsAPI(BaseAPI):
    model_cls = Document

    def _resource(self) -> str:
        return "documents/Documents"


class GLAccountsAPI(BaseAPI):
    model_cls = GLAccount

    def _resource(self) -> str:
        return "financial/GLAccounts"


class BulkFinancialGLAccountsAPI(BaseAPI):
    model_cls = GLAccount

    def _resource(self) -> str:
        return "bulk/Financial/GLAccounts"


class SyncFinancialGLAccountsAPI(BaseAPI):
    model_cls = GLAccount

    def _resource(self) -> str:
        return "sync/Financial/GLAccounts"


class StockBatchNumbersAPI(BaseAPI):
    model_cls = StockBatchNumber

    def _resource(self) -> str:
        return "inventory/StockBatchNumbers"


class StockCountLinesAPI(BaseAPI):
    model_cls = StockCountLine

    def _resource(self) -> str:
        return "inventory/StockCountLines"


class StockCountsAPI(BaseAPI):
    model_cls = StockCount

    def _resource(self) -> str:
        return "inventory/StockCounts"


class StockSerialNumbersAPI(BaseAPI):
    model_cls = StockSerialNumber

    def _resource(self) -> str:
        return "inventory/StockSerialNumbers"


class ItemGroupsAPI(BaseAPI):
    model_cls = ItemGroup

    def _resource(self) -> str:
        return "logistics/ItemGroups"


class ItemVersionsAPI(BaseAPI):
    model_cls = ItemVersion

    def _resource(self) -> str:
        return "logistics/ItemVersions"


class LogisticsReasonCodesAPI(BaseAPI):
    model_cls = ReasonCode

    def _resource(self) -> str:
        return "logistics/ReasonCodes"


class ReasonCodesLinkTypesAPI(BaseAPI):
    model_cls = ReasonCodesLinkType

    def _resource(self) -> str:
        return "logistics/ReasonCodesLinkTypes"


class SalesItemPricesAPI(BaseAPI):
    model_cls = SalesItemPrice

    def _resource(self) -> str:
        return "logistics/SalesItemPrices"


class SelectionCodesAPI(BaseAPI):
    model_cls = SelectionCode

    def _resource(self) -> str:
        return "logistics/SelectionCodes"


class SupplierItemAPI(BaseAPI):
    model_cls = SupplierItem

    def _resource(self) -> str:
        return "logistics/SupplierItem"


class UnitsAPI(BaseAPI):
    model_cls = Unit

    def _resource(self) -> str:
        return "logistics/Units"


class OpportunityContactsAPI(BaseAPI):
    model_cls = OpportunityContact

    def _resource(self) -> str:
        return "opportunities/OpportunityContacts"


class OpportunitiesAPI(BaseAPI):
    model_cls = Opportunity

    def _resource(self) -> str:
        return "opportunities/Opportunities"


class PurchaseOrderLinesAPI(BaseAPI):
    model_cls = PurchaseOrderLine

    def _resource(self) -> str:
        return "purchase/PurchaseOrderLines"


class PurchaseOrdersAPI(BaseAPI):
    model_cls = PurchaseOrder

    def _resource(self) -> str:
        return "purchase/PurchaseOrders"


class QuotationLinesAPI(BaseAPI):
    model_cls = QuotationLine

    def _resource(self) -> str:
        return "quotation/QuotationLines"


class QuotationsAPI(BaseAPI):
    model_cls = Quotation

    def _resource(self) -> str:
        return "quotation/Quotations"


class SalesInvoiceOrderChargeLinesAPI(BaseAPI):
    model_cls = SalesInvoiceOrderChargeLine

    def _resource(self) -> str:
        return "salesinvoice/SalesInvoiceOrderChargeLines"


class SalesInvoiceLinesAPI(BaseAPI):
    model_cls = SalesInvoiceLine

    def _resource(self) -> str:
        return "salesinvoice/SalesInvoiceLines"


class DropShipmentLinesAPI(BaseAPI):
    model_cls = DropShipmentLine

    def _resource(self) -> str:
        return "salesorder/DropShipmentLines"


class DropShipmentsAPI(BaseAPI):
    model_cls = DropShipment

    def _resource(self) -> str:
        return "salesorder/DropShipments"


class GoodsDeliveriesAPI(BaseAPI):
    model_cls = GoodsDelivery

    def _resource(self) -> str:
        return "salesorder/GoodsDeliveries"


class GoodsDeliveryLinesAPI(BaseAPI):
    model_cls = GoodsDeliveryLine

    def _resource(self) -> str:
        return "salesorder/GoodsDeliveryLines"


class PlannedSalesReturnLinesAPI(BaseAPI):
    model_cls = PlannedSalesReturnLine

    def _resource(self) -> str:
        return "salesorder/PlannedSalesReturnLines"


class PlannedSalesReturnsAPI(BaseAPI):
    model_cls = PlannedSalesReturn

    def _resource(self) -> str:
        return "salesorder/PlannedSalesReturns"


class SalesOrderLinesAPI(BaseAPI):
    model_cls = SalesOrderLine

    def _resource(self) -> str:
        return "salesorder/SalesOrderLines"


class SalesOrderOrderChargeLinesAPI(BaseAPI):
    model_cls = SalesOrderOrderChargeLine

    def _resource(self) -> str:
        return "salesorder/SalesOrderOrderChargeLines"


class SyncInventoryItemStorageLocationsAPI(BaseAPI):
    model_cls = InventoryItemStorageLocation

    def _resource(self) -> str:
        return "sync/Inventory/ItemStorageLocations"


class SyncInventoryItemWarehousesAPI(BaseAPI):
    model_cls = InventoryItemWarehouse

    def _resource(self) -> str:
        return "sync/Inventory/ItemWarehouses"


class SyncInventorySerialBatchNumbersAPI(BaseAPI):
    model_cls = InventorySerialBatchNumber

    def _resource(self) -> str:
        return "sync/Inventory/SerialBatchNumbers"


class SyncInventoryStockPositionsAPI(BaseAPI):
    model_cls = InventoryStockPosition

    def _resource(self) -> str:
        return "sync/Inventory/StockPositions"


class SyncInventoryStockSerialBatchNumbersAPI(BaseAPI):
    model_cls = InventoryStockSerialBatchNumber

    def _resource(self) -> str:
        return "sync/Inventory/StockSerialBatchNumbers"


class SyncInventoryStorageLocationStockPositionsAPI(BaseAPI):
    model_cls = InventoryStorageLocationStockPosition

    def _resource(self) -> str:
        return "sync/Inventory/StorageLocationStockPositions"


class SyncDocumentAttachmentsAPI(BaseAPI):
    model_cls = DocumentAttachment

    def _resource(self) -> str:
        return "sync/Documents/DocumentAttachments"


class SyncDocumentsAPI(BaseAPI):
    model_cls = Document

    def _resource(self) -> str:
        return "sync/Documents/Documents"


class AssemblyBillOfMaterialHeaderAPI(BaseAPI):
    model_cls = AssemblyBillOfMaterialHeader

    def _resource(self) -> str:
        return "inventory/AssemblyBillOfMaterialHeader"


class AssemblyBillOfMaterialMaterialsAPI(BaseAPI):
    model_cls = AssemblyBillOfMaterialMaterial

    def _resource(self) -> str:
        return "inventory/AssemblyBillOfMaterialMaterials"


class AssemblyOrdersAPI(BaseAPI):
    model_cls = AssemblyOrder

    def _resource(self) -> str:
        return "inventory/AssemblyOrders"


class BatchNumbersAPI(BaseAPI):
    model_cls = BatchNumber

    def _resource(self) -> str:
        return "inventory/BatchNumbers"


class ItemWarehousePlanningDetailsAPI(BaseAPI):
    model_cls = ItemWarehousePlanningDetail

    def _resource(self) -> str:
        return "inventory/ItemWarehousePlanningDetails"


class ItemWarehouseStorageLocationsAPI(BaseAPI):
    model_cls = ItemWarehouseStorageLocation

    def _resource(self) -> str:
        return "inventory/ItemWarehouseStorageLocations"


class ItemWarehousesAPI(BaseAPI):
    model_cls = ItemWarehouse

    def _resource(self) -> str:
        return "inventory/ItemWarehouses"


class StorageLocationsAPI(BaseAPI):
    model_cls = StorageLocation

    def _resource(self) -> str:
        return "inventory/StorageLocations"


class WarehouseTransferLinesAPI(BaseAPI):
    model_cls = WarehouseTransferLine

    def _resource(self) -> str:
        return "inventory/WarehouseTransferLines"


class WarehouseTransfersAPI(BaseAPI):
    model_cls = WarehouseTransfer

    def _resource(self) -> str:
        return "inventory/WarehouseTransfers"


class WarehousesAPI(BaseAPI):
    model_cls = Warehouse

    def _resource(self) -> str:
        return "inventory/Warehouses"


class CustomerItemsAPI(BaseAPI):
    model_cls = CustomerItem

    def _resource(self) -> str:
        return "logistics/CustomerItems"


class IncotermsAPI(BaseAPI):
    model_cls = Incoterm

    def _resource(self) -> str:
        return "logistics/Incoterms"


class ItemAssortmentAPI(BaseAPI):
    model_cls = ItemAssortment

    def _resource(self) -> str:
        return "logistics/ItemAssortment"


class ItemAssortmentPropertyAPI(BaseAPI):
    model_cls = ItemAssortmentProperty

    def _resource(self) -> str:
        return "logistics/ItemAssortmentProperty"


class ItemChargeRelationAPI(BaseAPI):
    model_cls = ItemChargeRelation

    def _resource(self) -> str:
        return "logistics/ItemChargeRelation"


class AccountInvolvedAccountsAPI(BaseAPI):
    model_cls = AccountInvolvedAccount

    def _resource(self) -> str:
        return "accountancy/AccountInvolvedAccounts"


class AccountOwnersAPI(BaseAPI):
    model_cls = AccountOwner

    def _resource(self) -> str:
        return "accountancy/AccountOwners"


class InvolvedUserRolesAPI(BaseAPI):
    model_cls = InvolvedUserRole

    def _resource(self) -> str:
        return "accountancy/InvolvedUserRoles"


class InvolvedUsersAPI(BaseAPI):
    model_cls = InvolvedUser

    def _resource(self) -> str:
        return "accountancy/InvolvedUsers"


class SolutionLinksAPI(BaseAPI):
    model_cls = SolutionLink

    def _resource(self) -> str:
        return "accountancy/SolutionLinks"


class TaskTypesAPI(BaseAPI):
    model_cls = TaskType

    def _resource(self) -> str:
        return "accountancy/TaskTypes"


class CommunicationNotesAPI(BaseAPI):
    model_cls = CommunicationNote

    def _resource(self) -> str:
        return "activities/CommunicationNotes"


class ComplaintsAPI(BaseAPI):
    model_cls = Complaint

    def _resource(self) -> str:
        return "activities/Complaints"


class EventsAPI(BaseAPI):
    model_cls = Event

    def _resource(self) -> str:
        return "activities/Events"


class ServiceRequestsAPI(BaseAPI):
    model_cls = ServiceRequest

    def _resource(self) -> str:
        return "activities/ServiceRequests"


class TasksAPI(BaseAPI):
    model_cls = Task

    def _resource(self) -> str:
        return "activities/Tasks"


class AssetGroupsAPI(BaseAPI):
    model_cls = AssetGroup

    def _resource(self) -> str:
        return "assets/AssetGroups"


class AssetsAPI(BaseAPI):
    model_cls = Asset

    def _resource(self) -> str:
        return "assets/Assets"


class CommercialBuildingValuesAPI(BaseAPI):
    model_cls = CommercialBuildingValue

    def _resource(self) -> str:
        return "assets/CommercialBuildingValues"


class DepreciationMethodsAPI(BaseAPI):
    model_cls = DepreciationMethod

    def _resource(self) -> str:
        return "assets/DepreciationMethods"


class BudgetsAPI(BaseAPI):
    model_cls = Budget

    def _resource(self) -> str:
        return "budget/Budgets"


class BudgetScenariosAPI(BaseAPI):
    model_cls = BudgetScenario

    def _resource(self) -> str:
        return "beta/{division}/budget/BudgetScenarios"


class AllocationRuleAPI(BaseAPI):
    model_cls = AllocationRule

    def _resource(self) -> str:
        return "beta/{division}/cashflow/AllocationRule"


class BanksAPI(BaseAPI):
    model_cls = Bank

    def _resource(self) -> str:
        return "cashflow/Banks"


class DirectDebitMandatesAPI(BaseAPI):
    model_cls = DirectDebitMandate

    def _resource(self) -> str:
        return "cashflow/DirectDebitMandates"


class PaymentConditionsAPI(BaseAPI):
    model_cls = PaymentCondition

    def _resource(self) -> str:
        return "cashflow/PaymentConditions"


class PaymentsAPI(BaseAPI):
    model_cls = Payment

    def _resource(self) -> str:
        return "cashflow/Payments"


class ReceivablesAPI(BaseAPI):
    model_cls = Receivable

    def _resource(self) -> str:
        return "cashflow/Receivables"


class EmploymentConditionGroupsAPI(BaseAPI):
    model_cls = EmploymentConditionGroup

    def _resource(self) -> str:
        return "beta/{division}/payroll/EmploymentConditionGroups"


class RequestAttachmentsAPI(BaseAPI):
    model_cls = RequestAttachment

    def _resource(self) -> str:
        return "beta/{division}/workflow/RequestAttachments"


class GLClassificationsAPI(BaseAPI):
    model_cls = GLClassification

    def _resource(self) -> str:
        return "financial/GLClassifications"


class TransactionLinesAPI(BaseAPI):
    model_cls = TransactionLine

    def _resource(self) -> str:
        return "financialtransaction/TransactionLines"


class BulkCashflowPaymentsAPI(BaseAPI):
    model_cls = Payment

    def _resource(self) -> str:
        return "bulk/Cashflow/Payments"


class BulkCashflowReceivablesAPI(BaseAPI):
    model_cls = Receivable

    def _resource(self) -> str:
        return "bulk/Cashflow/Receivables"


class BulkFinancialGLClassificationsAPI(BaseAPI):
    model_cls = GLClassification

    def _resource(self) -> str:
        return "bulk/Financial/GLClassifications"


class BulkFinancialTransactionLinesAPI(BaseAPI):
    model_cls = TransactionLine

    def _resource(self) -> str:
        return "bulk/Financial/TransactionLines"


class BulkLogisticsItemsAPI(BaseAPI):
    model_cls = Item

    def _resource(self) -> str:
        return "bulk/Logistics/Items"


class BulkLogisticsSalesItemPricesAPI(BaseAPI):
    model_cls = SalesItemPrice

    def _resource(self) -> str:
        return "bulk/Logistics/SalesItemPrices"


class BulkProjectProjectWBSAPI(BaseAPI):
    model_cls = ProjectWBS

    def _resource(self) -> str:
        return "bulk/Project/ProjectWBS"


class BulkSalesInvoiceSalesInvoiceLinesAPI(BaseAPI):
    model_cls = SalesInvoiceLine

    def _resource(self) -> str:
        return "bulk/SalesInvoice/SalesInvoiceLines"


class BulkSalesInvoiceSalesInvoicesAPI(BaseAPI):
    model_cls = SalesInvoice

    def _resource(self) -> str:
        return "bulk/SalesInvoice/SalesInvoices"


class BulkSalesOrderGoodsDeliveriesAPI(BaseAPI):
    model_cls = GoodsDelivery

    def _resource(self) -> str:
        return "bulk/SalesOrder/GoodsDeliveries"


class BulkSalesOrderGoodsDeliveryLinesAPI(BaseAPI):
    model_cls = GoodsDeliveryLine

    def _resource(self) -> str:
        return "bulk/SalesOrder/GoodsDeliveryLines"


class BulkSalesOrderSalesOrderLinesAPI(BaseAPI):
    model_cls = SalesOrderLine

    def _resource(self) -> str:
        return "bulk/SalesOrder/SalesOrderLines"


class BulkSalesOrderSalesOrdersAPI(BaseAPI):
    model_cls = SalesOrder

    def _resource(self) -> str:
        return "bulk/SalesOrder/SalesOrders"


# --- Expense Management ---


class ExpenseReportsAPI(BaseAPI):
    model_cls = ExpenseReport

    def _resource(self) -> str:
        return "expensemanagement/ExpenseReports"


class ExpensesAPI(BaseAPI):
    model_cls = Expense

    def _resource(self) -> str:
        return "expensemanagement/Expenses"


# --- Financial ---


class DeductibilityPercentagesAPI(BaseAPI):
    model_cls = DeductibilityPercentage

    def _resource(self) -> str:
        return "financial/DeductibilityPercentages"


class ExchangeRatesAPI(BaseAPI):
    model_cls = ExchangeRate

    def _resource(self) -> str:
        return "financial/ExchangeRates"


class FinancialPeriodsAPI(BaseAPI):
    model_cls = FinancialPeriod

    def _resource(self) -> str:
        return "financial/FinancialPeriods"


class GLAccountClassificationMappingsAPI(BaseAPI):
    model_cls = GLAccountClassificationMapping

    def _resource(self) -> str:
        return "financial/GLAccountClassificationMappings"


class GLSchemesAPI(BaseAPI):
    model_cls = GLScheme

    def _resource(self) -> str:
        return "financial/GLSchemes"


class GLTransactionSourcesAPI(BaseAPI):
    model_cls = GLTransactionSource

    def _resource(self) -> str:
        return "financial/GLTransactionSources"


class GLTransactionTypesAPI(BaseAPI):
    model_cls = GLTransactionType

    def _resource(self) -> str:
        return "financial/GLTransactionTypes"


class JournalsAPI(BaseAPI):
    model_cls = Journal

    def _resource(self) -> str:
        return "financial/Journals"


class OfficialReturnsAPI(BaseAPI):
    model_cls = OfficialReturn

    def _resource(self) -> str:
        return "financial/OfficialReturns"


class ReportingBalanceAPI(BaseAPI):
    model_cls = ReportingBalance

    def _resource(self) -> str:
        return "financial/ReportingBalance"


# --- Financial Transaction ---


class BankEntriesAPI(BaseAPI):
    model_cls = BankEntry

    def _resource(self) -> str:
        return "financialtransaction/BankEntries"


class BankEntryLinesAPI(BaseAPI):
    model_cls = BankEntryLine

    def _resource(self) -> str:
        return "financialtransaction/BankEntryLines"


class CashEntriesAPI(BaseAPI):
    model_cls = CashEntry

    def _resource(self) -> str:
        return "financialtransaction/CashEntries"


class CashEntryLinesAPI(BaseAPI):
    model_cls = CashEntryLine

    def _resource(self) -> str:
        return "financialtransaction/CashEntryLines"


# --- General ---


class CurrenciesAPI(BaseAPI):
    model_cls = Currency

    def _resource(self) -> str:
        return "general/Currencies"


class LayoutsAPI(BaseAPI):
    model_cls = Layout

    def _resource(self) -> str:
        return "general/Layouts"


# --- General Journal Entry ---


class GeneralJournalEntriesAPI(BaseAPI):
    model_cls = GeneralJournalEntry

    def _resource(self) -> str:
        return "generaljournalentry/GeneralJournalEntries"


class GeneralJournalEntryLinesAPI(BaseAPI):
    model_cls = GeneralJournalEntryLine

    def _resource(self) -> str:
        return "generaljournalentry/GeneralJournalEntryLines"


# --- HRM ---


class AbsenceRegistrationsAPI(BaseAPI):
    model_cls = AbsenceRegistration

    def _resource(self) -> str:
        return "hrm/AbsenceRegistrations"


class AbsenceRegistrationTransactionsAPI(BaseAPI):
    model_cls = AbsenceRegistrationTransaction

    def _resource(self) -> str:
        return "hrm/AbsenceRegistrationTransactions"


class CostcentersAPI(BaseAPI):
    model_cls = Costcenter

    def _resource(self) -> str:
        return "hrm/Costcenters"


class CostunitsAPI(BaseAPI):
    model_cls = Costunit

    def _resource(self) -> str:
        return "hrm/Costunits"


class DepartmentsAPI(BaseAPI):
    model_cls = Department

    def _resource(self) -> str:
        return "hrm/Departments"


class DivisionClassesAPI(BaseAPI):
    model_cls = DivisionClass

    def _resource(self) -> str:
        return "hrm/DivisionClasses"


class DivisionClassNamesAPI(BaseAPI):
    model_cls = DivisionClassName

    def _resource(self) -> str:
        return "hrm/DivisionClassNames"


class DivisionClassValuesAPI(BaseAPI):
    model_cls = DivisionClassValue

    def _resource(self) -> str:
        return "hrm/DivisionClassValues"


class DivisionsAPI(BaseAPI):
    model_cls = Division

    def _resource(self) -> str:
        return "hrm/Divisions"


class JobGroupsAPI(BaseAPI):
    model_cls = JobGroup

    def _resource(self) -> str:
        return "hrm/JobGroups"


class JobTitlesAPI(BaseAPI):
    model_cls = JobTitle

    def _resource(self) -> str:
        return "hrm/JobTitles"


class LeaveAbsenceHoursByDayAPI(BaseAPI):
    model_cls = LeaveAbsenceHoursByDay

    def _resource(self) -> str:
        return "hrm/LeaveAbsenceHoursByDay"


class LeaveBuildUpRegistrationsAPI(BaseAPI):
    model_cls = LeaveBuildUpRegistration

    def _resource(self) -> str:
        return "hrm/LeaveBuildUpRegistrations"


class LeaveRegistrationsAPI(BaseAPI):
    model_cls = LeaveRegistration

    def _resource(self) -> str:
        return "hrm/LeaveRegistrations"


class SchedulesAPI(BaseAPI):
    model_cls = Schedule

    def _resource(self) -> str:
        return "hrm/Schedules"


# --- Sync CRM ---


class SyncCRMAccountsAPI(BaseAPI):
    model_cls = Account

    def _resource(self) -> str:
        return "sync/CRM/Accounts"


class SyncCRMQuotationHeadersAPI(BaseAPI):
    model_cls = Quotation

    def _resource(self) -> str:
        return "sync/CRM/QuotationHeaders"


class SyncCRMQuotationLinesAPI(BaseAPI):
    model_cls = QuotationLine

    def _resource(self) -> str:
        return "sync/CRM/QuotationLines"


# --- Sync Cashflow ---


class SyncCashflowPaymentTermsAPI(BaseAPI):
    model_cls = PaymentCondition

    def _resource(self) -> str:
        return "sync/Cashflow/PaymentTerms"


# --- Sync Financial ---


class SyncFinancialGLClassificationsAPI(BaseAPI):
    model_cls = GLClassification

    def _resource(self) -> str:
        return "sync/Financial/GLClassifications"


class SyncFinancialTransactionLinesAPI(BaseAPI):
    model_cls = TransactionLine

    def _resource(self) -> str:
        return "sync/Financial/TransactionLines"


# --- Sync HRM ---


class SyncHRMAbsenceRegistrationTransactionsAPI(BaseAPI):
    model_cls = AbsenceRegistrationTransaction

    def _resource(self) -> str:
        return "sync/HRM/AbsenceRegistrationTransactions"


class SyncHRMAbsenceRegistrationsAPI(BaseAPI):
    model_cls = AbsenceRegistration

    def _resource(self) -> str:
        return "sync/HRM/AbsenceRegistrations"


class SyncHRMLeaveAbsenceHoursByDayAPI(BaseAPI):
    model_cls = LeaveAbsenceHoursByDay

    def _resource(self) -> str:
        return "sync/HRM/LeaveAbsenceHoursByDay"


class SyncHRMLeaveBuildUpRegistrationsAPI(BaseAPI):
    model_cls = LeaveBuildUpRegistration

    def _resource(self) -> str:
        return "sync/HRM/LeaveBuildUpRegistrations"


class SyncHRMLeaveRegistrationsAPI(BaseAPI):
    model_cls = LeaveRegistration

    def _resource(self) -> str:
        return "sync/HRM/LeaveRegistrations"


class SyncHRMSchedulesAPI(BaseAPI):
    model_cls = Schedule

    def _resource(self) -> str:
        return "sync/HRM/Schedules"


# --- Sync Logistics ---


class SyncLogisticsItemsAPI(BaseAPI):
    model_cls = Item

    def _resource(self) -> str:
        return "sync/Logistics/Items"


class SyncLogisticsSalesItemPricesAPI(BaseAPI):
    model_cls = SalesItemPrice

    def _resource(self) -> str:
        return "sync/Logistics/SalesItemPrices"


class SyncLogisticsSupplierItemAPI(BaseAPI):
    model_cls = SupplierItem

    def _resource(self) -> str:
        return "sync/Logistics/SupplierItem"


# --- Sync Payroll ---


class SyncPayrollBankAccountsAPI(BaseAPI):
    model_cls = BankAccount

    def _resource(self) -> str:
        return "sync/Payroll/BankAccounts"


# --- Sync Project ---


class SyncProjectProjectWBSAPI(BaseAPI):
    model_cls = ProjectWBS

    def _resource(self) -> str:
        return "sync/Project/ProjectWBS"


# --- Sync PurchaseOrder ---


class SyncPurchaseOrderPurchaseOrdersAPI(BaseAPI):
    model_cls = PurchaseOrder

    def _resource(self) -> str:
        return "sync/PurchaseOrder/PurchaseOrders"


# --- Sync SalesInvoice ---


class SyncSalesInvoiceSalesInvoicesAPI(BaseAPI):
    model_cls = SalesInvoice

    def _resource(self) -> str:
        return "sync/SalesInvoice/SalesInvoices"


# --- Sync SalesOrder ---


class SyncSalesOrderGoodsDeliveriesAPI(BaseAPI):
    model_cls = GoodsDelivery

    def _resource(self) -> str:
        return "sync/SalesOrder/GoodsDeliveries"


class SyncSalesOrderGoodsDeliveryLinesAPI(BaseAPI):
    model_cls = GoodsDeliveryLine

    def _resource(self) -> str:
        return "sync/SalesOrder/GoodsDeliveryLines"


class SyncSalesOrderSalesOrderHeadersAPI(BaseAPI):
    model_cls = SalesOrder

    def _resource(self) -> str:
        return "sync/SalesOrder/SalesOrderHeaders"


class SyncSalesOrderSalesOrderLinesAPI(BaseAPI):
    model_cls = SalesOrderLine

    def _resource(self) -> str:
        return "sync/SalesOrder/SalesOrderLines"


# --- System ---


class SystemDivisionsAPI(BaseAPI):
    model_cls = Division

    def _resource(self) -> str:
        return "system/Divisions"


# --- Current ---


class MeAPI(BaseAPI):
    model_cls = Me
    _skip_division: bool = True

    def _resource(self) -> str:
        return "current/Me"


# --- Mailbox ---


class MailMessageAttachmentsAPI(BaseAPI):
    model_cls = MailMessageAttachment

    def _resource(self) -> str:
        return "mailbox/MailMessageAttachments"


class MailMessagesSentAPI(BaseAPI):
    model_cls = MailMessagesSent

    def _resource(self) -> str:
        return "mailbox/MailMessagesSent"


class MailboxesAPI(BaseAPI):
    model_cls = Mailbox

    def _resource(self) -> str:
        return "mailbox/Mailboxes"


# --- Manufacturing ---


class BillOfMaterialMaterialsAPI(BaseAPI):
    model_cls = BillOfMaterialMaterial

    def _resource(self) -> str:
        return "manufacturing/BillOfMaterialMaterials"


class BillOfMaterialVersionsAPI(BaseAPI):
    model_cls = BillOfMaterialVersion

    def _resource(self) -> str:
        return "manufacturing/BillOfMaterialVersions"


class ByProductsAPI(BaseAPI):
    model_cls = ByProduct

    def _resource(self) -> str:
        return "manufacturing/ByProducts"


class ItemMaterialsPlanningAPI(BaseAPI):
    model_cls = ItemMaterialsPlanning

    def _resource(self) -> str:
        return "manufacturing/ItemMaterialsPlanning"


class MaterialReversalsAPI(BaseAPI):
    model_cls = MaterialReversal

    def _resource(self) -> str:
        return "manufacturing/MaterialReversals"


class OperationResourcesAPI(BaseAPI):
    model_cls = OperationResource

    def _resource(self) -> str:
        return "manufacturing/OperationResources"


class OperationsAPI(BaseAPI):
    model_cls = Operation

    def _resource(self) -> str:
        return "manufacturing/Operations"


class PlannedShopOrdersAPI(BaseAPI):
    model_cls = PlannedShopOrder

    def _resource(self) -> str:
        return "manufacturing/PlannedShopOrders"


class PlanningReleasesAPI(BaseAPI):
    model_cls = PlanningRelease

    def _resource(self) -> str:
        return "manufacturing/PlanningReleases"


class ProductionAreasAPI(BaseAPI):
    model_cls = ProductionArea

    def _resource(self) -> str:
        return "manufacturing/ProductionAreas"


class ProductionOrdersAPI(BaseAPI):
    model_cls = ProductionOrder

    def _resource(self) -> str:
        return "manufacturing/ProductionOrders"


class ShopOrderMaterialPlansAPI(BaseAPI):
    model_cls = ShopOrderMaterialPlan

    def _resource(self) -> str:
        return "manufacturing/ShopOrderMaterialPlans"


class ShopOrderRoutingStepPlansAPI(BaseAPI):
    model_cls = ShopOrderRoutingStepPlan

    def _resource(self) -> str:
        return "manufacturing/ShopOrderRoutingStepPlans"


class ShopOrdersAPI(BaseAPI):
    model_cls = ShopOrder

    def _resource(self) -> str:
        return "manufacturing/ShopOrders"


class SubOrderReversalsAPI(BaseAPI):
    model_cls = SubOrderReversal

    def _resource(self) -> str:
        return "manufacturing/SubOrderReversals"


# --- Payroll ---


class EmploymentActiveEmploymentsAPI(BaseAPI):
    model_cls = EmploymentActiveEmployment

    def _resource(self) -> str:
        return "payroll/EmploymentActiveEmployments"


class EmploymentContractsAPI(BaseAPI):
    model_cls = EmploymentContract

    def _resource(self) -> str:
        return "payroll/EmploymentContracts"


class EmploymentOrganizationalUnitsAPI(BaseAPI):
    model_cls = EmploymentOrganizationalUnit

    def _resource(self) -> str:
        return "payroll/EmploymentOrganizationalUnits"


class EmploymentSalariesAPI(BaseAPI):
    model_cls = EmploymentSalary

    def _resource(self) -> str:
        return "payroll/EmploymentSalaries"


class EmploymentStepsAPI(BaseAPI):
    model_cls = EmploymentStep

    def _resource(self) -> str:
        return "payroll/EmploymentSteps"


class EmploymentTaxAuthoritiesGeneralAPI(BaseAPI):
    model_cls = EmploymentTaxAuthoritiesGeneral

    def _resource(self) -> str:
        return "payroll/EmploymentTaxAuthoritiesGeneral"


class EmploymentTermsAPI(BaseAPI):
    model_cls = EmploymentTerm

    def _resource(self) -> str:
        return "payroll/EmploymentTerms"


class EmploymentWorkingHoursAPI(BaseAPI):
    model_cls = EmploymentWorkingHour

    def _resource(self) -> str:
        return "payroll/EmploymentWorkingHours"


class EmploymentsAPI(BaseAPI):
    model_cls = Employment

    def _resource(self) -> str:
        return "payroll/Employments"


# --- Project ---


class BlockedProjectPurchasesAPI(BaseAPI):
    model_cls = BlockedProjectPurchase

    def _resource(self) -> str:
        return "project/BlockedProjectPurchases"


class BlockedProjectSalesAPI(BaseAPI):
    model_cls = BlockedProjectSale

    def _resource(self) -> str:
        return "project/BlockedProjectSales"


class CostTypesAPI(BaseAPI):
    model_cls = CostType

    def _resource(self) -> str:
        return "project/CostTypes"


class EmploymentInternalRatesAPI(BaseAPI):
    model_cls = EmploymentInternalRate

    def _resource(self) -> str:
        return "project/EmploymentInternalRates"


class HourCostTypesAPI(BaseAPI):
    model_cls = HourCostType

    def _resource(self) -> str:
        return "project/HourCostTypes"


class HourTypeBudgetsAPI(BaseAPI):
    model_cls = HourTypeBudget

    def _resource(self) -> str:
        return "project/HourTypeBudgets"


class HourTypesAPI(BaseAPI):
    model_cls = HourType

    def _resource(self) -> str:
        return "project/HourTypes"


class ProjectsAPI(BaseAPI):
    model_cls = Project

    def _resource(self) -> str:
        return "project/Projects"


class ProjectClassificationsAPI(BaseAPI):
    model_cls = ProjectClassification

    def _resource(self) -> str:
        return "project/ProjectClassifications"


class ProjectHourBudgetsAPI(BaseAPI):
    model_cls = ProjectHourBudget

    def _resource(self) -> str:
        return "project/ProjectHourBudgets"


class ProjectPlanningAPI(BaseAPI):
    model_cls = ProjectPlanning

    def _resource(self) -> str:
        return "project/ProjectPlanning"


class ProjectPlanningRecurringAPI(BaseAPI):
    model_cls = ProjectPlanningRecurring

    def _resource(self) -> str:
        return "project/ProjectPlanningRecurring"


class CostsByDateAPI(BaseAPI):
    model_cls = CostByDate

    def _resource(self) -> str:
        return "read/project/CostsByDate"


class CostsByIdAPI(BaseAPI):
    model_cls = CostById

    def _resource(self) -> str:
        return "read/project/CostsById"


class HoursByDateAPI(BaseAPI):
    model_cls = HoursByDate

    def _resource(self) -> str:
        return "read/project/HoursByDate"


# --- ProjectWBS ---


class TimeAndBillingEntryAccountsAPI(BaseAPI):
    model_cls = TimeAndBillingEntryAccount

    def _resource(self) -> str:
        return "projectwbs/TimeAndBillingEntryAccounts"


# --- Subscription ---


class SubscriptionLineTypesAPI(BaseAPI):
    model_cls = SubscriptionLineType

    def _resource(self) -> str:
        return "subscription/SubscriptionLineTypes"


class SubscriptionLinesAPI(BaseAPI):
    model_cls = SubscriptionLine

    def _resource(self) -> str:
        return "subscription/SubscriptionLines"


class SubscriptionReasonCodesAPI(BaseAPI):
    model_cls = SubscriptionReasonCode

    def _resource(self) -> str:
        return "subscription/SubscriptionReasonCodes"


class SubscriptionRestrictionEmployeesAPI(BaseAPI):
    model_cls = SubscriptionRestrictionEmployee

    def _resource(self) -> str:
        return "subscription/SubscriptionRestrictionEmployees"


class SubscriptionRestrictionItemsAPI(BaseAPI):
    model_cls = SubscriptionRestrictionItem

    def _resource(self) -> str:
        return "subscription/SubscriptionRestrictionItems"


class SubscriptionTypesAPI(BaseAPI):
    model_cls = SubscriptionType

    def _resource(self) -> str:
        return "subscription/SubscriptionTypes"


class SubscriptionsAPI(BaseAPI):
    model_cls = Subscription

    def _resource(self) -> str:
        return "subscription/Subscriptions"


# --- System (new) ---


class AccountantInfoAPI(BaseAPI):
    model_cls = AccountantInfo

    def _resource(self) -> str:
        return "system/AccountantInfo"


class AllDivisionsAPI(BaseAPI):
    model_cls = AllDivision

    def _resource(self) -> str:
        return "system/AllDivisions"


class AvailableFeaturesAPI(BaseAPI):
    model_cls = AvailableFeature

    def _resource(self) -> str:
        return "system/AvailableFeatures"


class GetMostRecentlyUsedDivisionsAPI(BaseAPI):
    model_cls = GetMostRecentlyUsedDivision

    def _resource(self) -> str:
        return "system/GetMostRecentlyUsedDivisions"


# --- Users ---


class UserRolesAPI(BaseAPI):
    model_cls = UserRole

    def _resource(self) -> str:
        return "users/UserRoles"


class UserRolesPerDivisionAPI(BaseAPI):
    model_cls = UserRolesPerDivision

    def _resource(self) -> str:
        return "users/UserRolesPerDivision"


# --- VAT ---


class VATCodesAPI(BaseAPI):
    model_cls = VATCode

    def _resource(self) -> str:
        return "vat/VATCodes"


class VatPercentagesAPI(BaseAPI):
    model_cls = VatPercentage

    def _resource(self) -> str:
        return "vat/VatPercentages"


# --- Webhooks ---


class WebhookSubscriptionsAPI(BaseAPI):
    model_cls = WebhookSubscription

    def _resource(self) -> str:
        return "webhooks/WebhookSubscriptions"


# --- Sync HRM (new) ---


class SyncHRMScheduleEntriesAPI(BaseAPI):
    model_cls = ScheduleEntry

    def _resource(self) -> str:
        return "sync/HRM/ScheduleEntries"


# --- Sync Logistics (new) ---


class SyncLogisticsPurchaseItemPricesAPI(BaseAPI):
    model_cls = PurchaseItemPrice

    def _resource(self) -> str:
        return "sync/Logistics/PurchaseItemPrices"


# --- Sync Manufacturing ---


class SyncManufacturingBillOfMaterialMaterialsAPI(BaseAPI):
    model_cls = BillOfMaterialMaterial

    def _resource(self) -> str:
        return "sync/Manufacturing/BillOfMaterialMaterials"


class SyncManufacturingBillOfMaterialVersionsAPI(BaseAPI):
    model_cls = BillOfMaterialVersion

    def _resource(self) -> str:
        return "sync/Manufacturing/BillOfMaterialVersions"


class SyncManufacturingMaterialIssuesAPI(BaseAPI):
    model_cls = MaterialIssue

    def _resource(self) -> str:
        return "sync/Manufacturing/MaterialIssues"


class SyncManufacturingShopOrderMaterialPlansAPI(BaseAPI):
    model_cls = ShopOrderMaterialPlan

    def _resource(self) -> str:
        return "sync/Manufacturing/ShopOrderMaterialPlans"


class SyncManufacturingShopOrderPurchasePlanningAPI(BaseAPI):
    model_cls = ShopOrderPurchasePlanning

    def _resource(self) -> str:
        return "sync/Manufacturing/ShopOrderPurchasePlanning"


class SyncManufacturingShopOrderRoutingStepPlansAPI(BaseAPI):
    model_cls = ShopOrderRoutingStepPlan

    def _resource(self) -> str:
        return "sync/Manufacturing/ShopOrderRoutingStepPlans"


class SyncManufacturingShopOrderSubOrdersAPI(BaseAPI):
    model_cls = ShopOrderSubOrder

    def _resource(self) -> str:
        return "sync/Manufacturing/ShopOrderSubOrders"


class SyncManufacturingShopOrdersAPI(BaseAPI):
    model_cls = ShopOrder

    def _resource(self) -> str:
        return "sync/Manufacturing/ShopOrders"


# --- Sync Payroll (new) ---


class SyncPayrollEmployeesAPI(BaseAPI):
    model_cls = Employee

    def _resource(self) -> str:
        return "sync/Payroll/Employees"


class SyncPayrollEmploymentCLAsAPI(BaseAPI):
    model_cls = EmploymentCLA

    def _resource(self) -> str:
        return "sync/Payroll/EmploymentCLAs"


class SyncPayrollEmploymentContractsAPI(BaseAPI):
    model_cls = EmploymentContract

    def _resource(self) -> str:
        return "sync/Payroll/EmploymentContracts"


class SyncPayrollEmploymentOrganizationsAPI(BaseAPI):
    model_cls = EmploymentOrganization

    def _resource(self) -> str:
        return "sync/Payroll/EmploymentOrganizations"


class SyncPayrollEmploymentSalariesAPI(BaseAPI):
    model_cls = EmploymentSalary

    def _resource(self) -> str:
        return "sync/Payroll/EmploymentSalaries"


class SyncPayrollEmploymentTaxAuthoritiesGeneralAPI(BaseAPI):
    model_cls = EmploymentTaxAuthoritiesGeneral

    def _resource(self) -> str:
        return "sync/Payroll/EmploymentTaxAuthoritiesGeneral"


class SyncPayrollEmploymentsAPI(BaseAPI):
    model_cls = Employment

    def _resource(self) -> str:
        return "sync/Payroll/Employments"


# --- Sync Project (new) ---


class SyncProjectProjectPlanningAPI(BaseAPI):
    model_cls = ProjectPlanning

    def _resource(self) -> str:
        return "sync/Project/ProjectPlanning"


class SyncProjectProjectsAPI(BaseAPI):
    model_cls = Project

    def _resource(self) -> str:
        return "sync/Project/Projects"


class SyncProjectTimeCostTransactionsAPI(BaseAPI):
    model_cls = TimeCostTransaction

    def _resource(self) -> str:
        return "sync/Project/TimeCostTransactions"


# --- Sync Sales (new) ---


class SyncSalesSalesPriceListVolumeDiscountsAPI(BaseAPI):
    model_cls = SalesPriceListVolumeDiscount

    def _resource(self) -> str:
        return "sync/Sales/SalesPriceListVolumeDiscounts"


# --- Sync Subscription (new) ---


class SyncSubscriptionSubscriptionLinesAPI(BaseAPI):
    model_cls = SubscriptionLine

    def _resource(self) -> str:
        return "sync/Subscription/SubscriptionLines"


class SyncSubscriptionSubscriptionsAPI(BaseAPI):
    model_cls = Subscription

    def _resource(self) -> str:
        return "sync/Subscription/Subscriptions"
