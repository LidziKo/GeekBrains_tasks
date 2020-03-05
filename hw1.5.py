# 5

revenue = input('Выручка фирмы: ')
costs = input('Издержки фирмы: ')
revenue = int(revenue)
costs = int(costs)

if revenue > costs:

    # если гугл не врёт, то рентабельность рассчитывается так
    profitability = (revenue / costs)
    print('Фирма работает в прибыль!\nРентабельность выручки: ', int(profitability))
    number_of_employees = input('кол-во сотрудников в фирме?: ')
    number_of_employees = int(number_of_employees)
    profit = (revenue - costs)
    profit_to_employee = profit / number_of_employees
    print('Прибыль фирмы в расчете на одного сотрудника: ', int(profit_to_employee), '!')
else:
    print('Очень жаль, но фирма не имеет дохода или работает в убыток!')
