from .base import YoucanBase

class Product:
    def __init__(self, base_url):
        self.api = YoucanBase(base_url)

    def get_all_products(self, page=1, limit=None, sort_field=None, sort_order=None, filters=None):
        endpoint = "api/products"
        # TODO : Add filters
        params = {
            'page': page,
            'limit': limit,
            'sort_field': sort_field,
            'sort_order': sort_order
        }
        response = self.api.make_request('GET', endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
            
    def get_reviews(self, product_id, include=None, sort_field=None, sort_order=None):
        endpoint = f"api/products/{product_id}/reviews"
        params = {
            'include': include,
            'sort_field': sort_field,
            'sort_order': sort_order
        }
        response = self.api.make_request('GET', endpoint, params=params)
        if response.status_code == 200:
            return response.json()
        else:
            return None
