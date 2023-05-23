# YouCan Storefront Python SDK

The YouCan Python SDK is a Python package that provides a convenient way to interact with the YouCan storefront API. 

It simplifies the process of integrating your Python applications with YouCan, allowing you to retrieve orders, products, pages, and menus easily.


## Installation

You can install the YouCan Python SDK using pip:

```shell
pip install youcan
```

# Usage
Initialize the YouCan Client

To get started, create an instance of the YouCan client by providing your API credentials:

```python
from youcan import Product

base_url = 'store_url_here'

# Create an instance of the Product class with the base URL
product = Product(base_url)
```

#### Get Products
Retrieve a list of products:

```python
products_data = product.get_all_products(page=1, limit=10, sort_field='name', sort_order='asc')

if products_data:
    products = products_data['data']
    print(products_data['meta'])
    try:
        total_pages = products_data['meta']['pagination']['total_pages']
    except:
        total_pages = 1
    print(f'Total Products: {len(products)}')
    for p in products:
        print(f"Product ID: {p['id']}")
        print(f"Product Name: {p['name']}")
        # Access other product attributes as needed

```

# Contributing
Contributions are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue on the GitHub repository.

# License
This project is licensed under the MIT License.
