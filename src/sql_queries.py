"""This file contains all the SQL queries that are used in the application."""
from dotenv import load_dotenv
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from db import db
from routes import Reference

# Load environment variables from .env file
load_dotenv()

# Get the DATABASE_USER and DATABASE_PASSWORD from environment variables
DATABASE_USER = os.getenv('DATABASE_USER')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD')


print(f"Kokeilu {DATABASE_USER}")

try:

    # Load environment variables from .env file
    load_dotenv()

    # Get the DATABASE_URI from environment variables
    DATABASE_URI = os.getenv('DATABASE_URI')

    # Create the engine using the DATABASE_URI
    engine = create_engine(DATABASE_URI)
    Session = sessionmaker(bind=engine)
    session = Session()
except Exception as e:
    print(f"Connection failed: {e}")

def article_to_db(article: dict):
    """Add a new article to the database."""
    author = article["author"]
    title = article["title"]
    journal = article["journal"]
    year = article["year"]
    volume = article["volume"]
    number = article["number"]
    pages = article["pages"]
    month = article["month"]
    doi = article["doi"]
    note = article["note"]
    key = article["key"]

    try:
        reference = Reference(author=author, title=title, journal=journal, year=year, volume=volume, number=number,
                              pages=pages, month=month, doi=doi, note=note, key=key)
        session.add(reference)
        session.commit()
        return True
    except Exception as e:
        print(e, "error")
        session.rollback()
        return False

def all_references_from_db():
    """Get all references from the database."""
    try:
        references = session.query(Reference).filter(Reference.visible == 1).order_by(Reference.author.asc()).all()
        return references
    except Exception as e:
        print(e, "error")
        return None

def search_by_name_from_db(search):
    try:
        references = session.query(Reference).filter(Reference.visible == 1, Reference.author.ilike(f"%{search}%")).order_by(Reference.author.asc()).all()
        session.commit()
        return references
    except Exception as e:
        session.rollback()
        return None

def change_visible_to_false(citate_id):
    try:
        reference = session.query(Reference).filter(Reference.id == citate_id).first()
        reference.visible = 0
        session.commit()
    except Exception as e:
        session.rollback()
        raise e

def edit_queries():
    pass

def ids_list():
    ids_list = []
    try:
        ids = session.query(Reference.id).filter(Reference.visible == True).all()
        ids_list = [id[0] for id in ids]
    except Exception as e:
        session.rollback()
    return ids_list

def citates_to_list():
    citates_dict = {}
    ids = ids_list()
    for citate_id in ids:
        try:
            reference = session.query(Reference).filter(Reference.id == citate_id).first()
            citates_dict[citate_id] = {
                'author': reference.author,
                'title': reference.title,
                'year': reference.year,
                'type': reference.type
            }
        except Exception as e:
            session.rollback()
    return citates_dict

def edit_queries(author, title, booktitle, journal, year, volume, pages, publisher, id):
    try:
        reference = session.query(Reference).filter(Reference.id == id).first()
        reference.author = author if author else reference.author
        reference.title = title if title else reference.title
        reference.booktitle = booktitle if booktitle else reference.booktitle
        reference.journal = journal if journal else reference.journal
        reference.year = year if year else reference.year
        reference.volume = volume if volume else reference.volume
        reference.pages = pages if pages else reference.pages
        reference.publisher = publisher if publisher else reference.publisher
        session.commit()
    except Exception as e:
        session.rollback()
        return None

def make_changes(author, title, book_title, journal, year, volume, pages, publisher):
    pass
