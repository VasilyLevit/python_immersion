'''Напишите функцию для транспонирования матрицы'''


def matrix_transparent(*matrix: tuple[int]) -> tuple[int] | str:
    '''Транспонирование матрицы
    transparentable - возможность транспонирования (квадратность матрицы)'''
    print(*matrix, sep='\n')
    transparentable = True
    for raw in matrix:
        if len(raw) != len(matrix):
            transparentable = False
      
    if transparentable:       
        return zip(*matrix)
    else:
        return 'Матрицу нельзя транспорировать'


print("Транспонированная матрица: ",
      *matrix_transparent((1, 2, 3), (4, 5, 6), (7, 8, 9)), sep='\n')