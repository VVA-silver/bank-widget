def get_mask_card_number(card_number: int | str) -> str:
    """
    Маскирует номер банковской карты.

    :param card_number: номер карты (16 цифр)
    :return: строка вида '1234 56** **** 7890'
    """
    card_number = str(card_number)
    return f"{card_number[:4]} " f"{card_number[4:6]}** " f"**** " f"{card_number[-4:]}"


def get_mask_account(account_number: int | str) -> str:
    """
    Маскирует номер банковского счёта.

    :param account_number: номер счёта
    :return: строка вида '**7890'
    """
    account_number = str(account_number)
    return f"**{account_number[-4:]}"
