from sys import argv
from check_year import date_validator

if __name__ == '__main__':
    # data = '12.01.1999'
    # print(date_validator(data))
    print(date_validator(argv[1]))
