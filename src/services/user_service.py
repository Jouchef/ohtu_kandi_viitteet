"""Service for user related operations."""
from repositories.user_repository import (user_repository as default_user_repository) # pylint: disable=import-error no-name-in-module line-too-long
from werkzeug.security import generate_password_hash, check_password_hash # pylint: disable=import-error no-name-in-module
from models.user import User_model as User # pylint: disable=import-error no-name-in-module ungrouped-imports
from flask import session # pylint: disable=import-error no-name-in-module

class UserInputError(Exception):
    """Raised when user input is invalid."""
    pass # pylint: disable=unnecessary-pass


class AuthenticationError(Exception):
    """Raised when authentication fails."""
    pass # pylint: disable=unnecessary-pass


class UserService:
    """Service for user related operations."""
    def __init__(self, user_repository=default_user_repository):
        self._user_repository = user_repository

    def get_user_id(self):
        """Get user id from the session."""
        print("Session: ", session.get("user_id"))
        return session.get("user_id")

    def check_credentials(self, username, password):
        """Check if username and password match."""
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or not check_password_hash(user.password, password):
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password, password_confirmation):
        """Create a new user."""

        self.validate(username, password, password_confirmation)
        hashed_password = generate_password_hash(password)
        user = self._user_repository.create(User(username = username,
                                                 password = hashed_password))

        return user

    def validate(self, username, password, password_confirmation):
        """Validate user input from registration form."""
        if not username or not password:
            raise UserInputError("Username and password are required")
        if len(username) < 3:
            raise UserInputError("Username must be at least 3 characters long")
        if len(password) < 8:
            raise UserInputError("Password must be at least 8 characters long")
        if password.isalpha():
            raise UserInputError("Password must contain numbers")
        characters = "!@#$%^&*()-+?_=,<>/"
        if not any(char in characters for char in password):
            raise UserInputError("Password must contain special characters")
        if password != password_confirmation:
            raise UserInputError("Passwords do not match")

user_service = UserService()
