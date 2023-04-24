# basket = ['apples', 'grapes', 'pears']
# linked list: apples --> grapes --> pears
"""
apples 
8945 --> grapes
           1444 --> pears
                    5456 --> pears
"""
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None

# 10 --> 5 --> 16
class DoublyLinkedList():
    def __init__(self):
        # self.head = {value: 10, next: {value: 5, next: {value: 16, next: None} }}
        # self.head = {'value': value, 'next': None}
        # self.tail = self.head
        # self.length = 1
        self.head = None
        self.tail = self.head
        self.length = 0

    def printList(self):
        if self.head == None:
            return None
        else:
            data = []
            current_node = self.head
            while current_node != None:
                data.append(current_node.data)
                current_node = current_node.next
            return data

    def append(self, value):
        newNode = Node(value)
        if self.head  == None: 
            self.head = newNode
            self.tail = self.head
            self.length += 1
        else: 
            newNode.previous = self.tail
            self.tail.next = newNode
            self.tail = newNode 
            self.length +=1


    def prepend(self, value): 
        newNode = Node(value)
        if self.head == None: 
            self.head = newNode
            self.tail = self.head
            self.length = 1
        else:
            newNode.next = self.head 
            self.head.previous = newNode
            self.head = newNode
            self.length += 1

        
    def insert(self, position, value):
        if position == 0:
            self.prepend(value)
        elif position >= self.length:
            if position > self.length:
                print("This position is not vailable, Inserting at the end of the list")
            self.append(value)
        else: 
            newNode = Node(value)
            current_node = self.head
            for i in range(position-1): 
                current_node = current_node.next
            newNode.previous = current_node
            newNode.next = current_node.next
            current_node.next = newNode
            newNode.next.previous = newNode
            self.length +=1
    def remove(self, position):
        if position == 0:
            self.head = self.head.next
            if self.head == None or self.head.next == None:
                self.tail = self.head
            elif self.head != None:
                self.head.previous = None
            self.length -=1

        elif self.head == None:
            print('Linked list is empty')
    
        elif position > self.length:
            print('Position is larger than list length, no item removed')
        else:
            leader_node = self.head
            for i in range(position-1):
                leader_node = leader_node.next
            unwanted_node = leader_node.next
            leader_node.next = unwanted_node.next
            if leader_node.next != None:
                leader_node.next.previous = leader_node
            self.length -= 1
            if leader_node.next == None:
                self.tail = leader_node

    def reverse(self):
        if self.head.next == None:
            return self.printList()#self.head
        else:
            first = self.head
            second = first.next
            self.tail = self.head
            while second: 
                temp = second.next
                second.next = first
                first = second 
                second = temp
            self.head.next = None
            self.head = first

            return self.printList()


    # def insert(self, index, value): 
    


if __name__ == "__main__":
    myLinkedList = DoublyLinkedList()
    myLinkedList.append(5)
    # print(myLinkedList.printList(), myLinkedList.head.next)
    myLinkedList.append(16)
    # print(myLinkedList.printList(), myLinkedList.head.next)
    myLinkedList.append(1)
    myLinkedList.append(6)
    myLinkedList.append(7)
    myLinkedList.insert(100,9)

    # myLinkedList.insert(5)
    print(myLinkedList.printList())
    myLinkedList.insert(3,13)
    print(myLinkedList.printList())

    myLinkedList.remove(4)
    print(myLinkedList.printList())
    myLinkedList.reverse()
    print(myLinkedList.printList())


