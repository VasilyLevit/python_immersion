''' Домашнее задание
Напишите следующие функции:
○ Нахождение корней квадратного уравнения
○ Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.
○ Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой 
тройкой чисел из csv файла.
○ Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл.
Соберите пакет с играми из тех файлов, что уже были созданы в рамках курса'''
import csv
import json
import random
from cmath import sqrt
from typing import Callable


def with_csv_coeff(func: Callable) -> object:
    '''Декоратор, запускающий функцию нахождения корней квадратного уравнения с каждой 
тройкой чисел из csv файла'''
    def wrapper():
        equations = {}
        with open('seminar09_closures/coeff.csv', 'r') as f:
            reader = csv.reader(f, dialect='excel')
            count = 0
            equation = {}
            for row in reader:
                if count > 0: #условие пропуска первой строки с наименованиями
                    equation = {count: {'a': int(row[0]),
                                        'b': int(row[1]),
                                        'c': int(row[2]),
                                        'result': func(int(row[0]), int(row[1]), int(row[2]))}}
                equations.update(equation)
                count += 1
        return equations

    return wrapper


def write_json(func: Callable):
    '''Декоратор, сохраняющий переданные параметры и результаты работы функции в json файл'''
    def wrapper():
        result = func()
        # print(result)
        with open('seminar09_closures/coeff.json', 'w', encoding='utf-8') as f:
            json.dump(result, f, indent=2, ensure_ascii=False)

    return wrapper


@write_json
@with_csv_coeff
def solving_equation(a: int = 1, b: int = 0, c: int = 0) -> tuple[str] | str:
    '''Поиск корней квадратного урванения'''
    discriminant = (pow(b, 2)) - (4 * a * c)
    if discriminant < 0:
        return f'нет действительных корней'
    elif discriminant == 0:
        return str(-b / (2 * a))
    else:
        return str((-b + sqrt(discriminant)) / (2 * a)), str((-b - sqrt(discriminant)) / (2 * a))



def write_csv(file: str) -> None:
    '''Формирует файл с наборами случайно сгененрированных коэффициентов уравнеия'''
    LINES = 100 # количество строк
    list_csv = []
    for _ in range(LINES):
        num_1 = random.randint(1,10)
        num_2 = random.randint(-10, 10)
        num_3 = random.randint(-10, 10)
        list_csv.append([num_1, num_2, num_3])
    with open(file, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['a', 'b', 'c'])
        writer.writerows(list_csv)


if __name__ == '__main__':
    write_csv('seminar09_closures/coeff.csv')
    solving_equation()
