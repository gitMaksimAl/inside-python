# Выведите в консоль таблицу умножения
# от 2х2 до 9х10 как на школьной тетрадке.
# Таблицу создайте в виде однострочного генератора, где каждый элемент
# генератора — отдельный пример таблицы умножения.
# Для вывода результата используйте «принт»
# без перехода на новую строку.
LOW_LIMIT = 2
UP_LIMIT = 10
COLUMN = 4

mult_table_generator = (f"{k:>2} * {j:>2} = {k * j:>2}\t"
                        if k != i + COLUMN - 1
                        else f"{k:>2} * {j:>2} = {k * j:>2}\n" if j != UP_LIMIT
                        else f"{k:>2} * {j:>2} = {k * j:>2}\n\n"
                        for i in (LOW_LIMIT, COLUMN + LOW_LIMIT)
                        for j in range(LOW_LIMIT, UP_LIMIT + 1)
                        for k in range(i, i + COLUMN))

print(*mult_table_generator)
