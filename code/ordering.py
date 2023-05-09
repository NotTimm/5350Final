import adjList, degList
import random

def smallestLastVertOrder(adj, deg):
    removed = -1
    out = []
    while (removed := removed+1) < len(adj.vertices):
        smallest = deg.findSmallest()
        deg.removeVert(adj, smallest)
        deg.remove(smallest)
        smallest.removed = True
        out.append(smallest)
    return out

def smallestOriginalVertOrder(deg):
    out = []
    for i in range(len(deg.degrees)-1, -1, -1):
        if deg.degrees[i] != None:
            temp = deg.degrees[i]
            while temp != None:
                out.append(temp)
                temp = temp.next
    return out

def uniformRandomVertOrder(adj):
    copyAdj = adj.vertices.copy()
    random.shuffle(copyAdj)
    return copyAdj