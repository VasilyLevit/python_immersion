''' Напишите программу, которая получает целое число и возвращает его 
шестнадцатеричное строковое представление. Функцию hex используйте для 
проверки своего результата. '''

dec_num: int = 438 # Преобразуемое значение в 10м формате
hex_num = ''
base: int = 16 # Основание системы счисления

print(hex(dec_num)) # Проверка функцией hex

# symbol - символ разряда начиная с младшего
while dec_num > 0:
    symbol = dec_num % base
    dec_num //= base
    match symbol:
        case 10:
            symbol = 'a'
        case 11:
            symbol = 'b'
        case 12:
            symbol = 'c'
        case 13:
            symbol = 'd'
        case 14:
            symbol = 'e'
        case 15:
            symbol = 'f'
    hex_num = str(symbol) + hex_num
    
print(f'0x{hex_num}')
