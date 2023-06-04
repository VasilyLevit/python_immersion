'''Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа введённой  
строки отсортированный по убыванию'''

def unique_unicode(text: str) -> list[int]:
    res = set() # для создания списка уникальных элементов
    for s in text:
        res.add(ord(s))
    return sorted(res, reverse=True)

print(unique_unicode('привет, как дела?'))