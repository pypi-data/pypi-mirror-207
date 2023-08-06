import requests
from constants import PIXELA_ENDPOINT, X_USER_TOKEN


class Profile:
    def __init__(self):
        pass

    @staticmethod
    def view_user_profile(username: str = None):
        if username:
            requests.get(f'https://pixe.la/@{username}')

    def update_user_profile(self):
        pass
