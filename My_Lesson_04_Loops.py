# Пример цикла For
for x in range(10,10+2,2):
    print(x)
    print("----")
    print("Number x = " + str (x))


# Пример цикла For (еще вариант)
for x in range(10, 0, -2):
    print(x)
    print("----")
    print("Number x = " + str (x))
    if x == 6:
        break

print("--------------------EOF---------------------------")

# Бесконечный цикл
x=1
while True:
    print(x)
    x = x + 1

#################
x=1
while True:
    print(x)
    x = x + 1
    if x == 100000
        break