#!/usr/bin/env python3

import psycopg2

con = psycopg2.connect(
        database = "postgres",
        user = "postgres",
        password = "",
        host = "localhost",
        port = "5432"
      )                

print("Database opened successfully\n")

cur = con.cursor()

cur.execute("select * from student")

rows = cur.fetchall()

for row in rows:
      print("ADMISSION =", row[0])
      print("NAME =", row[1])
      print("AGE =", row[2])
      print("COURSE =", row[3])
      print("DEPARTMENT =", row[4], "\n")

print("\nOperation done successfully")  

con.close()

