# Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
# Экземпляр должен запоминать последние k значений.
# Параметр k передаётся при создании экземпляра.
# Добавьте метод для просмотра ранее вызываемых значений и их факториалов.

from json import dump
from collections import deque
# Создайте менеджер контекста, который при выходе сохраняет значения в
# JSON файл.


class Factorial:

    def __init__(self, num: int=0):
        self._history = deque(maxlen=5)
        self._end = num

    def __call__(self, *args, **kwargs):
        if args:
            self._end = args[0]
        result = 1
        for mult in range(2, self._end + 1):
            result *= mult
        self._history.append({self._end: result})
        return result

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        with open('history.json', 'w', encoding='utf-8') as f:
            for item in self._history:
                dump(item, f, indent=2)

    @property
    def history(self):
        return self._history


if __name__ == "__main__":
    with Factorial() as f:
        f(5)
        f(12)
        f(4)
