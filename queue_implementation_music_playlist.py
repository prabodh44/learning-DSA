""" A music player playlist simulation that plays all the songs in the order they were added. 
 
    This is only implemented using linear queue 
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
            
    """ dequeue method
    removes the first item from the queue and increases the head position by 1
    
    
    
    """
    def dequeue(self):
        try:
            if not self.is_empty():
                if self.head == self.tail == 0:
                    temp = self.queue[self.tail]
                    self.head = -1
                    self.tail = -1
                    return temp
                
                else:
                    temp = self.queue[self.head]
                    self.head += 1
                    return temp
        except IndexError:
            print("The queue is empty")
    
    def is_empty(self):
        if self.head == self.tail == -1:
            raise IndexError("The Queue is empty")
            
    def is_full(self):
        if self.tail == self.size - 1:
            raise IndexError("The Queue is full")
    
    def show(self):
        print(self.queue)
        
    """ display_queue method
    displays all the items of the queue
    """
    def display_queue(self):
        for i in range(self.head, self.tail + 1):
            print(self.queue[i], end=" ")

if __name__ == "__main__":
     playlist = Queue(10) # Playlist with a space to add 10 songs only
     
# Music Player functions
def add_music(song):
    playlist.enqueue(song)
    

def play_next_song():
    current_song = playlist.dequeue()
    print(f"The current song is {current_song}")

def view_playlist():
    playlist.display_queue()
    
# option picker logic
def show_menu():
    print("*** Choose your option ***")
    print("1. Add Music ")
    print("2. Play Next Song")
    print("3. View Playlist")
    print("4. Exit")
    
   
while True:
    show_menu()
    option = int(input("Enter your choice "))
    
    if option == 1:
        song = input("Enter the name of the song ")
        add_music(song)
    elif option == 2:
        play_next_song()
    elif option == 3:
        view_playlist()
    elif option == 4:
        print("Exiting application...")
        break
    else:
        print("Invalid choice. Pick numbers from 1 - 4")
        
    
    
