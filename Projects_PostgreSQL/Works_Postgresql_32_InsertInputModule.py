# import Module_Postgresql_32_Insert
from Module_Postgresql_32_Insert import pg_insert_module

i_admission = input("Введи восьмизнаяный код: ")
i_name = input("Введи свое имя: ")
i_age = input("Введи свой возраст: ")
i_course = input("Введи название курса: ")
i_department = input("Введи название дапартамента: ")

# Module_Postgresql_32_Insert.pg_insert_module(i_admission, i_name, i_age, i_course, i_department)
pg_insert_module(i_admission, i_name, i_age, i_course, i_department)
