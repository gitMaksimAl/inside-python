# Используйте генератор случайных чисел для случайной расстановки ферзей в
# задаче выше. Проверяйте различный случайные варианты и выведите 4 успешных
# расстановки.
"""
Eight queens problem.
"""
from itertools import combinations
from random import randint
from multiprocessing import Pool
from psutil import Process as ps_process

from task2 import is_attacking

__START_COORD = 1
__END_COORD = 8
__QUEENS_COUNT = 8
__BOARDS_COUNT = 4


def __create_board(process_number) -> list:
    """
    The function writes 8 pairs of coordinates (range 1-8) to the target by
    randomly selecting numbers. At the first intersection of the coordinates
    specified in the 'is_attack' function, the search starts all over again.
    :param target: list
    :param length: count of coordinates pair
    :return:
    """
    cpu = ps_process().cpu_num()
    target = []
    start = __START_COORD
    while len(target) < __QUEENS_COUNT:
        target.append((start, randint(__START_COORD, __END_COORD)))
        start += 1
        for q1, q2 in combinations(target, 2):
            if is_attacking(q1, q2):
                target.clear()
                start = 1
    print(f"\x1B[3mProcess N{process_number},"
          f"cpu N{cpu}: done!\x1B[0m", end='\r')
    return target


def generate_boards() -> list[list]:
    """
    Generates 4 sets of placements of 8 pieces on the board.
    Each set runs in a separate thread.
    :return: list of list
    """
    processes = [i for i in range(1, __BOARDS_COUNT + 1)]
    with Pool(__BOARDS_COUNT) as p:
        board_list = p.map(__create_board, processes)
    return board_list


if __name__ == '__main__':
    from timeit import timeit
    print(timeit(stmt=generate_boards, number=3))
