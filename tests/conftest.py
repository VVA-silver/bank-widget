import pytest


# ---------------------------------------------------------------------------
# Фикстуры для модуля masks
# ---------------------------------------------------------------------------


@pytest.fixture
def valid_card_number() -> str:
    return "7000792289606361"


@pytest.fixture
def valid_account_number() -> str:
    return "73654108430135874305"


# ---------------------------------------------------------------------------
# Фикстуры для модуля processing
# ---------------------------------------------------------------------------


@pytest.fixture
def operations() -> list[dict]:
    return [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]


@pytest.fixture
def operations_same_date() -> list[dict]:
    return [
        {"id": 1, "state": "EXECUTED", "date": "2024-01-01T10:00:00.000000"},
        {"id": 2, "state": "EXECUTED", "date": "2024-01-01T10:00:00.000000"},
        {"id": 3, "state": "CANCELED", "date": "2024-01-01T10:00:00.000000"},
    ]


@pytest.fixture
def operations_no_state() -> list[dict]:
    return [
        {"id": 1, "date": "2024-01-01T10:00:00.000000"},
        {"id": 2, "date": "2023-05-15T08:30:00.000000"},
    ]


@pytest.fixture
def operations_empty() -> list[dict]:
    return []
