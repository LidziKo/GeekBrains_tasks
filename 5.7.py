import json

my_file = open('file57.txt', 'r', encoding='UTF-8')

info_about_company = dict()
average_profit = dict()
number_of_firms = 0
total_profit = 0

for line in my_file:
    position = line.split(' ')
    company_name = position[0]
    revenue = position[2]
    losses = position[3].split('\n')[0]
    profit = float(revenue) - float(losses)
    if profit >= 0:
        total_profit += profit
    number_of_firms += 1
    info_about_company[company_name] = profit

average_profit['average_profit'] = (total_profit / number_of_firms)

finish_result = [info_about_company, average_profit]
print(finish_result)

with open('my_file.json', 'x') as write_f:
    json.dump(finish_result, write_f)
