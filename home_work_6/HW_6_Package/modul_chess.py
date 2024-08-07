__all__ = ['queen']

"""
 Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него напишите код, решающий задачу о 8 ферзях.
 Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
 Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
 Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
 Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
 ------------------------------------------------------------------------------------------------------------------
 Напишите функцию в шахматный модуль.
 Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
 Проверяйте различный случайные варианты и выведите 4 успешных расстановки.
"""


from random import randint


def rand_coord() -> list[list[int]]:
    random_coordinates = []
    for i in range(8):
        random_coordinates.append([])
        for j in range(2):
            random_coordinates[i].append(randint(1, 8))
    return random_coordinates


def queen(coordinates: list[list[int]]) -> bool:
    for prev_el in range(len(coordinates)):
        for next_el in range(prev_el + 1, len(coordinates)):
            x1 = coordinates[prev_el][0]
            y1 = coordinates[prev_el][1]
            x2 = coordinates[next_el][0]
            y2 = coordinates[next_el][1]
            if x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2):
                return False
    return True


if __name__ == '__main__':
    false_coordinates = [[1, 8], [6, 4], [3, 7], [3, 5], [4, 2], [7, 7], [5, 2], [7, 4]]
    true_coordinates = [[1, 1], [2, 7], [3, 5], [4, 8], [5, 2], [6, 4], [7, 6], [8, 3]]
    print(queen(false_coordinates))
    print(queen(true_coordinates))

    cnt = 1
    while cnt < 5:
        flag = True
        my_coord = rand_coord()
        for i in range(len(my_coord)):
            for j in range(i + 1, len(my_coord)):
                if i == j:
                    flag = False
                    break
        if flag:
            print(f'{cnt} - {my_coord}')
            cnt += 1

