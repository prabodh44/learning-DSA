""" A grocery list simulation using linked lists
The linked list implementation contains two classes: Node and LinkedList
Node class to store the data and the pointer
LinkedList class to store the HEAD and manage LinkedList functionality
"""

# Linked List implementation
class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def __repr__(self):
        return f"item: {self.item} next(points to): {self.next}"
    
    def __str__(self):
        return f"Item: {self.item}"

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __str__(self):
        items = []
        current = self.head

        while current is not None:
            items.append(str(current.item)) # __str__ only returns string 
            current = current.next
        return "->".join(items)
    
    # LinkedList functions
    def traverse(self):
        current = self.head
        items = []
        while current is not None:
            items.append(current.item)
            current = current.next
        return items

    def insert_at_beginning(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        
        # current = self.head
        # while(current is not None):
        #     current = current.next
        #     if current.next is None:
        #         last_node = current
        #         current = None
        
        # last_node.next = new_node

        # better implementation
        last = self.head
        # loop as long as there next pointer points to something
        while(last.next):
            last = last.next
        # when the loop end var last stores the last value
        last.next = new_node
# Linked List implementation ends

def show_menu():
    print("****** Grocery List Inventory Menu ******")
    print("1. Create a grocery list with items")
    print("2. Add item to the front of the list")
    print("3. Add item to the back of the list")
    print("4. Display Grocery List")
    print("5. Exit")

if __name__ == "__main__":
    grocery_list = LinkedList()
    
    while(True):
        show_menu()
        option = int(input("Enter your choice (1-5)"))
        

    first_item = Node("Milk")
    second_item = Node("Eggs")
    third_item = Node("Tea")


    # HEAD points to the first item
    grocery_list.head = first_item

    first_item.next = second_item

    second_item.next = third_item

    grocery_list.insert_at_beginning("Water")
    print(grocery_list.insert_at_end("Oil"))


    print(grocery_list)
    print(grocery_list.traverse())
    
