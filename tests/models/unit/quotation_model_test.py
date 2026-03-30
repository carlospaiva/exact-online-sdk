from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    Quotation,
    QuotationLine,
    QuotationStatus,
)


def test_quotation_parses_alias_payload() -> None:
    quotation_id = uuid4()
    order_account = uuid4()
    line_id = uuid4()
    item_id = uuid4()
    charge_line_id = uuid4()
    quotation_date = datetime.now(timezone.utc)

    payload = {
        "QuotationID": str(quotation_id),
        "OrderAccount": str(order_account),
        "QuotationDate": quotation_date.isoformat(),
        "QuotationLines": [
            {
                "ID": str(line_id),
                "QuotationID": str(quotation_id),
                "Item": str(item_id),
                "Quantity": 4,
            }
        ],
        "QuotationOrderChargeLines": [
            {
                "ID": str(charge_line_id),
                "QuotationID": str(quotation_id),
                "AmountFCInclVAT": 20.0,
            }
        ],
        "Status": QuotationStatus.DRAFT.value,
    }

    quotation = Quotation.model_validate(payload)

    assert quotation.quotation_id == quotation_id
    assert quotation.order_account == order_account
    assert quotation.quotation_date == quotation_date
    assert quotation.status == QuotationStatus.DRAFT
    assert len(quotation.quotation_lines) == 1
    assert quotation.quotation_order_charge_lines is not None
    assert len(quotation.quotation_order_charge_lines) == 1

    line = quotation.quotation_lines[0]
    assert line.id == line_id
    assert line.quotation_id == quotation_id
    assert line.item == item_id
    assert line.quantity == 4

    charge_line = quotation.quotation_order_charge_lines[0]
    assert charge_line.id == charge_line_id


def test_quotation_defaults_lists() -> None:
    order_account = uuid4()

    quotation = Quotation.model_validate({"OrderAccount": str(order_account)})

    assert quotation.quotation_lines == []
    assert quotation.quotation_order_charge_lines is None


def test_quotation_requires_order_account() -> None:
    with pytest.raises(ValidationError) as exc:
        Quotation.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("order_account",) in error_fields


def test_quotation_line_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        QuotationLine.model_validate({"Quantity": 1})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("quotation_id",) in error_fields
    assert ("item",) in error_fields


def test_quotation_line_alias_input() -> None:
    quotation_id = uuid4()
    item_id = uuid4()

    line = QuotationLine.model_validate(
        {
            "QuotationID": str(quotation_id),
            "Item": str(item_id),
            "Quantity": 3,
            "UnitPrice": 19.99,
        }
    )

    assert line.quotation_id == quotation_id
    assert line.item == item_id
    assert line.quantity == 3
    assert line.unit_price == 19.99
