"""
 Напишите функцию, которая принимает на вход строку - абсолютный путь до файла.
 Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.
"""


def file(path: str) -> tuple:
    *file_path, file_name = path.split('\\')
    file_path = '\\'.join(file_path)
    file_name, file_extension = path.split('\\')[-1].split('.')
    return file_path, file_name, file_extension


user_file_path = 'C:\Program Files\AMD\Chipset_Software\AMD_Chipset_Drivers.exe'

print(file(user_file_path))
