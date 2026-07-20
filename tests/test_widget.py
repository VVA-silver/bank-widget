import pytest

from src.widget import get_date, mask_account_card


class TestMaskAccountCard:
    def test_visa_card(self) -> None:
        """Карта Visa маскируется корректно."""
        result = mask_account_card("Visa Platinum 7000792289606361")
        assert result == "Visa Platinum 7000 79** **** 6361"

    def test_account(self) -> None:
        """Счёт маскируется корректно."""
        result = mask_account_card("Счет 73654108430135874305")
        assert result == "Счет **4305"

    def test_returns_string(self) -> None:
        """Функция возвращает строку."""
        assert isinstance(mask_account_card("Visa Classic 1234567890123456"), str)

    def test_preserves_card_name(self) -> None:
        """Название карты сохраняется в результате."""
        result = mask_account_card("Mastercard 1234567890123456")
        assert result.startswith("Mastercard")

    def test_preserves_account_label(self) -> None:
        """Метка 'Счет' сохраняется в результате."""
        result = mask_account_card("Счет 12345678901234567890")
        assert result.startswith("Счет")

    @pytest.mark.parametrize(
        "card_info, expected",
        [
            ("Visa Platinum 7000792289606361", "Visa Platinum 7000 79** **** 6361"),
            ("Visa Classic 1234567890123456", "Visa Classic 1234 56** **** 3456"),
            ("Mastercard 9876543210987654", "Mastercard 9876 54** **** 7654"),
            ("Maestro 1234567890123456", "Maestro 1234 56** **** 3456"),
            ("МИР 1111222233334444", "МИР 1111 22** **** 4444"),
        ],
    )
    def test_various_card_types(self, card_info: str, expected: str) -> None:
        """Параметризованная проверка разных типов карт."""
        assert mask_account_card(card_info) == expected

    @pytest.mark.parametrize(
        "account_info, expected",
        [
            ("Счет 73654108430135874305", "Счет **4305"),
            ("Счет 12345678901234567890", "Счет **7890"),
            ("Счет 00000000001234", "Счет **1234"),
        ],
    )
    def test_various_accounts(self, account_info: str, expected: str) -> None:
        """Параметризованная проверка разных счетов."""
        assert mask_account_card(account_info) == expected


class TestGetDate:
    def test_standard_date(self) -> None:
        """Стандартная дата ISO преобразуется корректно."""
        result = get_date("2024-03-11T02:26:18.671407")
        assert result == "11.03.2024"

    def test_returns_string(self) -> None:
        """Функция возвращает строку."""
        assert isinstance(get_date("2024-03-11T02:26:18.671407"), str)

    def test_format_dd_mm_yyyy(self) -> None:
        """Формат результата ДД.ММ.ГГГГ."""
        result = get_date("2024-03-11T02:26:18.671407")
        parts = result.split(".")
        assert len(parts) == 3
        assert len(parts[0]) == 2  # день
        assert len(parts[1]) == 2  # месяц
        assert len(parts[2]) == 4  # год

    @pytest.mark.parametrize(
        "date_string, expected",
        [
            ("2024-03-11T02:26:18.671407", "11.03.2024"),
            ("2019-07-03T18:35:29.512364", "03.07.2019"),
            ("2018-06-30T02:08:58.425572", "30.06.2018"),
            ("2000-01-01T00:00:00.000000", "01.01.2000"),
            ("1999-12-31T23:59:59.999999", "31.12.1999"),
        ],
    )
    def test_various_dates(self, date_string: str, expected: str) -> None:
        """Параметризованная проверка разных дат."""
        assert get_date(date_string) == expected

    def test_date_without_time(self) -> None:
        """Дата без временной части обрабатывается корректно."""
        result = get_date("2024-03-11")
        assert result == "11.03.2024"

    def test_day_is_correct(self) -> None:
        """День извлекается правильно."""
        result = get_date("2024-03-11T00:00:00.000000")
        assert result.startswith("11")

    def test_month_is_correct(self) -> None:
        """Месяц извлекается правильно."""
        result = get_date("2024-03-11T00:00:00.000000")
        assert result[3:5] == "03"

    def test_year_is_correct(self) -> None:
        """Год извлекается правильно."""
        result = get_date("2024-03-11T00:00:00.000000")
        assert result.endswith("2024")
