''' Задание 1
Создайте функцию-замыкание, которая запрашивает два целых числа:
от 1 до 100 для загадывания,
от 1 до 10 для количества попыток
Функция возвращает функцию, которая через консоль просит угадать загаданное 
число за указанное число попыток.'''

from typing import Callable


def two_numbers(numOffAttepts: int, hiddenNum: int) -> Callable[[], None]:
    '''Возвращает фуркцию, запрашивающую через консоль число
    :numOffAttepts: число попыток
    :hiddenNum: загаданное число '''
    def guess_number():
        for i in range(numOffAttepts):
            inputNum = int(input('Введите число для отгадывания от 1 до 100: '))
            if inputNum == hiddenNum:
                print(f'Вы угадали с {i+1} попытки')
                break
        else:
            print('Вы не угадали')

    return guess_number


two_numbers(3, 4)()
