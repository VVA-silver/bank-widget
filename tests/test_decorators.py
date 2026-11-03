import pytest

from decorators import log


def test_log_to_file(tmp_path):
    """Проверить запись успешного результата в файл."""
    log_file = tmp_path / "mylog.txt"

    @log(filename=str(log_file))
    def add(x: int, y: int) -> int:
        return x + y

    result = add(1, 2)

    assert result == 3
    assert log_file.read_text(encoding="utf-8") == "add ok\n"


def test_log_to_console(capsys):
    """Проверить вывод успешного результата в консоль."""

    @log()
    def greet() -> str:
        return "Hello"

    result = greet()
    captured = capsys.readouterr()

    assert result == "Hello"
    assert "greet ok" in captured.err


def test_log_error_to_file(tmp_path):
    """Проверить логирование ошибки и входных аргументов."""
    log_file = tmp_path / "errors.txt"

    @log(filename=str(log_file))
    def divide(x: int, y: int) -> float:
        return x / y

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    output = log_file.read_text(encoding="utf-8")

    assert "divide error: ZeroDivisionError" in output
    assert "Inputs: (1, 0), {}" in output


def test_log_error_to_console(capsys):
    """Проверить вывод ошибки в консоль."""

    @log()
    def fail(value: int) -> None:
        raise ValueError("invalid value")

    with pytest.raises(ValueError, match="invalid value"):
        fail(10)

    captured = capsys.readouterr()

    assert "fail error: ValueError" in captured.err
    assert "Inputs: (10,), {}" in captured.err


def test_log_keyword_arguments(tmp_path):
    """Проверить логирование именованных аргументов."""
    log_file = tmp_path / "kwargs.txt"

    @log(filename=str(log_file))
    def greet(name: str, greeting: str = "Hello") -> str:
        return f"{greeting}, {name}"

    assert greet(name="Anna") == "Hello, Anna"

    output = log_file.read_text(encoding="utf-8")
    assert "greet ok" in output