from functools import reduce


def reduce_function(a, b):
    return a + b


new_list = [x for x in range(99, 1001) if x % 2 == 0]

print(reduce(reduce_function, new_list))
