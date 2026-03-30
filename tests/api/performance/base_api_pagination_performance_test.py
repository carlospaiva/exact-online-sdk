from __future__ import annotations

import time
from typing import Any, List
from unittest.mock import MagicMock

import pytest

from exact_online_sdk.api.endpoints import BaseAPI
from exact_online_sdk.models import StrictModel

pytestmark = pytest.mark.performance


class DummyModel(StrictModel):
    id: int
    name: str


class DummyAPI(BaseAPI):
    model_cls = DummyModel

    def _resource(self) -> str:
        return "crm/Dummy"


def test_iter_all_large_result_set_is_fast() -> None:
    client = MagicMock()

    pages: List[List[dict[str, Any]]] = [
        [{"id": i, "name": f"Name {i}"} for i in range(page * 100, (page + 1) * 100)]
        for page in range(5)
    ]
    client.iter_pages.return_value = pages

    api = DummyAPI(client)

    start = time.perf_counter()
    items = list(api.iter_all(page_size=100))
    elapsed = time.perf_counter() - start

    assert len(items) == 500
    assert isinstance(items[0], DummyModel)
    assert elapsed < 1.0
