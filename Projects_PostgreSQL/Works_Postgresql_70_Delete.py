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

cur.execute("DELETE from STUDENT where AGE >= 50;")  

con.commit()  

print("Total deleted rows:", cur.rowcount)



con.close()

