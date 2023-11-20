# Добавьте в пакет, созданный на семинаре шахматный модуль.
# Внутри него напишите код, решающий задачу о 8 ферзях, включающий в себя
# функцию is_attacking(q1,q2), проверяющую, бьют ли ферзи друг друга и
# check_queens(queens), которая проверяет все возможные пары ферзей.
# Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били
# друг друга. Вам дана расстановка 8 ферзей на доске, определите, есть ли среди
# них пара бьющих друг друга. Программа получает на вход восемь пар чисел,
# каждое число от 1 до 8 - координаты 8 ферзей. Если ферзи не бьют друг друга
# верните истину, а если бьют - ложь. Не забудьте напечатать результат.

from itertools import combinations

queens = [[(1, 1), (2, 3), (3, 5), (4, 7), (5, 2), (6, 4), (7, 6), (8, 8)],
    [(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)],
    [(1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8)],
    [(1, 1), (2, 1), (3, 1), (4, 1), (5, 1), (6, 1), (7, 1), (8, 1)],
    [],
    [(4, 4)]]


def is_attacking(q1: tuple[int, int], q2: tuple[int, int]) -> bool:
    if q2[0] == q1[0] or q2[1] == q1[1]:
        return True
    if abs(q2[0] - q1[0]) == abs(q2[1] - q1[1]):
        return True
    if sum(q2) == sum(q1):
        return True
    return False


def check_queens(queen_set: list[tuple[int, int]]) -> bool:
    return not any(map(lambda pair: is_attacking(*pair),
                   combinations(queen_set, 2)))


def print_table(rows: int, columns: int,
                figures: list[tuple[int, int]]) -> None:
    for row in range(1, rows + 1):
        for column in range(1, columns + 1):
            if (row, column) in figures:
                print(f"{'♛':^5}", end=' ')
            else:
                print(f"{row:>2},{column:<2}", end=' ')
        print('\n')


# print_table(8, 8, queens)
for combo in queens:
    print(check_queens(combo))
