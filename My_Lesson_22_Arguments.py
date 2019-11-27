# Передача параметров/аргументов в скрипт
# Проверку результатов даного урока проводить в CMD:
# python My_Lesson_22_Arguments.py
# python My_Lesson_22_Arguments.py /?
# python My_Lesson_22_Arguments.py arg1 arg2
# python My_Lesson_22_Arguments.py arg1 arg2 arg3
import sys
x = len(sys.argv)
if (x == 2):
    if sys.argv[1] == "/?":
        print("Help Requested")
        print("Usage of this program is: python.exe ../path/myfile.py arg1 arg2 arg3")
    else:
        print("Arguments entered: " + str(sys.argv[1:]))
        print("Arguments N1 entered: " + str(sys.argv[0]))
        print("Arguments N2 entered: " + str(sys.argv[1]))
elif (x == 3):
    print("Arguments entered: " + str(sys.argv[1:]))
    print("Arguments N1 entered: " + str(sys.argv[0]))
    print("Arguments N2 entered: " + str(sys.argv[1]))
    print("Arguments N3 entered: " + str(sys.argv[2]))
elif (x == 4):
    print("Arguments entered: " + str(sys.argv[1:]))
    print("Arguments N1 entered: " + str(sys.argv[0]))
    print("Arguments N2 entered: " + str(sys.argv[1]))
    print("Arguments N3 entered: " + str(sys.argv[2]))
    print("Arguments N4 entered: " + str(sys.argv[3]))
else:
    print("Arguments NOT PROVIDED")

