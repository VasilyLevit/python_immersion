'''Добавить логирование ошибок и полезной информации. Также реализовать возможность запуска из
командной строки с передачей параметров'''

from random import randint
import logging
import argparse

FORMAT = "{levelname} - {asctime} - {funcName}: {msg}"

logging.basicConfig(format=FORMAT, style="{", filename='check_triangle.log', level=logging.INFO, encoding="UTF-8")
logger = logging.getLogger(__name__)


def check_triangle(a, b, c):
    '''Checking figure is a triangle
    :a, b, c: sides of triangle
    '''
    if a + b > c and b + c > a and a + c > b:
        logger.info(f'Треугольник со сторонами {a}/{b}/{b} существует')
        if a == b == c:
            logger.info(f'Треугольник со сторонами {a}/{b}/{b} равносторонний')
        elif a == b or b == c or c == a:
            logger.info(f'Треугольник со сторонами {a}/{b}/{b} равнобедренный')
        else:
            logger.info(f'Треугольник со сторонами {a}/{b}/{b} разносторонний')
    else:
        logger.error(f'Треугольника со сторонами {a}/{b}/{b} не существует')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Проверка треугольника")
    parser.add_argument("param", metavar="a b c", type=int, nargs=3, help="Введите a b c через пробел")
    args = parser.parse_args()
    check_triangle(*args.param)
