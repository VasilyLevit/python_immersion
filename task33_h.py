'''Напишите функцию принимающую на вход только ключевые параметры и возвращающую 
словарь, где ключ — значение переданного аргумента, а значение — имя аргумента. 
Если ключ не хешируем, используйте его строковое представление.'''


def academic_performance(**kwargs) -> dict:
    academic_dict = {}
    for key, value in kwargs.items():
        if isinstance(value, (list, dict, set, bytearray)): # проверка изменяемости данных
        # if hash(value): # проверка на хешируемость (потребуется обработка ошибки)
            value = str(value)
        academic_dict[value] = key
    return academic_dict


print(academic_performance(chemical=5, phisics=4, mathematics=3))