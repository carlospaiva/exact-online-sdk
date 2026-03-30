from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    StockBatchNumber,
    StockCount,
    StockCountLine,
    StockSerialNumber,
)


def test_stock_batch_number_parses_aliases() -> None:
    draft_transaction_id = uuid4()
    warehouse_id = uuid4()
    created = datetime.now(timezone.utc)

    payload = {
        "ID": str(uuid4()),
        "BatchNumber": "BATCH-001",
        "DraftStockTransactionID": str(draft_transaction_id),
        "Quantity": 3.5,
        "StockTransactionType": 10,
        "Warehouse": str(warehouse_id),
        "Created": created.isoformat(),
    }

    batch = StockBatchNumber.model_validate(payload)

    assert batch.batch_number == "BATCH-001"
    assert batch.draft_stock_transaction_id == draft_transaction_id
    assert batch.quantity == 3.5
    assert batch.stock_transaction_type == 10
    assert batch.warehouse == warehouse_id
    assert batch.created == created


def test_stock_batch_number_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        StockBatchNumber.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("batch_number",) in error_fields
    assert ("draft_stock_transaction_id",) in error_fields
    assert ("quantity",) in error_fields
    assert ("stock_transaction_type",) in error_fields
    assert ("warehouse",) in error_fields


def test_stock_batch_number_optional_fields_default_to_none() -> None:
    draft_transaction_id = uuid4()
    warehouse_id = uuid4()

    batch = StockBatchNumber.model_validate(
        {
            "BatchNumber": "BATCH-002",
            "DraftStockTransactionID": str(draft_transaction_id),
            "Quantity": 1.0,
            "StockTransactionType": 1,
            "Warehouse": str(warehouse_id),
        }
    )

    assert batch.item is None
    assert batch.storage_location is None
    assert batch.stock_transaction_id is None


def test_stock_serial_number_parses_aliases() -> None:
    draft_transaction_id = uuid4()
    warehouse_id = uuid4()
    created = datetime.now(timezone.utc)

    payload = {
        "ID": str(uuid4()),
        "DraftStockTransactionID": str(draft_transaction_id),
        "SerialNumber": "SN-001",
        "StockTransactionType": 20,
        "Warehouse": str(warehouse_id),
        "Created": created.isoformat(),
    }

    serial = StockSerialNumber.model_validate(payload)

    assert serial.serial_number == "SN-001"
    assert serial.draft_stock_transaction_id == draft_transaction_id
    assert serial.stock_transaction_type == 20
    assert serial.warehouse == warehouse_id
    assert serial.created == created


def test_stock_serial_number_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        StockSerialNumber.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("draft_stock_transaction_id",) in error_fields
    assert ("serial_number",) in error_fields
    assert ("stock_transaction_type",) in error_fields
    assert ("warehouse",) in error_fields


def test_stock_count_line_parses_aliases_and_nested_collections() -> None:
    item_id = uuid4()
    stock_count_id = uuid4()

    payload = {
        "Item": str(item_id),
        "StockCountID": str(stock_count_id),
        "QuantityNew": 5.0,
        "BatchNumbers": [{"BatchNumber": "B1"}],
        "SerialNumbers": [{"SerialNumber": "SN1"}],
    }

    line = StockCountLine.model_validate(payload)

    assert line.item == item_id
    assert line.stock_count_id == stock_count_id
    assert line.quantity_new == 5.0
    assert line.batch_numbers is not None
    assert line.serial_numbers is not None
    assert len(line.batch_numbers) == 1
    assert len(line.serial_numbers) == 1


def test_stock_count_line_requires_item_and_stock_count_id() -> None:
    with pytest.raises(ValidationError) as exc:
        StockCountLine.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("item",) in error_fields
    assert ("stock_count_id",) in error_fields


def test_stock_count_parses_aliases_and_nested_lines() -> None:
    stock_count_id = uuid4()
    item_id = uuid4()
    warehouse_id = uuid4()
    count_date = datetime.now(timezone.utc)

    payload = {
        "StockCountID": str(stock_count_id),
        "StockCountDate": count_date.isoformat(),
        "Warehouse": str(warehouse_id),
        "StockCountLines": [
            {
                "Item": str(item_id),
                "StockCountID": str(stock_count_id),
                "QuantityNew": 2.0,
            }
        ],
    }

    stock_count = StockCount.model_validate(payload)

    assert stock_count.stock_count_id == stock_count_id
    assert stock_count.stock_count_date == count_date
    assert stock_count.warehouse == warehouse_id
    assert len(stock_count.stock_count_lines) == 1

    line = stock_count.stock_count_lines[0]
    assert line.item == item_id
    assert line.stock_count_id == stock_count_id
    assert line.quantity_new == 2.0


def test_stock_count_defaults_lines_to_empty_list() -> None:
    warehouse_id = uuid4()
    count_date = datetime.now(timezone.utc)

    stock_count = StockCount(stock_count_date=count_date, warehouse=warehouse_id)

    assert stock_count.stock_count_lines == []


def test_stock_count_requires_stock_count_date_and_warehouse() -> None:
    with pytest.raises(ValidationError) as exc:
        StockCount.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("stock_count_date",) in error_fields
    assert ("warehouse",) in error_fields


def test_stock_batch_number_dump_by_alias_uses_exact_payload_keys() -> None:
    draft_transaction_id = uuid4()
    warehouse_id = uuid4()

    batch = StockBatchNumber(
        batch_number="BATCH-003",
        draft_stock_transaction_id=draft_transaction_id,
        quantity=7.0,
        stock_transaction_type=30,
        warehouse=warehouse_id,
    )

    dumped = batch.model_dump(by_alias=True)

    assert dumped["BatchNumber"] == "BATCH-003"
    assert dumped["DraftStockTransactionID"] == str(draft_transaction_id)
    assert dumped["Quantity"] == 7.0
    assert dumped["StockTransactionType"] == 30
    assert dumped["Warehouse"] == str(warehouse_id)


def test_stock_serial_number_dump_by_alias_uses_exact_payload_keys() -> None:
    draft_transaction_id = uuid4()
    warehouse_id = uuid4()

    serial = StockSerialNumber(
        draft_stock_transaction_id=draft_transaction_id,
        serial_number="SN-002",
        stock_transaction_type=40,
        warehouse=warehouse_id,
    )

    dumped = serial.model_dump(by_alias=True)

    assert dumped["DraftStockTransactionID"] == str(draft_transaction_id)
    assert dumped["SerialNumber"] == "SN-002"
    assert dumped["StockTransactionType"] == 40
    assert dumped["Warehouse"] == str(warehouse_id)


def test_stock_count_line_dump_by_alias_uses_exact_payload_keys() -> None:
    item_id = uuid4()
    stock_count_id = uuid4()

    line = StockCountLine(
        item=item_id,
        stock_count_id=stock_count_id,
        quantity_new=3.0,
    )

    dumped = line.model_dump(by_alias=True)

    assert dumped["Item"] == str(item_id)
    assert dumped["StockCountID"] == str(stock_count_id)
    assert dumped["QuantityNew"] == 3.0


def test_stock_count_dump_by_alias_includes_nested_lines() -> None:
    stock_count_id = uuid4()
    item_id = uuid4()
    warehouse_id = uuid4()
    count_date = datetime.now(timezone.utc)

    line = StockCountLine(
        item=item_id,
        stock_count_id=stock_count_id,
        quantity_new=1.0,
    )

    stock_count = StockCount(
        stock_count_id=stock_count_id,
        stock_count_date=count_date,
        warehouse=warehouse_id,
        stock_count_lines=[line],
    )

    dumped = stock_count.model_dump(by_alias=True)

    assert dumped["StockCountID"] == str(stock_count_id)
    assert dumped["StockCountDate"].replace("Z", "+00:00") == count_date.isoformat()
    assert dumped["Warehouse"] == str(warehouse_id)
    assert "StockCountLines" in dumped
    assert isinstance(dumped["StockCountLines"], list)
    assert len(dumped["StockCountLines"]) == 1

    dumped_line = dumped["StockCountLines"][0]
    assert dumped_line["Item"] == str(item_id)
    assert dumped_line["StockCountID"] == str(stock_count_id)
    assert dumped_line["QuantityNew"] == 1.0
