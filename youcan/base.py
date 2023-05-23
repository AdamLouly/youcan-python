# youcan/base.py
import requests

class YoucanBase:
    def __init__(self, base_url):
        self.base_url = base_url
        # Initialize any necessary configurations or setup

    def make_request(self, method, endpoint, params=None, headers=None, data=None):
        url = f"{self.base_url}/{endpoint}"
        headers = headers or {}

        try:
            response = requests.request(method, url, params=params, headers=headers, json=data)
            response.raise_for_status()
            return response
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None

    # Add more common functionality and methods as needed

