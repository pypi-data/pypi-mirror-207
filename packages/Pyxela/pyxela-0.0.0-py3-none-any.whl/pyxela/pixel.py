import json
import requests
from datetime import date
from model.colors import Colors
from constants import PIXELA_ENDPOINT, X_USER_TOKEN
from model.user_config import UserConfig
from collections import namedtuple

GRAPH_ID = 'test-graph'
PIXEL_DATE = str(date.today())
PIXELA_API_ENDPOINT = "https://pixe.la/v1/users/a-know/graphs/test-graph"


class Pixel:
    # def post_a_pixel(self, token: str, date: str, quantity: str, optional_data: dict):
    def __init__(self, user: UserConfig):
        self.user = user.dict()

    def post_a_pixel(self):

        headers = {
            "X-USER-TOKEN": self.user.token,
            "Content-Type": "application/json",
        }

        data = {
            "date": date,
            "quantity": quantity,
            "optionalData": optional_data,
        }

        response = requests.post(
            f"{PIXELA_API_ENDPOINT}/{GRAPH_ID}",
            headers=headers,
            json=data,
        )

        response.raise_for_status()

    def get_a_pixel(self):
        pass

    def update_a_pixel(self, token: str, username: str):
        PIXELA_USERNAME = 'shimon-d'
        GRAPH_ID = 'salt'
        DATE = '20230502'
        USER_TOKEN = '04adaa59-4fea-4c9f-afb2-fab7c6d2dcab'

        url = f'https://pixe.la/v1/users/{PIXELA_USERNAME}/graphs/{GRAPH_ID}/{DATE}'

        headers = {
            'X-USER-TOKEN': token,
            'Content-Type': 'application/json'
        }

        data = {
            'quantity': '7',
            'optionalData': json.dumps({'key': 'value'})
        }

        response = requests.put(url, headers=headers, json=data)

        if response.status_code == 200:
            print('Pixel updated successfully')
        else:
            print(f'Error updating pixel: {response.text}')

    def delete_a_pixel(self):
        pass


data = {
    'token': '04adaa59-4fea-4c9f-afb2-fab7c6d2dcab',
    'date': '',
    'quantity': '',
    'optional_data': '',

}

user = UserConfig(**data)

p = Pixel(user)
p.update_a_pixel()
