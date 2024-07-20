"""
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
“больше” или “меньше” после каждой попытки. Для генерации случайного числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
"""

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
TRY = 10

comp_num = randint(LOWER_LIMIT, UPPER_LIMIT)
i = 1
print(f'Игра началась...\nЯ загадал число от {LOWER_LIMIT} до {UPPER_LIMIT}\nНеобходимо угадать число за {TRY} попыток')
print()

while i <= TRY:
    print(f'Попытка {i}')
    user_num = int(input('Введите ваш вариант: '))
    if user_num < LOWER_LIMIT or user_num > UPPER_LIMIT:
        print(f'Число должно быть от {LOWER_LIMIT} до {UPPER_LIMIT}!')
    elif comp_num > user_num:
        print('Мое число больше!')
    elif comp_num < user_num:
        print('Мое число меньше!')
    else:
        print('Угадал, поздравляю!')
        break
    i += 1

if i > TRY:
    print('У вас закончились попытки')
print('Игра окончена!')
