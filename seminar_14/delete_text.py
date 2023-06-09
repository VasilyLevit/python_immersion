''' Задача 1
Создайте функцию, которая удаляет из текста все символы кроме букв латинского алфавита и пробелов.
Возвращается строка в нижнем регистре.'''

''' Задача 2
Напишите для задачи 1 тесты doctest. Проверьте следующие варианты:
возврат строки без изменений (т.е. всё введено правильно - все буквы латинские, с маленькой буквы и без пробелов)
возврат строки с преобразованием регистра без потери символов
возврат строки с удалением знаков пунктуации
возврат строки с удалением букв других алфавитов
возврат строки с учётом всех вышеперечисленных пунктов (кроме п. 1)'''

import string
import doctest


def remove_chars(text: str) -> str:    
    ''' Удаляет из текста все символы кроме букв латинского алфавита и пробелов. Возвращает строку в нижем регистре.
    :param text: input string
    :return: строка в нижнем регистре
    >>> remove_chars('dddddd dddd')
    'dddddd dddd'
    >>> remove_chars('AAA AA')
    'aaa aa'
    >>> remove_chars('a,a,n: v.v;')
    'aan vv'
    >>> remove_chars('БВАОПоаоваов')
    ''
    >>> remove_chars('WWW,3322,ГГ:')
    'www'
    '''
    abc = string.ascii_letters + ' ' # получаем с помощью модуля string коллекцию латинских символов
    out_text = ''
    for char in text:
        if char in abc:
        #    out_text += char
           out_text += ''.join(char)        
    return out_text.lower()


if __name__ == '__main__':
    # print(remove_chars('Hello mr Вася')) # Задание 1
    doctest.testmod(verbose=True) # Задание 2
