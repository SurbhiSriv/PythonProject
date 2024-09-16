class Node:
    def __init__(self, data):
        # Initialize a node with data and a pointer to the next node (initially None)
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        # Initialize the head of the linked list (initially None)
        self.head = None

    def display(self):
        # Display the elements of the linked list
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def insert_at_beginning(self, data):
        # Insert a new node at the beginning of the linked list
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        print(f"Inserted {data} at the beginning.")

    def insert_at_end(self, data):
        # Insert a new node at the end of the linked list
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        print(f"Inserted {data} at the end.")

    def delete_node(self, key):
        # Delete the first node with the given data (key)
        current = self.head

        # If the list is empty
        if not current:
            print("The list is empty. Nothing to delete.")
            return

        # If the node to be deleted is the head
        if current and current.data == key:
            self.head = current.next
            current = None
            print(f"Deleted {key} from the linked list.")
            return

        # Search for the node to be deleted, keep track of the previous node
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        # If the data (key) was not found in the list
        if not current:
            print(f"Node with data {key} not found.")
            return

        # Unlink the node from the linked list
        prev.next = current.next
        current = None
        print(f"Deleted {key} from the linked list.")