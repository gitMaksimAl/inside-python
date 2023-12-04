# Создайте три (или более) отдельных классов животных. Например рыбы, птицы и
# т.п. У каждого класса должны быть как общие свойства, например имя, так и
# специфичные для класса. Для каждого класса создайте метод, выводящий
# информацию специфичную для данного класса.

class Fish:
    DEPTH_LEVEL = {
        'Low depth': 10.0,
        'Middle depth': 30.0,
        'High depth': 100.0
    }

    def __init__(self, name: str, weight: float, max_depth: float):
        self.name = name
        self.weight = weight
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


class Bird:

    def __init__(self, name: str, weight: float, wingspan: float):
        self.name = name
        self.weight = weight
        self.wingspan = wingspan

    def wing_length(self):
        return round(self.wingspan / 2, 2)

    def __str__(self):
        return f"{self.name}, weight: {self.weight}," \
               f" wingspan: {self.wingspan}, wing length: {self.wing_length()}"


class Insect:
    LEGS_CATEGORY = {
        'Simple insect': 6,
        'Scary insect': 8,
        'Monster': 40
    }

    def __init__(self, name: str, weight: float, legs_count: int):
        self.name = name
        self.weight = weight
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
