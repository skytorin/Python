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



