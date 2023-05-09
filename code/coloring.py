import adjList, degList, ordering

def greedyColoring(adj, order): # can be given an adj list in both for random greedy, or an adj plus its slvo for slvo coloring
    for vert in order:
        available = [True] * len(order)
        cur = vert.edges
        while cur != None:
            if adj.vertices[cur.destination].color != None:
                available[adj.vertices[cur.destination].color] = False
            cur = cur.next
        for i in range(len(available)):
            if available[i]:
                vert.color = i
                break

def SLVOColoing(adj, deg):
    slvo = ordering.smallestLastVertOrder(adj, deg)
    greedyColoring(adj, slvo)