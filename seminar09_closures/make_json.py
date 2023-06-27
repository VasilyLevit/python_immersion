''' Задание 3
Напишите декоратор, который сохраняет в json файл параметры декорируемой функции 
и результат, который она возвращает. При повторном вызове файл должен расширяться, 
а не перезаписываться.
Каждый ключевой параметр сохраните как отдельный ключ json словаря.
Для декорирования напишите функцию, которая может принимать как позиционные, 
так и ключевые аргументы.
Имя файла должно совпадать с именем декорируемой функции.'''

import json
from typing import Callable


def deco_json(func: Callable):
    with open(f'seminar09_closures/{func.__name__}.json', 'r') as f: # октрываем файл с именем декорируемой функции
        existing_dict = json.load(f) # загрузка объекта из файла и десериализация в словарь

    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        existing_dict.update({str(args): res}) # расширене словаря новыми значениями
        # existing_dict.update({**kwargs})
        with open(f'seminar09_closures/{func.__name__}.json', 'w') as f: 
            json.dump(existing_dict, f, indent=2) # сохранение результата в файл

    return wrapper


@deco_json
def multy(a: int, b: int) -> int:
    return a * b

if __name__ == '__main__':
    multy(3, 4)
