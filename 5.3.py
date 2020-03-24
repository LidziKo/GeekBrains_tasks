my_file = open('file53.txt', 'r', encoding='UTF-8')

less_than_20k = []
bottom_line = 20000
amount_of_income = 0
number_of_employees = 0


for line in my_file:
    name, income = line.split(' ')
    if float(income) < bottom_line:
        less_than_20k.append(name)
    amount_of_income += float(income)
    number_of_employees += 1

average_income = amount_of_income / number_of_employees

print(f'Сотрудники {less_than_20k} имеют оклад меньше 20.000 рублей\n'
      f'Средняя величина дохода сотрудников составляет {average_income} рублей')

my_file.close()
