from random import randint

my_file = open('file55.txt', 'w', encoding='UTF-8')

random_int_list = []
for _ in range(20):
    random_int_list.append(randint(0, 100))

random_int_str = ' '.join(str(i) for i in random_int_list)
my_file.write(random_int_str)
my_file.close()

my_file = open('file55.txt', 'r', encoding='UTF-8')

str_num = my_file.read().split(' ')
str_num = map(int, str_num)
print(f'Сумма чисел из файла равна {sum(str_num)}')

my_file.close()
