"""
Напишите функцию для транспонирования матрицы
"""
from random import randint
ROWS = 3
COLUMNS = 4


def transposition(matrix: list[list[int]]) -> list[list[int]]:
    trans_matrix = []
    for col in range(len(matrix[0])):
        trans_matrix.append([])
        for row in range(len(matrix)):
            trans_matrix[col].append(matrix[row][col])
    return trans_matrix


my_matrix = []
for r in range(ROWS):
    my_matrix.append([])
    for c in range(COLUMNS):
        my_matrix[r].append(randint(0, 9))

print('Исходная матрица:')
print(*my_matrix, sep='\n')
print('Транспонированная матрица:')
print(*transposition(my_matrix), sep='\n')
