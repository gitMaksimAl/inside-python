# Функция получает на вход текст вида: “1-й четверг ноября”, “3-я среда мая”
# и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.
import datetime
import logging
import argparse

logging.basicConfig(filename='task2.log', filemode='a', level=logging.ERROR,
                    encoding='utf-8')
loger = logging.getLogger()


def parse():
    parser = argparse.ArgumentParser(prog='get_date()',
                                     description='Get date of the weekday.',
                                     )
    parser.add_argument('--count', default=1, help='Week count in month.')
    parser.add_argument('--weekday', default=datetime.datetime.now().weekday(),
                        help='Week day.')
    parser.add_argument('--month', default=datetime.datetime.now().month,
                        help='Month.')
    args = parser.parse_args()
    print(args.count, args.weekday, args.month)
    return get_date_from_string(f"{args.count} {args.weekday} {args.month}")


def get_date_from_string(date: str):
    count = _weekday = _month = None
    try:
        count, _weekday, *_, _month = date.split(' ')
        _weekday = _weekday.title()
        _month = _month.title()
        count = int(count[:1])
    except ValueError:
        loger.error('Wrong format.')
    print(count, _weekday, _month)
    return get_date(count, _weekday, _month)


def get_date(count: int, _weekday: str, _month: str):
    """
    Function return date of the date of the requested day of the week in
    the month of the current year
    :param count: int
    :param _weekday: string
    :param _month: string
    :return: datetime
    """
    try:
        int(_weekday)
        wd = 'w'
    except ValueError:
        wd = 'A'
    try:
        int(_month)
        mnt = 'm'
    except ValueError:
        mnt = 'B'

    # need this ?
    if count > 4:
        count = 4
    print(count, _weekday, _month)
    true_date = datetime.datetime(year=2023, month=1, day=1)
    while true_date.strftime(f'%{mnt}') != _month:
        true_date = true_date.replace(month=true_date.month + 1)
    while count > 0:
        # print(true_date.date())
        true_date = true_date.replace(day=true_date.day + 1)
        if true_date.strftime(f'%{wd}') == _weekday:
            count -= 1
    return true_date


if __name__ == "__main__":
    # _date = get_date(input('Please enter day of the month, like '
    #                        '1st thursday of the november: '))
    # d = '1st 4 of the 11'
    # d1 = '1st thursday of the november'
    # print(d1)
    # _date = get_date_from_string(d1)
    _date = parse()
    print(f"Date of this: {_date.date()}, weekday: {_date.strftime('%A')}")