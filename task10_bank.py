''' Задание №10 (недоделана)
Напишите программу банкомат.
✔ Начальная сумма равна нулю
✔ Допустимые действия: пополнить, снять, выйти
✔ Сумма пополнения и снятия кратны 50 у.е.
✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
✔ Нельзя снять больше, чем на счёте
✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
операцией, даже ошибочной
✔ Любое действие выводит сумму денег '''

BALANCE = 0
MIN = 50
COMMISS_RATE = 0.015
BONUS = 0.03
TAX = 0.10
count_opreration = 0
commission = 1

mode = input('Введите операцию up out exit: ')

match mode:
    case "top_up":
        pass
    case "out":
        ...
    case "exit":
        ...

cash = 0
# пополнение баланса
if cash % MIN == 0:
    BALANCE += cash
    count_opreration += 1

# снятие
if cash % MIN == 0 and BALANCE >= MIN:
    commission = cash * COMMISS_RATE
    if commission < 30:
        commission = 30
    elif commission > 600:
        commission = 600
    else:
        commission

if cash + commission <= BALANCE:
    BALANCE -= (cash + commission)
    count_opreration += 1

