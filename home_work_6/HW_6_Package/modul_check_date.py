"""
 В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.
"""

__all__ = ['check_date']
from sys import argv


def _is_leap(year: int) -> bool:
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def check_date(date: str) -> bool:
    day, month, year = [int(num) for num in date.split('.')]
    if (year > 9999 or year < 1) or day > 31 or month > 12:
        return False
    elif day == 31 and month in [2, 4, 6, 9, 11]:
        return False
    elif month == 2 and day == 29 and not _is_leap(year) or (month == 2 and day == 30):
        return False
    return True


if __name__ == '__main__':
    my_date = argv[1]
    if check_date(my_date):
        print(f'{my_date} - есть такой день')
    else:
        print(f'{my_date} - нет такого дня')
