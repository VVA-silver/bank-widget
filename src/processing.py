from typing import List


def filter_by_state(data: List[dict], state: str = "EXECUTED") -> List[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: список словарей с банковскими операциями
    :param state: значение статуса для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    return [item for item in data if item.get("state") == state]
