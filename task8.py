money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05


def get_months_left(money_capital_, salary_, spend_, increase_):
    month_count = 0
    while money_capital_ >= spend_:
        money_capital_ += salary_ - spend_
        spend_ *= 1 + increase_
        month_count += 1
    return month_count


print(get_months_left(money_capital, salary, spend, increase))
