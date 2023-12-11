"""User repository module handles all database operations related to users.""" # pylint: disable=missing-class-docstring
from db import db # pylint: disable=no-name-in-module import-error
from models.user import User_model # pylint: disable=no-name-in-module import-error

class UserRepository:
    """User repository class which handles all database operations 
    related to users."""
    def find_all(self):
        """Returns all users from the database."""
        return User_model.query.all()

    def find_by_username(self, username):
        """Returns a user with the given username."""
        return User_model.query.filter_by(username=username).first()

    def create(self, user):
        """Creates a new user to the database."""
        new_user = User_model(username=user.username,
                              password=user.password)
        db.session.add(new_user)
        db.session.commit()
        return new_user

    def delete(self, user_id):
        """Deletes a user from the database."""
        user = User_model.query.filter_by(id=user_id).first()
        db.session.delete(user)
        db.session.commit()

    def delete_all(self):
        """Deletes all users from the database."""
        User_model.query.delete()
        db.session.commit()

    def login(self, username, password):
        """Checks if the given username and password match."""
        user = User_model.query.filter_by(username=username).first()
        if user and user.password == password:
            return user
        return None

user_repository = UserRepository()
        