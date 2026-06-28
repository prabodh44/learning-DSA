""" A python implementation of the linked list

Implemented as two classes:
    Node class: contains the data and pointer
    LinkedList class: initializes the head pointer
"""

class Node:
    def __init__(self, item):
        self.item = item
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

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

    # display items in the linked list
    while linked_list.head != None:
        print(f"The item is node in {linked_list.head.item}")
        linked_list.head = linked_list.head.next
