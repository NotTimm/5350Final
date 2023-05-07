import adjList

class degreeList:
    def __init__(self, adj):
        self.degrees = []
        for i in range(len(adj.vertices)):
            deg = 0
            if((l := adj.vertices[i].edges) != None):
                while l != None:
                    deg += 1
                    l = l.next
            self.degrees.append(deg)

    def remove(self, adj, vertice):
        i = adj.vertices[vertice].edges
        while i != None:
            self.degrees[i.destination] -= 1
            self.degrees[vertice] -= 1
            adj.removeEdge(vertice, i.destination)
    
    def printList(self):
        print(self.degrees)