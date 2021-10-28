#!/usr/bin/env python3

import os
import pymssql


my_user = os.environ.get('USER_DB')         # .env
my_password = os.environ.get('PASS_DB')     # .env
server = "ioserver-sql17.neolant.loc"
user = 'n.sergeev'
password = 'gD1Ca768W4'
database = "NS_RELEASE_1_29_0"

connection = pymssql.connect(server, user, password, database)

cursor = connection.cursor()

mySQLQuery = ("SELECT userName, uuid, fullName, phone, email, lastActivity FROM dbo.ns_sec_Users")

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

print(my_user)
print(my_password)
