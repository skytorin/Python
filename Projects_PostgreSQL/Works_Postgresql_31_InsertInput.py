#!/usr/bin/env python3

import psycopg2

connect = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
        )                

i_admission = input("Введи восьмизнаяный код: ")
i_name = input("Введи свое имя: ")
i_age = input("Введи свой возраст: ")
i_course = input("Введи название курса: ")
i_department = input("Введи название дапартамента: ")

cursor = connect.cursor()
sql_string = "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) " \
             "VALUES (%s,%s,%s,%s,%s)"
cursor.execute(sql_string, (i_admission, i_name, i_age, i_course, i_department))

connect.commit()

connect.close()

