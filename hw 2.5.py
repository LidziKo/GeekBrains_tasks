rating_list = [9, 7, 7, 4, 2, 2, 1]

while True:
    user_number = input('Введите новый элемент рейтинга\n'
                        '(для выхода из программы оставьте поле пустым и нажмите Enter): ')
    if user_number.isdigit():
        user_number = int(user_number)
        rating_list.append(user_number)  # добавляет
        rating_list.sort()  # сортирует по возрастанию
        rating_list.reverse()  # переворачивает
        print(rating_list)
    elif user_number == '':  # сравнение с пустым вводом
        break
    else:
        continue
