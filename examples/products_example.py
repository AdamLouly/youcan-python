from youcan import Product

# Specify the base URL for the API
base_url = 'https://primecart.shop'

# Create an instance of the Product class with the base URL
product = Product(base_url)

# Call the get_all_products method
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
else:
    print('Failed to retrieve products.')

