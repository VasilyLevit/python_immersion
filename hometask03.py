# Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа
# должна подсказывать «больше» или «меньше» после каждой попытки.

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
count = 0
trys = 10

from random import randint
num = randint(LOWER_LIMIT, UPPER_LIMIT)
print('Угадайте число от 0 до 1000 за 10 попыток')

for i in range(1, trys+1):
    input_data = int(input(f"Попытка {i}: "))
    if input_data < num:
        print("больше")
    elif input_data > num:
        print("меньше")
    else:
        print("Вы отгадали")
        quit()
    if i == trys:
        print ("Вы исчерпали количество попыток")    
      