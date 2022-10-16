money_capital = 10000
salary = 5000
spend = 6000
increase = 0.05

month = -1  # количество месяцев, которое можно прожить
# TODO Оформить решение

while money_capital >= 0:
    left = salary - spend
    money_capital += left
    spend *= 1.05
    month += 1

print(month)
