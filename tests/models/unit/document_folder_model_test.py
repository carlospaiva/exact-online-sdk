from __future__ import annotations

from datetime import datetime, timezone
from uuid import uuid4

import pytest
from pydantic import ValidationError

from exact_online_sdk.models import DocumentFolder


def test_document_folder_requires_code_and_description() -> None:
    with pytest.raises(ValidationError) as exc:
        DocumentFolder.model_validate({})

    error_fields = {tuple(err["loc"]) for err in exc.value.errors()}
    assert ("code",) in error_fields
    assert ("description",) in error_fields


def test_document_folder_parses_aliases() -> None:
    folder_id = uuid4()
    created = datetime.now(timezone.utc)

    folder = DocumentFolder.model_validate(
        {
            "ID": str(folder_id),
            "Code": "ARCH",
            "Description": "Archive",
            "Created": created.isoformat(),
        }
    )

    assert folder.id == folder_id
    assert folder.code == "ARCH"
    assert folder.description == "Archive"
    assert folder.created == created
