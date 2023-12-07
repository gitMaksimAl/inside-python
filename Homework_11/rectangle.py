class Rectangle:

    def __init__(self, width: int | float, height: int | float=None):
        self.width = width
        self.height = height

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
        return Rectangle(width, height)

    def __sub__(self, other: "Rectangle"):
        """
                Subtraction of figures by perimeter is possible
                if one of their sides is equals.
                :param other:
                :return:
                """
        if self.perimeter() < other.perimeter():
            return None
        perimeter = self.perimeter() - other.perimeter()
        if self.width == other.width:
            length = perimeter / 2
            width = self.width
        elif self.height == other.height:
            width = perimeter / 2
            length = self.height
        else:
            raise TypeError('the operation is possible only on similar objects')
        return Rectangle(width, length)

    def __eq__(self, other: "Rectangle"):
        return self.area() == other.area()

    def __lt__(self, other: "Rectangle"):
        return self.area() < other.area()

    def __le__(self, other: "Rectangle"):
        return self.area() <= other.area()


if __name__ == "__main__":
    r1 = Rectangle(5, 10)
    r2 = Rectangle(3, 7)
    print(r1, r2, sep='\n')
