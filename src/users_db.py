from db import db
from flask import session, request
from sqlalchemy.sql import text
import secrets
from werkzeug.security import check_password_hash, generate_password_hash


def register(username, password):
    username = request.form["username"]
    password = request.form["password"]
    hash_value = generate_password_hash(password)
    sql = text("SELECT username FROM Users_Table")
    result = db.session.execute(sql)
    usernames = result.fetchall()
    usernames_list = [name[0].strip("'") for name in usernames]
    for i in usernames_list:
        if i == username:
            return False
    try:
        sql = text(
            "INSERT INTO users (username,password) VALUES (:username,:password)")
        db.session.execute(sql, {"username": username, "password": hash_value})
        db.session.commit()
    except:
        return False
    return login(username, password)


def login(username, password):
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
