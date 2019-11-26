# Перехват ошибок
# При ошибке (неверное имя файла/отсутствует файл) печатаем печатаем сообщение, программа  после продолжает выполняться
filename = "My_LessonXXX_20_Exceptions_List.txt"
try:
    print("Insert Try")
    myfile = open(filename, mode='r', encoding='Latin_1')
except Exception:
    print("Inside EXCEPT")
    print("Error Found!")
else:
    print("Inside ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")
print("=====================EOF=======================")


# При ошибке (неверное имя файла/отсутствует файл) печатаем сообщение, далее завершаем программу, используя библиоеку SYS
import sys
filename = "My_Lesson_20_Exceptions_List.txt"
try:
    print("Insert Try")
    myfile = open(filename, mode='r', encoding='Latin_1')
except Exception:
    print("Inside EXCEPT")
    print("Error Found!")
    sys.exit()
else:
    print("Inside ELSE")
    print(myfile.read())
finally:
    print("Inside FINALLY")
print("=====================EOF=======================")


# При ошибке выводиться имя ошибки и в цикле будет запрошено корректное имя файла
import sys
filename = "My_LessonXXX_20_Exceptions_List.txt"
while True:
    try:
        print("Insert Try")
        myfile = open(filename, mode='r', encoding='Latin_1')
    except Exception:
        print("Inside EXCEPT")
        print("Error Found!")
        print(sys.exc_info())
        print(sys.exc_info()[1])
        filename = input("Enter Correct File Name: ")
    else:
        print("Inside ELSE")
        print(myfile.read())
        sys.exit()
    finally:
        print("Inside FINALLY")
print("=====================EOF=======================")



