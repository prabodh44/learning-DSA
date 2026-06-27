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
    adds an item to the end of the queue
    """
    def enqueue(self, item):
        if self.is_full():
            return False
            
        if self.head == -1:
            self.head = 0
            self.tail = 0
            self.queue[self.tail] = item
        else:
            self.tail += 1
            self.queue[self.tail] = item

            
    """ dequeue method
    removes the first item from the queue and increases the head position by 1
    """
    def dequeue(self):
        if self.is_empty():
            return False
            
        if self.head == self.tail:
            temp = self.queue[self.tail]
            self.head = -1
            self.tail = -1
            return temp
        else:
            temp = self.queue[self.head]
            self.head += 1
            return temp


    def is_empty(self):
        return self.head == self.tail == -1
            
    def is_full(self):
        return self.tail == self.size - 1
    
    """ display_queue method
    displays all the items of the queue
    """
    def display_queue(self):
        if self.is_empty():
            return False
        for i in range(self.head, self.tail + 1):
            print(self.queue[i], end=" ")

if __name__ == "__main__":
    q = Queue(5)
    q.enqueue(3)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(4)
    q.enqueue(7)
    print("Queue after enqueue")
    q.display_queue()
    print("dequeue operation ")
    print(q.dequeue())
    print("Queue after first dequeue operation")
    q.display_queue()
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
  
    
   
