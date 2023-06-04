'''Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до 
наибольшего включительно'''


def convert_text(text: str) -> dict[int: int]:
    res = {}
    splited_text = sorted([int(i) for i in text.split()])
    for i in range(splited_text[0], splited_text[1] + 1):
        res[chr(i)] = i
    return res


print(convert_text('509 501'))