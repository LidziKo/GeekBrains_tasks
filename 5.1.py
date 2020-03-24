my_file = open('file51.txt', 'w', encoding='UTF-8')

while True:
    file_recording = input('Давайте что-нибудь запишем в файл\n'
                           '(Для завершения записи введите пустую строку): ')
    if file_recording == '':
        print('Завершение программы')
        break
    else:
        my_file.write(file_recording + '\n')

my_file.close()
