'''Пользователь вводит строку текста. Вывести каждое слово с новой строки.
Строки нумеруются начиная с единицы. Слова выводятся отсортированными согласно 
кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.'''

text = 'Пользователь вводит строку текста. Вывести каждое слово с новой строки'
# решение с семинара, непонятно
result = sorted(text.split())
[print(f"{i} - {word:>{len(max(result, key=len))}}") for i, word in enumerate(result, 1)]