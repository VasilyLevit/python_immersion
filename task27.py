'''Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком. Её описание есть в википедии'''

def bubble_sort(numbers: list[int]) -> list[int]:
    length = len(numbers)
    for i in range(length):
        for j in range(length - 1 - i):
            if numbers[j + 1] < numbers[j]:
                numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]
    return numbers


print(bubble_sort([2, 1, 3, 6, 1, 2]))