import pytest
from src.generators import (
filter_by_currency, transaction_descriptions, card_number_generator,
)

@pytest.fixture
def transactions():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100.00",
                "currency": {
                    "name": "USD",
                    "code": "USD",
                },
            }, "description": "Перевод организации",
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200.00",
                "currency":
                    { "name": "EUR",
                      "code": "EUR",
                },
            },
            "description": "Перевод со счета на счет",
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300.00",
                "currency": {
                    "name": "USD",
                    "code": "USD",
                },
            },
            "description": "Перевод с карты на карту",
        },
    ]

@pytest.mark.parametrize(
    "currency, expected_ids",
    [
        ("USD", [1, 3]),
        ("EUR", [2]),
        ("GBP", []),
    ],
)
def test_filter_by_currency(transactions, currency, expected_ids):
    result = list(filter_by_currency(transactions, currency))

    assert [transaction["id"] for transaction in result] == expected_ids

def test_filter_by_currency_empty_list():
    assert list(filter_by_currency([], "USD")) == []
def test_filter_by_currency_without_currency():
    transactions = [
        {
            "id": 1,
            "description": "Без валюты",
        }
    ]

    assert list(filter_by_currency(transactions, "USD")) == []

@pytest.mark.parametrize(
    "count",
    [0, 1, 2, 3],
)
def test_transaction_descriptions(transactions, count):
    result = list(transaction_descriptions(transactions[:count]))
    expected = [
         "Перевод организации",
         "Перевод со счета на счет",
         "Перевод с карты на карту",
    ][:count]
    assert result == expected

def test_transaction_descriptions_empty_list():
    assert list(transaction_descriptions([])) == []

@pytest.mark.parametrize(
    "start, stop, expected",
    [
        (
                1,
                5,
                [ "0000 0000 0000 0001",
                  "0000 0000 0000 0002",
                  "0000 0000 0000 0003",
                  "0000 0000 0000 0004",
                  "0000 0000 0000 0005",
                ],
        ),
        (
                9999999999999998,
                9999999999999999,
                [
                    "9999 9999 9999 9998",
                    "9999 9999 9999 9999",
                ],
        ),
    ],
)
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected

def test_card_number_format():
    result = list(card_number_generator(1, 1))
    assert result == ["0000 0000 0000 0001"]
    assert len(result[0]) == 19
    assert result[0].count(" ") == 3

def test_card_number_generator_single_value():
    generator = card_number_generator(1234, 1234)
    assert next(generator) == "0000 0000 0000 1234"
    with pytest.raises(StopIteration):
        next(generator)

def test_card_number_generator_empty_range():
    assert list(card_number_generator(5, 1)) == []