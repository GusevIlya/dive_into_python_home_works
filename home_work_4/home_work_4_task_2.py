"""
Напишите функцию, принимающую на вход только ключевые параметры
и возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента. Если ключ не хешируем, используйте его строковое представление.
"""


def change_items(**kwargs) -> dict:
    res_dict = dict()
    for param, value in kwargs.items():
        if isinstance(value, list) or isinstance(value, set):
            value = str(value)
        res_dict[value] = param
    return res_dict


print(change_items(integer=9, my_float=3.14, string='hello, world', my_tuple=(3, 45, 'python'),
                   my_list=[2, 5.76, 'good', [0, 0, 0]], my_set={3, 7, 5}))
