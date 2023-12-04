"""Library for interacting with the application."""
import requests


class AppLibrary:
    """Library for interacting with the application."""
    def __init__(self):
        self._base_url = "http://localhost:5000"

        self.reset_application()

    def reset_application(self):
        """Resets the application to a known state."""
        requests.post(f"{self._base_url}/tests/reset") # pylint: disable=missing-timeout

    def create_user(self, username, password):
        """Creates a new user with the given username and password."""
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password
        }

        requests.post(f"{self._base_url}/register", data=data) # pylint: disable=missing-timeout
