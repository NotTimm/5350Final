import adjList, degList
import random

def smallestLastVertOrder(adj, deg):
    removed = -1
    out = [None] * len(adj.vertices)
    while (removed := removed+1) < len(adj.vertices):
        # print('Step #: ', removed+1)
        smallest = deg.findSmallest()
        deg.removeVert(adj, smallest)
        deg.remove(smallest)
        smallest.removed = True
        out[len(adj.vertices)-removed-1] = smallest
        # adj.printList()
    return out

def smallestOriginalVertOrder(adj, deg):
    out = [None] * len(adj.vertices)
    i = 1
    for obj in deg.degrees:
        copy = obj
        while copy != None:
            out[len(adj.vertices)-i] = copy
            copy = copy.next
            i += 1
    return out

def smallestOriginalVertOrderFlipped(adj, deg): # My personal final order for the coloring
    out = []
    for obj in deg.degrees:
        copy = obj
        while copy != None:
            out.append(copy)
            copy = copy.next
    return out

def uniformRandomVertOrder(adj):
    copyAdj = adj.vertices.copy()
    random.shuffle(copyAdj)
    return copyAdj

def SLVOTerminalClique(order):
    size = 0
    for vert in order:
        if vert.color == size:
            size += 1
        else:
            break
    return size