class Vertice:
    def __init__(self, degree):
        self.degree = degree
        self.edges = None

class Edge:
    def __init__(self, destination, next):
        self.destination = destination
        self.next = next

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
            if curEdge.destination == vert2:
                return True
            curEdge = curEdge.next
        return False
    
    def addEdge(self, vert1, vert2):
        self.checkIDs(vert1, vert2)
        edge1 = Edge(vert2, self.vertices[vert1].edges)
        edge2 = Edge(vert1, self.vertices[vert2].edges)

        self.vertices[vert1].edges = edge1
        self.vertices[vert1].degree += 1

        self.vertices[vert2].edges = edge2
        self.vertices[vert2].degree += 1
    
    def printList(self):
        print("Vert #: ", len(self.vertices))
        for index, i in enumerate(self.vertices):
            print("index:", index, ", degree:", i.degree, " }", sep = "", end ="")
            cur = i.edges
            while(cur):
                print("->", cur.destination, end = " ")
                cur = cur.next
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