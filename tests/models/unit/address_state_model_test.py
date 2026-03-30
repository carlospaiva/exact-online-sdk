from __future__ import annotations

import pytest

from exact_online_sdk.models import AddressState


def test_address_state_parses_alias_and_geo_fields() -> None:
    state = AddressState.model_validate(
        {
            "ID": "6b5bca64-bf96-4ae0-9c33-8ce49963d8da",
            "Country": "US",
            "DisplayValue": "California",
            "Latitude": "36.7783",
            "Longitude": "-119.4179",
            "Name": "California",
            "State": "CA",
        }
    )

    assert state.country == "US"
    assert state.display_value == "California"
    assert state.latitude == pytest.approx(36.7783)
    assert state.longitude == pytest.approx(-119.4179)
    assert state.state == "CA"


def test_address_state_invalid_latitude_raises() -> None:
    with pytest.raises(ValueError):
        AddressState.model_validate({"Latitude": "not-a-number"})
