class LotteryGame:

    def __init__(self, ls1: list[int], ls2: list[int]):
        self.number_set1 = ls1
        self.number_set2 = ls2

    def compare_lists(self):
        bingo = []
        if self.number_set1 == self.number_set2:
            print(f"Совпадающие числа: {self.number_set1}\n"
                  f"Количество совпадающих чисел: {len(self.number_set1)}")
            return self.number_set2
        for item in self.number_set1:
            if item in self.number_set2:
                bingo.append(item)
        if bingo:
            print(f"Совпадающие числа: {bingo}\n"
                  f"Количество совпадающих чисел: {len(bingo)}")
            return bingo
        else:
            print("Совпадающих чисел нет.")
            return None

