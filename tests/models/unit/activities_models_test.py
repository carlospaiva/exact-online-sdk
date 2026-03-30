from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    CommunicationNote,
    Complaint,
    Event,
    ServiceRequest,
    Task,
)


def test_communication_note_parses_aliases() -> None:
    uid = uuid4()
    created = datetime.now(timezone.utc)

    obj = CommunicationNote.model_validate(
        {
            "ID": str(uid),
            "AccountName": "Acme",
            "Subject": "Call back",
            "Status": 1,
            "StatusDescription": "Open",
            "Created": created.isoformat(),
            "HID": 100,
        }
    )

    assert obj.id == uid
    assert obj.account_name == "Acme"
    assert obj.subject == "Call back"
    assert obj.status == 1
    assert obj.hid == 100


def test_communication_note_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        CommunicationNote.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_complaint_parses_aliases() -> None:
    uid = uuid4()

    obj = Complaint.model_validate(
        {
            "ID": str(uid),
            "AccountName": "Client X",
            "Complaint": "Product defective",
            "Status": 2,
            "StatusDescription": "In Progress",
        }
    )

    assert obj.id == uid
    assert obj.complaint == "Product defective"
    assert obj.status == 2


def test_complaint_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Complaint.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_event_parses_aliases() -> None:
    uid = uuid4()
    start = datetime.now(timezone.utc)
    end = start.replace(hour=(start.hour + 1) % 24)

    obj = Event.model_validate(
        {
            "ID": str(uid),
            "Description": "Team meeting",
            "StartDate": start.isoformat(),
            "EndDate": end.isoformat(),
            "Status": 0,
        }
    )

    assert obj.id == uid
    assert obj.description == "Team meeting"
    assert obj.start_date == start
    assert obj.end_date == end


def test_event_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Event.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_service_request_parses_aliases() -> None:
    uid = uuid4()
    receipt = datetime.now(timezone.utc)

    obj = ServiceRequest.model_validate(
        {
            "ID": str(uid),
            "Description": "Server down",
            "ReceiptDate": receipt.isoformat(),
            "Status": 1,
            "StatusDescription": "Open",
        }
    )

    assert obj.id == uid
    assert obj.description == "Server down"
    assert obj.receipt_date == receipt


def test_service_request_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        ServiceRequest.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_task_parses_aliases() -> None:
    uid = uuid4()
    action_date = datetime.now(timezone.utc)

    obj = Task.model_validate(
        {
            "ID": str(uid),
            "Description": "Follow up with client",
            "ActionDate": action_date.isoformat(),
            "TaskType": 1,
            "TaskTypeDescription": "Call",
            "Status": 0,
        }
    )

    assert obj.id == uid
    assert obj.description == "Follow up with client"
    assert obj.action_date == action_date
    assert obj.task_type == 1


def test_task_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        Task.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"
