class ShoppingCart:
    def __init__(self):
        # Initialize an empty dictionary to store items and their quantities and prices
        self.cart = {}

    def add_item(self, item_name, quantity, price):
        # Add an item to the cart or update the quantity if it already exists
        if item_name in self.cart:
            self.cart[item_name]['quantity'] += quantity
            self.cart[item_name]['price'] = price  # Update the price in case it changes
        else:
            self.cart[item_name] = {'quantity': quantity, 'price': price}
        print(f"Added {quantity} of {item_name} at ${price} each.")

    def remove_item(self, item_name, quantity):
        # Remove a certain quantity of an item from the cart
        if item_name in self.cart:
            if quantity >= self.cart[item_name]['quantity']:
                del self.cart[item_name]
                print(f"Removed all of {item_name} from the cart.")
            else:
                self.cart[item_name]['quantity'] -= quantity
                print(f"Removed {quantity} of {item_name}. Remaining: {self.cart[item_name]['quantity']}.")
        else:
            print(f"{item_name} is not in the cart.")

    def calculate_total(self):
        # Calculate the total price of the items in the cart
        total = sum(item['quantity'] * item['price'] for item in self.cart.values())
        return total

    def display_cart(self):
        # Display the items in the cart
        if not self.cart:
            print("The cart is empty.")
        else:
            print("Items in the cart:")
            for item_name, details in self.cart.items():
                print(f"{item_name}: {details['quantity']} @ ${details['price']} each")
            print(f"Total: ${self.calculate_total():.2f}")