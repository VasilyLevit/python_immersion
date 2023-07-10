''' Домашнее задание (к задаче прямоугольник из 12 семинара)
Написать классы исключения с выводом подробной информации.
Поднимайте исключения внутри основного кода. Например
нельзя создавать прямоугольник со сторонами
отрицательной длины.'''

from custom_errors import SideError

class Rectangle:
    '''Класс прямоугольник.'''

    __slots__ = ('_a', '_b')
    '''Метод экономии памяти для хранения свойств экземпляра без словаря __dict__
    указываем переыень имён свойств, которые будут использоваться в классе'''

    def __init__(self, a: int, b: int = None):
        '''Метод инициализации прямоугольника со сторонами a и b.'''
        self._a = a # передаём атрибуты контсруктора в защищённые свойства
        self._b = b if b is not None else a

    @property #позволяет обращаться к методу как к переменной (т.е. без скобок, поскольку сама переменная защищена _а)
    def a(self):
        return self._a

    @property
    def b(self):
        return self._b

    @a.setter
    def a(self, value):
        if value > 0: # контроль недопустимых значений (отрицательных)
            self._a = value
        else:
            raise SideError(value)

    @b.setter
    def b(self, value):
        if value > 0:
            self._b = value
        else:
            raise SideError(value)

    def perimeter(self):
        '''Метод расчета периметра прямоугольника.'''
        return 2 * (self.a + self.b)

    def area(self):
        '''Метод расчета площади прямоугольника.'''
        return self.a * self.b

    def __add__(self, other):
        '''Переопределенный дандер метод сложения двух прямоугольников.'''
        new_perimeter = self.perimeter() + other.perimeter()
        new_a = self.a
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __sub__(self, other):
        '''Переопределенный дандер метод вычетания двух прямоугольников.'''
        new_perimeter = abs(self.perimeter() - other.perimeter())
        new_a = min([self.a, self.b, other.a, other.b])
        new_b = new_perimeter / 2 - new_a
        return Rectangle(new_a, new_b)

    def __str__(self):
        '''Переопределенный дандер метод строчного выведения экземпляра класса'''
        return f'Прямоугольник {self.a} x {self.b}'


if __name__ == '__main__':
    rect_1 = Rectangle(2, 5)
    # rect_2 = Rectangle(5, 10)
    # print(rect_1.a)
    # print(rect_1.b)
    
    rect_1.a = -1 # пытаемся передать отрицательное значение    
    print(rect_1)
    # print(rect_2)
    # # print(f'{rect.perimeter()= } {rect.area()= }')
    # # print(f'{rect_1.perimeter()= } {rect_1.area()= }')
    # res_sum = rect_1 + rect_2
    # print(res_sum.a, res_sum.b)
    # res_sub = rect_1 - rect_2
    # print(res_sub.a, res_sub.b)

    # rect_1.__dict__ # получим ошибку, поскольку экземпрляр хранит только атрибуты перечисленные в __slots__ 