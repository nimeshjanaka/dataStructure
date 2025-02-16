# Create node
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Node initial
class Sll:
    def __init__(self):
        self.head = None
        self.tail = None
    
    # Iterator for looping through the list
    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
    
    # Display method
    def display(self):
        if self.head is None:
            print("No any values")
        else:
            node = self.head
            while node is not None:
                print(node.value, end="  ")
                node = node.next
            print()  # For a new line at the end
    
    # Insert method
    def insert(self, value, location):
        newNode = Node(value)
        if self.head is None:  # If the list is empty
            self.head = newNode
            self.tail = newNode
        else:
            if location == 0:  # Insert at the beginning
                newNode.next = self.head
                self.head = newNode
            elif location == -1:  # Insert at the end
                self.tail.next = newNode
                self.tail = newNode
            else:  # Insert at a specific location
                tempNode = self.head
                index = 0
                while index < location - 1 and tempNode.next is not None:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode 
                if nextNode is None:  # Update tail if inserted at the end
                    self.tail = newNode
    
    # Search method
    def search(self, searchValue):
        if self.head is None:
            print("No any values")
        else:
            node = self.head
            while node is not None:
                if node.value == searchValue:
                    print(f"Value {searchValue} Found")
                    return
                node = node.next
            print(f"Value {searchValue} Not Found")

    # Delete method
    def delete(self, location):
        if self.head is None:
            print("No values to delete")
            return
        
        if location == 0:  # Delete from the beginning
            self.head = self.head.next
            if self.head is None:  # List becomes empty
                self.tail = None
        elif location == -1:  # Delete from the end
            if self.head == self.tail:  # Only one node
                self.head = None
                self.tail = None
            else:
                node = self.head
                while node.next != self.tail:
                    node = node.next
                node.next = None
                self.tail = node
        else:  # Delete at a specific location
            tempNode = self.head
            index = 0
            while index < location - 1 and tempNode.next is not None:
                tempNode = tempNode.next
                index += 1
            if tempNode.next is not None:
                tempNode.next = tempNode.next.next
                if tempNode.next is None:  # Update tail if needed
                    self.tail = tempNode

# Create linked list and nodes
linkedList = Sll()
node1 = Node(4)
node2 = Node(5)
node3 = Node(6)
node4 = Node(8)

linkedList.head = node1
node1.next = node2
node2.next = node3
node3.next = node4
linkedList.tail = node4

# Display initial list
linkedList.display()

# Insert a node at the beginning
linkedList.insert(6, 0)

# Search for a value
linkedList.search(2)

# Delete the first node
linkedList.delete(0)

# Display list after deletion
linkedList.display()
