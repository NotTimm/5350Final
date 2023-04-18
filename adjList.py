class Vertice:
    def __init__(self, degree):
        self.degree = degree
        self.edges = None

class Edge:
    def __init__(self, origin, destination):
        self.origin = origin
        self.destination = destination
        self.next = None

class AdjacencyList:
    def __init__(self, vertCount, genType, conflicts):
        self.vertices = []
        for i in range(vertCount):
            new = Vertice(0)
            self.vertices.append(new)

    def checkIDs(self, vert1, vert2):
        if vert1 < 0 or vert1 >= len(self.vertices):
            print("ERROR out of bounds")
            exit(69)
        elif vert2 < 0 or vert2 >= len(self.vertices):
            print("ERROR out of bounds")
            exit(69)

    def edgeExists(self, vert1, vert2):
        self.checkIDs(vert1, vert2)
        curEdge = self.vertices[vert1].edges
        while(curEdge):
            if curEdge.origin == vert2:
                return True
            curEdge = curEdge.next
        return False
    
    def printList(self):
        for i in range(len(self.vertices)):
            print(self.vertices[i].degree, i, end = " ")
        print()

# if __name__ == '__main__':
#     lltest = LinkedList()
#     lltest.head = Node('poo')
#     temp = lltest.head
#     for i in range(10):
#         new = Node(i)
#         temp.next = new
#         temp = temp.next
#     lltest.printList()