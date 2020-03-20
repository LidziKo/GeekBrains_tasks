import sys


def payment_salary():
    wt = working_time
    rph = rate_per_hour
    bon = bonus
    return (wt * rph) + bon


if len(sys.argv) == 4:
    while True:
        working_time = sys.argv[1]
        rate_per_hour = sys.argv[2]
        bonus = sys.argv[3]

        if working_time.isdigit() and rate_per_hour.isdigit() and bonus.isdigit():
            working_time = float(working_time)
            rate_per_hour = float(rate_per_hour)
            bonus = float(bonus)

            if working_time > 0 or rate_per_hour > 0:
                month_salary = payment_salary()
                print(f'Заработная плата сотрудника составила: {month_salary} рублей')
                break
            else:
                print('Введены некорректрые значения рабочих часов / ставки в час!')
                continue

        else:
            print('Введите данные в числовом формате!')
            continue
else:
    print('аргументы: working_time rate_per_hour bonus\n'
          'working_time - кол-во отработанных часов\n'
          'rate_per_hour - ставка в час\n'
          'bonus - размер премии')
