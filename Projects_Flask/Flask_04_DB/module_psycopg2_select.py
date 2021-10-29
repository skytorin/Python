import psycopg2


def psycopg2_select():
    con = psycopg2.connect(
        database="postgres",
        user="postgres",
        password="",
        host="localhost",
        port="5432"
    )

    cur = con.cursor()

    cur.execute("select * from student")

    rows = cur.fetchall()

    print('-----------------------------------------------------------------------------------------------------')
    print('| ADMISSION    | NAME  | AGE   | COURSE                                                | DEPARTMENT |')
    print('-----------------------------------------------------------------------------------------------------')

    for row in rows:
        print(row[0], row[1], row[2], row[3], row[4], sep='\t')

    con.close()

