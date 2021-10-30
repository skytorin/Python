#!/usr/bin/env python3

import os
import psycopg2
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

my_server = os.environ.get('POSTGRES_SERVER')      # .env
my_database = os.environ.get('POSTGRES_DB')        # .env
my_port = os.environ.get('POSTGRES_PORT')          # .env
my_user = os.environ.get('POSTGRES_USER')          # .env
my_password = os.environ.get('POSTGRES_PASS')      # .env

con = psycopg2.connect(host = my_server,
                       database = my_database,
                       user = my_user,
                       password = my_password,
                       port = my_port)

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

