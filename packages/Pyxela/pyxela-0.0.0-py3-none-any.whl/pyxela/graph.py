import requests
from constants import X_USER_TOKEN
from constants import PIXELA_ENDPOINT
from model.graph_config import GraphConfig
from model.colors import Colors
from pydantic import json


class Graph:
    def __init__(self):
        pass

    def create_graph(self, token, username, graph_config: GraphConfig):
        response = requests.post(
            f"{PIXELA_ENDPOINT}/{username}/graphs",
            json=graph_config.json(),
            headers={
                X_USER_TOKEN: token,
                'Content-Type': 'application/json',
            }
        )

        response.raise_for_status()

        response.raise_for_status()

    def get_graph_definitions(self):
        pass

    def get_a_graph_definition(self):
        pass

    def get_a_graph_svg(self):
        pass

    def update_a_graph(self):
        pass

    def delete_a_graph(self):
        pass

    def view_graph_detail(self):
        pass

    def get_graph_pixels_list(self):
        pass

    def get_a_graph_stats(self):
        pass


# g = Graph()
#
# conf = {
#     'id': 'example',
#     'name': 'example',
#     'unit': 'example',
#     'type': 'int',
#     'color': Colors.light_orange
# }
#
#
# g.create_graph(
#     token='',
#     username='',
#     graph_config=GraphConfig(**conf)
# )
