# Напишите для задачи 1 тесты pytest. Проверьте следующие варианты:
# возврат строки без изменений
# возврат строки с преобразованием регистра без потери символов
# возврат строки с удалением знаков пунктуации
# возврат строки с удалением букв других алфавитов
# возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)

import pytest

from task1 import del_not_ascii


def test_not_change():
    assert del_not_ascii('HelloWorld') == 'HelloWorld'


def test_del_punkts():
    assert del_not_ascii('Hello, World!!!') == 'HelloWorld'


def test_not_ascii():
    assert del_not_ascii('Привет Мир') == ''
