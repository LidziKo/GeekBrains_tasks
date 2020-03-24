my_file = open('file54.txt', 'r', encoding='UTF-8')
my_file2 = open('file544.txt', 'w', encoding='UTF-8')

russian_numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре',
}

for line in my_file:
    line = line.split()

    if len(line) != 3:
        continue

    replace = russian_numbers.get(line[0], 'n/a')
    my_file2.write(f'{replace} - {line[2]}\n')

my_file.close()
my_file2.close()
