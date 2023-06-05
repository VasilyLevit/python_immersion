'''Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег'''

def input_amount():
    '''Получение данных о сумме опереции и проверка условию'''
    cash = int(input(f'Введите сумму кратную {MIN}: '))
    if cash % MIN == 0:
        return cash
    print('Неверная сумма')
    return 0


def calc_bonus():
    '''Рсчёт коэффициента начисления за количество операций'''
    global count_opreration
    bonus = 0
    if count_opreration % (LIMIT_OPERATION + 1) == 0:
        bonus = BONUS
        count_opreration = 0
    return bonus


def calc_commission(cash):
    '''Расчёт коммиссии'''
    commiss_rate = 0.015
    commission = cash * commiss_rate
    if commission < 30:
        commission = 30
    elif commission > 600:
        commission = 600
    else:
        commission
    return commission


def top_up() -> None:
    '''Пополнение счёта'''
    global count_opreration
    global balance
    cash = input_amount()
    if cash:        
        balance += cash + (cash * calc_bonus())
        print('Cчёт пополнен')
        count_opreration += 1
    else:
        print('Ошибка пополнения')
 

def out() -> None:
    '''Выдача наличных'''
    global count_opreration
    global balance
    cash = input_amount()
    if cash:
        commission = calc_commission(cash)
        if cash + commission <= balance:
            balance -= (cash + commission - cash * calc_bonus())
            print(f'Выдача произведена. Комиссия составила: {commission}')
            count_opreration += 1
        else:
            print('Недостаточно средств')
    else:
        print('Ошибка снятия')


MIN = 50
BONUS = 0.03
TAX = 0.10
LIMIT_OPERATION = 3
count_opreration = 1
balance = 0.0

while True:
    mode = input('Введите операцию up out exit: ')
    match mode:
        case "up":
            print(f'Баланс: {balance}')
            top_up()
            print(f'Баланс: {balance}')
        case "out":
            print(f'Баланс: {balance}')
            out()
            print(f'Баланс: {balance}')
        case "exit":
            break
