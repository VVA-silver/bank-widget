import pytest

from src.processing.processing import filter_by_state, sort_by_date


class TestFilterByState:
    def test_filter_executed(self, operations: list[dict]) -> None:
        """Фильтрация по статусу EXECUTED."""
        result = filter_by_state(operations, state="EXECUTED")
        assert len(result) == 2
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_filter_canceled(self, operations: list[dict]) -> None:
        """Фильтрация по статусу CANCELED."""
        result = filter_by_state(operations, state="CANCELED")
        assert len(result) == 2
        assert all(op["state"] == "CANCELED" for op in result)

    def test_default_state_is_executed(self, operations: list[dict]) -> None:
        """По умолчанию фильтруется статус EXECUTED."""
        result = filter_by_state(operations)
        assert all(op["state"] == "EXECUTED" for op in result)

    def test_returns_list(self, operations: list[dict]) -> None:
        """Функция возвращает список."""
        result = filter_by_state(operations)
        assert isinstance(result, list)

    def test_empty_list(self, operations_empty: list[dict]) -> None:
        """Пустой список возвращает пустой список."""
        result = filter_by_state(operations_empty)
        assert result == []

    def test_no_matching_state(self, operations: list[dict]) -> None:
        """Если нет совпадений по state, возвращается пустой список."""
        result = filter_by_state(operations, state="PENDING")
        assert result == []

    def test_operations_without_state_key(self, operations_no_state: list[dict]) -> None:
        """Операции без ключа state не проходят фильтр."""
        result = filter_by_state(operations_no_state, state="EXECUTED")
        assert result == []

    @pytest.mark.parametrize(
        "state, expected_count",
        [
            ("EXECUTED", 2),
            ("CANCELED", 2),
            ("PENDING", 0),
            ("DECLINED", 0),
        ],
    )
    def test_various_states(self, operations: list[dict], state: str, expected_count: int) -> None:
        """Параметризованная проверка разных статусов."""
        result = filter_by_state(operations, state=state)
        assert len(result) == expected_count

    def test_filter_with_same_state(self, operations_same_date: list[dict]) -> None:
        """Фильтрация списка, где все имеют одинаковый статус."""
        result = filter_by_state(operations_same_date, state="EXECUTED")
        assert len(result) == 2

    def test_original_list_not_mutated(self, operations: list[dict]) -> None:
        """Оригинальный список не изменяется."""
        original_length = len(operations)
        filter_by_state(operations, state="EXECUTED")
        assert len(operations) == original_length


class TestSortByDate:
    def test_sort_descending_by_default(self, operations: list[dict]) -> None:
        """По умолчанию сортировка по убыванию (новые первыми)."""
        result = sort_by_date(operations)
        assert result[0]["date"] == "2019-07-03T18:35:29.512364"
        assert result[-1]["date"] == "2018-06-30T02:08:58.425572"

    def test_sort_ascending(self, operations: list[dict]) -> None:
        """Сортировка по возрастанию (старые первыми)."""
        result = sort_by_date(operations, reverse=False)
        assert result[0]["date"] == "2018-06-30T02:08:58.425572"
        assert result[-1]["date"] == "2019-07-03T18:35:29.512364"

    def test_returns_list(self, operations: list[dict]) -> None:
        """Функция возвращает список."""
        result = sort_by_date(operations)
        assert isinstance(result, list)

    def test_returns_new_list(self, operations: list[dict]) -> None:
        """Функция возвращает новый список, не изменяя оригинальный."""
        original_first_id = operations[0]["id"]
        result = sort_by_date(operations)
        assert operations[0]["id"] == original_first_id
        assert result is not operations

    def test_empty_list(self, operations_empty: list[dict]) -> None:
        """Пустой список возвращает пустой список."""
        result = sort_by_date(operations_empty)
        assert result == []

    def test_same_dates(self, operations_same_date: list[dict]) -> None:
        """Операции с одинаковыми датами сортируются стабильно."""
        result = sort_by_date(operations_same_date)
        assert len(result) == 3
        assert all(op["date"] == "2024-01-01T10:00:00.000000" for op in result)

    def test_sorting_preserves_all_items(self, operations: list[dict]) -> None:
        """Все элементы сохраняются после сортировки."""
        result = sort_by_date(operations)
        assert len(result) == len(operations)

    @pytest.mark.parametrize("reverse", [True, False])
    def test_sort_direction(self, operations: list[dict], reverse: bool) -> None:
        """Параметризованная проверка направления сортировки."""
        result = sort_by_date(operations, reverse=reverse)
        dates = [op["date"] for op in result]
        if reverse:
            assert dates == sorted(dates, reverse=True)
        else:
            assert dates == sorted(dates, reverse=False)

    def test_operations_without_date_key(self) -> None:
        """Операции без ключа date обрабатываются (пустая строка)."""
        ops = [
            {"id": 1},
            {"id": 2, "date": "2024-01-01T00:00:00.000000"},
        ]
        result = sort_by_date(ops)
        # Операция без даты (пустая строка) окажется в конце при reverse=True
        assert result[0]["id"] == 2
        assert result[1]["id"] == 1
