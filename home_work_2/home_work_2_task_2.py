"""
 Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
 Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions
"""
from math import gcd
from fractions import Fraction

frac_1 = input('Введите первую дробь в формате "a/b": ')
frac_2 = input('Введите вторую дробь в формате "a/b": ')

frac_list_1 = [int(i) for i in frac_1.split('/')]  # Получаем список из числителя и знаменателя 1 дроби
frac_list_2 = [int(i) for i in frac_2.split('/')]  # Получаем список из числителя и знаменателя 2 дроби

numerator_sum = frac_list_1[1] * frac_list_2[0] + frac_list_2[1] * frac_list_1[0]  # Числитель для суммы
numerator_pro = frac_list_1[0] * frac_list_2[0]  # Числитель для произведения
denominator_sum = frac_list_1[1] * frac_list_2[1]  # Знаменатель для суммы
denominator_pro = frac_list_1[1] * frac_list_2[1]  # Знаменатель для произведения

nod_sum = gcd(numerator_sum, denominator_sum)  # НОД для суммы
nod_pro = gcd(numerator_pro, denominator_pro)  # НОД для произведения
numerator_sum //= nod_sum
numerator_pro //= nod_pro
denominator_sum //= nod_sum
denominator_pro //= nod_pro
check_sum = Fraction(frac_list_1[0], frac_list_1[1]) + Fraction(frac_list_2[0], frac_list_2[1])
check_pro = Fraction(frac_list_1[0], frac_list_1[1]) * Fraction(frac_list_2[0], frac_list_2[1])

print(f'{frac_1} + {frac_2} = {numerator_sum}/{denominator_sum}')
print(f'{frac_1} x {frac_2} = {numerator_pro}/{denominator_pro}')
print(f'Проверка: {frac_1} + {frac_2} = {check_sum}')
print(f'          {frac_1} x {frac_2} = {check_pro}')
