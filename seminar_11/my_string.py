''' Задача 1
Создайте класс Моя Строка, где:
будут доступны все возможности str
дополнительно хранятся имя автора строки и время создания (time.time)'''

# Добавьте к задачам 1 и 2 строки документации для классов.
from time import time


class MyString(str):
    '''Класс str дополнительно сохраняющий имя автора строки и время создания.'''

    def __new__(cls, note: str, autor: str):
        '''Расширяеи метод new параметрами value и name.'''
        instance = super().__new__(cls, note)        
        instance.autor = autor
        instance.creat_time = time()
        return instance

    def __str__(self):
        '''Переопределенние строчного выведения экземпляра класса.'''
        return self + " " + f'{self.autor} {self.creat_time}'


if __name__ == '__main__':
    mystr = MyString('Запись_1', 'Иванов')
    # print(mystr.autor)
    # print(mystr.creat_time)
    print(mystr)
    # print(mystr.upper())
    help(MyString)

