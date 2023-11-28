# """Main module for the application."""
# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# import routes
# app = Flask(__name__)

# # Configuration
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


from flask import Flask

app = Flask(__name__)

import routes
