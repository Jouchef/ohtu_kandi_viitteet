import requests


class AppLibrary:
    def __init__(self):
        self._base_url = "http://localhost:5001"

        self.reset_application()

    def reset_application(self):
        """Resets the application to a known state."""
        requests.post(f"{self._base_url}/tests/reset")        

    def create_user(self, username, password):
        data = {
            "username": username,
            "password": password,
            "password_confirmation": password
        }

        requests.post(f"{self._base_url}/register", data=data)
