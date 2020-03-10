my_list = input('Введите список чего-нибудь: ').split()  # split возвращает список, разрезав строку на части
index = 0

while index + 1 < len(my_list):  # так как цикл проходится по двум элементам за раз, и берется +1 элемент.
    my_list[index], my_list[index + 1] = my_list[index + 1], my_list[index]  # по классике меняем местами переменные
    index += 2  # к index добавляем + 2, чтобы перейти к следующей паре элементов
print(my_list)
