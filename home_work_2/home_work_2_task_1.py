"""
Напишите программу, которая получает целое число и возвращает его шестнадцатеричное строковое представление.
Функцию hex используйте для проверки своего результата.
"""

HEX_DIV = 16

num = int(input('Введите число: '))
num_copy = num
res = ''
symbols = {10: 'a', 11: 'b', 12: 'c', 13: 'd', 14: 'e', 15: 'f'}

while num:
    remainder = num % HEX_DIV
    if remainder > 9:
        remainder = symbols[remainder]
    res = str(remainder) + res
    num //= HEX_DIV

check = hex(num_copy)[2:]

print(f'Число {num_copy} в шестнадцатеричном представлении: {res}')
print(f'Проверка функцией hex(): {check}')

if res == check:
    print('Проверка успешна!')
