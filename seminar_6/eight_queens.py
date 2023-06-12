''' Добавьте в пакет, созданный на семинаре шахматный модуль. Внутри него 
напишите код, решающий задачу о 8 ферзях. Известно, что на доске 8×8 можно 
расставить 8 ферзей так, чтобы они не били друг друга. 
Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара 
бьющих друг друга.
Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 
8 ферзей. Если ферзи не бьют друг друга верните истину, а если бьют - ложь.'''

import random

SIZE_DESK = 8
EMPTY = 0
BUSY = 1

def show_board(desk: list[int]) -> None:
    '''Вывод координат ферзей'''
    print("Координаты ферзей")
    print(*desk, sep='\n')


def pure_board () -> list[list[int]]:
    ''' Создаёт чистую доску (поля заполнены нулями)
        :return: доска (матрица) заполненная нулями
        '''    
    return [[EMPTY for _ in range(SIZE_DESK)] for _ in range(SIZE_DESK)]


def chess_position(queen_positions: list[list[int]]) -> list[list[int]]:
    '''Заполняет доску ферзями. 1 - поле с ферзём, 0 - поле пустое
    :queen_positions: список с поизициями ферзей
    :return: доска (матрица) с единицами на позициях ферзей
    '''
    board = pure_board()
    for i in range(len(queen_positions)):
        board[queen_positions[i][0]][queen_positions[i][1]] = BUSY
    return board


def _check_lines(chess_pos: list[int]) -> bool:
    '''Проверка горизонталей и вертикалей на наличие больше одного ферьзя'''
    for raw in chess_pos:
        if sum(raw) > 1:
            return False
    for col in zip(*chess_pos):
        if sum(col) > 1:
            return False
    return True


def _check_diagonal_1(chess_pos: list[int]) -> bool:
    '''Проверка диагоналей от главной вниз и вверх'''
    sum_diag = 0
    for raw in range(SIZE_DESK):
        for el in range(SIZE_DESK - raw): # пробегаем по значениям диагонали
            # print(SIZE_DESK - 1 - el, SIZE_DESK - 1 - raw - el, sum_diag) # тестовая
            sum_diag += chess_pos[SIZE_DESK - 1 - el][SIZE_DESK - 1 - raw - el]           
            if sum_diag > 1:
                return False
        sum_diag = 0
        # от главной вверх
        for el in range(SIZE_DESK - raw): # пробегаем по значениям диагонали
            sum_diag += chess_pos[SIZE_DESK - 1 - raw - el][SIZE_DESK - 1 - el]
            # print(SIZE_DESK - 1 - el, SIZE_DESK - 1 - raw - el, sum_diag) # тестовая
            if sum_diag > 1:
                return False
        sum_diag = 0
    return True


def _check_diagonal_2(chess_pos: list[int]) -> bool:
    '''Проверка диагоналей от побочной вверх'''
    sum_diag = 0
    for raw in range(SIZE_DESK):
        for el in range(SIZE_DESK - raw): # пробегаем по значениям диагонали
            sum_diag += chess_pos[el][SIZE_DESK - 1 - raw - el]
            # print(el, SIZE_DESK - 1 - raw - el, sum_diag) # тестовая
            if sum_diag > 1:
                return False
        sum_diag = 0
    return True


def _check_diagonal_3(chess_pos: list[int]) -> bool:
    '''Проверка диагоналей от побочной вниз'''
    sum_diag = 0
    for raw in range(SIZE_DESK):
        for el in range(raw, SIZE_DESK): # пробегаем по значениям диагонали
            sum_diag += chess_pos[SIZE_DESK - 1 - el + raw][el]
            # print(SIZE_DESK - 1 - el + raw , el, chess_pos[SIZE_DESK - 1 - el][el]) # тестовая
            if sum_diag > 1:
                return False
        sum_diag = 0
    return True


def is_capture(position: list[int]) -> bool:
    '''Проверяет, возможно ли взятие ферзями друг друга'''
    if _check_lines(position) and \
       _check_diagonal_1(position) and \
       _check_diagonal_2(position) and \
       _check_diagonal_3(position):
        return True
    return False


def random_queen_position() -> list[(int)]:
    '''Генерация случайных координат ферзей'''    
    coordinates = []
    i = 0
    while i < SIZE_DESK:
        x, y = random.randint(0, SIZE_DESK-1), random.randint(0, SIZE_DESK-1)
        if (x, y) not in coordinates:
            coordinates.append((x, y))
            i += 1
    return coordinates


def show_success_position(count: int) -> None:
    '''Вывод удачных комбинаций при рандомной герерации'''   
    count_gen_position = 0 # счётчик сгенерированных случайных комбинаций
    while count > 0 and count_gen_position < 100_000:       
        chess_pos = chess_position(random_queen_position())
        count_gen_position += 1
        print(is_capture(chess_pos)) # тест - выдача резултьтатов проверки
        if is_capture(chess_pos):
            show_board(chess_pos) # вывод удачной расстановки ферзей
            count -= 1


if __name__ == "__main__":
    queen_positions = [(0, 2), (1, 5), (2, 3), (3, 0), (4, 7), (5, 4), (6, 6), (7, 1)]
    chess_pos = chess_position(queen_positions)  
    show_board(chess_pos)
    print(is_capture(chess_pos))

    
    show_success_position(1) # запуск программы с рандом генерацией ферзей
