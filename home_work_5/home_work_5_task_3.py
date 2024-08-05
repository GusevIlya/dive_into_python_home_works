"""
Создайте функцию генератор чисел Фибоначчи
"""


def fibonacci(n: int):
    prev_num, next_num = 0, 1
    yield prev_num
    if n > 1:
        yield next_num
    for _ in range(3, n + 1):
        fib = prev_num + next_num
        yield fib
        prev_num, next_num = next_num, fib


count_fibonacci = int(input('Сколько чисел Фибоначчи вывести?: '))
print(*fibonacci(count_fibonacci))
