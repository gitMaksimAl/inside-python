from Animals import Animal, Fish, Bird, Mammal


class AnimalFactory:

    __animal_instance = None

    @staticmethod
    def create_animal(animal_type, *args) -> Animal:
        match animal_type:
            case Mammal.__name__:
                __animal_instance = Mammal(*args)
            case Bird.__name__:
                __animal_instance = Bird(*args)
            case Fish.__name__:
                __animal_instance = Fish(*args)
            case _:
                raise ValueError("Недопустимый тип животного")
        return __animal_instance
