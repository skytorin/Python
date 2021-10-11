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

cur.execute('update STUDENT set ADMISSION = 10000000 where age = 18')
cur.execute('update STUDENT set ADMISSION = 10000001 where age = 19')
cur.execute('update STUDENT set ADMISSION = 10000010 where age = 23')
cur.execute('update STUDENT set ADMISSION = 10000011 where age = 25')
cur.execute('update STUDENT set ADMISSION = 10000100 where age = 35')


con.commit()

print("Update inserted successfully")  

con.close()

