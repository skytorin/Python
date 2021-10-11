import psycopg2

def pg_insert_module(i_admission, i_name, i_age, i_course, i_department):
        connect = psycopg2.connect(
                database="postgres",
                user="postgres",
                password="",
                host="localhost",
                port="5432"
        )                
        cursor = connect.cursor()
        sql_string = "INSERT INTO STUDENT (ADMISSION,NAME,AGE,COURSE,DEPARTMENT) " \
             "VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql_string, (i_admission, i_name, i_age, i_course, i_department))

        connect.commit()

        connect.close()

