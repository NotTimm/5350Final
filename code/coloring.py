import adjList, degList, ordering

def greedyColoring(adj):
    result = [-1] * len(adj.vertices)
    result[0] = 0
    available = [False] * len(adj.vertices)
    for i in range(1, len(adj.vertices)):
        cur = adj.vertices[i].edges
        while cur != None:
            if result[cur.destination] != -1:
                available[result[cur.destination]] = True
            cur = cur.next
        cr = 0
        while cr < len(adj.vertices):
            if(available[cr] == False):
                break
            cr += 1
        result[i] = cr
        cur = adj.vertices[i].edges
        while cur != None:
            if result[cur.destination] != -1:
                available[result[cur.destination]] = False
            cur = cur.next
    for i in range(len(adj.vertices)):
        print("Vert:",i,"---> Color:",result[i])