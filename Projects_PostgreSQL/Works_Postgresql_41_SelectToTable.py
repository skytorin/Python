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

print('-----------------------------------------------------------------------------------------------------')
print('| ADMISSION    | NAME  | AGE   | COURSE                                                | DEPARTMENT |')
print('-----------------------------------------------------------------------------------------------------')

for row in rows:
    print(row[0],row[1],row[2],row[3],row[4], sep = '\t')

print("\nOperation done successfully")  

con.close()

