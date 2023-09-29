class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.search_history = []
        self.cart = []

class ShoppingSystem:
    def __init__(self):
        self.products = []
        self.users = []

    def add_product(self, product):
        self.products.append(product)

    def register_user(self, user):
        self.users.append(user)

    def search_products(self, user, keyword):
        user.search_history.append(keyword)
        matching_products = [product for product in self.products if keyword.lower() in product.name.lower()]
        return matching_products

    def recommend_products(self, user):
        recommended_products = []
        # Implement recommendation logic here (e.g., based on user's search history)
        return recommended_products

    def display_cart(self, user):
        total_price = sum(product.price for product in user.cart)
        print(f"Items in cart for {user.name}:")
        for product in user.cart:
            print(f"{product.name} - ${product.price}")
        print(f"Total: ${total_price}")

# Create a shopping system instance
shopping_system = ShoppingSystem()

# Add products
shopping_system.add_product(Product("P001", "Laptop", "Electronics", 1000))
shopping_system.add_product(Product("P002", "Smartphone", "Electronics", 800))
# ... add more products

# Register users
user1 = User("U001", "Alice")
user2 = User("U002", "Bob")
shopping_system.register_user(user1)
shopping_system.register_user(user2)

# Simulate user interactions
keyword = input("Enter a product keyword to search: ")
matching_products = shopping_system.search_products(user1, keyword)

if matching_products:
    print("Matching products:")
    for product in matching_products:
        print(f"{product.name} - ${product.price}")

    recommendation = shopping_system.recommend_products(user1)
    if recommendation:
        print("Recommended products:")
        for product in recommendation:
            print(f"{product.name} - ${product.price}")
else:
    print("No products found matching the keyword.")

# Add a product to the user's cart
chosen_product_id = input("Enter the product ID to add to cart: ")
chosen_product = next((product for product in matching_products if product.product_id == chosen_product_id), None)
if chosen_product:
    user1.cart.append(chosen_product)
    shopping_system.display_cart(user1)
else:
  print("Invalid product ID.")
  class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.search_history = []
        self.cart = []

class ShoppingSystem:
    def __init__(self):
        self.products = []
        self.users = []

    def add_product(self, product):
        self.products.append(product)

    def register_user(self, user):
        self.users.append(user)

    def search_products(self, user, keyword):
        user.search_history.append(keyword)
        matching_products = [product for product in self.products if keyword.lower() in product.name.lower()]
        return matching_products

    def recommend_products(self, user):
        recommended_products = []
        # Implement recommendation logic here (e.g., based on user's search history)
        return recommended_products

    def display_cart(self, user):
        total_price = sum(product.price for product in user.cart)
        print(f"Items in cart for {user.name}:")
        for product in user.cart:
            print(f"{product.name} - ${product.price}")
        print(f"Total: ${total_price}")

# Create a shopping system instance
shopping_system = ShoppingSystem()

# Add products
shopping_system.add_product(Product("P001", "Laptop", "Electronics", 1000))
shopping_system.add_product(Product("P002", "Smartphone", "Electronics", 800))
# ... add more products

# Register users
user1 = User("U001", "Alice")
user2 = User("U002", "Bob")
shopping_system.register_user(user1)
shopping_system.register_user(user2)

# Simulate user interactions
keyword = input("Enter a product keyword to search: ")
matching_products = shopping_system.search_products(user1, keyword)

if matching_products:
    print("Matching products:")
    for product in matching_products:
        print(f"{product.name} - ${product.price}")

    recommendation = shopping_system.recommend_products(user1)
    if recommendation:
        print("Recommended products:")
        for product in recommendation:
            print(f"{product.name} - ${product.price}")
else:
    print("No products found matching the keyword.")

# Add a product to the user's cart
chosen_product_id = input("Enter the product ID to add to cart: ")
chosen_product = next((product for product in matching_products if product.product_id == chosen_product_id), None)
if chosen_product:
    user1.cart.append(chosen_product)
    shopping_system.display_cart(user1)
else:
  print("Invalid product ID.")
  class Product:
    def __init__(self, product_id, name, category, price):
        self.product_id = product_id
        self.name = name
        self.category = category
        self.price = price

class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.search_history = []
        self.cart = []

class ShoppingSystem:
    def __init__(self):
        self.products = []
        self.users = []

    def add_product(self, product):
        self.products.append(product)

    def register_user(self, user):
        self.users.append(user)

    def search_products(self, user, keyword):
        user.search_history.append(keyword)
        matching_products = [product for product in self.products if keyword.lower() in product.name.lower()]
        return matching_products

    def recommend_products(self, user):
        recommended_products = []
        # Implement recommendation logic here (e.g., based on user's search history)
        return recommended_products

    def display_cart(self, user):
        total_price = sum(product.price for product in user.cart)
        print(f"Items in cart for {user.name}:")
        for product in user.cart:
            print(f"{product.name} - ${product.price}")
        print(f"Total: ${total_price}")

# Create a shopping system instance
shopping_system = ShoppingSystem()

# Add products
shopping_system.add_product(Product("P001", "Laptop", "Electronics", 1000))
shopping_system.add_product(Product("P002", "Smartphone", "Electronics", 800))
# ... add more products

# Register users
user1 = User("U001", "Alice")
user2 = User("U002", "Bob")
shopping_system.register_user(user1)
shopping_system.register_user(user2)

# Simulate user interactions
keyword = input("Enter a product keyword to search: ")
matching_products = shopping_system.search_products(user1, keyword)

if matching_products:
    print("Matching products:")
    for product in matching_products:
        print(f"{product.name} - ${product.price}")

    recommendation = shopping_system.recommend_products(user1)
    if recommendation:
        print("Recommended products:")
        for product in recommendation:
            print(f"{product.name} - ${product.price}")
else:
    print("No products found matching the keyword.")

# Add a product to the user's cart
chosen_product_id = input("Enter the product ID to add to cart: ")
chosen_product = next((product for product in matching_products if product.product_id == chosen_product_id), None)
if chosen_product:
    user1.cart.append(chosen_product)
    shopping_system.display_cart(user1)
else:
    print("Invalid product ID.")