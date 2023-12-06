# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

from Lesson_10.task1 import Rectangle


class RectangleExtend(Rectangle):

    def __init__(self, a: int, b: int):
        super(RectangleExtend, self).__init__(a, b)

    def __add__(self, other: Rectangle):
        perimeter = self.perimeter() + other.perimeter()
        width = self.width + other.width
        length = perimeter / 2 - width
        return RectangleExtend(width, length)

    def __sub__(self, other: Rectangle):
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
        return RectangleExtend(width, length)

    def __eq__(self, other: Rectangle):
        return self.area() == other.area()

    def __lt__(self, other: Rectangle):
        return self.area() < other.area()

    def __qt__(self, other: Rectangle):
        return self.area() > other.area()

    def __repr__(self):
        return f"RectangleMixin({self.width=}, {self.height=})"


if __name__ == "__main__":
    r1 = Rectangle(3, 1)
    r2 = RectangleExtend(3, 5)
    r3 = r2 + r1
    r4 = r2 - r1
    print(f"{r1.perimeter()=}, {r2.perimeter()=},"
          f" {r3.perimeter()=}, {r3.area()=}\n")
    print(f"{r2=}: {r2.perimeter()=}\n- {r1=}: {r1.perimeter()=}\n = {r4=}"
          f"{r4.perimeter()=}")

