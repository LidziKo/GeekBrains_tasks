def division(a, b):
    return a / b


while True:
    number1 = input('Введите число 1: ')
    number2 = input('Введите число 2: ')
    if number2 == '0':
        print('делить на 0 нельзя!')
    elif number1.isdigit() and number2.isdigit():
        number1 = int(number1)
        number2 = int(number2)
        print(f'Результат деления {number1} на {number2} =', division(number1, number2))
        break
    else:
        print('введите числа!')
