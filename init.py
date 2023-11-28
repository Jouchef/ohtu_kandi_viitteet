from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import getpass
from src.schema import Base, User, Reference, UserReference, Tag

def initialize_database():
    # PostgreSQL connection information
    DB_NAME = 'ohtu'
    DB_USER = input("Username: ")
    DB_PASSWORD = getpass.getpass("Password: ")
    DB_HOST = 'localhost'
    DB_PORT = '5432'

    # SQLAlchemy database URL
    DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

    # Create engine
    engine = create_engine(DATABASE_URL)

    # Create all tables
    Base.metadata.create_all(engine)

    print("Tables created successfully!")

if __name__ == "__main__":
    initialize_database()
