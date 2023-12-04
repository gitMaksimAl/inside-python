"""
Class Animal with childs.
"""


class Animal:

    def __init__(self, name):
        self.name = name


class Fish(Animal):

    def __init__(self, name, depth):
        super().__init__(name)
        self.max_depth = depth

    def depth(self):
        if self.max_depth < 10:
            return 'Мелководная рыба'
        elif self.max_depth > 100:
            return 'Глубоководная рыба'
        else:
            return 'Средневодная рыба'


class Bird(Animal):

    def __init__(self, name, wingspan):
        super().__init__(name)
        self.wingspan = wingspan

    def wing_length(self):
        return round(self.wingspan / 2, 2)


class Mammal(Animal):

    def __init__(self, name, weight):
        super().__init__(name)
        self.weight= weight

    def category(self) -> str:
        if self.weight < 1:
            return 'Малявка'
        elif self.weight > 200:
            return 'Гигант'
        else:
            return 'Обычный'
