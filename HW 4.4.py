from random import randint


def gen_list(int_list):
    for el in int_list:
        if int_list.count(el) == 1:
            yield el


random_list = []
for _ in range(20):
    random_list.append(randint(1, 10))

print(random_list)
print([x for x in gen_list(random_list)])
