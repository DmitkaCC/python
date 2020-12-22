# 4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.
user_number = int(input('Введите целое положительное число: '))
local_max = 0
num = user_number

while num > 0:
    digit = num % 10
    if digit > local_max:
        local_max = digit
    num = num // 10

print(f'Наибольшая цифра у введенного числа {user_number}:', local_max)