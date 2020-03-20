from random import randint


def number_list(rand_ints):
    standard = float('-inf')
    for number in rand_ints:
        if number > standard:
            yield number
            standard = number


random_int_list = []
for _ in range(20):
    random_int_list.append(randint(-1000, 1000))

print(random_int_list)
print([x for x in number_list(random_int_list)])
