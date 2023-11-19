# Создайте модуль и напишите в нём функцию, которая получает на вход дату в
# формате DD.MM.YYYY Функция возвращает истину, если дата может существовать или
# ложь, если такая дата невозможна. Для простоты договоримся, что год может быть
# в диапазоне [1, 9999]. Весь период (1 января 1 года - 31 декабря 9999 года)
# действует Григорианский календарь. Проверку года на високосность вынести в
# отдельную защищённую функцию.
__all__ = ['valid_date']


def __isleap_year(year: int) -> bool:
    return year % 400 == 0 or year % 4 == 0 and year % 100 != 0


def valid_date(date: str) -> bool:
    day, month, year = (int(i) for i in date.split('.'))
    if not (0 < day < 32 and 0 < month < 13 and 0 < year < 10_000):
        return False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    if month == 2:
        if day > 29:
            return False
        if day == 29 and not __isleap_year(year):
            return False
    return True


if __name__ == '__main__':
    print(valid_date(input("Enter date 'dd.mm.yyyy': ")))
