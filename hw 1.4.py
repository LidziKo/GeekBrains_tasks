# 4

number = input('Введите число: ')
maximum = 0
number = int(number)


while number != 0:
    digit = number % 10  # получаем при помощи % последнюю цифру из числа
    if digit > maximum:  # сравниваем полученную последнюю цифру из числа с переменной maximum, если >
        maximum = digit  # то устанавливаем новое значение в переменную maximum
    number = number - digit  # делаем самую правую цифру равной 0, чтобы поделилось без остатка
    number = number // 10  # делим без остатка, возвращаемся в начало цикла к следющей слева цифре

print(maximum)
