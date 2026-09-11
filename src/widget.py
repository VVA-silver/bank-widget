from src.masks import get_mask_card_number, get_mask_account


def mask_account_card(card_info: str) -> str:
    """
    Маскирует номер карты или счёта.

    :param card_info: строка с типом и номером, например
        'Visa Platinum 1234567890123456' или 'Счет 12345678901234567890'
    :return: строка с замаскированным номером
    """
    name, number = card_info.rsplit(" ", 1)

    if name == "Счет":
        return f"{name} {get_mask_account(number)}"

    return f"{name} {get_mask_card_number(number)}"


def get_date(date_string: str) -> str:
    """
    Преобразует дату из формата ISO в формат ДД.ММ.ГГГГ.

    :param date_string: дата в формате '2024-03-11T02:26:18.671407'
    :return: дата в формате '11.03.2024'
    """
    date = date_string[:10]
    year, month, day = date.split("-")
    return f"{day}.{month}.{year}"
