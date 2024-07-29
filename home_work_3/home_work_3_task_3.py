"""
Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака.
"""

MAX_WEIGHT = 10

things = {'палатка': 3, 'топор': 1, 'вода': 1.5, 'тушенка': 2, 'спички': 0.2,
          'аптечка': 2, 'спальный мешок': 4, 'фонарик': 0.5, 'посуда': 3}
cur_weight = 0

things_in_bag = []
for thing, weight in things.items():
    if cur_weight + weight <= MAX_WEIGHT:
        things_in_bag.append(thing)
        cur_weight += weight

print(f'При грузоподъемности рюкзака {MAX_WEIGHT}кг влезут вещи:')
print(*things_in_bag, sep='\n')
