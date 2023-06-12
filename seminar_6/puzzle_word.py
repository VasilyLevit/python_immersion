'''Создайте модуль с функцией внутри.
Функция получает на вход загадку, список с возможными вариантами отгадок и 
количество попыток на угадывание.
Программа возвращает номер попытки, с которой была отгадана загадка или ноль, 
если попытки исчерпаны'''

from extension_puzzle import save_statistic


def puzzle(question: str, answers: list[str], limit: int) -> str:
    '''Возвращает номер попытки на угадывание
    :param question: загадка
    :param answer: список вариантов правильных ответов
    :limit: максимальное количество попыток
    :return: сообщение с номером удачной попытки или неудачи
    '''
    count = 1 # счётчик попыток
    guess_right = True
    while count <= limit:
        answer = input(f'Отгадайте загадку: {question}: ')
        if answer in answers:
            save_statistic(question, count)   
            print(f'Поздравляю. Вы отгадали с {count} попытки')
            return
        else:
            guess_right = False
            count += 1
            print('Ответ не верный, попробуйте ещё раз')
    if not guess_right:
        save_statistic(question, count)
        return f'У вас осталось 0 попыток. К сожалению вы не угадали.'
