import requests


class HttpError(Exception):
    def __init__(self, msg):
        self.msg = msg

    def __str__(self):
        return f'{self.msg}'


def handle_http_exceptions(fn):
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except requests.exceptions.HTTPError as e:
            print(f"HTTP Error: {e}")
            raise HttpError
    return wrapper
