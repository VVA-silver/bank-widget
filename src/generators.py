def filter_by_currency(transactions, currency):
    """Возвращает транзакции, соответствующие заданной валюте."""
    for transaction in transactions:
        if (
            transaction.get("operationAmount", {})
            .get("currency", {})
            .get("code")
            == currency
        ):
            yield transaction


def transaction_descriptions(transactions):
    """Возвращает описания транзакций по очереди."""
    for transaction in transactions:
        yield transaction.get("description", "")


def card_number_generator(start, stop):
    """Генерирует номера банковских карт в формате XXXX XXXX XXXX XXXX."""
    for number in range(start, stop + 1):
        card_number = f"{number:016d}"
        yield " ".join(
            card_number[i:i + 4] for i in range(0, 16, 4)
        )