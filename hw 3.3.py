def my_func(number1, number2, number3):
    my_list = [number1, number2, number3]
    var = max(my_list)
    my_list.remove(var)
    var2 = max(my_list)
    return var + var2


while True:
    a = input('Введите число 1 ')
    b = input('Введите число 2 ')
    c = input('Введите число 3 ')

    if a.isdigit() and b.isdigit() and c.isdigit():
        a = int(a)
        b = int(b)
        c = int(c)

        print(f'сумма наибольших двух чисел равна {my_func(a, b, c)}')
        break
    else:
        print('введите корректрые числа')
