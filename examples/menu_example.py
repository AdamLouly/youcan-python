from youcan.menu import Menu

# Specify the base URL for the API
base_url = 'https://primecart.shop'

# Create an instance of the Menu class with the base URL
menu = Menu(base_url)

# Call the get_all_menus method
menus_data = menu.get_all_menus()

if menus_data:
    menus = menus_data
    total_menus = len(menus)

    print(f'Total Menus: {total_menus}')
    for menu in menus:
        print(f"Menu ID: {menu['id']}")
        print(f"Menu Name: {menu['name']}")
        print(f"Menu Slug: {menu['slug']}")
        print("Links:")
        for link in menu['links']:
            print(f" - Link ID: {link['id']}")
            print(f"   Link Name: {link['name']}")
            print(f"   Link URL: {link['link']}")
            print(f"   Link Order: {link['order']}")
            # Access other link attributes as needed
        print()  # Print a blank line between menus
else:
    print('Failed to retrieve menus.')
