my_file = open('file52.txt', 'r', encoding='UTF-8')

count_lines = 0  # кол-во строк
count_words_in_line = 0  # кол-во слов в строке

for line in my_file:
    count_lines += 1
    count_words_in_line = len(line.split(' '))
    print(f'В строке #{count_lines} {count_words_in_line} слов')

print(f'В этом стихотворении {count_lines} строк')

my_file.close()
