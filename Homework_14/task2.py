import unittest


class NegativeValueError(ValueError):
    pass


class Rectangle:

    def __init__(self, width, height=None):
        if width <= 0:
            raise NegativeValueError(f'Ширина должна быть положительной,'
                                      f' а не {width}')
        self._width = width
        if height is None:
            self._height = width
        else:
            if height <= 0:
                raise NegativeValueError(f'Высота должна быть положительной,'
                                         f' а не {height}')
            self._height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if value > 0:
            self._width = value
        else:
            raise NegativeValueError(f'Ширина должна быть положительной,'
                                     f' а не {value}')

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value > 0:
            self._height = value
        else:
            raise NegativeValueError(f'Высота должна быть положительной,'
                                      f' а не {value}')

    def perimeter(self):
        return 2 * (self._width + self._height)

    def area(self):
        return self._width * self._height

    def __add__(self, other):
        width = self._width + other._width
        perimeter = self.perimeter() + other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        if self.perimeter() < other.perimeter():
            self, other = other, self
        width = abs(self._width - other._width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)


class TestRectangle(unittest.TestCase):

    def setUp(self) -> None:
        self.r1 = Rectangle(5)
        self.r2 = Rectangle(3, 4)

    def test_width(self):
        self.assertEqual(self.r1.width, 5)

    def test_height(self):
        self.assertEqual(self.r2.height, 4)

    def test_perimeter(self):
        self.assertEqual(self.r1.perimeter(), 20)

    def test_area(self):
        self.assertEqual(self.r2.area(), 12)

    def test_addition(self):
        r3 = self.r1 + self.r2
        with self.subTest():
            self.assertEqual(r3.width, 8)
            self.assertEqual(r3.height, 6.0)
