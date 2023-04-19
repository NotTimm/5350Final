import adjList
import sys

print(len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
# if len(sys.argv) < 5:
#     print("Run with arguments V, E, G, and DIST")
#     exit()
adj = adjList.AdjacencyList(25)
adj1 = adjList.AdjacencyList(10)
# adj.addEdge(0,1)
# adj.addEdge(2,3)
# adj.addEdge(2,1)
# adj.completeBuild()
# adj.cycleBuild()
# adj.randomUniformBuild(50)
# adj.randomSkewedBuild(75)
adj.randomPersonalBuild(75)
adj.printList()
# V = sys.argv[1]
# E = sys.argv[2]
# G = sys.argv[3]
# DIST = sys.argv[4]