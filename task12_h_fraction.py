''' Напишите программу, которая принимает две строки вида “a/b” — дробь с 
числителем и знаменателем. Программа должна возвращать сумму и *произведение 
дробей. Для проверки своего кода используйте модуль fractions. '''

import fractions


# Функция определения НОД
def gcd_euclid(num1, num2):
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 or num2


f1 = fractions.Fraction(1, 3) 
f2 = fractions.Fraction(3, 11)
print('Операции с дробями ',f1,'и',f2)
print('Используя тип fractions')  
print(f'{f1} + {f2} =',f1 + f2)
print(f'{f1} * {f2} =',f1 * f2)
print('Без использования класса')

# принимаемые дроби в виде строк
fs1 = '1/3'
fs2 = '3/11'

# разделяем строку на лист строкоых переменных
components_f1 = fs1.split('/')
components_f2 = fs2.split('/')

# преобразуем лист переменных в компоненты дроби
a1 = int(components_f1[0])
b1 = int(components_f1[1])
a2 = int(components_f2[0])
b2 = int(components_f2[1])

# сложение дробей
a = a1 * b2 + a2 * b1
b = b1 * b2
common_devisor = gcd_euclid(a,b) # получение наибольшого общего делителя для сокращения дроби
if common_devisor > 1:
    a //= common_devisor
    b //= common_devisor
print(f'{a1}/{b1} + {a2}/{b2} = {a}/{b}')

# умножение дробей
a = a1 * a2
b = b1 * b2
common_devisor = gcd_euclid(a,b)
if common_devisor > 1:
    a //= common_devisor
    b //= common_devisor
print(f'{a1}/{b1} * {a2}/{b2} = {a}/{b}')

