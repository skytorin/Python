import os
import pypyodbc


def mssql_select():
    mysqlserver = "ioserver-sql17.neolant.loc"
    mydatabase = "NS_RELEASE_1_29_0"
    myuid = os.environ['UID']     # .env
    mypwd = os.environ['PWD']     # .env


    connection = pypyodbc.connect('Driver={SQL Server};'
                              'Server=' + mysqlserver + ';'
                              'Database=' + mydatabase + ';'
                              'uid=' + myuid + ';'
                              'pwd=' + mypwd)


    cursor = connection.cursor()

    mySQLQuery = (""" SELECT userName, uuid, fullName, phone, email, lastActivity 
                  FROM dbo.ns_sec_Users
              """)

    cursor.execute(mySQLQuery)
    results = cursor.fetchall()

    # print(results)    # вывод в формате list

    for row in results:
        username = row[0]
        fullname = row[2]
        phone = row[3]
        email = row[4]
        lastActivity = row[5]

        print(str(username) + ";" + str(uuid) + ";" + str(fullname) + ";" + str(phone) + ";" +str(email) + ";" + str(lastActivity))

    connection.close()

