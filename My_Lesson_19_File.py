# Работа с файлами
# Читаем файл с диска целиком в кодировке cp1251
# inputfile = "My_Lesson_19_File_user_names.txt"    
# файл находится на уровень выше самого скрипта
inputfile = "My_Lesson_19_File_user_names.txt"
myfile = open(inputfile, mode="r", encoding="cp1251")
print(myfile.read())


print ("==============================================================================================================")
# Вывод данных из файла построчно c добавлением инфы, c удалением разрыва между строками
inputfile = "My_Lesson_19_File_user_names.txt"
myfile = open(inputfile, mode="r", encoding="cp1251")
for line in myfile:
    print("Hello " + line.strip())


print ("==============================================================================================================")
# Вывод данных из файла построчно c добавлением инфы и посточной НУМЕРАЦИИ, c удалением разрыва между строками
inputfile = "My_Lesson_19_File_user_names.txt"
myfile = open(inputfile, mode="r", encoding="cp1251")
for num, line in enumerate(myfile):
    print("Line N: " + str(num) + " : " + line.strip())


print ("==============================================================================================================")
# Поиск строк содержащих текст vasya и запись найденных строк в новый файл, 
# c ПЕРЕЗАПИСЬЮ содержимого
inputfile = "My_Lesson_19_File_list_of_passwords.txt"
outputfile = "My_Lesson_19_File_my_passwords.txt"
password_tolookfor = "vasya"
myfile_input = open(inputfile, mode="r", encoding="latin_1")
myfile_out = open(outputfile, mode="w", encoding="latin_1")
for num, line in enumerate(myfile_input, 1):
    if password_tolookfor in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile_out.write("Found password : " + line)
myfile_input.close()
myfile_out.close()


print ("==============================================================================================================")
# Поиск строк содержащих текст vasya и запись найденных строк в новый файл, 
# c СОХРАНЕНИЕМ содержимого
inputfile = "My_Lesson_19_File_list_of_passwords.txt"
outputfile = "My_Lesson_19_File_my_passwords.txt"
password_tolookfor = "Petya"
myfile_input = open(inputfile, mode="r", encoding="latin_1")
myfile_out = open(outputfile, mode="a", encoding="latin_1")
for num, line in enumerate(myfile_input, 1):
    if password_tolookfor in line:
        print("Line N: " + str(num) + " : " + line.strip())
        myfile_out.write("Found password : " + line)
myfile_input.close()
myfile_out.close()

