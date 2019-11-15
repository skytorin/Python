# Присваеваем переменной дааные из массива
cars = ['bmw', 'vw', 'seat',  'scoda', 'kada']
print(cars)

# Вырезание куска массива от - до
mycars = cars[1:3+1]
print(mycars)
# Вырезание куска массива сначала и до
mycars = cars[:4]
print(mycars)
# Вырезание куска массива с конца и до
mycars = cars[-3:]
print(mycars)
# Копирование массива
mycars = cars[:]
print(cars)

# Работа с данными массива используя циклы
for x in cars:
    print(x.upper())
# Автоматическое заполнение массива данными
mynumber_list = list(range(0, 10))
print(mynumber_list)

# Арифметические операции с данными изи массива
for x in mynumber_list:
    x = x * 2
    print(x)

# Обратная сортировка данных в массиве
mynumber_list.sort(reverse=True)
print(mynumber_list)

#  Нахождение максимального, минимального значения или суммы всех чисел в массиве
print("Max number is: " + str(max(mynumber_list)))
print("Min number is: " + str(min(mynumber_list)))
print("Sum number is: " + str(sum(mynumber_list)))

