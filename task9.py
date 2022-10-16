salary = 5000  # зарплата
spend = 6000  # траты
months = 10  # количество месяцев
increase = 0.03  # рост цен

# TODO Оформить решение

i = 1
all_spend = 0
all_salary = 0

while i <= 10:
    all_salary += salary
    i += 1
    all_spend += spend
    spend *= 1.03

need_money = all_spend - all_salary
print(round(need_money))
