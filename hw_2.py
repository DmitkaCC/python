# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды
# и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
user_time = int(input('Введите время в секундах: '))
hours = user_time // 60
hours = hours // 60
minutes = (user_time // 60) - (hours * 60)
seconds = user_time % 60
print(f'{hours:02}:{minutes:02}:{seconds:02}')