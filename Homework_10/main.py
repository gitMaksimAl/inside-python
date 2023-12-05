from Homework_10.factory import AnimalFactory
from Homework_10.lottery_game import LotteryGame

if __name__ == "__main__":
    animal1 = AnimalFactory.create_animal('Bird', 'Орел', 200)
    animal2 = AnimalFactory.create_animal('Fish', 'Лосось', 50)
    animal3 = AnimalFactory.create_animal('Mammal', 'Слон', 5000)

    zoo = [animal3, animal2, animal1]
    for animal in zoo:
        print(f"{type(animal)}: {animal.name}")

    list1 = [3, 12, 8, 41, 7, 21, 9, 14, 5, 30]
    list2 = [9, 5, 6, 12, 14, 22, 17, 41, 8, 3]
    # list1 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # list2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    game = LotteryGame(list1, list2)
    matching_numbers = game.compare_lists()
