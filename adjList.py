class Vertice:
    def __init__(self, data):
        self.data = data
        self.next = None

class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination

class AdjacencyList:
    def __init__(self, vertCount, genType, conflicts):
        self.vertices = []
        for i in range(vertCount-1):
            new = Vertice(i)
            self.vertices.append(new)
        self.head = None

    def printList(self):
        for i in range(len(self.vertices)):
            print(self.vertices[i].data, end = " ")
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