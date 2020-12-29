# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами.
# Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
# Если слово длинное, выводить только первые 10 букв в слове.

user_string = input('Введите строку из нескольких слов, разделенных пробелами: ')
splitted_list = user_string.split(' ')
str_counter = 1
for counter in splitted_list:
    counter = counter[:10]
    print('Строка - ', str_counter, ' ', counter)
    str_counter += 1

