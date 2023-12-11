"""Main module for the application.""" # pylint: disable=missing-function-docstring
import os
from flask import Flask
from db import db # pylint: disable=no-name-in-module import-error
from routes.user_routes import users # pylint: disable=no-name-in-module import-error
from routes.reference_routes import references # pylint: disable=no-name-in-module import-error

def create_app():
    """Creates the Flask app."""
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.register_blueprint(users)
    app.register_blueprint(references)

    db.init_app(app)

    return app
