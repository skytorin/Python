# Выполнение DOS / BASH команд из скрипта
#
import os
import sys

os.system("dir")
os.system("ipconfig")
os.system("dir > My_Lesson_07_CMD.txt")

# Указание необходимого кода выхода отличного от 0
# Последний код завершения приложения можно увидеть в CMD:
# python My_Lesson_07_CMD.py > %errorlevel%
# echo %errorlevel%
#
sys.exit(555)

