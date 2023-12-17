class Rectangle:

    def __init__(self, width: int | float, height: int | float=None):
        self.width = width
        self.height = height if height else width

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
    rect1 = Rectangle(5, 10)
    rect2 = Rectangle(3, 7)

    print(f"Периметр rect1: {rect1.perimeter()}")
    print(f"Площадь rect2: {rect2.area()}")
    print(f"rect1 < rect2: {rect1 < rect2}")
    print(f"rect1 == rect2: {rect1 == rect2}")
    print(f"rect1 <= rect2: {rect1 <= rect2}")

    rect3 = rect1 + rect2
    print(f"Периметр rect3: {rect3.perimeter()}")
    rect4 = rect1 - rect2
    print(f"Ширина rect4: {rect4.width}")
    print(Rectangle(3, 7) <= Rectangle(5, 10))
    print(Rectangle(4, 5) <= Rectangle(3, 3))
