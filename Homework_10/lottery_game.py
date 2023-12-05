class LotteryGame:

    def __init__(self, ls1: list[int], ls2: list[int]):
        self.number_set1 = ls1
        self.number_set2 = ls2

    def compare_lists(self):
        bingo = set()
        if self.number_set1 == self.number_set2:
            print(f"Совпадающие числа: {self.number_set2}\n"
                  f"Количество совпадающих чисел: {len(self.number_set2)}")
            return self.number_set2
        for i in range(len(self.number_set2)):
            if self.number_set2[i] in self.number_set1:
                bingo.add(self.number_set2[i])
            if self.number_set1[i] in self.number_set2:
                bingo.add(self.number_set1[i])
        if bingo:
            print(f"Совпадающие числа: {list(bingo)}\n"
                  f"Количество совпадающих чисел: {len(bingo)}")
            return list(bingo)
        else:
            print("Совпадающих чисел нет.")
            return None

