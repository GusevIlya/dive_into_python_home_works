"""
Напишите код, который запрашивает число и сообщает, является ли оно простым или составным. Используйте правило для
проверки: “Число является простым, если делится нацело только на единицу и на себя”. Сделайте ограничение на ввод
отрицательных чисел и чисел больше 100 тысяч.
"""

LOWER_LIMIT = 0
UPPER_LIMIT = 10 ** 5

while True:
    user_num = int(input(f'Введите число от {LOWER_LIMIT} до {UPPER_LIMIT}: '))
    if LOWER_LIMIT <= user_num <= UPPER_LIMIT:
        break

if user_num == LOWER_LIMIT:
    res = f'Число {user_num} - составное'
else:
    for i in range(2, int(user_num ** 0.5) + 1):
        if user_num % i == 0:
            res = f'Число {user_num} - составное'
            break
    else:
        res = f'Число {user_num} - простое'

print(res)
