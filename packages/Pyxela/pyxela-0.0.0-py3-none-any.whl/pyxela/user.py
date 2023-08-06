import requests
from constants import PIXELA_ENDPOINT, X_USER_TOKEN
from handler import handle_http_exceptions


class User:
    def __init__(self, token: str = None, username: str = None):
        self.headers = {
            X_USER_TOKEN: token
        }

        self.token = token
        self.username = username

    # User
    @handle_http_exceptions
    def create(self):
        if self.token and self.username:
            body = {
                'token': self.token,
                'username': self.username,
                'agreeTermsOfService': 'yes',
                'notMinor': 'yes'
            }

            response = requests.post(url=PIXELA_ENDPOINT, json=body, headers=self.headers)
            response.raise_for_status()

    @handle_http_exceptions
    def update(self, new_token: str):
        self.headers = {
            X_USER_TOKEN: self.token
        }

        user_params = {
            'newToken': new_token
        }

        response = requests.put(url=f'{PIXELA_ENDPOINT}{self.username}', json=user_params, headers=self.headers)
        response.raise_for_status()

    @handle_http_exceptions
    def delete(self):
        response = requests.delete(url=f'{PIXELA_ENDPOINT}{self.username}', headers=self.headers)
        response.raise_for_status()
