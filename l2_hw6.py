# 6. Реализовать структуру данных «Товары». Она должна представлять собой список кортежей.
# Каждый кортеж хранит информацию об отдельном товаре.
# В кортеже должно быть два элемента — номер товара и словарь с параметрами,
# то есть характеристиками товара: название, цена, количество, единица измерения.
# Структуру нужно сформировать программно, запросив все данные у пользователя.
article = []
description = {'название': '', 'цена': '', 'количество': '', 'единица измерения': ''}
analitics = {'название': [], 'цена': [], 'количество': [], 'единица измерения': []}
num = 0
while True:
    check_break = input('Выход - Q, \nЛюбая клавиша - продолжить: ')
    if check_break.upper() == 'Q' or check_break.upper() == 'Й':
        break
        num += 1
    for counter in description.keys():
        user_data = input(f'{counter}: ')
        if counter == 'цена' or counter == 'количество':
            try:
                description[counter] = int(user_data)
            except ValueError:
                print('введено не число!!!')
        else:
            description[counter] = user_data
        analitics[counter].append(description[counter])
    article.append((num, description.copy()))
    print('Текущая аналитика по товарам:\n')

    for key, value in analitics.items():
        print(key, value)

print(article)

