from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import (
    EmploymentConditionGroup,
    GLClassification,
    ProjectWBS,
    RequestAttachment,
    TransactionLine,
)


def test_employment_condition_group_parses_aliases() -> None:
    uid = uuid4()

    obj = EmploymentConditionGroup.model_validate(
        {
            "ID": str(uid),
            "Code": "ECG01",
            "Description": "Full-time",
            "HoursPerWeek": 40.0,
            "SBICode": "6201",
        }
    )

    assert obj.id == uid
    assert obj.code == "ECG01"
    assert obj.hours_per_week == 40.0
    assert obj.sbi_code == "6201"


def test_employment_condition_group_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        EmploymentConditionGroup.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_request_attachment_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        RequestAttachment.model_validate({})


def test_request_attachment_parses_aliases() -> None:
    uid = uuid4()

    obj = RequestAttachment.model_validate(
        {
            "ID": str(uid),
            "FileName": "doc.pdf",
            "FileSize": 1024.0,
            "Division": 1,
            "DownloadUrl": "https://example.com/doc.pdf",
        }
    )

    assert obj.id == uid
    assert obj.file_name == "doc.pdf"
    assert obj.file_size == 1024.0


def test_request_attachment_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        RequestAttachment.model_validate({"FileName": "x.pdf", "UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_gl_classification_parses_aliases() -> None:
    uid = uuid4()

    obj = GLClassification.model_validate(
        {
            "ID": str(uid),
            "Code": "GLC001",
            "Description": "Balance Sheet",
            "Abstract": True,
            "Nillable": False,
            "PeriodType": "instant",
        }
    )

    assert obj.id == uid
    assert obj.code == "GLC001"
    assert obj.abstract is True
    assert obj.nillable is False
    assert obj.period_type == "instant"


def test_gl_classification_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        GLClassification.model_validate({"UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_transaction_line_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        TransactionLine.model_validate({})


def test_transaction_line_parses_aliases() -> None:
    uid = uuid4()
    entry_id = uuid4()
    dt = datetime.now(timezone.utc)

    obj = TransactionLine.model_validate(
        {
            "ID": str(uid),
            "EntryID": str(entry_id),
            "AmountDC": 500.0,
            "AmountFC": 500.0,
            "GLAccount": str(uuid4()),
            "GLAccountCode": "8000",
            "Date": dt.isoformat(),
            "LineNumber": 1,
            "Status": 20,
            "Type": 20,
        }
    )

    assert obj.id == uid
    assert obj.entry_id == entry_id
    assert obj.amount_dc == 500.0
    assert obj.gl_account_code == "8000"
    assert obj.line_number == 1
    assert obj.status == 20


def test_transaction_line_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        TransactionLine.model_validate(
            {"EntryID": str(uuid4()), "UnknownField": "value"}
        )

    assert exc.value.errors()[0]["type"] == "extra_forbidden"


def test_project_wbs_requires_mandatory_fields() -> None:
    with pytest.raises(ValidationError):
        ProjectWBS.model_validate({})


def test_project_wbs_parses_aliases() -> None:
    uid = uuid4()
    start = datetime.now(timezone.utc)

    obj = ProjectWBS.model_validate(
        {
            "ID": str(uid),
            "Description": "Phase 1",
            "Cost": 10000.0,
            "Hours": 100.0,
            "Revenue": 15000.0,
            "StartDate": start.isoformat(),
            "Type": 1,
            "BlockEntry": False,
            "SequenceNumber": 10,
        }
    )

    assert obj.id == uid
    assert obj.description == "Phase 1"
    assert obj.cost == 10000.0
    assert obj.hours == 100.0
    assert obj.revenue == 15000.0
    assert obj.block_entry is False
    assert obj.sequence_number == 10


def test_project_wbs_forbids_unknown_fields() -> None:
    with pytest.raises(ValidationError) as exc:
        ProjectWBS.model_validate({"Description": "X", "UnknownField": "value"})

    assert exc.value.errors()[0]["type"] == "extra_forbidden"
