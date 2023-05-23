from .base import YoucanBase

class Menu:
    def __init__(self, base_url):
        self.api = YoucanBase(base_url)

    def get_all_menus(self):
        endpoint = "api/menus"
        response = self.api.make_request('GET', endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None
