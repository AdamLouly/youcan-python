from youcan import Product

# Specify the base URL for the API
base_url = 'https://primecart.shop'
product = Product(base_url)

# Call the get_reviews method
product_id = '0fbe4391-5afd-4f86-aedf-f14fb1c762a8'  # Replace with the actual product ID
reviews_data = product.get_reviews(product_id, include='product', sort_field='created_at', sort_order='desc')

if reviews_data:
    reviews = reviews_data['data']
    total_reviews = len(reviews)
    print(reviews)
    print(f'Total Reviews: {total_reviews}')
    for review in reviews:
        print(f"Reviewer: {review['first_name']} {review['last_name']}")
        print(f"Rating: {review['ratings']}")
        try:
            print(f"Review: {review['review_text']}")
        except:
            print("No text")
        # Access other review attributes as needed
else:
    print('Failed to retrieve reviews.')
