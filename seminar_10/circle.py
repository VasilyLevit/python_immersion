''' Задача 1
Создайте класс окружность.
Класс должен принимать радиус окружности при создании экземпляра.
У класса должно быть два метода, возвращающие длину окружности и её площадь.'''

from math import pi


class Circle:
    "Класс для получения длины окружности и площади окружности"
    def __init__(self, radius):
        self.r = radius # r - атрибут экземпляра класса

    def get_lenght(self):
        return 2 * pi * self.r

    def get_area(self):
        return pi * pow(self.r, 2)


if __name__ == '__main__':
    circle = Circle(5) # Создание экземляра класса cirlcle с передачей аргумента
    print(f'{circle.lenght()= } {circle.area()= }')
