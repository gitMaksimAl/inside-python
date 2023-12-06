# Создайте класс окружность.
# Класс должен принимать радиус окружности при создании экземпляра.
# У класса должно быть два метода, возвращающие длину окружности и её площадь.
from math import pi


class Circle:

    def __init__(self, radius: int):
        self.radius = radius

    def perimeter(self):
        return 2 * pi * self.radius

    def square(self):
        return pi * self.radius ** 2


# Создайте класс прямоугольник.
# Класс должен принимать длину и ширину при создании экземпляра.
# У класса должно быть два метода, возвращающие периметр и площадь.
# Если при создании экземпляра передаётся только одна сторона, считаем что у
# нас квадрат.


class Rectangle:

    def __init__(self, width: int, height: int=None):
        self.width = width
        self.height = height if height else width

    def perimeter(self):
        return 2 * (self.width + self.height)

    def area(self):
        return self.width * self.height

    def __repr__(self):
        return f"Rectangle({self.width=}, {self.height=})"


# Напишите класс для хранения информации о человеке: ФИО, возраст и т.п. на
# ваш выбор. У класса должны быть методы birthday для увеличения возраста на
# год, full_name для вывода полного ФИО и т.п. на ваш выбор. Убедитесь,
# что свойство возраст недоступно для прямого изменения, но есть возможность
# получить текущий возраст.
class Person:

    def __init__(self, name: str, surname: str, lastname: str, age: int):
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.__age = age

    @property
    def age(self) -> int:
        return self.__age

    def fullname(self):
        return f"{self.name} {self.surname} {self.lastname}"


# Создайте класс Сотрудник.
# Воспользуйтесь классом человека из прошлого задания.
# У сотрудника должен быть:
# шестизначный идентификационный номер
# уровень доступа вычисляемый как остаток от деления суммы цифр id на семь

class Employee(Person):
    MAX_LEVEL: int = 7

    def __init__(self, name: str, surname: str, lastname: str,
                 age: int, person_id: int):
        super().__init__(name, surname, lastname, age)
        if 100_000 <= person_id < 1_000_000:
            self.id = person_id
        else:
            self.id = 100_000

    def get_level(self):
        return sum(int(num) for num in str(self.id)) % Employee.MAX_LEVEL


if __name__ == "__main__":
    c = Circle(3)
    r = Rectangle(5, 8)
    p = Person('Arseni', 'Efgrafov', 'Sergeevich', 33)
    e = Employee('Inokenti', 'Drobinin', 'Ivanovich', 32, 102_342)
    print(c.square(), c.perimeter(), sep='\n')
    print(r.area(), r.perimeter(), sep='\n')
    print(f"{p.fullname()}, age: {p.age}")
    print(f"{e.fullname()}, age: {e.age}, level:{e.get_level()}")
