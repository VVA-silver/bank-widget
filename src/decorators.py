import logging
from functools import wraps
from typing import Any, Callable, ParamSpec, TypeVar

P = ParamSpec("P")
R = TypeVar("R")


def log(
    filename: str | None = None,
) -> Callable[[Callable[P, R]], Callable[P, R]]:
    """Логировать результат выполнения функции или возникшую ошибку."""
    logger = logging.getLogger(
        f"log_decorator_{filename or 'console'}"
    )
    logger.setLevel(logging.INFO)
    logger.propagate = False

    if not logger.handlers:
        if filename:
            handler = logging.FileHandler(
                filename,
                encoding="utf-8",
            )
        else:
            handler = logging.StreamHandler()

        handler.setFormatter(logging.Formatter("%(message)s"))
        logger.addHandler(handler)

    def decorator(func: Callable[P, R]) -> Callable[P, R]:
        """Обернуть функцию логированием."""
        @wraps(func)
        def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
            """Записать результат или ошибку вызова функции."""
            try:
                result = func(*args, **kwargs)
            except Exception as error:
                logger.error(
                    "%s error: %s. Inputs: %s, %s",
                    func.__name__,
                    type(error).__name__,
                    args,
                    kwargs,
                )
                raise

            logger.info("%s ok", func.__name__)
            return result

        return wrapper

    return decorator