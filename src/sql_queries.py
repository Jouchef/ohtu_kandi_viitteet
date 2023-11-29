"""This file contains all the SQL queries that are used in the application."""

from werkzeug.security import check_password_hash, generate_password_hash
import secrets
from flask import session, request
from db import db
from sqlalchemy import text
import psycopg2
conn = psycopg2.connect(database="ohtu", user="postgres",
                        host="localhost", port="5432")


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

    # insert the data into the table
    sql = text(
        "INSERT INTO References_Table (author, title, journal, year, volume, number, pages, month, doi, note, key) VALUES (:author, :title, :journal, :year, :volume, :number, :pages, :month, :doi, :note, :key)") #pylint: disable=line-too-long
    try:
        cur = conn.cursor()
        cur.execute(sql, author=author, title=title, journal=journal, year=year, volume=volume, number=number,
                    pages=pages, month=month, doi=doi, note=note, key=key) #pylint: disable=no-value-for-parameter
        conn.commit()
        cur.close()
        conn.close()

        return True
    except Exception as e:
        print(e, "error")
        return False


def all_references_from_db():
    """Get all references from the database."""
    sql = text(
        "SELECT * FROM References_Table WHERE visible = 1 ORDER BY Author ASC")

    try:
        cur = conn.cursor()
        result = cur.execute(sql)
        references = result.fetchall()  # this is a list of tuples
        cur.close()
        conn.close()

        return references
    except Exception as e:
        print(e, "error")
        return None


def search_by_name_from_db(search):
    """Search for references by author name."""
    sql = text(
        "SELECT * FROM References_Table WHERE visible = 1 AND LOWER(author) LIKE LOWER(:author) ORDER BY author ASC")

    try:
        cur = conn.cursor()
        result = cur.execute(sql, {"author": f"%{search}%"})
        reference = result.fetchall()  # this is a list of tuples
        cur.close()
        conn.close()

        return reference
    except Exception as e:
        print(e, "error")
        return None




def ids_list():
    sql = text("SELECT id FROM References_Table WHERE visible = TRUE")
    try:
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchall()
        cur.close()
        conn.close()

        ids_list = []
        for id in result:
            ids_list.append(id[0])

        return ids_list
    except Exception as e:
        print(e, "error")
        return None


def citates_to_list():
    citates_dict = {}
    print(ids_list())
    for index, citate_id in enumerate(ids_list()):
        cur = conn.cursor()
        sql = text(
            "SELECT author, title, year, type FROM References_Table WHERE id = :id")
        result = cur.execute(sql, {"id": citate_id}).fetchall()
        for author, title, year, citate_type in result:
            citates_dict[citate_id] = {
                'author': author,
                'title': title,
                'year': year,
                'type': citate_type
            }
        conn.commit()
        cur.close()
        conn.close()
    print(citates_dict)
    return citates_dict


def edit_queries(author, title, booktitle, journal, year, volume, pages, publisher, id):
    sql = text("UPDATE References_Table SET"
               " author = COALESCE(:author, author),"
               " title = COALESCE(:title, title),"
               " booktitle = COALESCE(:booktitle, booktitle),"
               " journal = COALESCE(:journal, journal),"
               " year = COALESCE(:year, year),"
               " volume = COALESCE(:volume, volume),"
               " pages = COALESCE(:pages, pages),"
               " publisher = COALESCE(:publisher, publisher)"
               " WHERE id = :id")

    try:
        cur = conn.cursor()
        cur.execute(sql, {"author": author, "title": title, "booktitle": booktitle,
                          "journal": journal, "year": year, "volume": volume,
                          "pages": pages, "publisher": publisher, "id": id})

        conn.commit()
        cur.close()
        conn.close()

        return
    except Exception as e:
        cur.rollback()
        print(e, "error")
        return None


def delete_reference(id):
    sql = text(
        "UPDATE References_Table SET visible = false WHERE id=id")
    try:
        cur = conn.cursor()
        cur.execute(sql, {"id": id})
        conn.commit()
        cur.close()
        conn.close()
        return True
    except Exception as e:
        print(e, "error")
        return False


def make_changes(author, title, book_title, journal, year, volume, pages, publisher):
    """Make changes to the database for a specific reference."""

    # sql = text("UPDATE References_Table SET"
    #           " title = COALESCE(:title, title),"
    #           " booktitle = COALESCE(:booktitle, booktitle),"
    #           " journal = COALESCE(:journal, journal),"
    #           " year = COALESCE(:year, year),"
    #           " volume = COALESCE(:volume, volume),"
    #           " pages = COALESCE(:pages, pages),"
    #           " publisher = COALESCE(:publisher, publisher)"
    #          " WHERE id = :id")


def register(username, password):  # UUSI
    hash_value = generate_password_hash(password)
    sql = text("SELECT username FROM Users_Table")
    result = db.session.execute(sql)
    usernames = result.fetchall()
    usernames_list = [name[0].strip("'") for name in usernames]
    for i in usernames_list:
        if i == username:
            return False
    print(username)
    print(password)
    email = "jotain"
    try:
        sql = text(
            "INSERT INTO Users_Table (username,email,password) VALUES (:username,:email, :password)")
        db.session.execute(
            sql, {"username": username, "email": email, "password": hash_value})
        db.session.commit()
    except:
        return False
    return (username, password)


def login(username, password):  # UUSI
    sql = text("SELECT id, password FROM Users_Table WHERE username=:username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)

            return True
        else:
            return False
