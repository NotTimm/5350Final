import adjList

class listVal:
    def __init__(self, value, next):
        self.last = None
        self.vert = value
        self.next = next

class degreeList:
    def __init__(self, adj):
        self.degrees = [None] * len(adj.vertices)
        n = -1
        while((n := n+1) < len(adj.vertices)):
            self.insert(adj.vertices[n], adj.vertices[n].degree)

    def insert(self, value, degree):
        if value.last != None or value.next != None:
            exit(69)
        print(degree)
        temp = listVal(value, self.degrees[degree])
        if self.degrees[degree] != None:
            self.degrees[degree].last = temp
        self.degrees[degree] = temp

    def removeVert(self, adj, vertice):
        vert = adj.vertices[vertice]
        vert.removed = True
        curTemp = vert.edges
        while curTemp != None:
            dest = adj.vertices[curTemp.destination]
            if(not dest.removed):
                self.remove(dest)
                dest.degree -= 1
                self.insert(dest, dest.degree)
            curTemp = curTemp.next

    def remove(self, vert):
        if vert.last != None:
            vert.last.next = vert.next
        else:
            self.degrees[vert.degree] = vert.next
        if vert.next != None:
            vert.next.last = vert.last
        vert.last = None
        vert.next = None
    
    def printList(self):
        print(self.degrees)