'''Создайте модуль с функцией внутри.
Функция принимает на вход три целых числа: нижнюю и верхнюю границу и количество 
попыток.
Внутри генерируется случайное число в указанных границах и пользователь должен 
угадать его за заданное число попыток.
Функция выводит подсказки “больше” и “меньше”.
Если число угадано, возвращается истина, а если попытки исчерпаны - ложь.'''

'''Улучшаем задачу
Добавьте возможность запуска функции “угадайки” из модуля в командной строке 
терминала.
Строка должна принимать от 1 до 3 аргументов: параметры вызова функции.
Для преобразования строковых аргументов командной строки в числовые параметры 
используйте генераторное выражение'''

from random import randint as rnd
# from sys import argv
# from extension_puzzle import lib_puzzle as lib
# from extension_puzzle import show_statistic
# import check_year


def gen_num(low: int = 1, height: int = 2, try_count: int = 5) -> bool:
    '''Возварщает результат попытки угадать число
    @param '''
    result = False
    num = rnd(low, height+1)
    search_count = 0
    while search_count < try_count:
        ask_value = int(input(f"Введите число от {low} до {height}: "))
        if ask_value == num:
            print("Вы угадали")
            result = True
            break
        if ask_value < num:
            print("Загаданное число больше")
        else:
            print("Загаданное число меньше")
        search_count += 1
    else:
        print("Попытки закончились")

    return result
