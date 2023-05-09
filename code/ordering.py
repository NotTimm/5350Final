import adjList, degList

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