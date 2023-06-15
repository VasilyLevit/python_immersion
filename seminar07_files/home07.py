'''Задание домашнее: Напишите функцию группового переименования файлов. 
Она должна:
✔ принимать параметр желаемое конечное имя файлов. При переименовании в конце имени 
добавляется порядковый номер.
✔ принимать параметр количество цифр в порядковом номере.
✔ принимать параметр расширение исходного файла.
Переименование должно работать только для этих файлов внутри каталога.
✔ принимать параметр расширение конечного файла.
✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
[3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
✔ Соберите из созданных на уроке и в рамках домашнего задания функций пакет для 
работы с файлами.'''

from pathlib import Path



def rename_files(quantity_digits: int, extension: str, new_extension: str,
                min_letter_num: int, max_letter_num: int, new_name: Path = 'new') -> None:
    '''Групповое переименование файлов
    :quantity_digits: количество цифр в порядковом номере
    :extension: расширение исходного файла
    :new_extension: расширение конечного файла
    :min_letter_num: начало диапазоно - номер буквы имени исходного файла
    :max_letter_num: конец диапазона - номер буквы имени исходного файла
    :new_name: конечное имя файла'''
    ordinal_number = 1 # порядковый номер
    p = Path.cwd() # текущая директория
    for obj in p.iterdir(): # возвращаем объекты из текущей директории
        file = str(obj).split('/')[-1] # выделям название файла из общего пути       
        name, *ext = file.split('.')    # выделяем имя и расширение (*.ext для файлов без раширения, иначе приведет к ошибке)   
        # print(f'{file = }, {name = }, {ext = }\n') #test
        if  "".join(ext) == extension:
            Path(file).rename(f'{_cut_old_name(name, min_letter_num, max_letter_num)}{new_name}{_ordinal_counter(quantity_digits, ordinal_number)}.{new_extension}')
            ordinal_number += 1
           


def _ordinal_counter(quantity_digits: int, ordinal_number: int = 1) -> str:
    '''Возварщает порядковый номер'''
    string_num = str(ordinal_number)
    return (quantity_digits - len(string_num)) * '0' + string_num      
   


def _cut_old_name(name: str, min_letter_num: int, max_letter_num: int) -> str:
    '''Возвращает часть исходного имени в заданном диапазоне'''
    return name[min_letter_num:max_letter_num] #срез диапазона имени
