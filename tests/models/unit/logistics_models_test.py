from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    CustomerItem,
    Incoterm,
    ItemAssortment,
    ItemAssortmentProperty,
    ItemChargeRelation,
)

# ---------------------------------------------------------------------------
# CustomerItem
# ---------------------------------------------------------------------------


def test_customer_item_parses_aliases() -> None:
    ci_id = uuid4()
    account_id = uuid4()
    item_id = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "ID": str(ci_id),
        "Account": str(account_id),
        "AccountCode": "CUST-001",
        "AccountName": "Acme Corp",
        "Item": str(item_id),
        "ItemCode": "ITEM-001",
        "CustomerItemCode": "CI-001",
        "Created": now.isoformat(),
        "Type": "Standard",
    }

    ci = CustomerItem.model_validate(payload)

    assert ci.id == ci_id
    assert ci.account == account_id
    assert ci.account_code == "CUST-001"
    assert ci.item == item_id
    assert ci.customer_item_code == "CI-001"
    assert ci.type == "Standard"
    assert ci.created == now


def test_customer_item_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        CustomerItem.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("account",) in error_fields
    assert ("item",) in error_fields


def test_customer_item_optional_fields_default_to_none() -> None:
    account_id = uuid4()
    item_id = uuid4()

    ci = CustomerItem(account=account_id, item=item_id)

    assert ci.id is None
    assert ci.account_code is None
    assert ci.customer_item_code is None
    assert ci.type is None


def test_customer_item_dump_by_alias() -> None:
    account_id = uuid4()
    item_id = uuid4()

    ci = CustomerItem(account=account_id, item=item_id, customer_item_code="CI-X")

    dumped = ci.model_dump(by_alias=True)

    assert dumped["Account"] == str(account_id)
    assert dumped["Item"] == str(item_id)
    assert dumped["CustomerItemCode"] == "CI-X"


def test_customer_item_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        CustomerItem.model_validate(
            {
                "Account": str(uuid4()),
                "Item": str(uuid4()),
                "Bogus": "bad",
            }
        )


# ---------------------------------------------------------------------------
# Incoterm
# ---------------------------------------------------------------------------


def test_incoterm_parses_aliases() -> None:
    payload = {
        "ID": 1,
        "Code": "FOB",
        "Description": "Free on Board",
        "Version": 2020,
    }

    ic = Incoterm.model_validate(payload)

    assert ic.id == 1
    assert ic.code == "FOB"
    assert ic.description == "Free on Board"
    assert ic.version == 2020


def test_incoterm_all_optional() -> None:
    ic = Incoterm()

    assert ic.id is None
    assert ic.code is None
    assert ic.description is None
    assert ic.version is None


def test_incoterm_dump_by_alias() -> None:
    ic = Incoterm(id=5, code="CIF", description="Cost Insurance Freight")

    dumped = ic.model_dump(by_alias=True)

    assert dumped["ID"] == 5
    assert dumped["Code"] == "CIF"
    assert dumped["Description"] == "Cost Insurance Freight"


def test_incoterm_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        Incoterm.model_validate({"Code": "FOB", "Unknown": 42})


# ---------------------------------------------------------------------------
# ItemAssortment
# ---------------------------------------------------------------------------


def test_item_assortment_parses_aliases() -> None:
    ia_id = uuid4()

    payload = {
        "ID": str(ia_id),
        "Code": 10,
        "Description": "Assortment A",
        "Division": 1,
    }

    ia = ItemAssortment.model_validate(payload)

    assert ia.id == ia_id
    assert ia.code == 10
    assert ia.description == "Assortment A"
    assert ia.division == 1


def test_item_assortment_all_optional() -> None:
    ia = ItemAssortment()

    assert ia.id is None
    assert ia.code is None
    assert ia.properties is None


def test_item_assortment_dump_by_alias() -> None:
    ia = ItemAssortment(code=20, description="Assortment B")

    dumped = ia.model_dump(by_alias=True)

    assert dumped["Code"] == 20
    assert dumped["Description"] == "Assortment B"


# ---------------------------------------------------------------------------
# ItemAssortmentProperty
# ---------------------------------------------------------------------------


def test_item_assortment_property_parses_aliases() -> None:
    prop_id = uuid4()

    payload = {
        "ID": str(prop_id),
        "Code": "PROP-1",
        "Description": "Color",
        "Division": 1,
        "ItemAssortmentCode": 10,
    }

    prop = ItemAssortmentProperty.model_validate(payload)

    assert prop.id == prop_id
    assert prop.code == "PROP-1"
    assert prop.description == "Color"
    assert prop.item_assortment_code == 10


def test_item_assortment_property_all_optional() -> None:
    prop = ItemAssortmentProperty()

    assert prop.id is None
    assert prop.code is None
    assert prop.item_assortment_code is None


def test_item_assortment_property_dump_by_alias() -> None:
    prop = ItemAssortmentProperty(
        code="PROP-2", description="Size", item_assortment_code=5
    )

    dumped = prop.model_dump(by_alias=True)

    assert dumped["Code"] == "PROP-2"
    assert dumped["Description"] == "Size"
    assert dumped["ItemAssortmentCode"] == 5


# ---------------------------------------------------------------------------
# ItemChargeRelation
# ---------------------------------------------------------------------------


def test_item_charge_relation_parses_aliases() -> None:
    rel_id = uuid4()
    charge_id = uuid4()
    item_id = uuid4()
    now = datetime.now(timezone.utc)

    payload = {
        "ID": str(rel_id),
        "Amount": 25.50,
        "ChargeCode": "FREIGHT",
        "ChargeDescription": "Freight charge",
        "ChargeID": str(charge_id),
        "ChargeVATCode": "V21",
        "ChargeVATPercentage": 21.0,
        "ChargeVATType": "E",
        "ItemID": str(item_id),
        "ItemCode": "ITEM-100",
        "Currency": "EUR",
        "Quantity": 10.0,
        "TotalAmount": 255.0,
        "Created": now.isoformat(),
    }

    rel = ItemChargeRelation.model_validate(payload)

    assert rel.id == rel_id
    assert rel.amount == 25.50
    assert rel.charge_code == "FREIGHT"
    assert rel.charge_id == charge_id
    assert rel.charge_vat_percentage == 21.0
    assert rel.charge_vat_type == "E"
    assert rel.item_id == item_id
    assert rel.currency == "EUR"
    assert rel.quantity == 10.0
    assert rel.total_amount == 255.0
    assert rel.created == now


def test_item_charge_relation_all_optional() -> None:
    rel = ItemChargeRelation()

    assert rel.id is None
    assert rel.amount is None
    assert rel.charge_id is None
    assert rel.item_id is None
    assert rel.quantity is None


def test_item_charge_relation_dump_by_alias() -> None:
    item_id = uuid4()
    charge_id = uuid4()

    rel = ItemChargeRelation(
        item_id=item_id,
        charge_id=charge_id,
        amount=10.0,
        quantity=5.0,
        total_amount=50.0,
    )

    dumped = rel.model_dump(by_alias=True)

    assert dumped["ItemID"] == str(item_id)
    assert dumped["ChargeID"] == str(charge_id)
    assert dumped["Amount"] == 10.0
    assert dumped["Quantity"] == 5.0
    assert dumped["TotalAmount"] == 50.0


def test_item_charge_relation_rejects_extra_fields() -> None:
    with pytest.raises(ValidationError):
        ItemChargeRelation.model_validate({"Amount": 10.0, "Bogus": "bad"})
