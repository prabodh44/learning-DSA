""" A stack implementation that undos mathematical calculations 
"""

# stack implementation
# creating the stack
def create_stack():
    stack = []
    return stack
    
# push operation
def push(stack, item):
    stack.append(item)
    return len(stack)

# pop operation
def pop(stack):
    if isEmpty(stack):
        return False
    return stack.pop()

# peek functionlaity
def peek(stack):
    if isEmpty(stack):
        return False
    return(stack[-1])
    
# check if stack is empty
def isEmpty(stack):
    return len(stack) == 0

def show(stack):
    print(stack)

# stack implementation ends 

def show_menu():
    print("Calculator Functionality")
    print("1. Add")
    print("2. Subtract")
    print("3. Undo operation")
    print("4. Show history")
    print("5. Exit")

class Calculator:
    def __init__(self):
        self.result = 0
        self.history = create_stack()
    
    def add(self, num):
        self.result += num
        push(self.history, self.result)
        print(f"The value {num} has been added")
        print(f"The current value of result is {self.result}")
    
    def subtract(self, num):
        self.result -= num
        push(self.history, self.result)
        print(f"The value {num} has been subtracted")
        print(f"The current value of result is {self.result}")
    
    def undo(self):
        result = pop(self.history)
        if result == False:
            print("Nothing to undo")
            return
        print(f"Undo result: {result}")

    def show_history(self):
        show(self.history)


# main function
if __name__ == "__main__":
    # create an empty stack
    calculations = Calculator()

    # options logic
    while True:
        show_menu()
        option = int(input("Enter your option "))
        
        if option == 1:
            number = int(input("Enter the number to add "))
            calculations.add(number)
        
        elif option == 2:
            number = int(input("Enter the number to subtract "))
            calculations.subtract(number)
        
        elif option == 3:
            calculations.undo()
        
        elif option == 4:
            calculations.show_history()
        
        elif option == 5:
            print("Exiting Program...")
            break

        else:
            print("Invalid option. Please enter a valid number")
    