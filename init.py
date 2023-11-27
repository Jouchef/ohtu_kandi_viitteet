# python script to initialize the database called ohtu
# tätä pitäis testaaaaa
# usage: python db_init.py

import psycopg2

# PostgreSQL connection information
DB_NAME = 'ohtu'
# ask for username 
username = input("Username: ")
DB_USER = username
DB_HOST = 'localhost'  # Change if your PostgreSQL server is hosted elsewhere
DB_PORT = '5432'  # Change if your PostgreSQL is using a different port

# Function to read schema.sql file
def read_schema_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
# Function to initialize database and add tables
def initialize_database():
    try:
        # Connect to the PostgreSQL server
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )

        # Create a cursor object using the connection
        cur = conn.cursor()

        # Read schema file content
        schema_content = read_schema_file('src/schema.sql')

        # Execute the SQL commands from the schema file
        cur.execute(schema_content)
        conn.commit()

        print("Tables created successfully!")

    except psycopg2.Error as e:
        print("Error:", e)

    finally:
        # Close communication with the database
        if conn is not None:
            cur.close()
            conn.close()

# Call the function to initialize the database
initialize_database()