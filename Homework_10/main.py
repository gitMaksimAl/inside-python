from Homework_10.factory import AnimalFactory

if __name__ == "__main__":
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

    zoo = [animal3, animal2, animal1]
    for animal in zoo:
        print(f"{type(animal)}: {animal.name}")
