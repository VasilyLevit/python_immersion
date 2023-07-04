''' Задача 2
Создайте класс Архив, который хранит пару свойств.
Например, число и строку.
При создании нового экземпляра класса, старые данные из ранее
созданных экземпляров сохраняются в пару списков архивов
list-архивы также являются свойствами экземпляра'''

''' Задача 3
Добавьте к задачам 1 и 2 строки документации для классов.'''

''' Задача 4
Доработаем класс Архив из задачи 2.
Добавьте методы представления экземпляра для программиста и для пользователя.'''


class Archive:
    '''Сохраняем данные экземпляров класса в списки numbers и values.'''
    numbers = []
    values = []

    # def __new__(cls, number: int, value: str):
    #     '''Переопределили метод new для сохранения аргументов в списки.'''
    #     instance = super().__new__(cls)
    #     cls.numbers.append(number)
    #     cls.values.append(value)
    #     return instance

    def __init__(self, number: int, value: str):
        '''Переопределённый метод инициализации добавляет параметры к спискам уровня класса.'''
        self.number = number
        self.value = value
        Archive.numbers.append(number)
        Archive.values.append(value)


    def __repr__(self):
        '''Переопределили метод выведения информации для разработчика'''
        return f'Archive({self.number}, "{self.value}")'

    def __str__(self):
        '''Переопределили метод выведения строчного представления класса для пользователя'''
        return f'Номер: {self.number}, Значение: "{self.value}"'


if __name__ == '__main__':
    a_1 = Archive(1, "Один")
    # print(f'{a_1.numbers} {a_1.values}')
    # a_2 = Archive(2, "Два")    
    # print(f'{a_2.numbers} {a_2.values}')
    # a_3 = Archive(3, "Три")
    # print(f'{a_3.numbers} {a_3.values}')
    # help(a_1)
    # help(Archive)
    print(a_1.__repr__()) # вывод с __repr__
    print(f'{a_1 = }') # вывод с __repr__
    print(a_1) # вывод с __str__ при его наличии, если нет, то выведет __repr__