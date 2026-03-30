from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    BulkCRMAccount,
    BulkCRMAddress,
    BulkCRMContact,
    BulkCRMQuotation,
)


def test_bulk_crm_account_parses_aliases() -> None:
    account_id = uuid4()

    account = BulkCRMAccount.model_validate({"ID": str(account_id), "Name": "Bulk Co"})

    assert isinstance(account, BulkCRMAccount)
    assert account.id == account_id
    assert account.name == "Bulk Co"


def test_bulk_crm_address_parses_datetime_fields() -> None:
    created = datetime.now(timezone.utc)

    address = BulkCRMAddress.model_validate({"Created": created.isoformat()})

    assert isinstance(address, BulkCRMAddress)
    assert address.created == created


def test_bulk_crm_contact_validator_applies() -> None:
    with pytest.raises(ValidationError) as exc:
        BulkCRMContact.model_validate({"Account": str(uuid4())})

    errors = exc.value.errors()
    assert errors[0]["type"] == "value_error"
    assert "FirstName" in errors[0]["msg"] or "LastName" in errors[0]["msg"]


def test_bulk_crm_quotation_defaults_nested_collections() -> None:
    quotation = BulkCRMQuotation.model_validate({"OrderAccount": str(uuid4())})

    assert isinstance(quotation, BulkCRMQuotation)
    assert quotation.quotation_lines == []
    assert quotation.quotation_order_charge_lines is None
