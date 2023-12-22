from itertools import combinations as combs


__all__ = [
    "Queen"
]


class Queen:

    def __init__(self, x: int, y: int, actor: str='♛'):
        self._x = x
        self._y = y
        self.character = actor

    @property
    def coords(self):
        return self._x, self._y

    @coords.setter
    def coords(self, value):
        self._x, self._y = value

    @property
    def actor(self):
        return self.character

    @actor.setter
    def actor(self, value):
        self.character = value

    def is_attack(self, other: 'Queen') -> bool:
        """
        >>> q1 = Queen(1, 1)
        >>> q2 = Queen(5, 5)
        >>> q1.is_attack(q2)
        True
        >>> q3 = Queen(5, 1)
        >>> q3.is_attack(q1)
        True
        >>> q3.is_attack(q2)
        True
        """
        if other._x == self._x or other._y == self._y:
            return True
        if abs(other._x - self._x) == abs(other._y - self._y):
            return True
        return False

    @staticmethod
    def check_queens(queen_list: list['Queen']):
        """
        >>> ls = [Queen(1, 1), Queen(2, 3), Queen(3, 5), Queen(4, 7), \
        Queen(5, 2), Queen(6, 4), Queen(7, 6), Queen(8, 8)]
        >>> Queen.check_queens(ls)
        False
        """
        return not any(map(lambda pair: pair[0].is_attack(pair[1]),
                           combs(queen_list, 2)))

    def __eq__(self, other: 'Queen'):
        """
        >>> q1 = Queen(1, 8)
        >>> q2 = Queen(8, 1)
        >>> q1 == q2
        False
        >>> q3 = Queen(1, 8)
        >>> q3 == q1
        True
        """
        return self._x == other._x and self._y == other._y

    def __hash__(self):
        return hash((self._x, self._y))

    def __repr__(self):
        return f"Queen({self._x}, {self._y})"

    def __str__(self):
        return f"({self._x}, {self._y})"

