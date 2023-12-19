# Напишите программу, которая использует модуль logging для вывода сообщения об
# ошибке в файл. Например отлавливаем ошибку деления на ноль.

import logging
from typing import Callable

# logging.basicConfig(level=logging.ERROR, filename='task1.log', filemode='a',
#                     encoding='utf-8')
# loger = logging.getLogger('task1')
#
# try:
#     print(2 / 0)
# except ZeroDivisionError:
#     loger.error('Divisor is ZERO!')


def my_logger(func: Callable) -> Callable:
    FORMAT = "{levelname} - {asctime}\n\t{msg}"
    logging.basicConfig(level=logging.INFO, filename=f'{func.__name__}',
                        filemode='a', encoding='utf-8',
                        format=FORMAT, style='{')
    loger = logging.getLogger()

    def wrapper(*args, **kwargs):
        data = {'args': args, **kwargs}
        data['result'] = func(*args, **kwargs)
        loger.info(data)

    return wrapper


@my_logger
def get_sum(*args, **kwargs):
    return sum(args)


if __name__ == "__main__":
    get_sum(1, 2, 3, 4)

