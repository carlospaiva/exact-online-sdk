from __future__ import annotations

from uuid import UUID, uuid4

import pytest
from pydantic import ValidationError
from pydantic_core import ErrorDetails

from exact_online_sdk.models.base import StrictModel, _snake_to_pascal


class ExampleModel(StrictModel):
    id: UUID
    account_manager_full_name: str
    optional_field: str | None = None


def test_snake_to_pascal_alias_generation() -> None:
    assert _snake_to_pascal("account_manager_full_name") == "AccountManagerFullName"
    assert _snake_to_pascal("id") == "ID"


def test_strict_model_accepts_alias_input() -> None:
    identifier = uuid4()
    model = ExampleModel.model_validate(
        {
            "ID": str(identifier),
            "AccountManagerFullName": "Ada Lovelace",
            "OptionalField": "value",
        }
    )

    assert model.id == identifier
    assert model.account_manager_full_name == "Ada Lovelace"
    assert model.optional_field == "value"


def test_strict_model_populates_by_field_name() -> None:
    identifier = uuid4()
    model = ExampleModel(id=identifier, account_manager_full_name="Alan Turing")

    dumped = model.model_dump(by_alias=True)
    assert dumped == {
        "ID": str(identifier),
        "AccountManagerFullName": "Alan Turing",
        "OptionalField": None,
    }


def test_strict_model_forbids_extra_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        ExampleModel.model_validate(
            {
                "ID": str(uuid4()),
                "AccountManagerFullName": "Grace Hopper",
                "unexpected": "boom",
            }
        )

    error: list[ErrorDetails] = exc.value.errors()
    assert error[0]["type"] == "extra_forbidden"
