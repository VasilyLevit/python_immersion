''' Задача 1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали текстовый файл с 
псевдо именами и произведением чисел. Напишите функцию, которая создаёт из 
созданного ранее файла новый с данными в формате JSON.
Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.'''

from pathlib import Path
from typing import TextIO
import json


def create_json(file: Path) -> None:
    file_data = {}
    with open(file, 'r', encoding='utf-8') as f:
        for line in f: # Заполняе словарь разделёнными занчениями из файла
            name, number = line.split()
            file_data[name.capitalize()] = float(number)
    with open(file.stem + '.json', 'w', encoding='utf-8') as f_2: # file.stem + '.json' - сохраняем
        # считанное ранее имя файла и добавляем новое разрешение (лучше это делать f строками)
        json.dump(file_data, f_2, ensure_ascii=False, indent=2)
