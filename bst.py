class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insertNode(rootNode, nodeValue):
    if rootNode.data == None:
        rootNode.data = nodeValue
    elif nodeValue <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(nodeValue)
        else:
            insertNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild == None:
            rootNode.rightChild = BSTNode(nodeValue)
        else: 
            insertNode(rootNode.rightChild, nodeValue)
    return "Node Inserted"     



def preorderTraversal(rootNode):
    if not rootNode:
        return

    print(rootNode.data, end=" ")
    preorderTraversal(rootNode.leftChild)
    preorderTraversal(rootNode.righChild)

def inorderTraversal(rootNode):
    if not rootNode:
        return
    
    inorderTraversal(rootNode.leftChild)
    print(rootNode.data, end="")
    inorderTraversal(rootNode.righChild)

def postOrderTraversal(rootNode):
    if not rootNode:
        return
    postOrderTraversal(rootNode.leftChild)
    postOrderTraversal(rootNode.rightChild)
    print(rootNode.data , end=" ")


def searchNode(rootNode, nodeValue):
    if rootNode.data == nodeValue:
        print("Found")
    elif nodeValue < rootNode.data:
        if rootNode.leftChild is not None:
            if rootNode.leftChild == nodeValue:
                print("Found")
            else:
                searchNode(rootNode.leftChild, nodeValue)
    else:
        if rootNode.rightChild is not None:
            if rootNode.rightChild == nodeValue:
                print("Found")
            else:
                searchNode(rootNode.rightChild, nodeValue)
        else:
            print("Not found")
        
def deleteNode(rootNode, nodeValue):
    if rootNode is None:
        return rootNode
    if nodeValue < rootNode.data:
        rootNode.leftChild = deleteNode(nodeValue)
    elif nodeValue > rootNode.data:
        rootNode.rightChild = deleteNode(nodeValue)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp



newBST = BSTNode(10)
insertNode(newBST, 4)
insertNode(newBST, 8)
insertNode(newBST, 2)
insertNode(newBST, 5)
insertNode(newBST, 9)
insertNode(newBST, 1)
insertNode(newBST, 2)
insertNode(newBST, 7)

deleteNode(newBST, 7)
