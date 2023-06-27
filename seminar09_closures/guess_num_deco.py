''' Задание 2 
Дорабатываем задачу 1. Превратите внешнюю функцию в декоратор.
Он должен проверять входят ли переданные в функцию угадайку числа в диапазоны 
[1, 100] и [1, 10].
Если не входят, вызывать функцию со случайными числами из диапазонов.'''

import random
from typing import Callable
# from count_start_deco import counter



def range_check(func: Callable):
    '''Проверка вхождения параметров внешней функции в заданный диапазон
    Возвращает функцию с изменёнными параметрами'''
    MAX_ATTEMPT = 10 
    MIN_ATTEMPT = 1 
    MAX_NUM = 100    
    MIN_NUM = 1

    def wrapper(*args, **kwargs):
        input_attempt, input_num = args
        if MIN_ATTEMPT >= input_attempt >= MAX_ATTEMPT:
            input_attempt = random.randint(MIN_ATTEMPT, MAX_ATTEMPT)
        if MIN_NUM >= input_num >= MAX_NUM:
            input_num = random.randint(MIN_NUM, MAX_NUM)
        return func(input_attempt, input_num)

    return wrapper


# @counter(3)
@range_check
def two_numbers(num_off_attepts: int, hidden_num: int) -> Callable[[], None]:
    def guess_number():
        for i in range(num_off_attepts):
            inputNum = int(input('Введите число для отгадывания от 1 до 100: '))
            if inputNum == hidden_num:
                print(f'Вы угадали с {i+1} попытки')
                break
        else:
            print('Вы не угадали')

    return guess_number


res = two_numbers(3, 102)
res()
