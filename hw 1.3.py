# 3

# переменная была введена для того, чтобы не прописывать вручную int перед переменными,
# где требуется перевод в числовой формат
user_number_str = input('Введите число: ')
user_number = int(user_number_str)

if user_number == 0:
    print(f'сумма чисел {user_number} + {user_number:>02} + {user_number:>03} =', user_number)

# этот странный print у меня для тренировки выравнивания
elif 0 < user_number < 10:
    second_num = user_number * 11
    third_num = user_number * 111
    answer = user_number + second_num + third_num
    print(f'Сумма чисел {user_number} + {second_num} + {third_num} =', answer)
else:
    second_num = int(user_number_str * 2)
    third_num = int(user_number_str * 3)
    answer = user_number + second_num + third_num
    print(f'Сумма чисел {user_number} + {second_num} + {third_num} =', answer)

# можно было бы присвоить переменную для повторяющихся строк print.
