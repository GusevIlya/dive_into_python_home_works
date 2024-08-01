"""
Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список.
"""

import decimal

decimal.getcontext().prec = 6
MULTIPLICITY = 50
PERCENT = decimal.Decimal(15) / decimal.Decimal(1000)
PERCENT_BONUS = decimal.Decimal(3) / decimal.Decimal(100)
COUNT_PERC = 3
MIN_LIMIT = decimal.Decimal(30)
MAX_LIMIT = decimal.Decimal(600)
PERCENT_RICHNESS = decimal.Decimal(10) / decimal.Decimal(100)
RICHNESS_AMOUNT = 5_000_000
CMD_DEPOSIT = 'п'
CMD_WITHDRAW = 'с'
CMD_EXIT = 'в'


def request_to_user():
    global MULTIPLICITY
    total = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    return total


def check_for_correct(total):
    global MULTIPLICITY
    while total % MULTIPLICITY:
        print('Некорректная сумма')
        total = int(input(f'Введите сумму, кратную {MULTIPLICITY}: '))
    return total


def deposit(bal, oper, total):
    oper += 1
    bal += total
    return bal, oper, total


def withdraw(bal, oper, total):
    global PERCENT, MAX_LIMIT, MAX_LIMIT
    tax = total * PERCENT
    if tax < MIN_LIMIT:
        tax = MIN_LIMIT
    elif tax > MAX_LIMIT:
        tax = MAX_LIMIT
    if tax + total > bal:
        print(f'На счету недостаточно средств')
    else:
        oper += 1
        bal -= (total + tax)
    print(f'Сумма снятия: {total}, комиссия: {tax}, общая сумма: {total + tax}')
    return bal, oper, total


def bonus_crediting(bal):
    global PERCENT_BONUS
    bonus = bal * PERCENT_BONUS
    bal += bonus
    print(f'Сумма бонуса: {bonus}')
    return bal, bonus


def rich(bal):
    global PERCENT_RICHNESS
    sum_percent = bal * PERCENT_RICHNESS
    bal -= sum_percent
    print(f'Вычтен налог на богатство в размере {sum_percent}')
    print(f'Текущий баланс: {bal}')
    return bal


balance = 0
operations = 0
sum_bonus = 0
actions_list = []

while True:
    action = input(
        f'пополнить - {CMD_DEPOSIT}\n'
        f'снять - {CMD_WITHDRAW}\n'
        f'выход - {CMD_EXIT}\n'
        f'Введите действие: '
    )
    if balance > RICHNESS_AMOUNT and action != 'в':
        balance = rich(balance)
    if action in ('п', 'с'):
        amount = request_to_user()
        amount = check_for_correct(amount)
        if action == 'п':
            balance, operations, amount = deposit(balance, operations, amount)
            actions_list.append(f'пополнение на {amount}$')
        else:
            balance, operations, amount = withdraw(balance, operations, amount)
            actions_list.append(f'снятие {amount}$')
        if operations % COUNT_PERC == 0:
            balance, sum_bonus = bonus_crediting(balance)
            actions_list.append(f'начисление бонуса {sum_bonus}$')
        print(f'Текущий баланс: {balance}')
    elif action == 'в':
        print(*actions_list, sep='\n')
        print(f'Ваш баланс: {balance}$')
        break
    else:
        print('Введена неверная команда!')
