# !/usr/bin/env python3
import os
import psycopg2
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

def psycopg2_select():
    my_server = os.environ.get('POSTGRES_SERVER')   # .env
    my_database = os.environ.get('POSTGRES_DB')     # .env
    my_port = os.environ.get('POSTGRES_PORT')       # .env
    my_user = os.environ.get('POSTGRES_USER')       # .env
    my_password = os.environ.get('POSTGRES_PASS')   # .env

    con = psycopg2.connect(host=my_server,
                           database=my_database,
                           user=my_user,
                           password=my_password,
                           port=my_port)

    cur = con.cursor()

    cur.execute("select * from student")

    rows = cur.fetchall()

#    for row in rows:
#        print(row[0], row[1], row[2], row[3], row[4], sep='\t')
    con.close()
    return rows
