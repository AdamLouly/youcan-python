from .base import YoucanBase

class Page:
    def __init__(self, base_url):
        self.api = YoucanBase(base_url)

    def get_all_pages(self):
        endpoint = "api/pages"
        response = self.api.make_request('GET', endpoint)
        if response.status_code == 200:
            return response.json()
        else:
            return None

    # Add more methods specific to pages
