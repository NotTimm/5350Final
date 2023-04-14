class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def printList(self):
        temp = self.head
        while(temp):
            print(temp.data, end = " ")
            temp = temp.next
        print()

if __name__ == '__main__':
    lltest = LinkedList()
    lltest.head = Node('poo')
    temp = lltest.head
    for i in range(10):
        new = Node(i)
        temp.next = new
        temp = temp.next
    lltest.printList()