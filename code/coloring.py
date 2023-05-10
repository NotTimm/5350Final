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

def SOVOColoring(adj, deg):
    sovo = ordering.smallestOriginalVertOrder(adj, deg)
    greedyColoring(adj, sovo)

def UROColoring(adj):
    uro = ordering.uniformRandomVertOrder(adj)
    for i in uro:
        print(i.id)
    greedyColoring(adj, uro)

def SOVOFColoring(adj, deg):
    sovoFlipped = ordering.smallestOriginalVertOrderFlipped(adj, deg)
    greedyColoring(adj, sovoFlipped)