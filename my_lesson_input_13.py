# Ожидание ввода имени от пользователя
name = input("Please Enter your name: ")
print("Privet " + name + " !!!")

# Суммирование введеных значений
num1 = input("Enter X: ")
num2 = input("Enter Y: ")
summa = int(num1) + int(num2)
print(summa)

# Проверка введеного пароля (1 вариант)
messages = ""
while messages != 'secret':
    messages = input("Enter Password: ")
    if messages == 'secret':
        print("!!! ACCEPT SUCCESSFULY !!!")
    else:
        print(messages + " - Password Not Correct")

# Проверка введеного пароля (2 вариант)
messages = ""
while True:
    messages = input("Enter Password: ")
    if messages == 'secret':
        break
    print(messages + " - Password Not Correct")
print("Password was: " + messages)

# Запись в массив всех введенных данных поьзователя с выходом при вводе ключевого слова STOP
mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish: ")
    mylist.append(msg)
print(mylist)

















