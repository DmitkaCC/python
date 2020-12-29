# 2. Для списка реализовать обмен значений соседних элементов, т.е.
# Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
# При нечетном количестве элементов последний сохранить на своем месте.
# Для заполнения списка элементов необходимо использовать функцию input()

my_list = list(input('введите строку для преобразования в список: '))
print('до: ', my_list)
counter = 1
temp_cell = ''
while counter < len(my_list):
    temp_cell = my_list[counter - 1]
    my_list[counter - 1] = my_list[counter]
    my_list[counter] = temp_cell
    counter += 2
print('после: ', my_list)
