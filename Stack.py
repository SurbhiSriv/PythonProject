class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.items = []

    def push(self, item):
        # Add an item to the top of the stack
        self.items.append(item)
        print(f"Pushed {item} to the stack.")

    def pop(self):
        # Remove and return the top item of the stack
        if not self.is_empty():
            popped_item = self.items.pop()
            print(f"Popped {popped_item} from the stack.")
            return popped_item
        else:
            print("Stack is empty. Cannot pop.")
            return None

    def is_empty(self):
        # Check if the stack is empty
        return len(self.items) == 0

    def peek(self):
        # Return the top item of the stack without removing it
        if not self.is_empty():
            return self.items[-1]
        else:
            print("Stack is empty. Nothing to peek.")
            return None

    def size(self):
        # Return the number of items in the stack
        return len(self.items)

    def display(self):
        # Display the elements of the stack
        print("Stack:", self.items)