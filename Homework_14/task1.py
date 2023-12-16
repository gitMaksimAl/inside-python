class NegativeValueError(Exception):

    def __init__(self, side, value):
        super().__init__(f"{side} должна быть положительной, а не {value}")


class WidthValue:

    def __set_name__(self, owner, name):
        self._value = f"_{name}"

    def __set__(self, instance, value):
        if value <= 0:
            raise NegativeValueError('Ширина', value)
        setattr(instance, self._value, value)

    def __get__(self, instance, owner):
        return getattr(instance, self._value)


class HeightValue:

    def __set_name__(self, owner, name):
        self._value = f"_{name}"

    def __set__(self, instance, value):
        if value <= 0:
            raise NegativeValueError('Высота', value)
        setattr(instance, self._value, value)

    def __get__(self, instance, owner):
        return getattr(instance, self._value)


class Rectangle:
    """
    >>> r1 = Rectangle(5)
    >>> r1.width
    5
    >>> r4 = Rectangle(-2)
    Traceback (most recent call last):
    ...
    task1.NegativeValueError: Ширина должна быть положительной, а не -2
    >>> r2 = Rectangle(3, 4)
    >>> r2.width
    3
    >>> r2.height
    4
    """

    width = WidthValue()
    height = HeightValue()

    def __init__(self, width, height=None):
        self.width = width
        if height is None:
            self.height = width
        else:
            self.height = height

    def perimeter(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.perimeter()
        20
        >>> r2 = Rectangle(3, 4)
        >>> r2.perimeter()
        14
        """
        return 2 * (self.width + self.height)

    def area(self):
        """
        >>> r1 = Rectangle(5)
        >>> r1.area()
        25
        >>> r2 = Rectangle(3, 4)
        >>> r2.area()
        12
        """
        return self.width * self.height

    def __add__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 + r2
        >>> r3.width
        8
        >>> r3.height
        6.0
        """
        perimeter = self.perimeter() + other.perimeter()
        width = self.width + other.width
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __sub__(self, other):
        """
        >>> r1 = Rectangle(5)
        >>> r2 = Rectangle(3, 4)
        >>> r3 = r1 - r2
        >>> r3.width
        2
        >>> r3.height
        2.0
        """
        if self.perimeter() < other.perimeter():
            # never do this shit
            self, other = other, self
        width = abs(self.width - other.width)
        perimeter = self.perimeter() - other.perimeter()
        height = perimeter / 2 - width
        return Rectangle(width, height)

    def __lt__(self, other):
        return self.area() < other.area()

    def __eq__(self, other):
        return self.area() == other.area()

    def __le__(self, other):
        return self.area() <= other.area()

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"


if __name__ == "__main__":
    r1 = Rectangle(3, -0.2)
    print(f"{r1} created!")
    r1.height = -1.1
    print(r1)
