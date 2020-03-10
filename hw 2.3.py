name_of_months = ['зима', 'зима', 'весна', 'весна', 'весна', 'лето', 'лето', 'лето', 'осень', 'осень', 'осень', 'зима']
dict_of_months = {1: 'зима', 2: 'зима', 3: 'весна', 4: 'весна', 5: 'весна', 6: 'лето', 7: 'лето', 8: 'лето', 9: 'осень',
                  10: 'осень', 11: 'осень', 12: 'зима'}

str_month_number = input('Введите номер месяца в виде целого числа от 1 до 12: ')

if str_month_number.isdigit():
    month_number = int(str_month_number)
    if 0 < month_number < 13:
        # реализация через список
        season = name_of_months[month_number - 1]  # -1, потому что обращаемся к индексу списка
        print(f'{month_number}-й месяц - это {season} (список)')

        # реализация через словарь
        season = dict_of_months[month_number]  # обращаемся непосредственно к ключу
        print(f'{month_number}-й месяц - это {season} (словарь)')
