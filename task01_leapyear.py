# Високосный год Григорианского календаря

START_TEAR = 1582
year = int(input('Введите год в формате yyyy: '))

if year < START_TEAR:
    result = "Григорианский календарь начинается с 1582 года"
elif year % 4 != 0:
    result = "обычный"
elif year % 100 == 0:
    if year % 400 == 0:
        result = "високосный"
    else:
        result ="обычный"
else:
    result = "високосный"
print (result)

# Краткая запись условия
# if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
#     print("Обычный")
# else:
#     print("Високосный")