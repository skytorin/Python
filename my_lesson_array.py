# Создаем и заполняем массив данными
cities = ["New York", "Mockow", "new dehli", "Simferopol","Toronto"]
print(cities[-3])
print(len(cities))
print(cities[2].title())
print(cities[-3].upper())

# Изменение данных в определенной позиции массива
cities[2] = "Tula"
print(cities)

# Добавление данных в конец массива
cities.append("Курск")
print(cities)

# Вставка данных в определённое место в массиве
cities.insert(2, "Feodosiya")
print(cities)

# Удаление данных из массива по его индексу
del cities[-1]
print(cities)

# Удаление данных из массива по его имени
cities.remove("Tula")
print(cities)

# Еще вариант удаления
delete_city = cities.pop()
print("delete_city is: " + delete_city)
print(cities)

# Сортировка данных в массиве A->Z
cities.sort()
print(cities)
# Сортировка данных в массиве Z->A
cities.sort(reverse=True)
print(cities)
или
cities.reverse()
print(cities)








