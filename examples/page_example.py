from youcan.page import Page

# Specify the base URL for the API
base_url = 'https://primecart.shop'

# Create an instance of the Page class with the base URL
page = Page(base_url)

# Call the get_all_pages method
pages_data = page.get_all_pages()

if pages_data:
    pages = pages_data['data']
    total_pages = len(pages)

    print(f'Total Pages: {total_pages}')
    for page in pages:
        print(f"Page ID: {page['id']}")
        print(f"Page Name: {page['name']}")
        print(f"Page Slug: {page['slug']}")
        print(f"Page Content: {page['content']}")
        # Access other page attributes as needed
else:
    print('Failed to retrieve pages.')
