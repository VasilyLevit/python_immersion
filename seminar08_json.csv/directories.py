'''Домашнее задание 8.
Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и 
все вложенные директории. Результаты обхода сохраните в файлы json, csv и pickle.
○ Для дочерних объектов указывайте родительскую директорию.
○ Для каждого объекта укажите файл это или директория.
○ Для файлов сохраните его размер в байтах, а для директорий размер
файлов в ней с учётом всех вложенных файлов и директорий.'''

import os
import json
import csv
import pickle


def get_dirs(up_dir: str) -> list(dict[str: str | int ]):
    '''Обходит вложенные директории
    :current_dir: начальная директория'''
    result = []     
    for dir_path, dir_name, file_name in os.walk(up_dir):  # обход рекурсивно вложенных дирректорий     
        for name in dir_name:
            result.append({'name': name, 
                         'parent': dir_path.split('/')[-1], 
                         'type': 'folder', 
                         'size': os.path.getsize(os.path.join(dir_path, name))})        
        for name in file_name:
            result.append({'name': name, 
                         'parent': dir_path.split('/')[-1], 
                         'type': 'file', 
                         'size': os.path.getsize(os.path.join(dir_path, name))})               
    return result


def write_json(file, data: list(dict[str: str | int ])) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def write_csv(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'w', encoding='utf-8') as f:
        writer = csv.writer(f, dialect='excel', quoting=csv.QUOTE_NONNUMERIC, delimiter=',')
        writer.writerow(('id', 'name', 'parent', 'type', 'size'))
        for k, v in data.items():
            writer.writerow((k, v['name'], v['parent'], v['type'], v['size']))


def write_pickle(file, data: dict[int:{str: str | int}]) -> None:
    with open(file, 'wb') as f:
        pickle.dump(data, f)


if __name__ == '__main__':

    dict_json = get_dirs('/Users/Addison/OneDrive/Geekbrains/Python')
    write_json('dir_info.json', dict_json)    
    # write_csv('dir_info.csv', dict_json)
    # write_pickle('dir_info.pickle', dict_json)