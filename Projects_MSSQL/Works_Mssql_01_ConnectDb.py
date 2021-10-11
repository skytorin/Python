# Работа с базами данных (SQL Server)

import pypyodbc

mySQLServer = "ioserver-sql17"
myDatabase = "NS_RELEASE_1_28"

connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mySQLServer + ';'
                              'Database=' + myDatabase + ';')
                              #'uid=username;'
                              #'pwd=mypassword;'

cursor = connection.cursor()

mySQLQuery = (""" SELECT userName, uuid, fullName, phone, email, lastActivity 
                  FROM dbo.ns_sec_Users
              """)

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
