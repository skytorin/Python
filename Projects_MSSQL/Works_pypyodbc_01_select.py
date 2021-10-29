# Работа с базами данных SQL Server (библиотека - pypyodbc )

import os
import pypyodbc
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


myServer = os.environ.get('SERVER_DB')            # .env
myDatabase = os.environ.get('DATABASE_DB')        # .env
myUsername = os.environ.get('USER_DB')            # .env
myPassword = os.environ.get('PASS_DB')            # .env

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + myServer + ';'
                              'Database=' + myDatabase + ';'
                              'Uid=' + myUsername + ';'
                              'Pwd=' + myPassword)

cursor = connection.cursor()

mySQLQuery = 'SELECT userName, uuid, fullName, phone, email, lastActivity FROM dbo.ns_sec_Users'

cursor.execute(mySQLQuery)
results = cursor.fetchall()

# print(results)    # вывод в формате list

for row in results:
    username = row[0]
    uuid = row[1]
    fullname = row[2]
    phone = row[3]
    email = row[4]
    lastActivity = row[5]

    print(str(username) + ";" + str(uuid) + ";" + str(fullname) + ";" + str(phone) + ";" +str(email) + ";" + str(lastActivity))

connection.close()
