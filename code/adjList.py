import random
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
            self.vertices.append(new := Vertice(0))

    def checkIDs(self, vert1, vert2):
        if vert1 < 0 or vert1 >= len(self.vertices):
            print("ERROR out of bounds")
            exit(69)
        elif vert2 < 0 or vert2 >= len(self.vertices):
            print("ERROR out of bounds")
            exit(69)

    def edgeExists(self, vert1, vert2):
        self.checkIDs(vert1, vert2)
        curEdge = Edge(None, self.vertices[vert1].edges)
        while curEdge := curEdge.next:
            if curEdge.destination == vert2:
                return True
        return False
    
    def addEdge(self, vert1, vert2):
        self.checkIDs(vert1, vert2)
        edge1 = Edge(vert2, self.vertices[vert1].edges)
        edge2 = Edge(vert1, self.vertices[vert2].edges)

        self.vertices[vert1].edges = edge1
        self.vertices[vert1].degree += 1

        self.vertices[vert2].edges = edge2
        self.vertices[vert2].degree += 1

    ### Build Scenarios Below ###

    def completeBuild(graph):
        vertI = -1
        while (vertI := vertI+1) < len(graph.vertices)-1:
            vertO = vertI+1
            graph.addEdge(vertI, vertO)
    
    def cycleBuild(graph):
        vertI = -1
        while (vertI := vertI+1) < len(graph.vertices)-1:
            graph.addEdge(vertI, vertI+1)
        graph.addEdge(0, len(graph.vertices)-1)

    def randomUniformBuild(graph, conflicts):
        if conflicts > len(graph.vertices) * (len(graph.vertices)-1)/2:
            print("ERROR too many conflicts")
            exit(420)
        i = -1
        while (i := i+1) < conflicts:
            vert1 = 0
            vert2 = 0

            while vert1 == vert2 or graph.edgeExists(vert1, vert2):
                vert1 = random.randint(0, len(graph.vertices)-1)
                vert2 = random.randint(0, len(graph.vertices)-1)
            graph.addEdge(vert1, vert2)
    
    def randomSkewedBuild(graph, conflicts):
        if conflicts > len(graph.vertices) * (len(graph.vertices)-1)/2:
            print("ERROR too many conflicts")
            exit(420)
        i = -1
        while (i := i+1) < conflicts:
            vert1 = 0
            vert2 = 0

            while vert1 == vert2 or graph.edgeExists(vert1, vert2):
                vert1 = int(random.triangular(0,len(graph.vertices), len(graph.vertices)*.5))
                vert2 = int(random.triangular(0,len(graph.vertices), len(graph.vertices)*.5))
            graph.addEdge(vert1, vert2)

    def randomPersonalBuild(graph, conflicts):
        if conflicts > len(graph.vertices) * (len(graph.vertices)-1)/2:
            print("ERROR too many conflicts")
            exit(420)
        i = -1
        while (i := i+1) < conflicts:
            vert1 = 0
            vert2 = 0

            while vert1 == vert2 or graph.edgeExists(vert1, vert2):
                vert1 = int(random.betavariate(.5,.5) * len(graph.vertices))
                vert2 = int(random.betavariate(.5,.5) * len(graph.vertices))
            graph.addEdge(vert1, vert2)

    ### Print Function ###
    
    def printList(self):
        print("Vert #: ", len(self.vertices))
        for index, i in enumerate(self.vertices):
            print("VertID: ", index, ", Degree: ", i.degree, " }", sep = "", end ="")
            cur = Edge(None, i.edges)
            while cur := cur.next:
                print("->", cur.destination, sep = "", end = "")
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