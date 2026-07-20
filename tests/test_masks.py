import pytest

from src.masks import get_mask_account, get_mask_card_number


class TestGetMaskCardNumber:
    def test_standard_16_digit_card(self, valid_card_number: str) -> None:
        """Стандартная 16-значная карта маскируется правильно."""
        result = get_mask_card_number(valid_card_number)
        assert result == "7000 79** **** 6361"

    def test_returns_string(self, valid_card_number: str) -> None:
        """Функция всегда возвращает строку."""
        assert isinstance(get_mask_card_number(valid_card_number), str)

    def test_accepts_int(self) -> None:
        """Функция принимает int и корректно маскирует."""
        result = get_mask_card_number(7000792289606361)
        assert result == "7000 79** **** 6361"

    @pytest.mark.parametrize(
        "card_number, expected",
        [
            ("1234567890123456", "1234 56** **** 3456"),
            ("0000000000000000", "0000 00** **** 0000"),
            ("9999999999999999", "9999 99** **** 9999"),
            ("1111222233334444", "1111 22** **** 4444"),
        ],
    )
    def test_various_card_numbers(self, card_number: str, expected: str) -> None:
        """Параметризованная проверка разных номеров карт."""
        assert get_mask_card_number(card_number) == expected

    def test_mask_format_has_spaces(self, valid_card_number: str) -> None:
        """Результат содержит пробелы в нужных позициях."""
        result = get_mask_card_number(valid_card_number)
        parts = result.split(" ")
        assert len(parts) == 4

    def test_mask_hides_middle_digits(self, valid_card_number: str) -> None:
        """Средние цифры заменены на звёздочки."""
        result = get_mask_card_number(valid_card_number)
        assert "**" in result

    def test_first_four_digits_visible(self, valid_card_number: str) -> None:
        """Первые 4 цифры видны в результате."""
        result = get_mask_card_number(valid_card_number)
        assert result.startswith("7000")

    def test_last_four_digits_visible(self, valid_card_number: str) -> None:
        """Последние 4 цифры видны в результате."""
        result = get_mask_card_number(valid_card_number)
        assert result.endswith("6361")


class TestGetMaskAccount:
    def test_standard_account_number(self, valid_account_number: str) -> None:
        """Стандартный номер счёта маскируется правильно."""
        result = get_mask_account(valid_account_number)
        assert result == "**4305"

    def test_returns_string(self, valid_account_number: str) -> None:
        """Функция всегда возвращает строку."""
        assert isinstance(get_mask_account(valid_account_number), str)

    def test_accepts_int(self) -> None:
        """Функция принимает int."""
        result = get_mask_account(73654108430135874305)
        assert result.startswith("**")

    def test_starts_with_double_asterisk(self, valid_account_number: str) -> None:
        """Результат начинается с **."""
        result = get_mask_account(valid_account_number)
        assert result.startswith("**")

    def test_shows_last_four_digits(self, valid_account_number: str) -> None:
        """Последние 4 цифры видны."""
        result = get_mask_account(valid_account_number)
        assert result.endswith("4305")

    @pytest.mark.parametrize(
        "account_number, expected",
        [
            ("12345678901234567890", "**7890"),
            ("00000000001234", "**1234"),
            ("9999", "**9999"),
            (12345678, "**5678"),
        ],
    )
    def test_various_account_numbers(self, account_number: str | int, expected: str) -> None:
        """Параметризованная проверка разных номеров счетов."""
        assert get_mask_account(account_number) == expected

    def test_short_account_number(self) -> None:
        """Короткий номер счёта — возвращает ** + все цифры."""
        result = get_mask_account("12")
        assert result == "**12"
