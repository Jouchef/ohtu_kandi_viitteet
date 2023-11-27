# python script to initialize the database called ohtu
# tätä pitäis testaaaaa
# usage: python db_init.py

import psycopg2

# PostgreSQL connection information
DB_NAME = 'postgres'
# ask for username
username = input("Username: ")
DB_USER = username
DB_HOST = 'localhost'
DB_PORT = '5432' 
NEW_DB_NAME = input("Database name: ")

# Function to read schema.sql file
def read_schema_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
# Function to create a new database and tables
def create_database():
    conn = None
    try:
        # Connect to the default database 'postgres'
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            host=DB_HOST,
            port=DB_PORT
        )
        print ("Opened database successfully")
    except:
        print("Error while creating connection PostgreSQL database")
    
    if conn is not None:
        conn.autocommit = True

        cursor = conn.cursor()

        print("Database does not exist")
        print("Creating a new database with name: " + NEW_DB_NAME + "........")
        sql = '''CREATE database ''' + NEW_DB_NAME + ''';'''
            #print(sql)
        cursor.execute(sql)
        print("Database created successfully........")

        #Closing the connection
        conn.close()


    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        # Close communication with the database
        if conn is not None:
            cur.close()
            conn.close()

# Call the function to initialize the database
initialize_database()
