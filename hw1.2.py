# 2

sec_in_hour = 3600
sec_in_min = 60

seconds = input('введите количество секунд: ')
seconds = int(seconds)

hours = seconds // sec_in_hour  # делим общее количество секунд на 3600 без остатка, получаем кол-во часов
seconds -= (hours*sec_in_hour)  # из общего кол-ва секунд отнимаем секунды, которые задействованы в часах
minutes = seconds // sec_in_min  # остаток от секунд делим без остатка на 60, чтобы получить минуты
seconds -= (minutes*sec_in_min)  # от количества секунд отнимаем те, которые зайдействованы в минутах

# ">" - добавление символа (0) слева;
# "0" - тот символ, который добавляется;
# "2" - минимальное кол-во символов, по которым необходимо выровнять
print(f'Время: {hours:>02}:{minutes:>02}:{seconds:>02}')
