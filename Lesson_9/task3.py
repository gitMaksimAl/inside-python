# Создайте декоратор с параметром.
# Параметр - целое число, количество запусков декорируемой функции.

from typing import Callable, Any
from functools import wraps


def to_times(count: int=1) -> Callable:

    def save_result(func: Callable) -> Callable:
        results = []

        @wraps(func)
        def wrapp(*args, **kwargs) -> list:
            for _ in range(count):
                results.append(func(*args, **kwargs))

            return results

        return wrapp

    return save_result


@to_times(3)
def foo(a: Any, b: Any, c: Any) -> str:
    return f"{a} - {b} - {c}"


if __name__ == "__main__":
    print(foo(1, 2, 3))
