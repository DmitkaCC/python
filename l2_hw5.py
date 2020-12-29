# 5.Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел,
# который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.

my_list = [7, 5, 3, 3, 2]
user_number = input('введите число: ')
lenght = len(my_list)
counter = 0
while counter < lenght:
    if int(user_number) < int(my_list[counter]):
        counter += 1
        continue
    my_list.insert(counter, user_number)
    break
else:
    my_list.append(user_number)
print(my_list)
