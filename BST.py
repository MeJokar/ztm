class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        return 

class BinarySearchTree():
    def __init__(self):
        self.root = None
        self.number_of_nodes = 0

    def insert(self, value):
        newNode = Node(value)
        if self.root == None:
            self.root = newNode
            self.number_of_nodes += 1
            return
        else:
            currentNode = self.root
            while(True):
                if value < currentNode.value:
                    # go to left 
                    if currentNode.left == None:
                        currentNode.left = newNode
                        self.number_of_nodes += 1
                        return 
                    currentNode = currentNode.left
                else:
                    # right 
                    if currentNode.right == None: 
                        currentNode.right = newNode
                        self.number_of_nodes += 1
                        return
                    currentNode = currentNode.right
                             
    def lookup(self, value):
        if self.root == None:
            return False
        currentNode = self.root

        while currentNode != None:
            if value < currentNode.value:
                # left 
                currentNode = currentNode.left
            elif value > currentNode.value:
                # right
                currentNode = currentNode.right
            elif currentNode.value == value:
                return currentNode, currentNode.value
        return False



if __name__ == "__main__":
    tree = BinarySearchTree()
    tree.insert(9)
    tree.insert(4)
    tree.insert(6)
    tree.insert(20)
    tree.insert(170)
    tree.insert(15)
    tree.insert(1)
    print(tree.lookup(9))
    print(tree.lookup(13))
    aa = {2:3, 4:6, "a":5}
    print(aa, aa[2], aa["a"])
    print('a' in aa)


