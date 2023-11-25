from os import getenv
from extensions import db, app

db.init_app(app)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
