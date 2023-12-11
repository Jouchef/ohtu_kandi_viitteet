"""python script to initialize the database called ohtu
currently only tested on mac OS 
 Heidi Putkuri / 2023 """

import psycopg2

DB_NAME = 'postgres'
username = input("Username of your database in postgres: ")
DB_USER = username
DB_HOST = 'localhost'
DB_PORT = '5432'
NEW_DB_NAME = 'ohtu'


def create_database():
    """Creates a new database"""
    conn = None
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            host=DB_HOST,
            port=DB_PORT
        )
        print("Opened database successfully")
    except psycopg2.Error as e:
        print("Error while connecting to PostgreSQL", e)

    if conn is not None:
        conn.autocommit = True

        cursor = conn.cursor()

        print("Database does not exist")
        print("Creating a new database with name: " + NEW_DB_NAME + "........")
        sql = '''CREATE database ''' + NEW_DB_NAME + ''';'''
        cursor.execute(sql)
        print("Database created successfully........")
        print("Creating tables........")

        with psycopg2.connect(dbname=NEW_DB_NAME, user=DB_USER, host=DB_HOST, port=DB_PORT) as conn:
            with conn.cursor() as cursor:
                # Read and execute commands from the schema file
                with open("src/schema.sql", "r", encoding= 'UTF-8') as file:
                    sql_commands = file.read().split(';')
                    for command in sql_commands:
                        if command.strip():
                            cursor.execute(command)
                print("Tables created successfully.")

        conn.close()


create_database()
