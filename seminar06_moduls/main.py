from sys import argv
# from guess_num import gen_num
from puzzle_word import puzzle as puz
from extension_puzzle import lib_puzzle as lib, show_statistic


if __name__ == '__main__':
    # gen_num(10, 20, 5) # Задача_1
    # gen_num(*(int(i) for i in argv[1:])) # Задача_2
    print(puz('Зимой и летом одним цветом', ['ель', 'ёлка', 'Елка', 'Ель'], 3)) # Задача 3
    puzzle_dict = {
        'Зимой и летом одним цветом': ['ель', 'ёлка', 'Елка', 'Ель'],
        'Красна девица, а коса на улице': ['морковь', 'морковка'],
        'Два кольца, два конца, в по середине гвоздик': ['ножницы']
    }
    print(lib(puzzle_dict, 3))
    show_statistic()
