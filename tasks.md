# Задача_1 
Программа запрашивает год и проверяет его на високосность.
*Распишите все возможные проверки в цепочке elif. Откажитесь от магических чисел.*
*Обязательно учтите год ввода Григорианского календаря. В коде должны быть один input и один print.*
# Задача_2 
Пользователь вводит число от 1 до 999. Используя операции с числами
сообщите что введено: цифра, двузначное число или трёхзначное число.
Для цифры верните её квадрат, например 5 - 25
Для двузначного числа произведение цифр, например 30 - 0
Для трёхзначного числа его зеркальное отображение, например 520 - 25
Если число не из диапазона, запросите новое число
Откажитесь от магических чисел
В коде должны быть один input и один print
# Задача_3
Нарисовать в консоли ёлку спросив у пользователя количество рядов.
Пример результата: Сколько рядов у ёлки? 5
    *
   ***
  *****
 *******
*********
# Задача_4
Выведите в консоль таблицу умножения от 2х2 до 9х10 как на школьной тетрадке.
2 строки и 4 столбца

# Домашние задачи 1
Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано a, b, c —
стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой
двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника
с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним,
равнобедренным или равносторонним.

# Домашние задачи 2
Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

# Домашние задачи 3
Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
должна подсказывать «больше» или «меньше» после каждой попытки. Для генерации случайного
числа используйте код:
from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)

# Задание 5
Создайте несколько переменных разных типов. Проверьте к какому типу относятся созданные переменные.

# Задание 6
Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. Для каждого элемента в цикле выведите:
✔ порядковый номер начиная с единицы
✔ значение
✔ адрес в памяти
✔ размер в памяти
✔ хэш объекта
✔ результат проверки на целое число только если он положительный
✔ результат проверки на строку только если он положительный
Добавьте в список повторяющиеся элементы и сравните на результаты

# Задание 7
✔ Напишите программу, которая получает целое число и возвращает его двоичное, 
восьмеричное строковое представление.
✔ Функции bin и oct используйте для проверки своего результата, а не для решения.
Дополнительно:
✔ Попробуйте избежать дублирования кода в преобразованиях к разным системам счисления
✔ Избегайте магических чисел
✔ Добавьте аннотацию типов где это возможно

# Задание 8
✔ Напишите программу, которая вычисляет площадь круга и длину окружности по 
введённому диаметру.
✔ Диаметр не превышает 1000 у.е.
✔ Точность вычислений должна составлять не менее 42 знаков после запятой.

# Задание 9
✔ Напишите программу, которая решает квадратные уравнения даже если дискриминант 
отрицательный.
✔ Используйте комплексные числа для извлечения квадратного корня.

# Задание 10
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег

# Домашние задачи 11
Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. Функцию hex используйте для 
проверки своего результата.

# Домашние задачи 12
Напишите программу, которая принимает две строки вида “a/b” — дробь с 
числителем и знаменателем. Программа должна возвращать сумму и *произведение 
дробей. Для проверки своего кода используйте модуль fractions.

# Задание No13
Вручную создайте список с целыми числами, которые
повторяются. Получите новый список, который содержит
уникальные (без повтора) элементы исходного списка.
*Подготовьте два решения, короткое и длинное, которое
не использует другие коллекции помимо списков.

# Задание 14
Погружение в Python | Коллекции
Пользователь вводит данные. Сделайте проверку данных
и преобразуйте если возможно в один из вариантов ниже:
Целое положительное число
Вещественное положительное или отрицательное число
Строку в нижнем регистре, если в строке есть
хотя бы одна заглавная буква
Строку в нижнем регистре в остальных случаях

# Задание 15
Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.

# Задание 16
Создайте вручную список с повторяющимися элементами.
Удалите из него все элементы, которые встречаются дважды.

# Задание 17
Создайте вручную список с повторяющимися целыми числами. Сформируйте список с 
порядковыми номерами нечётных элементов исходного списка.
Нумерация начинается с единицы.

# Задание 18
Пользователь вводит строку текста. Вывести каждое слово с новой строки.
Строки нумеруются начиная с единицы. Слова выводятся отсортированными согласно кодировки Unicode.
Текст выравнивается по правому краю так, чтобы у самого длинного
слова был один пробел между ним и номером строки.

# Задание 19
Пользователь вводит строку текста.
Подсчитайте сколько раз встречается каждая буква в строке без использования
метода count и с ним.
Результат сохраните в словаре, где ключ — символ, а значение — частота встречи
символа в строке.
Обратите внимание на порядок ключей.
Объясните почему они совпадают или не совпадают в ваших решениях.

# Задание 20
Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции с множествами. Код должен расширяться
на любое большее количество друзей.


# Домашнее задание 21
Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов.

# Домашнее задание 22
В большой текстовой строке подсчитать количество встречаемых
слов и вернуть 10 самых частых. Не учитывать знаки препинания
и регистр символов. За основу возьмите любую статью
из википедии или из документации к языку

# Домашнее задание 23
Создайте словарь со списком вещей для похода в качестве
ключа и их массой в качестве значения. Определите какие
вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака

# Задание 24
Напишите функцию, которая принимает строку текста. Вывести функцией каждое слово с новой строки.
Строки нумеруются начиная с единицы
Слова выводятся отсортированными согласно кодировки Unicode
Текст выравнивается по правому краю так, чтобы у самого длинного слова был один пробел между ним и номером строки.

# Задание 25
Напишите функцию, которая принимает строку текста.
Сформируйте список с уникальными кодами Unicode каждого символа введённой строки отсортированный по убыванию.

# Задание 26
Функция получает на вход строку из двух чисел через пробел.
Сформируйте словарь, где ключом будет символ из Unicode, а значением - целое число.
Диапазон пар ключ-значение от наименьшего из введённых пользователем чисел до 
наибольшего включительно.

# Задание 27
Функция получает на вход список чисел.
Отсортируйте его элементы in place без использования встроенных в язык сортировок.
Как вариант напишите сортировку пузырьком. Её описание есть в википедии

# Задание 28
Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида “10.25%”.
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии

# Задание 29
Функция получает на вход список чисел и два индекса.
Вернуть сумму чисел между между переданными индексами.
Если индекс выходит за пределы списка, сумма считается до конца и/или начала списка.

# Задание 30
Функция получает на вход словарь с названием компании в качестве ключа
и списком с доходами и расходами (3-10 чисел) в качестве значения.
Вычислите итоговую прибыль или убыток каждой компании. Если все компании
прибыльные, верните истину, а если хотя бы одна убыточная — ложь.

# Задание 31
Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая при запуске заменяет содержимое переменных
оканчивающихся на s (кроме переменной из одной буквы s) на None.
Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

# Задание 32 (домашная)

Напишите функцию для транспонирования матрицы

# Задание 33 (домашная)
Напишите функцию принимающую на вход только ключевые
параметры и возвращающую словарь, где ключ — значение
переданного аргумента, а значение — имя аргумента. Если
ключ не хешируем, используйте его строковое представление.

# Задание 34 (домашная task10)
Возьмите задачу о банкомате из семинара 2. Разбейте её
на отдельные операции — функции. Дополнительно сохраняйте
все операции поступления и снятия средств в список.