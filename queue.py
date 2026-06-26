""" A program to implement queue functionality in python

    This queue demonstrates a static queue with 
    the size of the list fixed.
    
    The list is initialized with None values according to the given size
"""

class Queue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.head = self.tail = -1
    
    """ enqueue method
    """
    def enqueue(item):
        pass
    
    def is_empty(self):
        if self.head == self.tail == -1:
            raise IndexError("The Queue is empty")
    
    def show(self):
        print(self.queue)

if __name__ == "__main__":
    q = Queue(5)
    q.is_empty()
    q.show()
