# Функция принимает на вход три списка одинаковой длины:
# имена str,
# ставка int,
# премия str с указанием процентов вида «10.25%».
# Вернуть словарь с именем в качестве ключа и суммой
# премии в качестве значения.
# Сумма рассчитывается как ставка умноженная на процент премии.
from decimal import Decimal


def get_salaries(names: list[str], salaries: list[int], awards: list[str]) \
        -> dict[str, Decimal]:
    return {name: salary * Decimal(award[:-1]) / 100
            for name, salary, award in zip(names, salaries, awards)}


n = ["Иван", "Николай", "Пётр", "Харитон"]
s = [125_000, 96_000, 109_000, 100_000]
a = ['10%', '25.5%', '13.3%', '42.73%']
print(get_salaries(n, s, a))
