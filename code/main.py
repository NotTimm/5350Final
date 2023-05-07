import pickle
import adjList, degList
import sys

# def smallestLastVertOrder(adj):
#     removed = -1
#     while (removed := removed+1) < len(adj.vertices):
#         smallest = self.

print(len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
# if len(sys.argv) < 5:
#     print("Run with arguments V, E, G, and DIST")
#     exit()
# adj = adjList.AdjacencyList(10000)
adj = adjList.AdjacencyList(500)
# adj.addEdge(0,1)
# adj.addEdge(2,3)
# adj.addEdge(2,1)
# adj.completeBuild()
# adj.cycleBuild()
# adj.randomUniformBuild(50)
# adj.randomSkewedBuild(2000000)
adj.randomSkewedBuild(20000)
adj.save('test.poo')
with open('test.poo', 'rb') as file:
    adj1 = pickle.load(file) # new save and load procedure
# adj.randomPersonalBuild(75)
deg = degList.degreeList(adj)
deg.removeVert(adj, 5)
adj1.printList()
# deg.printList()
# V = sys.argv[1]
# E = sys.argv[2]
# G = sys.argv[3]
# DIST = sys.argv[4]