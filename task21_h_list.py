''' Дан список повторяющихся элементов. Вернуть список с дублирующимися элементами. 
В результирующем списке не должно быть дубликатов. '''

input_list = [1,4,7,4,9,5,9]
result_list = []

print('Input List:', input_list)

for i in input_list:
    if input_list.count(i) > 1 and i not in result_list:
        result_list.append(i)

print('Output list:', result_list)