
# Запись в массив всех введенных данных поьзователя с выходом при вводе ключевого слова STOP
mylist = []
msg = ""
while msg != 'stop'.upper():
    msg = input("Enter new item, and STOP to finish: ")
    mylist.append(msg)
print(mylist)