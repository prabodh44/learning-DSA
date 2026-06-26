# stack implementation
# basic functions: push, pop, isempty. isfull, peek

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
        raise IndexError("The stack is empty")
    """ this is better than just returning a string like return "The stack is empty" or print("The stack is empty") 
    """
    return stack.pop()

# peek functionlaity
def peek(stack):
    if isEmpty(stack):
        raise IndexError("The stack is empty")
    return(stack[-1])
    
# check if stack is empty
def isEmpty(stack):
    return len(stack) == 0

def show(stack):
    print(stack)

if __name__ == "__main__":
    stack = create_stack()
    
    push(stack, 3)
    push(stack, 5)
    push(stack, 6)
    
    show(stack)
    
    print(f"show last item without removing. {peek(stack)}")
    
    print(pop(stack))
    
    show(stack)
    
    
    
