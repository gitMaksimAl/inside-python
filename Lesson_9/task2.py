# Напишите декоратор, который сохраняет в json файл параметры декорируемой
# функции и результат, который она возвращает. При повторном вызове файл должен
# расширяться, а не перезаписываться.
# Каждый ключевой параметр сохраните как отдельный ключ json словаря.
# Для декорирования напишите функцию, которая может принимать как позиционные,
# так и ключевые аргументы.
# Имя файла должно совпадать с именем декорируемой функции.

from json import load as j_load, dump as j_dump
from pathlib import Path
from typing import Callable, Any
from functools import wraps


def invoke_logg(func: Callable) -> Callable:
    """
    Wrapper. Logging of the function invoke(params and result) to json fie.
    :param func: callable function.
    :return: inner function.
    """
    target = Path(func.__name__).with_suffix('.json')
    data = []
    if not target.exists():
        target.with_suffix('.json').touch(0o644, exist_ok=False)
    else:
        with target.open('r', encoding='utf-8', newline='') as f:
            f_data = (j_load(f))
            if isinstance(f_data, list):
                data += f_data
            else:
                data.append(f_data)

    @wraps(func)
    def invoke_and_save(*args, **kwargs):
        func_data = {'args': args, **kwargs}
        func_data['result'] = func(*args, **kwargs)
        data.append(func_data)

        with target.open('w', encoding='utf-8') as f:
            j_dump(data, f, indent=2)

    return invoke_and_save


# @invoke_logg
def concat_args(*args, **kwargs) -> Any:
    return f"{args} {kwargs}"


if __name__ == "__main__":
    concat_args(num1=12, num2=30)
