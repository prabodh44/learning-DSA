""" A browser history simulation that use stacks 
implemented through python class
"""
class Stack:
    # Create a stack upon initialization
    def __init__(self):
        self.stack = []
    
    # Stack functions: push, pop, peek, is_empty, display
    def push(self, item):
        self.stack.append(item)
    
    def pop(self):
        return self.stack.pop()
    
    def is_empty(self):
        return len(self.stack) == 0
    
    def show_stack(self):
        if self.is_empty():
            return None
        return list(reversed(self.stack))

    def peek(self):
        if self.is_empty():
            return None
        return self.stack[-1]
    
# Stack implementation ends

def show_menu():
    print("Choose the options ")
    print("1. Add URL")
    print("2. Go Back")
    print("3. View Current Site")
    print("4. See full history")
    print("5. Exit")

# Browser history functions

def add_url(browser_history, url_string):
    browser_history.push(url_string)

def go_back(browser_history):
    site = browser_history.pop()
    if not site:
        return None
    else:
        return site

def view_current_site(browser_history):
    current_site = browser_history.peek()
    if not current_site:
        return None
    else:
        return current_site

def show_history(browser_history):
    if browser_history.is_empty():
        print("The list is empty")
    else:
        return browser_history.show_stack()
    
if __name__ == "__main__":
    browser_history = Stack()

    while True:
        show_menu()
        option = int(input("Enter your choice "))

        if option == 1:
            url_string = input("Enter the site you have just browsed ")
            add_url(browser_history, url_string)
        
        elif option == 2:
            prev_site = go_back(browser_history)
            if not prev_site:
                print("Browser history is empty")
            else:
                print(f"The prev site is {prev_site}")
        
        elif option == 3:
            current_site = browser_history.peek()
            if not current_site:
                print("Browser history is empty")
            else:
                print(f"The current site is {current_site}")
        
        elif option == 4:
            sites = show_history(browser_history)
            if not sites:
                print("The browser history is empty")
            else:
                for site in sites:
                    print(site)
        
        elif option == 5:
            print("Exiting Application...")
            break

        else:
            print("The option is invalid. Please choose from options 1 to 4")
    
    