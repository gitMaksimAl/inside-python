# Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных
# расстановки.
"""
Eight queens problem.
"""
from itertools import combinations
from random import randint
from threading import Thread, current_thread

from task2 import is_attacking

__QUEENS_COUNT = 8
__BOARDS_COUNT = 4


def __create_board(target: list, length: int) -> None:
    """
    The function writes 8 pairs of coordinates (range 1-8) to the target by
    randomly selecting numbers. At the first intersection of the coordinates
    specified in the 'is_attack' function, the search starts all over again.
    :param target: list
    :param length: count of coordinates pair
    :return:
    """
    start = 1
    while len(target) < length:
        target.append((start, randint(1, __QUEENS_COUNT)))
        start += 1
        for q1, q2 in combinations(target, 2):
            if is_attacking(q1, q2):
                target.clear()
                start = 1
    print(f'{current_thread().name}: \x1B[3mdone\x1B[0m', end='\r')


def generate_boards() -> list[list]:
    """
    Generates 4 sets of placements of 8 pieces on the board.
    Each set runs in a separate thread.
    :return: list of list
    """
    board_list = []
    threads = {}
    for i in range(__BOARDS_COUNT):
        board_list.append([])
        threads[f'{i}'] = Thread(target=__create_board,
                                name=f'board_{i}',
                                args=(board_list[i], __QUEENS_COUNT))
        threads[f'{i}'].start()
        for thread in threads.values():
            thread.join()
    return board_list


if __name__ == '__main__':
    for board in generate_boards():
        print(board)
