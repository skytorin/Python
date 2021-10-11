#!/usr/bin/env python3

import psycopg2

con = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "",
        host = "localhost",
        port = "5432"
        )                

print("Database opened successfully")

cur = con.cursor()

cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (10000000, 'Kale', 35, 'Computer Science', 'IT')")
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (10000001, 'Jain', 19, 'Management', 'Econom')")
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (10000010, 'Sara', 23, 'Computer Science', 'FIST')")
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (10000011, 'Alex', 25, 'Management', 'Econom')")
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (10000100, 'Nick', 50, 'English', 'TRET')")
cur.execute("INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) VALUES (10000101, 'Jone', 60, 'Driving', 'OBSY')")

con.commit()

print("Record inserted successfully")  

con.close()

