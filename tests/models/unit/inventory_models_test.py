from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    AssemblyBillOfMaterialHeader,
    AssemblyBillOfMaterialMaterial,
    AssemblyOrder,
    BatchNumber,
    ItemWarehouse,
    ItemWarehousePlanningDetail,
    ItemWarehouseStorageLocation,
    StorageLocation,
    Warehouse,
    WarehouseTransfer,
    WarehouseTransferLine,
)

# ---------------------------------------------------------------------------
# AssemblyBillOfMaterialMaterial
# ---------------------------------------------------------------------------


def test_assembly_bom_material_parses_aliases() -> None:
    assembled = uuid4()
    part = uuid4()

    payload = {
        "ID": str(uuid4()),
        "AssembledItem": str(assembled),
        "PartItem": str(part),
        "Quantity": 2.5,
        "LineNumber": 10,
        "Division": 1,
    }

    mat = AssemblyBillOfMaterialMaterial.model_validate(payload)

    assert mat.assembled_item == assembled
    assert mat.part_item == part
    assert mat.quantity == 2.5
    assert mat.line_number == 10


def test_assembly_bom_material_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        AssemblyBillOfMaterialMaterial.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("assembled_item",) in error_fields
    assert ("part_item",) in error_fields


def test_assembly_bom_material_optional_fields_default_to_none() -> None:
    assembled = uuid4()
    part = uuid4()

    mat = AssemblyBillOfMaterialMaterial(assembled_item=assembled, part_item=part)

    assert mat.id is None
    assert mat.quantity is None
    assert mat.batch_quantity is None
    assert mat.creator is None


def test_assembly_bom_material_dump_by_alias() -> None:
    assembled = uuid4()
    part = uuid4()

    mat = AssemblyBillOfMaterialMaterial(
        assembled_item=assembled, part_item=part, quantity=3.0
    )

    dumped = mat.model_dump(by_alias=True)

    assert dumped["AssembledItem"] == str(assembled)
    assert dumped["PartItem"] == str(part)
    assert dumped["Quantity"] == 3.0


# ---------------------------------------------------------------------------
# AssemblyBillOfMaterialHeader
# ---------------------------------------------------------------------------


def test_assembly_bom_header_parses_aliases() -> None:
    header_id = uuid4()
    assembled = uuid4()
    part = uuid4()

    payload = {
        "ID": str(header_id),
        "Code": "ITEM-001",
        "Description": "Assembly item",
        "AssembledLeadDays": 5,
        "BatchQuantity": 10.0,
        "AssemblyBillOfMaterialMaterials": [
            {
                "AssembledItem": str(assembled),
                "PartItem": str(part),
                "Quantity": 2.0,
            }
        ],
    }

    header = AssemblyBillOfMaterialHeader.model_validate(payload)

    assert header.id == header_id
    assert header.code == "ITEM-001"
    assert header.assembled_lead_days == 5
    assert len(header.assembly_bill_of_material_materials) == 1
    assert header.assembly_bill_of_material_materials[0].part_item == part


def test_assembly_bom_header_defaults_materials_to_empty_list() -> None:
    header = AssemblyBillOfMaterialHeader()

    assert header.assembly_bill_of_material_materials == []


def test_assembly_bom_header_dump_by_alias_includes_nested() -> None:
    assembled = uuid4()
    part = uuid4()

    mat = AssemblyBillOfMaterialMaterial(assembled_item=assembled, part_item=part)
    header = AssemblyBillOfMaterialHeader(
        code="H-1",
        assembly_bill_of_material_materials=[mat],
    )

    dumped = header.model_dump(by_alias=True)

    assert dumped["Code"] == "H-1"
    assert len(dumped["AssemblyBillOfMaterialMaterials"]) == 1
    assert dumped["AssemblyBillOfMaterialMaterials"][0]["AssembledItem"] == str(
        assembled
    )


# ---------------------------------------------------------------------------
# AssemblyOrder
# ---------------------------------------------------------------------------


def test_assembly_order_parses_aliases() -> None:
    order_id = uuid4()
    item_id = uuid4()
    wh_id = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "ID": str(order_id),
        "AssemblyDate": now.isoformat(),
        "Item": str(item_id),
        "OrderNumber": 100,
        "OrderStatus": 20,
        "PlannedQuantity": 50.0,
        "Warehouse": str(wh_id),
        "Type": 8060,
    }

    order = AssemblyOrder.model_validate(payload)

    assert order.id == order_id
    assert order.assembly_date == now
    assert order.item == item_id
    assert order.order_number == 100
    assert order.order_status == 20
    assert order.planned_quantity == 50.0
    assert order.type == 8060


def test_assembly_order_all_optional() -> None:
    order = AssemblyOrder()

    assert order.id is None
    assert order.item is None
    assert order.warehouse is None


def test_assembly_order_dump_by_alias() -> None:
    item_id = uuid4()

    order = AssemblyOrder(item=item_id, order_status=30)

    dumped = order.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["OrderStatus"] == 30


# ---------------------------------------------------------------------------
# BatchNumber
# ---------------------------------------------------------------------------


def test_batch_number_parses_aliases() -> None:
    bn_id = uuid4()
    item_id = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "ID": str(bn_id),
        "BatchNumber": "BN-001",
        "AvailableQuantity": 100.0,
        "Item": str(item_id),
        "Created": now.isoformat(),
        "IsBlocked": 0,
    }

    bn = BatchNumber.model_validate(payload)

    assert bn.id == bn_id
    assert bn.batch_number == "BN-001"
    assert bn.available_quantity == 100.0
    assert bn.item == item_id
    assert bn.is_blocked == 0


def test_batch_number_all_optional() -> None:
    bn = BatchNumber()

    assert bn.id is None
    assert bn.batch_number is None
    assert bn.item is None


def test_batch_number_dump_by_alias() -> None:
    bn = BatchNumber(batch_number="BN-002", available_quantity=50.0)

    dumped = bn.model_dump(by_alias=True)

    assert dumped["BatchNumber"] == "BN-002"
    assert dumped["AvailableQuantity"] == 50.0


# ---------------------------------------------------------------------------
# ItemWarehousePlanningDetail
# ---------------------------------------------------------------------------


def test_item_warehouse_planning_detail_parses_aliases() -> None:
    detail_id = uuid4()
    item_id = uuid4()
    wh_id = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "ID": str(detail_id),
        "Item": str(item_id),
        "Warehouse": str(wh_id),
        "PlannedDate": now.isoformat(),
        "PlannedQuantity": 25.0,
        "PlanningType": 120,
    }

    detail = ItemWarehousePlanningDetail.model_validate(payload)

    assert detail.id == detail_id
    assert detail.item == item_id
    assert detail.warehouse == wh_id
    assert detail.planned_quantity == 25.0
    assert detail.planning_type == 120


def test_item_warehouse_planning_detail_all_optional() -> None:
    detail = ItemWarehousePlanningDetail()

    assert detail.id is None
    assert detail.item is None


def test_item_warehouse_planning_detail_dump_by_alias() -> None:
    item_id = uuid4()

    detail = ItemWarehousePlanningDetail(item=item_id, planning_type=130)

    dumped = detail.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["PlanningType"] == 130


# ---------------------------------------------------------------------------
# ItemWarehouseStorageLocation
# ---------------------------------------------------------------------------


def test_item_warehouse_storage_location_parses_aliases() -> None:
    loc_id = uuid4()
    item_id = uuid4()
    wh_id = uuid4()
    sl_id = uuid4()

    payload = {
        "ID": str(loc_id),
        "Item": str(item_id),
        "Warehouse": str(wh_id),
        "StorageLocation": str(sl_id),
        "Stock": 12.5,
        "IsFractionAllowedItem": 1,
    }

    loc = ItemWarehouseStorageLocation.model_validate(payload)

    assert loc.id == loc_id
    assert loc.item == item_id
    assert loc.warehouse == wh_id
    assert loc.storage_location == sl_id
    assert loc.stock == 12.5
    assert loc.is_fraction_allowed_item == 1


def test_item_warehouse_storage_location_all_optional() -> None:
    loc = ItemWarehouseStorageLocation()

    assert loc.item is None
    assert loc.stock is None


def test_item_warehouse_storage_location_dump_by_alias() -> None:
    item_id = uuid4()

    loc = ItemWarehouseStorageLocation(item=item_id, stock=5.0)

    dumped = loc.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Stock"] == 5.0


# ---------------------------------------------------------------------------
# ItemWarehouse
# ---------------------------------------------------------------------------


def test_item_warehouse_parses_aliases() -> None:
    iw_id = uuid4()
    item_id = uuid4()
    wh_id = uuid4()

    payload = {
        "ID": str(iw_id),
        "Item": str(item_id),
        "Warehouse": str(wh_id),
        "CurrentStock": 100.0,
        "MaximumStock": 500.0,
        "SafetyStock": 10.0,
        "ReorderPoint": 20.0,
    }

    iw = ItemWarehouse.model_validate(payload)

    assert iw.id == iw_id
    assert iw.item == item_id
    assert iw.warehouse == wh_id
    assert iw.current_stock == 100.0
    assert iw.maximum_stock == 500.0
    assert iw.safety_stock == 10.0


def test_item_warehouse_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        ItemWarehouse.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("item",) in error_fields
    assert ("warehouse",) in error_fields


def test_item_warehouse_optional_fields_default_to_none() -> None:
    item_id = uuid4()
    wh_id = uuid4()

    iw = ItemWarehouse(item=item_id, warehouse=wh_id)

    assert iw.current_stock is None
    assert iw.maximum_stock is None
    assert iw.reorder_point is None


def test_item_warehouse_dump_by_alias() -> None:
    item_id = uuid4()
    wh_id = uuid4()

    iw = ItemWarehouse(item=item_id, warehouse=wh_id, current_stock=42.0)

    dumped = iw.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Warehouse"] == str(wh_id)
    assert dumped["CurrentStock"] == 42.0


# ---------------------------------------------------------------------------
# StorageLocation
# ---------------------------------------------------------------------------


def test_storage_location_parses_aliases() -> None:
    sl_id = uuid4()
    wh_id = uuid4()

    payload = {
        "ID": str(sl_id),
        "Code": "LOC-A",
        "Description": "Shelf A",
        "Warehouse": str(wh_id),
        "Main": 1,
        "PickSequence": 5,
    }

    sl = StorageLocation.model_validate(payload)

    assert sl.id == sl_id
    assert sl.code == "LOC-A"
    assert sl.warehouse == wh_id
    assert sl.main == 1
    assert sl.pick_sequence == 5


def test_storage_location_requires_warehouse() -> None:
    with pytest.raises(ValidationError) as exc:
        StorageLocation.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("warehouse",) in error_fields


def test_storage_location_dump_by_alias() -> None:
    wh_id = uuid4()

    sl = StorageLocation(code="LOC-B", warehouse=wh_id)

    dumped = sl.model_dump(by_alias=True)

    assert dumped["Code"] == "LOC-B"
    assert dumped["Warehouse"] == str(wh_id)


# ---------------------------------------------------------------------------
# Warehouse
# ---------------------------------------------------------------------------


def test_warehouse_parses_aliases() -> None:
    wh_id = uuid4()
    manager = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "ID": str(wh_id),
        "Code": "WH-01",
        "Description": "Main warehouse",
        "Main": 1,
        "ManagerUser": str(manager),
        "Created": now.isoformat(),
        "EMail": "wh@example.com",
        "UseStorageLocations": 1,
    }

    wh = Warehouse.model_validate(payload)

    assert wh.id == wh_id
    assert wh.code == "WH-01"
    assert wh.description == "Main warehouse"
    assert wh.main == 1
    assert wh.manager_user == manager
    assert wh.e_mail == "wh@example.com"
    assert wh.use_storage_locations == 1


def test_warehouse_all_optional() -> None:
    wh = Warehouse()

    assert wh.id is None
    assert wh.code is None


def test_warehouse_dump_by_alias() -> None:
    wh = Warehouse(code="WH-02", description="Secondary")

    dumped = wh.model_dump(by_alias=True)

    assert dumped["Code"] == "WH-02"
    assert dumped["Description"] == "Secondary"


# ---------------------------------------------------------------------------
# WarehouseTransferLine
# ---------------------------------------------------------------------------


def test_warehouse_transfer_line_parses_aliases() -> None:
    line_id = uuid4()
    item_id = uuid4()
    transfer_id = uuid4()
    sl_from = uuid4()
    sl_to = uuid4()

    payload = {
        "ID": str(line_id),
        "Item": str(item_id),
        "Quantity": 10.0,
        "TransferID": str(transfer_id),
        "StorageLocationFrom": str(sl_from),
        "StorageLocationTo": str(sl_to),
        "LineNumber": 1,
    }

    line = WarehouseTransferLine.model_validate(payload)

    assert line.id == line_id
    assert line.item == item_id
    assert line.quantity == 10.0
    assert line.transfer_id == transfer_id
    assert line.storage_location_from == sl_from
    assert line.storage_location_to == sl_to


def test_warehouse_transfer_line_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        WarehouseTransferLine.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("item",) in error_fields
    assert ("quantity",) in error_fields
    assert ("transfer_id",) in error_fields


def test_warehouse_transfer_line_optional_fields_default_to_none() -> None:
    item_id = uuid4()
    transfer_id = uuid4()

    line = WarehouseTransferLine(item=item_id, quantity=5.0, transfer_id=transfer_id)

    assert line.storage_location_from is None
    assert line.picked_by is None


def test_warehouse_transfer_line_dump_by_alias() -> None:
    item_id = uuid4()
    transfer_id = uuid4()

    line = WarehouseTransferLine(item=item_id, quantity=3.0, transfer_id=transfer_id)

    dumped = line.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Quantity"] == 3.0
    assert dumped["TransferID"] == str(transfer_id)


# ---------------------------------------------------------------------------
# WarehouseTransfer
# ---------------------------------------------------------------------------


def test_warehouse_transfer_parses_aliases_and_nested_lines() -> None:
    transfer_id = uuid4()
    wh_from = uuid4()
    wh_to = uuid4()
    item_id = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "TransferID": str(transfer_id),
        "EntryDate": now.isoformat(),
        "WarehouseFrom": str(wh_from),
        "WarehouseTo": str(wh_to),
        "Status": 10,
        "TransferNumber": 42,
        "WarehouseTransferLines": [
            {
                "Item": str(item_id),
                "Quantity": 5.0,
                "TransferID": str(transfer_id),
            }
        ],
    }

    transfer = WarehouseTransfer.model_validate(payload)

    assert transfer.transfer_id == transfer_id
    assert transfer.entry_date == now
    assert transfer.warehouse_from == wh_from
    assert transfer.warehouse_to == wh_to
    assert transfer.status == 10
    assert transfer.transfer_number == 42
    assert len(transfer.warehouse_transfer_lines) == 1
    assert transfer.warehouse_transfer_lines[0].item == item_id
    assert transfer.warehouse_transfer_lines[0].quantity == 5.0


def test_warehouse_transfer_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        WarehouseTransfer.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("entry_date",) in error_fields
    assert ("warehouse_from",) in error_fields
    assert ("warehouse_to",) in error_fields


def test_warehouse_transfer_defaults_lines_to_empty_list() -> None:
    wh_from = uuid4()
    wh_to = uuid4()
    now = datetime.now(timezone.utc)

    transfer = WarehouseTransfer(
        entry_date=now, warehouse_from=wh_from, warehouse_to=wh_to
    )

    assert transfer.warehouse_transfer_lines == []


def test_warehouse_transfer_dump_by_alias_includes_nested() -> None:
    wh_from = uuid4()
    wh_to = uuid4()
    item_id = uuid4()
    transfer_id = uuid4()
    now = datetime.now(timezone.utc)

    line = WarehouseTransferLine(item=item_id, quantity=2.0, transfer_id=transfer_id)
    transfer = WarehouseTransfer(
        transfer_id=transfer_id,
        entry_date=now,
        warehouse_from=wh_from,
        warehouse_to=wh_to,
        warehouse_transfer_lines=[line],
    )

    dumped = transfer.model_dump(by_alias=True)

    assert dumped["WarehouseFrom"] == str(wh_from)
    assert dumped["WarehouseTo"] == str(wh_to)
    assert len(dumped["WarehouseTransferLines"]) == 1
    assert dumped["WarehouseTransferLines"][0]["Item"] == str(item_id)
    assert dumped["WarehouseTransferLines"][0]["Quantity"] == 2.0


def test_warehouse_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        Warehouse.model_validate({"Code": "WH-01", "UnknownField": "bad"})


def test_batch_number_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        BatchNumber.model_validate({"BatchNumber": "BN-1", "Bogus": 123})
