# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

input_incorrect = True
min_value = 1
max_value = 100000

while input_incorrect:
    number = int(input("Введиет целое число от 1 до 100 тысяч: "))
    if min_value <= number <= max_value:
        input_incorrect = False

simple_num = True
for i in range(2,number):
    if number % i == 0:
        simple_num = False
        break

print('Число простое') if simple_num else print('Число составное')    
