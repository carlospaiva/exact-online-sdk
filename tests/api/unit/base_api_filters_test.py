from __future__ import annotations

from datetime import date, datetime, timezone
from unittest.mock import MagicMock
from uuid import uuid4

import pytest

from exact_online_sdk.api.endpoints import BaseAPI
from exact_online_sdk.exceptions import ValidationError
from exact_online_sdk.models import StrictModel


class DummyModel(StrictModel):
    id: int
    name: str


class DummyAPI(BaseAPI):
    model_cls = DummyModel

    def _resource(self) -> str:
        return "crm/Dummy"


class DictOnlyAPI(BaseAPI):
    model_cls = None

    def _resource(self) -> str:
        return "crm/DictOnly"


def test_build_params_populates_query_and_filter() -> None:
    client = MagicMock()
    api = DummyAPI(client)

    params = {"custom": "1"}
    filters = {"Name": "Test"}
    select = ["ID", "Name"]

    result = api._build_params(
        params,
        filters,
        select,
        order_by="Name desc",
        top=10,
        skip=5,
    )

    assert result is not None
    assert result["$filter"] == "Name eq 'Test'"
    assert result["$select"] == "ID,Name"
    assert result["$orderby"] == "Name desc"
    assert result["$top"] == 10
    assert result["$skip"] == 5
    assert result["custom"] == "1"


def test_build_params_conflicting_filter_raises_validation_error() -> None:
    api = DummyAPI(MagicMock())

    with pytest.raises(ValidationError):
        api._build_params(
            {"$filter": "Existing"}, {"Name": "New"}, None, None, None, None
        )


def test_build_filter_and_format_value_supports_multiple_types() -> None:
    api = DummyAPI(MagicMock())
    u1 = uuid4()
    u2 = uuid4()
    today = date.today()
    now = datetime.now(timezone.utc)

    flt = api._build_filter(
        {
            "IdIn": ("in", [u1, u2]),
            "Active": True,
            "Count": 3,
            "CreatedOn": now,
            "BirthDate": today,
            "Name": "O'Reilly",
            "Nothing": None,
        }
    )

    assert "IdIn in (" in flt
    assert "guid'" in flt
    assert "active eq true" in flt.lower() or "Active eq true" in flt
    assert "Count eq 3" in flt
    assert "datetimeoffset" in flt
    assert today.isoformat() in flt
    assert "O''Reilly" in flt
    assert "Nothing eq null" in flt


def test_serialize_payload_accepts_strict_model_and_dict() -> None:
    api = DummyAPI(MagicMock())

    model = DummyModel(id=1, name="Acme")
    body_from_model = api._serialize_payload(model)
    assert body_from_model["id"] == 1
    assert body_from_model["name"] == "Acme"

    body_from_dict = api._serialize_payload({"id": 2, "name": "Foo"})
    assert body_from_dict["id"] == 2
    assert body_from_dict["name"] == "Foo"


def test_serialize_payload_rejects_non_dict_non_model() -> None:
    api = DummyAPI(MagicMock())

    with pytest.raises(ValidationError):
        api._serialize_payload("not-a-dict")  # type: ignore[arg-type]


def test_serialize_payload_validates_dict_with_model_cls() -> None:
    api = DummyAPI(MagicMock())

    with pytest.raises(ValidationError):
        api._serialize_payload({"id": "abc", "name": "Name"})


def test_serialize_payload_passes_through_when_no_model_cls() -> None:
    api = DictOnlyAPI(MagicMock())
    payload = {"any": "value"}

    assert api._serialize_payload(payload) is payload


def test_deserialize_item_success_and_error_paths() -> None:
    api = DummyAPI(MagicMock())

    ok = api._deserialize_item({"id": 1, "name": "X"}, raw=False)
    assert isinstance(ok, DummyModel)

    with pytest.raises(ValidationError):
        api._deserialize_item({"id": "abc", "name": "X"}, raw=False)


def test_deserialize_item_respects_raw_and_none() -> None:
    api = DummyAPI(MagicMock())

    data = {"id": 1, "name": "Raw"}
    assert api._deserialize_item(data, raw=True) is data
    assert api._deserialize_item(None, raw=False) is None


def test_deserialize_many_handles_none_scalar_and_list() -> None:
    api = DummyAPI(MagicMock())

    assert api._deserialize_many(None, raw=False) == []

    one = api._deserialize_many({"id": 1, "name": "One"}, raw=False)
    assert len(one) == 1
    assert isinstance(one[0], DummyModel)

    many = api._deserialize_many(
        [{"id": 1, "name": "One"}, {"id": 2, "name": "Two"}], raw=False
    )
    assert [m.id for m in many] == [1, 2]


def test_iter_pages_and_iter_all_use_client_iter_pages() -> None:
    client = MagicMock()
    client.iter_pages.return_value = [
        [{"id": 1, "name": "One"}],
        [{"id": 2, "name": "Two"}],
    ]
    api = DummyAPI(client)

    pages = list(api.iter_pages(filters={"id": 1}, page_size=10, raw=False))
    assert len(pages) == 2
    assert isinstance(pages[0][0], DummyModel)

    called_path = client.iter_pages.call_args[0][0]
    params = client.iter_pages.call_args[1]["params"]
    assert called_path == "crm/Dummy"
    assert "$filter" in params

    all_items = list(api.iter_all(page_size=10, raw=False))
    assert [item.id for item in all_items] == [1, 2]


# =============================================================================
# Regression Tests for JSON Response Negotiation Fix (Task 6)
# These tests prove that:
# - BaseAPI methods preserve caller-supplied $format overrides
# - raw=True semantics remain unaffected by negotiation changes
# - JSON deserialization continues to work correctly
# =============================================================================


def test_list_preserves_explicit_format_override() -> None:
    """Prove that list() preserves caller-supplied $format parameter."""
    client = MagicMock()
    client.get.return_value = [{"id": 1, "name": "Test"}]
    api = DummyAPI(client)

    api.list(params={"$format": "xml"})

    call_args = client.get.call_args
    params_passed = call_args[1]["params"]
    assert "$format" in params_passed
    assert params_passed["$format"] == "xml"


def test_iter_pages_preserves_explicit_format_override() -> None:
    """Prove that iter_pages() preserves caller-supplied $format parameter."""
    client = MagicMock()
    client.iter_pages.return_value = [[{"id": 1, "name": "Test"}]]
    api = DummyAPI(client)

    list(api.iter_pages(params={"$format": "atom"}, page_size=10))

    call_args = client.iter_pages.call_args
    params_passed = call_args[1]["params"]
    assert "$format" in params_passed
    assert params_passed["$format"] == "atom"


def test_iter_all_preserves_explicit_format_override() -> None:
    """Prove that iter_all() preserves caller-supplied $format parameter."""
    client = MagicMock()
    client.iter_pages.return_value = [[{"id": 1, "name": "Test"}]]
    api = DummyAPI(client)

    list(api.iter_all(params={"$format": "json"}, page_size=10))

    call_args = client.iter_pages.call_args
    params_passed = call_args[1]["params"]
    assert "$format" in params_passed
    assert params_passed["$format"] == "json"


def test_list_with_format_override_and_other_params() -> None:
    """Prove $format override works alongside other query parameters."""
    client = MagicMock()
    client.get.return_value = [{"id": 1, "name": "Test"}]
    api = DummyAPI(client)

    api.list(
        params={"$format": "xml", "custom": "value"},
        filters={"Name": "Test"},
        select=["ID", "Name"],
        top=5,
    )

    call_args = client.get.call_args
    params_passed = call_args[1]["params"]

    assert params_passed["$format"] == "xml"
    assert params_passed["custom"] == "value"
    assert "$filter" in params_passed
    assert "$select" in params_passed
    assert "$top" in params_passed


def test_raw_true_returns_unparsed_data() -> None:
    """Prove raw=True returns raw data without model deserialization."""
    client = MagicMock()
    raw_data = [{"id": 1, "name": "Raw"}]
    client.get.return_value = raw_data
    api = DummyAPI(client)

    result = api.list(raw=True)

    assert result == raw_data


def test_raw_true_in_get_returns_unparsed_data() -> None:
    """Prove raw=True in get() returns raw data without model deserialization."""
    client = MagicMock()
    raw_data = {"id": 1, "name": "Raw"}
    client.get.return_value = raw_data
    api = DummyAPI(client)

    result = api.get("guid-123", raw=True)

    assert result is raw_data


def test_raw_true_in_create_returns_unparsed_data() -> None:
    """Prove raw=True in create() returns raw data without model deserialization."""
    client = MagicMock()
    raw_data = {"id": 1, "name": "Created"}
    client.post.return_value = raw_data
    api = DummyAPI(client)

    result = api.create({"id": 1, "name": "Created"}, raw=True)

    assert result is raw_data


def test_raw_true_in_update_returns_unparsed_data() -> None:
    """Prove raw=True in update() returns raw data without model deserialization."""
    client = MagicMock()
    raw_data = {"id": 1, "name": "Updated"}
    client.patch.return_value = raw_data
    api = DummyAPI(client)

    result = api.update("guid-123", {"id": 1, "name": "Updated"}, raw=True)

    assert result is raw_data


def test_raw_true_in_iter_pages_returns_unparsed_items() -> None:
    """Prove raw=True in iter_pages() yields raw items without deserialization."""
    client = MagicMock()
    raw_items = [{"id": 1, "name": "One"}, {"id": 2, "name": "Two"}]
    client.iter_pages.return_value = [raw_items]
    api = DummyAPI(client)

    pages = list(api.iter_pages(raw=True))

    assert len(pages) == 1
    assert pages[0] == raw_items
    assert isinstance(pages[0][0], dict)
    assert not isinstance(pages[0][0], DummyModel)


def test_raw_true_in_iter_all_returns_unparsed_items() -> None:
    """Prove raw=True in iter_all() yields raw items without deserialization."""
    client = MagicMock()
    raw_items = [{"id": 1, "name": "One"}, {"id": 2, "name": "Two"}]
    client.iter_pages.return_value = [raw_items]
    api = DummyAPI(client)

    items = list(api.iter_all(raw=True))

    assert len(items) == 2
    assert isinstance(items[0], dict)
    assert not isinstance(items[0], DummyModel)


def test_raw_false_deserializes_to_model() -> None:
    """Prove raw=False (default) deserializes JSON to model instances."""
    client = MagicMock()
    client.get.return_value = [{"id": 1, "name": "Test"}]
    api = DummyAPI(client)

    result = api.list(raw=False)

    assert len(result) == 1
    assert isinstance(result[0], DummyModel)
    assert result[0].id == 1
    assert result[0].name == "Test"


def test_json_deserialization_works_after_negotiation_changes() -> None:
    """Prove JSON payloads deserialize correctly after negotiation fix."""
    client = MagicMock()

    client.get.return_value = [{"id": 1, "name": "Test"}]
    api = DummyAPI(client)

    result = api.list()
    assert isinstance(result[0], DummyModel)

    client.get.return_value = {"id": 2, "name": "Single"}
    single = api.get("guid-123")
    assert isinstance(single, DummyModel)
    assert single.id == 2

    client.post.return_value = {"id": 3, "name": "Created"}
    created = api.create({"id": 3, "name": "Created"})
    assert isinstance(created, DummyModel)
    assert created.id == 3

    client.patch.return_value = {"id": 4, "name": "Updated"}
    updated = api.update("guid-123", {"id": 4, "name": "Updated"})
    assert isinstance(updated, DummyModel)
    assert updated.id == 4


def test_iter_pages_deserializes_json_correctly() -> None:
    """Prove iter_pages() deserializes JSON payloads correctly."""
    client = MagicMock()
    client.iter_pages.return_value = [
        [{"id": 1, "name": "One"}],
        [{"id": 2, "name": "Two"}],
    ]
    api = DummyAPI(client)

    pages = list(api.iter_pages(raw=False))

    assert len(pages) == 2
    assert isinstance(pages[0][0], DummyModel)
    assert pages[0][0].id == 1
    assert pages[1][0].id == 2


def test_iter_all_deserializes_json_correctly() -> None:
    """Prove iter_all() deserializes JSON payloads correctly."""
    client = MagicMock()
    client.iter_pages.return_value = [
        [{"id": 1, "name": "One"}],
        [{"id": 2, "name": "Two"}],
    ]
    api = DummyAPI(client)

    items = list(api.iter_all(raw=False))

    assert len(items) == 2
    assert isinstance(items[0], DummyModel)
    assert items[0].id == 1
    assert items[1].id == 2


def test_format_override_with_iterators() -> None:
    """Prove $format override is preserved through iterator chains."""
    client = MagicMock()
    client.iter_pages.return_value = [[{"id": 1, "name": "Test"}]]
    api = DummyAPI(client)

    list(api.iter_all(params={"$format": "xml"}, page_size=10))

    call_args = client.iter_pages.call_args
    params_passed = call_args[1]["params"]
    assert params_passed["$format"] == "xml"


def test_dict_only_api_raw_mode() -> None:
    """Prove DictOnlyAPI (no model_cls) raw mode works correctly."""
    client = MagicMock()
    raw_data = [{"custom": "value"}]
    client.get.return_value = raw_data
    api = DictOnlyAPI(client)

    result_raw = api.list(raw=True)
    assert result_raw == raw_data

    result_not_raw = api.list(raw=False)
    assert result_not_raw == raw_data
