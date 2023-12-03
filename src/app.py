"""Main module for the application."""
import os
from flask import Flask
from src.db import db # pylint: disable=no-name-in-module import-error
from src.routes.user_routes import users # pylint: disable=no-name-in-module import-error
from src.routes.reference_routes import references # pylint: disable=no-name-in-module import-error
#from flask_wtf.csrf import CSRFProtect # pylint: disable=import-error

def create_app():
    """Creates the Flask app."""
    app = Flask(__name__)

    # Configuration
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    #import routes  # nopep8
    app.register_blueprint(users)
    app.register_blueprint(references)

    db.init_app(app)

    return app
