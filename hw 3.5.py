def calc_str_sum(numbers, pos):  # "! 1 2 3 4"
    if pos != -1:
        numbers = numbers[:pos]
    numbers = numbers.split()
    numbers = list(map(int, numbers))
    return sum(numbers)


special = '!'
nums_sum = 0

while True:
    user_numbers = input('Введите строку из нескольких чисел, разделённых пробелами.\nДля завершения программы '
                         'введите "!": ')

    spec_pos = user_numbers.find(special)
    nums_sum += calc_str_sum(user_numbers, spec_pos)
    print(f'Сумма чисел равна {nums_sum}')

    if spec_pos != -1:
        break
