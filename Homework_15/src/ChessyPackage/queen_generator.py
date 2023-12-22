from itertools import combinations
from random import randint
from multiprocessing import Pool
from psutil import Process as UtilProc

from src.ChessyPackage.queen import Queen


__all__ = [
    "QueensGenerator"
]


class Coordinate:

    def __set_name__(self, owner, name):
        self._prop = f"_{name}"

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Not possible.')
        setattr(instance, self._prop, value)

    def __get__(self, instance, owner):
        return getattr(instance, self._prop)


class QueensGenerator:

    _instance = None

    x = Coordinate()
    y = Coordinate()

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, queens_count: int, x_start: int, y_start: int):
        """
        Queens generator
        :param queens_count: count of the generated queens == cell count
        :param x_start: symbol of the x - coordinates
        :param y_start: symbol of the y - coordinates
        """
        self.__queens_count = queens_count
        self.x = x_start
        self.y = y_start
        self._boards = None

    def create_board(self, process_number) -> list:
        """
        Generate one queen per x and y line
        """
        cpu = UtilProc().cpu_num()
        print(f"{process_number}st/th queens generation on cpu{cpu}.")
        target = []
        start = self.x
        while len(target) < self.__queens_count:
            target.append(Queen(start, randint(self.y,
                                          self.y + self.__queens_count)))
            start += 1
            for q1, q2 in combinations(target, 2):
                if q1.is_attack(q2):
                    target.clear()
                    start = 1
        return target

    def generate_boards(self, count: int) -> None:
        """
        Generates 4 sets of placements of 8 pieces on the board.
        Each set runs in a separate thread.
        :return: list of list
        """
        processes = [i for i in range(1, count + 1)]
        with Pool(count) as p:
            self._boards = board_list = p.map(self.create_board,
                                              processes)

    def boards_count(self):
        try:
            return len(self._boards)
        except TypeError:
            return 0

    def print_board(self, board: int) -> None:
        for row in range(self.x, self.x + self.__queens_count):
            for column in range(self.y, self.y + self.__queens_count):
                if (row, column) == self._boards[board][row - 1].coords:
                    print(f"{self._boards[board][row - 1].character:^5}",
                          end=' ')
                else:
                    print(f"{row:>2},{column:<2}", end=' ')
            print('\n')
