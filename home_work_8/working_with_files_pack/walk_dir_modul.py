"""
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах,
а для директорий размер файлов в ней с учётом всех вложенных файлов и директорий.
3. Соберите из созданных на уроке и в рамках домашнего задания функций пакет для работы с файлами разных форматов.
"""
__all__ = ['wolk_directory']

import os
from pathlib import Path
import json
import csv
import pickle


def wolk_directory(wolk_path: Path, save_json_path: Path, save_csv_path: Path, save_pickle_path: Path) -> None:
    json_data = {}
    csv_data = []
    header = ['directory', 'file', 'size']
    for dir_path, dir_name, file_name in os.walk(wolk_path):
        os.chdir(dir_path)
        parent_2 = dir_path.split('\\')[-2]
        parent = dir_path.split('\\')[-1]
        size = 0
        for file in file_name:
            os.chdir(dir_path)
            size += os.path.getsize(file)
        json_data[f'{parent_2}/{parent}'] = f'Директория размером {size} байт'
        csv_data.append([f'{parent_2}/{parent}', ' ', f'{size} байт'])
        if file_name:
            files = []
            for file in file_name:
                files.append({file: f'{os.path.getsize(file)} байт'})
                all_data = [f'{parent_2}/{parent}', file, f'{os.path.getsize(file)} байт']
                csv_data.append(all_data)
            json_data[f'{parent_2}/{parent} files'] = files
    os.chdir(wolk_path)
    with (
        open(save_json_path, 'w', encoding='utf-8') as f_json_write,
        open(save_csv_path, 'w', newline='', encoding='utf-8') as f_csv_write,
        open(save_pickle_path, 'wb') as f_pickle_write
    ):
        json.dump(json_data, f_json_write, indent=4, ensure_ascii=False)
        csv_write = csv.writer(f_csv_write)
        csv_write.writerow(header)
        csv_write.writerows(csv_data)
        pickle.dump(json_data, f_pickle_write)


if __name__ == '__main__':
    wolk_directory(Path('F:\Учеба GeekBrains\Погружение в Python\Семинары\dive_into_python_home_works\home_work_8'),
                   Path('F:\Учеба GeekBrains\Погружение в Python\Семинары\project_new\my_json.json'),
                   Path('F:\Учеба GeekBrains\Погружение в Python\Семинары\project_new\my_csv.csv'),
                   Path('F:\Учеба GeekBrains\Погружение в Python\Семинары\project_new\my_pickle.pickle'))

