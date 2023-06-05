'''Создайте словарь со списком вещей для похода в качестве ключа и их массой в 
качестве значения. Определите какие вещи влезут в рюкзак передав его максимальную
грузоподъёмность. Достаточно вернуть один допустимый вариант.
*Верните все возможные варианты комплектации рюкзака'''

backpack = {'tent': 5, 'sleep_bag': 2, 'food': 4, 'bottle': 2, 'camera': 1 }
max_weight = 12
list_things = []
total_weight = 0

for thing in backpack:
    if total_weight + backpack[thing] <= max_weight:
        total_weight += backpack[thing]
        list_things.append(thing)

print(*list_things,f'- общий вес {total_weight}кг.')
