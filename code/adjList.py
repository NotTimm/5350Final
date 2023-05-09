import random, math, pickle, struct
class Vertice:
    def __init__(self, degree, id):
        self.id = id
        self.degree = degree
        self.edges = None
        self.next = None
        self.last = None
        self.removed = False

class Edge:
    def __init__(self, destination, next):
        self.destination = destination
        self.next = next

class AdjacencyList:
    def __init__(self, vertCount):
        self.vertices = []
        for i in range(vertCount):
            self.vertices.append(Vertice(0,i))

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
            vertO = vertI
            while (vertO := vertO+1) < len(graph.vertices):
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
                vert1 = len(graph.vertices)-1-int(math.sqrt(4.0*2.0*float(random.randint(0,(len(graph.vertices)-1)*len(graph.vertices)/2))+1.0)/2.0-.5)
                vert2 = len(graph.vertices)-1-int(math.sqrt(4.0*2.0*float(random.randint(0,(len(graph.vertices)-1)*len(graph.vertices)/2))+1.0)/2.0-.5)
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
                vert1 = int(math.pow(random.random(), 2) * float(len(graph.vertices)))
                vert2 = int(math.pow(random.random(), 2) * float(len(graph.vertices)))
                # vert1 = int(random.betavariate(.5,.5) * len(graph.vertices))
                # vert2 = int(random.betavariate(.5,.5) * len(graph.vertices))
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
    
    def removeEdge(self, vert1, vert2):
        vertTemp = self.vertices[vert1].edges
        while vertTemp.destination != vert2:
            vertTemp = vertTemp.next
        vertTemp.removed = True
        vertTemp = self.vertices[vert2].edges
        while vertTemp.destination != vert1:
            vertTemp = vertTemp.next
        vertTemp.removed = True

    def save(self, path):
        with open(path, 'wb') as file:
            pickle.dump(self, file)

    def serialize(self, path):
        with open(path, 'wb') as file:
            file.write(struct.pack('<L', len(self.vertices)))
            for vert in self.vertices:
                cur = vert.edges
                while cur != None:
                    if cur.destination > vert.id:
                        file.write(struct.pack('<L', cur.destination))
                    cur = cur.next
                file.write(struct.pack('<L', 0))

    def deserialize( path):
        with open(path, 'rb') as file:
            size = struct.unpack('<L', file.read(4))[0]
            temp = AdjacencyList(size)
            i = -1
            while (i := i+1) < size:
                while(True):
                    dest = struct.unpack('<L', file.read(4))[0]
                    if dest == 0:
                        break
                    temp.addEdge(i, dest)
            return temp
        

# if __name__ == '__main__':
#     lltest = LinkedList()
#     lltest.head = Node('poo')
#     temp = lltest.head
#     for i in range(10):
#         new = Node(i)
#         temp.next = new
#         temp = temp.next
#     lltest.printList()