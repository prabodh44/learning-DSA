""" A python implementation of the linked list

Implemented as two classes:
    Node class: contains the data and pointer
    LinkedList class: initializes the head pointer
"""

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None
    
    def __str__(self):
        return f"Item: {self.item} - Next: {self.next}"
    
    def __repr__(self):
        return f"Item: {self.item} - Next: {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None
    
    def __repr__(self):
        return f"LinkedList class: self.head value: {self.head}"
    
    # Linked List functionalities: Traversal, Insert, Delete, Search and Sort
    def traverse_linked_list(self):
        # TODO: Understand this code??
        # temp variable to store the head 
        current = self.head
        # display items in the linked list
        while current is not None:
            print(f"The item is node in {current.item}")
            current = current.next
    
    # Insert methods
    def insert_at_front(self, data):
        # create a new node
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


if __name__ == "__main__":
    # create linked list
    linked_list = LinkedList()

    # creating the nodes
    first_node = Node("First Node")
    second_node = Node("Second Node")
    third_node = Node("Third Node")
    
    # connect the first node to head
    linked_list.head = first_node
    print(f"HEAD value: {linked_list.head}")
    print("*" * 10)

    # connect the first node to the second node
    linked_list.head.next = second_node
    print(f"first_node next value: {linked_list.head.next}")
    print("*" * 10)

    # connect the second node to the third node
    second_node.next = third_node
    print(f"second_node next value: {second_node.next}")
    print("*" * 10)

    # connect the last node to null
    # third_node.next = None

    # no need to write this code since all nodes
    # point to None when they are initialized in the __init__ method

    # linked list methods
    # 1. Traversal
    linked_list.traverse_linked_list()

    # # 2. Insert linked list at the beginning
    # linked_list.insert_at_front("Zero Node")

    # linked_list.insert_at_front("Before Zero Node")

    # print("****** AFTER NEW NODES INSERTION *******")
    
    # linked_list.traverse_linked_list()
    
