# способ 1
def my_func(x, y):
    if y < 0:
        x = 1 / x
    return x ** abs(y)


while True:
    number1 = input('Введите действительное положительное число: ')
    number2 = input('Введите целое отрицательное число: ')

    try:
        number1 = int(number1)
        number2 = int(number2)

        if number2 >= 0:
            print('Второе число должно быть отрицательным!')
            continue

        print(my_func(number1, number2))
        break
    except ValueError:
        print('Введите числа!')


# способ 2
def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    if y < 0:
        return 1 / result
    else:
        return result


while True:
    number1 = input('Введите действительное положительное число: ')
    number2 = input('Введите целое отрицательное число: ')

    try:
        number1 = int(number1)
        number2 = int(number2)

        if number2 >= 0:
            print('Второе число должно быть отрицательным!')
            continue

        print(my_func(number1, number2))
        break
    except ValueError:
        print('Введите числа!')
