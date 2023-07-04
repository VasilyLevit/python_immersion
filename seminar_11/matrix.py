''' Домашнее задание
Добавьте ко всем задачам с семинара строки документации и методы вывода информации на печать.
Создайте класс Матрица. Добавьте методы для:
○ вывода на печать,
○ сравнения,
○ сложения,
○ *умножения матриц'''


class Matrix:
    '''Класс матрица переопределенными методами печати, сравнения, сложения и умножения.'''

    def __init__(self, matrix: list[int]):
        '''Метод принимает параметр - матрица.'''
        self.matrix = matrix   

    def __eq__(self, other):
        '''Метод сравнения матриц. Равны, когда равны их длины и каждый элемент.'''
        return True if self.matrix == other.matrix else False

    def __add__(self, other):
        '''Метод поэлементного сложения матриц. '''
        result = []
        row = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[0])):
                row.append(self.matrix[i][j] + other.matrix[i][j])
            result.append(row)
            row = []
        return Matrix(result)

    def __mul__(self, other):
        '''Метод умножения матриц.'''
        m = len(self.matrix)
        n = len(other.matrix)
        k = len(other.matrix[0])
        result = [[0 for _ in range(k)] for _ in range(m)]
        for i in range(m):
            for j in range(k):
                result[i][j] = sum(self.matrix[i][k] * other.matrix[k][j] for k in range(n))
        return Matrix(result)
    
    def __str__(self):
        'Метод печати матрицы.'
        result = ''
        for row in self.matrix:
            for elem in row:
                result += ''.join(f'{elem}\t')
            result += ''.join('\n')
        return result


if __name__ == '__main__':
    m_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    m_2 = Matrix([[2, 2, 2], [2, 2, 2], [2, 2, 2]])    
    m_3 = m_1 + m_2    
    m_4 = m_1 * m_2
    print(m_3)
    print(m_4)
    print('True') if m_1 == m_2 else print('False')
