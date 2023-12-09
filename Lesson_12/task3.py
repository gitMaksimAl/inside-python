# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину на дескриптор с
# валидацией размера.

class Range:

    def __set_name__(self, owner, name):
        self._param_name = f"_{name}"

    def __get__(self, instance, owner):
        return getattr(instance, self._param_name)

    @staticmethod
    def _validate(value):
        if value <= 0:
            raise ValueError("Rectangle can't be with negative or zero side.")
    
    def __set__(self, instance, value):
        Range._validate(value)
        setattr(instance, self._param_name, value)


class Rectangle:

    __slots__ = (
        '_width',
        '_height'
    )

    width = Range()
    height = Range()

    def __init__(self, width: int | float, height: int | float=None):
        self._width = width
        self._height = height

    def perimeter(self) -> int:
        return int(2 * (self.width + self.height))

    def area(self) -> int:
        return int(self.width * self.height)

    def __str__(self):
        return f"Прямоугольник со сторонами {self.width} и {self.height}"

    def __repr__(self):
        return f"Rectangle({self.width}, {self.height})"

    def __add__(self, other: "Rectangle"):
        perimeter = self.perimeter() + other.perimeter()
        width = self.width + other.width
        height = perimeter / 2 - width
        return Rectangle(int(width), int(height))

    def __sub__(self, other: "Rectangle"):
        perimeter = abs(self.perimeter() - other.perimeter())
        width = abs(self.width - other.width)
        height = perimeter / 2 - width
        return Rectangle(int(width), int(height))

    def __eq__(self, other: "Rectangle") -> bool:
        return self.area() == other.area()

    def __lt__(self, other: "Rectangle") -> bool:
        return self.area() < other.area()

    def __le__(self, other: "Rectangle") -> bool:
        return self.area() <= other.area()


if __name__ == "__main__":
    r1 = Rectangle(1, 2)
    r1.width = 12
    print(type(r1.width))
    print(r1)
