'''Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
Напишите функцию, которая заменяет содержимое переменных оканчивающихся на s 
(кроме переменной из одной буквы s) на None. Значения не удаляются, 
а помещаются в одноимённые переменные без s на конце.'''


def insteadof_s(balls, ball, games, game, s) -> None:
    '''Заменяет значения переменных различающихся окончанием "s" '''
    words = locals()
    print(words)
    for key in words:
        if key.endswith('s') and key != 's':
            words[key[:-1:]] = words[key]
            words[key] = None
    print(words)

print(insteadof_s(6, 1, 4, 1, 9))
 