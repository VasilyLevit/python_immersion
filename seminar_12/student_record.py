''' Домашнее задание
Создайте класс студента.
○ Используя дескрипторы проверяйте ФИО на первую заглавную букву и наличие только букв.
○ Названия предметов должны загружаться из файла CSV при создании экземпляра. Другие 
предметы в экземпляре недопустимы.
○ Для каждого предмета можно хранить оценки (от 2 до 5) и результаты тестов (от 0 до 100).
○ Также экземпляр должен сообщать средний балл по тестам для каждого предмета и по оценкам 
всех предметов вместе взятых.'''

import csv
from statistics import mean


class NameValidator:
    '''Класс-дескриптор'''
    def __set_name__(self, owner, name):
        '''Метод инкапсулирует имена свойств (first_name, last_name) передаваемых в качестве параметров '''
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        '''Метод получения у объекта instance значения для свойства self.param_name'''       
        return getattr(instance, self.param_name)

    def __set__(self, obj, value):
        self._validate_name(value)
        setattr(obj, self.param_name, value)

    def _validate_name(self, value):
        if not isinstance(value, str):
            raise AttributeError('Имя должно быть строкой')
        if not value.isalpha():
            raise AttributeError('Имя должно состоять из букв')
        if not value.istitle():
            raise AttributeError('Имя должно начинаться с заглавной буквы')


class ItemValidator:
    '''Класс дескриптор'''
    def __init__(self, min_value: int = None, max_value: int = None):        
        self._min_value = min_value
        self._max_value = max_value

    def __set_name__(self, owner, name):
        '''Метод инкапсулирует имена свойств (grades, tests) передаваемых в качестве параметров '''
        self.param_name = '_' + name

    def __get__(self, instance, owner):
        '''Метод получения у объекта instance значения для свойства self.param_name''' 
        return getattr(instance, self.param_name)

    def __set__(self, instance, value: dict):
        '''Метод устанавливает значение и проверяет попадание в заданный диапазон с помощью внутреннего метода validate'''
        self.validate_range(value)
        self.validate_items(value)
        # если validate не вернула ошибку, присваиваем свойству param_name объекта instance значение value
        setattr(instance, self.param_name, value)

    def validate_range(self, value: dict):
        '''Метод проверяте значения в словарях на попадание в допустимый диапазон'''
        for value in value.values():
            for value_tuple in value:
                if not isinstance(value_tuple, int):
                    raise TypeError(f'Значение {value_tuple} должно быть целым числом')
                if value_tuple is not None and value_tuple < self._min_value:
                    raise ValueError(f'Значение {value_tuple} должно быть больше или равно {self._min_value}')
                if value_tuple is not None and value_tuple > self._max_value:
                    raise ValueError(f'Значение {value_tuple} должно быть меньше или равно {self._max_value}')

    def validate_items(self, value: dict):
        data = self._load_data()
        valid = 0
        for d in data:
            for v in value:
                if d == v:
                    valid += 1
        if valid != len(value):
            raise AttributeError(f'Предмета нет в списке')

    def _load_data(self):
        ''' Метод получение названия предмета из файла'''
        data = {}
        file_name = 'seminar_12/school_items.csv'
        i = 0
        with open(file_name, encoding='utf-8') as f:
            csv_reader = csv.reader(f)
            for item in csv_reader:
                res = ''.join(item).strip()
                i += 1
                if i != 1:
                    data[res] = None
        return data


class Student:
    first_name = NameValidator()
    last_name = NameValidator()
    grades: dict = ItemValidator(2, 5)
    tests: dict = ItemValidator(0, 100)

    def __init__(self, first_name, last_name):        
        self.first_name = first_name
        self.last_name = last_name
        self._grades: dict[str: tuple] = {}
        self._tests: dict[str: tuple] = {}

    def __str__(self):
        grades = '\n'.join(f'{k}: {v}' for k, v in self._grades.items())
        tests = '\n'.join(f'{k}: {v}' for k, v in self._tests.items())
        avg_test_results = '\n'.join(f'{k}: {v}' for k, v in self._avg_tests().items())
        return f'{self.first_name} {self.last_name}' \
               f'\n\nОценки по предметам:\n{grades}' \
               f'\nСредний оценка: {self._avg_grades()}' \
               f'\n\nРезультаты тестов:\n{tests}' \
               f'\n\nСредняя оценка по тестам:\n{avg_test_results}\n'

    def _avg_tests(self):
        avg_results = dict()
        for key, value in self._tests.items():
            avg_results[key] = round(mean(value), 1)
        return avg_results

    def _avg_grades(self):
        '''Метод возвращает среднюю оценку по всем предметам'''
        summ_values = 0
        for values in self._grades.values(): # values принимает кортежи значений из словаря
            summ_values += mean(values)
        result = summ_values / len(self._grades.values())        
        return round(result, 1)


if __name__ == '__main__':
    std1 = Student('Mихаил','Ломоносов') 
    std1.grades = {'Физика': (4, 5, 5), 'Биология': (5, 5, 4, 5), 'Математика': (4, 5, 5, 5)}
    std1.tests = {'Литература': (0, 99, 100), 'Химия': (90, 97, 99)}
    print(std1)
