salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен


def get_money_needed(salary_, spend_, months_, increase_):
    need_money = 0
    for i in range(1, months_ + 1):
        if i >= 2:
            spend_ *= 1 + increase_
        need_money += spend_ - salary_
    return round(need_money)


print(get_money_needed(salary, spend, months, increase))
