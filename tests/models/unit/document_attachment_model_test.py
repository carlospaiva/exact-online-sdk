from __future__ import annotations

from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import DocumentAttachment


def test_document_attachment_parses_aliases() -> None:
    document_id = uuid4()

    attachment = DocumentAttachment.model_validate(
        {
            "Document": str(document_id),
            "FileName": "attachment.txt",
            "FileSize": 4.2,
            "Url": "https://example.com/attachment.txt",
        }
    )

    assert attachment.document == document_id
    assert attachment.file_name == "attachment.txt"
    assert attachment.file_size == 4.2
    assert attachment.url == "https://example.com/attachment.txt"


def test_document_attachment_requires_document_and_file_name() -> None:
    with pytest.raises(ValidationError) as exc:
        DocumentAttachment.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("document",) in error_fields
    assert ("file_name",) in error_fields
