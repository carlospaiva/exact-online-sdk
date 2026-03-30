from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    InventoryItemStorageLocation,
    InventoryItemWarehouse,
    InventorySerialBatchNumber,
    InventoryStockPosition,
    InventoryStockSerialBatchNumber,
    InventoryStorageLocationStockPosition,
)


def test_inventory_item_storage_location_parses_aliases() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()
    created = datetime.now(timezone.utc)

    payload = {
        "Item": str(item_id),
        "Warehouse": str(warehouse_id),
        "Created": created.isoformat(),
        "StorageLocationCode": "LOC-01",
    }

    location = InventoryItemStorageLocation.model_validate(payload)

    assert location.item == item_id
    assert location.warehouse == warehouse_id
    assert location.created == created
    assert location.storage_location_code == "LOC-01"


def test_inventory_item_storage_location_requires_item_and_warehouse() -> None:
    with pytest.raises(ValidationError) as exc:
        InventoryItemStorageLocation.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("item",) in error_fields
    assert ("warehouse",) in error_fields


def test_inventory_item_warehouse_parses_aliases() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()
    default_storage_location_id = uuid4()

    payload = {
        "Item": str(item_id),
        "Warehouse": str(warehouse_id),
        "DefaultStorageLocation": str(default_storage_location_id),
        "MaximumStock": 10.0,
    }

    item_warehouse = InventoryItemWarehouse.model_validate(payload)

    assert item_warehouse.item == item_id
    assert item_warehouse.warehouse == warehouse_id
    assert item_warehouse.default_storage_location == default_storage_location_id
    assert item_warehouse.maximum_stock == 10.0


def test_inventory_item_warehouse_requires_item_and_warehouse() -> None:
    with pytest.raises(ValidationError) as exc:
        InventoryItemWarehouse.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("item",) in error_fields
    assert ("warehouse",) in error_fields


def test_inventory_serial_batch_number_accepts_minimal_payload() -> None:
    serial_batch = InventorySerialBatchNumber.model_validate({})

    assert serial_batch.serial_batch_number is None
    assert serial_batch.item is None


def test_inventory_serial_batch_number_parses_aliases() -> None:
    identifier = uuid4()
    created = datetime.now(timezone.utc)

    payload = {
        "ID": str(identifier),
        "SerialBatchNumber": "BATCH-001",
        "Created": created.isoformat(),
    }

    serial_batch = InventorySerialBatchNumber.model_validate(payload)

    assert serial_batch.id == identifier
    assert serial_batch.serial_batch_number == "BATCH-001"
    assert serial_batch.created == created


def test_inventory_stock_position_parses_aliases() -> None:
    warehouse_id = uuid4()

    payload = {
        "ItemCode": "ITEM-001",
        "ItemDescription": "Demo Item",
        "CurrentStock": 5.0,
        "FreeStock": 2.0,
        "Warehouse": str(warehouse_id),
    }

    position = InventoryStockPosition.model_validate(payload)

    assert position.item_code == "ITEM-001"
    assert position.item_description == "Demo Item"
    assert position.current_stock == 5.0
    assert position.free_stock == 2.0
    assert position.warehouse == warehouse_id


def test_inventory_stock_serial_batch_number_requires_stock_transaction_type() -> None:
    with pytest.raises(ValidationError) as exc:
        InventoryStockSerialBatchNumber.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("stock_transaction_type",) in error_fields


def test_inventory_stock_serial_batch_number_parses_aliases() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()

    payload = {
        "Item": str(item_id),
        "Warehouse": str(warehouse_id),
        "StockTransactionType": 1,
        "Quantity": 4.0,
    }

    stock_serial_batch = InventoryStockSerialBatchNumber.model_validate(payload)

    assert stock_serial_batch.item == item_id
    assert stock_serial_batch.warehouse == warehouse_id
    assert stock_serial_batch.stock_transaction_type == 1
    assert stock_serial_batch.quantity == 4.0


def test_inventory_storage_location_stock_position_parses_aliases() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()
    storage_location_id = uuid4()

    payload = {
        "Item": str(item_id),
        "Warehouse": str(warehouse_id),
        "StorageLocation": str(storage_location_id),
        "Stock": 10.0,
        "UnitCode": "PCS",
    }

    position = InventoryStorageLocationStockPosition.model_validate(payload)

    assert position.item == item_id
    assert position.warehouse == warehouse_id
    assert position.storage_location == storage_location_id
    assert position.stock == 10.0
    assert position.unit_code == "PCS"


def test_inventory_item_storage_location_dump_by_alias_uses_exact_payload_keys() -> (
    None
):
    item_id = uuid4()
    warehouse_id = uuid4()

    location = InventoryItemStorageLocation(
        item=item_id,
        warehouse=warehouse_id,
        storage_location_code="LOC-ALIAS",
    )

    dumped = location.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Warehouse"] == str(warehouse_id)
    assert dumped["StorageLocationCode"] == "LOC-ALIAS"


def test_inventory_item_warehouse_dump_by_alias_uses_exact_payload_keys() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()

    item_warehouse = InventoryItemWarehouse(
        item=item_id,
        warehouse=warehouse_id,
        maximum_stock=15.0,
    )

    dumped = item_warehouse.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Warehouse"] == str(warehouse_id)
    assert dumped["MaximumStock"] == 15.0


def test_inventory_serial_batch_number_dump_by_alias_uses_exact_payload_keys() -> None:
    identifier = uuid4()

    serial_batch = InventorySerialBatchNumber(
        id=identifier,
        serial_batch_number="BATCH-ALIAS",
    )

    dumped = serial_batch.model_dump(by_alias=True)

    assert dumped["ID"] == str(identifier)
    assert dumped["SerialBatchNumber"] == "BATCH-ALIAS"


def test_inventory_stock_position_dump_by_alias_uses_exact_payload_keys() -> None:
    warehouse_id = uuid4()

    position = InventoryStockPosition(
        item_code="ITEM-ALIAS",
        current_stock=8.0,
        free_stock=3.0,
        warehouse=warehouse_id,
    )

    dumped = position.model_dump(by_alias=True)

    assert dumped["ItemCode"] == "ITEM-ALIAS"
    assert dumped["CurrentStock"] == 8.0
    assert dumped["FreeStock"] == 3.0
    assert dumped["Warehouse"] == str(warehouse_id)


def test_inv_stock_serial_batch_dump_by_alias_uses_exact_payload_keys() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()

    stock_serial_batch = InventoryStockSerialBatchNumber(
        item=item_id,
        warehouse=warehouse_id,
        stock_transaction_type=2,
        quantity=6.0,
    )

    dumped = stock_serial_batch.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Warehouse"] == str(warehouse_id)
    assert dumped["StockTransactionType"] == 2
    assert dumped["Quantity"] == 6.0


def test_inv_storage_loc_stock_position_dump_by_alias_uses_exact_payload_keys() -> None:
    item_id = uuid4()
    warehouse_id = uuid4()
    storage_location_id = uuid4()

    position = InventoryStorageLocationStockPosition(
        item=item_id,
        warehouse=warehouse_id,
        storage_location=storage_location_id,
        stock=12.0,
        unit_code="PCS",
    )

    dumped = position.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["Warehouse"] == str(warehouse_id)
    assert dumped["StorageLocation"] == str(storage_location_id)
    assert dumped["Stock"] == 12.0
    assert dumped["UnitCode"] == "PCS"
