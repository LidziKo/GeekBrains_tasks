# бесконечный итератор, генерирующий целые числа, начиная с указанного:
#
from itertools import count, cycle
import time

number = input('Введите число: ')

if number.isdigit():
    number = float(number)
else:
    print('Необходимо ввести число!')

for i in count(number):
    print(i)
    time.sleep(1)

# бесконечный итератор, повторяющий элементы некоторого списка, определенного заранее

list_elements = input('Введите что-нибудь:')
counter = 0
for i in cycle(list_elements):
    print(i)
    counter += 1
    time.sleep(1)
