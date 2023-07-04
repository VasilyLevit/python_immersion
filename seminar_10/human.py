''' Задача 3
Напишите класс для хранения информации о человеке:
ФИО, возраст и т.п. на ваш выбор.
У класса должны быть методы birthday для увеличения возраста на год, 
full_name для вывода полного ФИО и т.п. на ваш выбор.
Убедитесь, что свойство возраст недоступно для прямого изменения, но есть 
возможность получить текущий возраст'''


class Human:
    "Класс для хранения инофрмации о человеке"
    def __init__(self, firstname: str, lastname: str, age: int, sex: str):
        self.firstname = firstname
        self.lastname = lastname
        self.__age = age # __защищаем свойство ворзрас для прямого изменения
        self.sex = sex


    def get_age(self):
        '''Метод получения позраста'''
        return self.__age


    def increase_age(self):
        '''Метод увеличения возраста на 1 год'''
        self.__age += 1


    def __str__(self):
        '''Строчное представление вывода информации'''
        return f'{self.firstname} {self.lastname} {self.get_age()} {self.sex}'


if __name__ == '__main__':
    h_1 = Human('Иван', 'Иванов', 23, 'мужской')
    h_2 = Human('Петр', 'Сидоров', 40, 'мужской') 
    print(h_1)
    print(h_2)
    h_1.increase_age()
    h_2.increase_age()
    print(h_1)
    print(h_2)
