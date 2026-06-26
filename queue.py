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
    def enqueue(self, item):
        try:
            if not self.is_full():
                if self.head == -1:
                    self.head = 0
                    self.tail = 0
                    self.queue[self.tail] = item
                else:
                    self.tail += 1
                    self.queue[self.tail] = item
                    
                print(f"Item added is {item}")
                print(f"head: {self.head}")
                print(f"tail: {self.tail}")
                
        except IndexError:
            print("The queue is full")
    
    def is_empty(self):
        if self.head == self.tail == -1:
            raise IndexError("The Queue is empty")
    def is_full(self):
        if self.tail == self.size - 1:
            raise IndexError("The Queue is full")
    
    def show(self):
        print(self.queue)

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(14)
