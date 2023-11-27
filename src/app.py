"""Main module for the application."""
import os
from flask import Flask
app = Flask(__name__)

# Configuration
app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

import routes