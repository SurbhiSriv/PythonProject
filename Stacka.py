class Stacka:
    def __init__(self):
        # Initialize an empty list to store Stacka elements
        self.items = []

    def push(self, item):
        # Add an item to the top of the Stacka
        self.items.append(item)
        print(f"Pushed {item} to the Stacka.")

    def pop(self):
        # Remove and return the top item of the Stacka
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from the Stacka.")
            return popped_item
        else:
            print("Stacka is empty. Cannot pop.")
            return None

    def display(self):
        # Display the elements of the Stacka
        if self.is_empty():
            print("Stacka is empty.")
        else:
            print("Stacka elements:", self.items)

    def is_empty(self):
        # Check if the Stacka is empty
        return len(self.items) == 0