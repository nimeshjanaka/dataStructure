class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        return str(self.list)

    def isEmpty(self):
        return self.list == []
    
    def push(self, value):
        return self.list.append(value)

# Create a Stack instance
myStack = Stack()

# Check if the stack is empty
myStack.push(5)
print (myStack)