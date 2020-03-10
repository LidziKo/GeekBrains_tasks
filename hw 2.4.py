user_words = input('Введите строку из нескольких слов, разделённых пробелами: ').split()

# с испотльзованием for in range с указанием длины строки
for i in range(len(user_words)):
    print(i + 1, user_words[i][:10])  # тут каждую строку режем в диапазоне от начала по 10-ый символ включительно

# с использованием enumerate, который в пару из двух переменных (i, user_word)
# возвращает индекс в i, а элемент, соответвущий индексу, возвращает в user_word.
for i, user_word in enumerate(user_words):
    print(f'{i+1}. {user_word[:10]}')
