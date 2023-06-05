'''Напишите функцию, которая принимает строку текста. Сформируйте список с 
уникальными кодами Unicode каждого символа введённой строки отсортированный по 
убыванию'''


def unicode(text: str) -> list[int]:
    '''Возварщает unicode символов по убыванию'''
    result = set() # для создания списка уникальных элементов
    for symbol in text:
        result.add(ord(symbol))
    return sorted(result, reverse=True)


print(*unicode('Строки нумеруются начиная с единицы.'))