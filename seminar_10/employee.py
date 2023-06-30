''' Задача 4
Создайте класс Сотрудник.
Воспользуйтесь классом человека из прошлого задания (Сотрудник является 
наследником класса Человек).
У сотрудника должен быть:
○ шестизначный идентификационный номер
○ уровень доступа вычисляемый как остаток от деления суммы цифр id на семь'''

import random


class Human:

    def __init__(self, firstname: str, lastname: str, age: int, sex: str):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = age # __защищаем свойство ворзрас для прямого изменения
        self.sex = sex


    def get_age(self):
        '''Получения позраста'''
        return self.__age


    def birthday(self):
        '''Увеличение возраста на 1 год'''
        self.__age += 1


    def __str__(self):
        '''Строчное представление вывода информации'''
        return f'{self.firstname} {self.lastname} {self.get_age()} {self.sex}'

class Employee(Human):

    def __init__(self, profession: str, firstname: str, lastname: str, age: int, gender: str):
        super().__init__(firstname, lastname, age, gender) # init поскольку изменяем конструктор
        self.eml_id = self._gen_number()
        self.sec_level = self._secure_level()
        self.profession = profession

    def _gen_number(self):
        '''Генератор идентификационного номера'''
        MIN_NUM = 100000
        MAX_NUM = 1000000
        return random.randint(MIN_NUM, MAX_NUM)

    def _secure_level(self):
        sec_id = self._gen_number()
        LEVEL_NUM = 7
        level_num = 0
        while sec_id > 0: # суммируем цифры идентификационного номера
            last_num = sec_id % 10
            level_num += last_num 
            sec_id /= 10
        return level_num % LEVEL_NUM

    def __str__(self):
        return f'{self.eml_id} {self.sec_level} {self.firstname} {self.lastname} {self.get_age()} {self.sex} {self.profession}'


if __name__ == '__main__':
    eml_1 = Employee('Рабочий', 'Иван', 'Иванов', 25, 'мужской')
    print(eml_1)
