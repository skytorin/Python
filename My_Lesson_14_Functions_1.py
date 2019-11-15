# Пример двух функций
def napeshatat_privetstvie(name):
    """napeshatat_privetstvie"""
    print("Congratulation " + name + " wish you all the best!")


def summa(x, y):
    """summa"""
    print(x + y)
    return x + y

print("--------------------------------------")
napeshatat_privetstvie("Denis")
napeshatat_privetstvie("Vasya")
x = summa(33, 22)
print(x)


# Функция вычесления факториала
def factorial(x):
    """Calculate Factorial of number X"""
    otvet = 1
    for i in range(1, x + 1):
        otvet = otvet * i
    return otvet

for i in range(1, 10 + 1):
    print(str(i) + "!\t= " + str(factorial(i)))

















