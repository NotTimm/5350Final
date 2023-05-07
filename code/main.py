import pickle
import adjList, degList
import sys

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

sys.setrecursionlimit(10000)
print(len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
# if len(sys.argv) < 5:
#     print("Run with arguments V, E, G, and DIST")
#     exit()
# adj = adjList.AdjacencyList(10000)
adj = adjList.AdjacencyList(3000)
# adj.addEdge(0,1)
# adj.addEdge(2,3)
# adj.addEdge(2,1)
adj.completeBuild()
# adj.cycleBuild()
# adj.randomUniformBuild(50)
# adj.randomSkewedBuild(2000000)
# adj.randomSkewedBuild(20000)
# adj.save('test.poo')
# with open('test.poo', 'rb') as file:
#     adj1 = pickle.load(file) # new save and load procedure
# adj.randomPersonalBuild(75)
# deg = degList.degreeList(adj)
# print(smallestLastVertOrder(adj, deg))
adj.serialize('test.poo')
adj1 = adjList.AdjacencyList.deserialize('test.poo')
adj1.printList()
# adj1.printList()
# deg.printList()
# V = sys.argv[1]
# E = sys.argv[2]
# G = sys.argv[3]
# DIST = sys.argv[4]