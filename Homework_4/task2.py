# Напишите функцию key_params, принимающую на вход только ключевые параметры и
# возвращающую словарь, где ключ - значение переданного аргумента, а значение
# - имя аргумента.
# Если ключ не хешируем, используйте его строковое представление.
from typing import Hashable


def key_params(**kwargs):
    k_args = {}
    for key, value in kwargs.items():
        if not isinstance(value, Hashable) or value is None:
            k_args[str(value)] = key
        else:
            k_args[value] = key
    return k_args


print(key_params(a=12,  b=10, c='hello', d=[1, 2, 3], e=True, f=[], g=None))
