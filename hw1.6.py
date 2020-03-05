#6

a = input('Количество преодолённых километров в первый день: ')
b = input('Желаемое количество километров: ')
a = int(a)
b = int(b)
day = 1


while True:
    if a < b:
        # print(day, a)
        day += 1
        a += a*0.1
    else:
        print(f'На {day}-й день спортсмен достиг результата не менее {b} км')
        break
