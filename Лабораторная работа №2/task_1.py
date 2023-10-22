money_capital = 20000.00  # Подушка безопасности
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
increase = 0.05  # Ежемесячный рост цен


months = 0
increasing = 1 + increase
count_of_increasings = 0

while money_capital > 0:
    months += 1
    money_capital += salary
    money_capital -= spend * increasing ** months
    count_of_increasings += 1

print("Количество месяцев, которое можно протянуть без долгов:", months)
