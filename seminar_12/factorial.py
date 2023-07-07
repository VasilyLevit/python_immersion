'''Задача 1 
Создайте класс-функцию, который считает факториал числа при вызове экземпляра.
Экземпляр должен запоминать последние k значений.
Параметр k передаётся при создании экземпляра.
Добавьте метод для просмотра ранее вызываемых значений и их факториалов.'''

''' Задача 2
Доработаем задачу 1.
Создайте менеджер контекста, который при выходе сохраняет значения в JSON файл.'''

import json


class Fact:
    _context_dict = dict() # словарь для сохранения в файл

    def __init__(self, k: int):
        self.k = k
        self.save_list = list() # список для хранения k значений факториалов

    def __call__(self, value):
        '''Метод вызываемый при обращении к экземпляру как к функции
        : value: число, для определения факториала'''
        res = 1
        for i in range(2, value + 1):
            res *= i
        self.save_list.append(res)
        if len(self.save_list) > self.k:
            self.save_list.pop(0) # удаляем первый элемент при условии превышения k (pop удаляет по индексу)
        return f'{value}! = {res}'  # возвращаем вычисленный факториал

    def __enter__(self):
        '''Запускаем менеджер контекста'''
        return self
 
    def mapper(self):
        '''Делает из списка словарь'''
        for i, value in enumerate(self.save_list, start=1):
            self._context_dict[i] = value

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.mapper()
        with open('seminar_12/factorials.json', 'w') as f:
            json.dump(self._context_dict, f, indent=2)

    def __str__(self):
        ''' Метод для вывода списка'''
        return f'{self.save_list}'


if __name__ == '__main__':
 
    # fact = Fact(3)
    # print(fact(3))
    # print(fact(4))
    # print(fact(5))
    # print(fact(6))
    # print(fact)
    
    '''Менеджер контекста'''
    with Fact(3) as fact:        
        print(fact(5))
        print(fact(6))
        print(fact(7))
        print(fact(8))
        print(fact(9))
        print(fact(10))
        print(fact)
