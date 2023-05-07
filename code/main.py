import pickle
import adjList, degList
import sys

print(len(sys.argv), 'arguments.')
print('Argument List:', str(sys.argv))
# if len(sys.argv) < 5:
#     print("Run with arguments V, E, G, and DIST")
#     exit()
adj = adjList.AdjacencyList(25)
# adj.addEdge(0,1)
# adj.addEdge(2,3)
# adj.addEdge(2,1)
# adj.completeBuild()
# adj.cycleBuild()
# adj.randomUniformBuild(50)
adj.randomSkewedBuild(75)
# adj.save('test.poo')
# with open('test.poo', 'rb') as file:
#     adj1 = pickle.load(file) new save and load procedure
# adj.randomPersonalBuild(75)
deg = degList.degreeList(adj)
adj.printList()
deg.printList()
# V = sys.argv[1]
# E = sys.argv[2]
# G = sys.argv[3]
# DIST = sys.argv[4]