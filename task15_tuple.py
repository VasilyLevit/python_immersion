'''Создайте вручную кортеж содержащий элементы разных типов.
Получите из него словарь списков, где:
ключ — тип элемента,
значение — список элементов данного типа.'''

input_tuple = (3, 'Hello', 5.12, 14, 'Hi')
result_dict = {}

for i in input_tuple:
    result_dict.setdefault(type(i),[]).append(i)
    
print(result_dict)