'''Добавьте в модуль с загадками функцию, которая хранит словарь списков.
Ключ словаря - загадка, значение - список с отгадками.
Функция в цикле вызывает загадывающую функцию, чтобы передать ей все свои загадки.'''


import puzzle_word

__all__ = ['new_puzzle', 'save_statistic', 'show_statistic']

_ANSWERS = dict()


def lib_puzzle(puzles: dict, limit: int) -> None:
    '''Вызывает в цикле модуль с загадывающей функцией передавая загадки из словаря
    :param puzles: словарь загадок с ответами
    :param limit: количество попыток на отгадывание
    '''
    for key, value in puzles.items():
        puzzle_word.puzzle(key, value, limit)


''' Добавьте в модуль с загадками функцию, которая принимает на вход строку
(текст загадки) и число (номер попытки, с которой она угадана).
Функция формирует словарь с информацией о результатах отгадывания.
Для хранения используйте защищённый словарь уровня модуля.
Отдельно напишите функцию, которая выводит результаты угадывания из защищённого 
словаря в удобном для чтения виде.
Для формирования результатов используйте генераторное выражение.'''


def save_statistic(puzzle: str, count_right: int) -> None:
    '''Формирует словарь с информацией о результатах отгадывания'''
    _ANSWERS[puzzle] = count_right


def show_statistic():
    '''Выводит результаты угадываний из словаря'''
    print(*(f'{key} - {value}\n' for key, value in _ANSWERS.items()))
