# Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных
# расстановки.
import random
from itertools import combinations, combinations_with_replacement
from random import randint, seed
from task2 import is_attacking
from threading import Thread
from pprint import pprint


def __create_board(target: list, length: int, start: int) -> None:
    while len(target) < length:
        target.append((randint(start, 8), randint(1, 8)))
        for q1, q2 in combinations(target, 2):
            if is_attacking(q1, q2):
                try:
                    target.remove(q2)
                except ValueError:
                    continue
    print('Out')


def generate_boards():
    board_list = []
    threads = {}
    for i in (0, 2, 4, 6):
        for j in range(i, i + 2):
            board_list.append([])
            threads[str(j)] = Thread(target=__create_board,
                                     name=f'board_{j}',
                                     args=(board_list[j], 8, j + 1))
            threads[str(j)].start()
        for thread in threads:
            threads[thread].join()
    return board_list


# print(*generate_boards())
generate_boards()