from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import Document


def test_document_parses_alias_payload() -> None:
    document_id = uuid4()
    attachment_id = uuid4()
    created = datetime.now(timezone.utc)

    payload = {
        "ID": str(document_id),
        "Subject": "Document",
        "Type": 10,
        "Created": created.isoformat(),
        "Attachments": [
            {
                "ID": str(attachment_id),
                "AttachmentFileName": "contract.pdf",
                "AttachmentFileSize": 12.5,
                "AttachmentUrl": "https://example.com/contract.pdf",
                "CanShowInWebView": True,
            }
        ],
    }

    document = Document.model_validate(payload)

    assert document.id == document_id
    assert document.subject == "Document"
    assert document.type == 10
    assert document.created == created
    assert document.attachments is not None
    assert len(document.attachments) == 1

    attachment = document.attachments[0]
    assert attachment.id == attachment_id
    assert attachment.attachment_file_name == "contract.pdf"
    assert attachment.attachment_file_size == 12.5
    assert attachment.attachment_url == "https://example.com/contract.pdf"
    assert attachment.can_show_in_web_view is True


def test_document_requires_subject_and_type() -> None:
    with pytest.raises(ValidationError) as exc:
        Document.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("subject",) in error_fields
    assert ("type",) in error_fields
