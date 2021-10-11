# Проверка введеного значения
x = 25
if x == 25:
    print("YES you RIGNT")
else:
    print("NO you are WRONG")

# Проверка введеного возраста с указанием на принадлежность возрасной группе
age = 19
if (age <= 4):
    print("You are BABY")
elif (age > 4) and (age < 12):
    print("You are KID")
elif (age >=12) and (age < 19):
    print("You are TEENAGER")
else:
    print("You are old")

# Проверка есть ли указанная машина в масссиве
all_cars = ['chrusler','dacia','bmv','KIA','vw','seat','skoda','lada','audi','ford','chevrolett']
german_cars =  ['bmv','vw','audi']
if "lada" in all_cars:
    print("Yes LADA is in the list")
else:
    print("LADA Not in the list")

# Поиск в массиве только германских авто
all_cars = ['chrusler', 'dacia', 'bmv', 'KIA', 'vw', 'seat', 'skoda','lada', 'audi', 'ford', 'chevrolett']
german_cars =  ['bmv', 'vw', 'audi']
for xxxx in all_cars:
    if xxxx in german_cars:
        print(xxxx + " In German Car")
    else:
        print(xxxx + " Is NOT German Car")

