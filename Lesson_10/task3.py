# Доработайте задачу 5.
# Вынесите общие свойства и методы классов в класс Животное.
# Остальные классы наследуйте от него.
# Убедитесь, что в созданные ранее классы внесены правки.

class Animal:

    def __init__(self, name: str, weight: float):
        self.name = name
        self.weight = weight


class Fish(Animal):

    DEPTH_LEVEL = {
        'Low depth': 10.0,
        'Middle depth': 30.0,
        'High depth': 100.0
    }

    def __init__(self, name: str, weight: float, max_depth: float):
        super().__init__(name, weight)
        self.max_depth = max_depth

    def depth_level(self) -> str:
        if self.max_depth < Fish.DEPTH_LEVEL['Low depth']:
            return 'Low depth'
        elif self.max_depth < Fish.DEPTH_LEVEL['Middle depth']:
            return 'Middle depth'
        else:
            return 'High depth'

    def __str__(self):
        return f"{self.name}, weight: {self.weight}," \
               f" max depth: {self.max_depth}, water level: {self.depth_level()}"


class Bird(Animal):

    def __init__(self, name: str, weight: float, wingspan: float):
        super().__init__(name, weight)
        self.wingspan = wingspan

    def wing_length(self):
        return round(self.wingspan / 2, 2)

    def __str__(self):
        return f"{self.name}, weight: {self.weight}," \
               f" wingspan: {self.wingspan}, wing length: {self.wing_length()}"


class Insect(Animal):

    LEGS_CATEGORY = {
        'Simple insect': 6,
        'Scary insect': 8,
        'Monster': 40
    }

    def __init__(self, name: str, weight: float, legs_count: int):
        super().__init__(name, weight)
        self.legs = legs_count

    def category(self) -> str:
        if self.legs < Insect.LEGS_CATEGORY['Simple insect']:
            return 'Simple insect'
        elif self.legs < Insect.LEGS_CATEGORY['Scary insect']:
            return 'Scary insect'
        else:
            return 'Monster'

    def __str__(self):
        return f"{self.name}, weight: {self.weight}," \
               f" legs: {self.legs}, category: {self.category()}"


if __name__ == "__main__":
    fish = Fish('shark', 50.0, 200)
    bird = Bird('vorobei', 0.2, 40.0)
    insect = Insect('spider', 0.1, 6)
    print(fish)
    print(bird)
    print(insect)
