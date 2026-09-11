from typing import List


def filter_by_state(data: List[dict], state: str = "EXECUTED") -> List[dict]:
    """
    Фильтрует список словарей по значению ключа 'state'.

    :param data: список словарей с банковскими операциями
    :param state: значение статуса для фильтрации (по умолчанию 'EXECUTED')
    :return: отфильтрованный список словарей
    """
    return [item for item in data if item.get("state") == state]


def sort_by_date(data: List[dict], reverse: bool = True) -> List[dict]:
    """
    Сортирует список словарей по значению ключа 'date'.

    :param data: список словарей с банковскими операциями
    :param reverse: порядок сортировки; True — убывание (новые первыми),
                    False — возрастание (старые первыми); по умолчанию True
    :return: новый список словарей, отсортированный по дате
    """
    return sorted(data, key=lambda item: item.get("date", ""), reverse=reverse)
