# Создайте генератор чётных чисел от нуля до 100.
# Из последовательности исключите
# числа, сумма цифр которых равна 8.
# Решение в одну строку.

num_generator = (i for i in range(0, 100, 2) if i // 10 + i % 10 != 8)

fizz_generator = ('FizzBuzz' if i % 15 == 0 else
                  'Fizz' if i % 3 == 0 else
                  'Buzz' if i % 5 == 0 else
                    i for i in range(1, 100))

print(*num_generator)
print(*fizz_generator)
