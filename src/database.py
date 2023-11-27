from os import getenv
from extensions import db, app

<< << << < HEAD
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
db = SQLAlchemy(app)
== == == =
db.init_app(app)
app.config["SQLALCHEMY_DATABASE_URI"] = getenv("DATABASE_URL")
>>>>>> > 25ec1af36744ac1f33dd54adaad39ca40e35d6be
