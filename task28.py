'''Функция принимает на вход три списка одинаковой длины:
имена str,
ставка int,
премия str с указанием процентов вида “10.25%”.
Вернуть словарь с именем в качестве ключа и суммой премии в качестве значения.
Сумма рассчитывается как ставка умноженная на процент премии'''

def calc_bonus(names: list[str], salary: list[int], bonus: list[str]) -> dict[str: float]:
    return {names: salary / 100 * bonus
            for names, salary, bonus in zip(names, salary, (float(i[:-1]) for i in bonus))}


print(calc_bonus(['вася', 'петя', 'коля'], [10000, 20000, 30000], ['12.5%', '15%', '10%']))
