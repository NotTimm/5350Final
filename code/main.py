import pickle, sys, time
import adjList, degList, coloring, ordering

def distGraph(path, adj):
    # with open(path) as file:
    print("vertID, degree")
    for vert in adj.vertices:
        print(str(vert.id) + ', ' + str(vert.degree))
        # file.write(vert.id,',',vert.degree,'\n')

startTime = time.time()
# sys.setrecursionlimit(10000)
# print(len(sys.argv), 'arguments.')
# print('Argument List:', str(sys.argv))
# if len(sys.argv) < 5:
#     print("Run with arguments V, E, G, and DIST")
#     exit()
# adj = adjList.AdjacencyList(10000)
V = int(sys.argv[1])
adj = adjList.AdjacencyList(V)
# adj.addEdge(0,1)
# adj.addEdge(2,3)
# adj.addEdge(2,1)
# adj.completeBuild()
# adj.cycleBuild()
print(time.time()-startTime)
# adj.randomUniformBuild(1500)
# adj.randomSkewedBuild(200000)
# adj.randomPersonalBuild(200000)
# adj.randomSkewedBuild(40000)
# distGraph('uniform.out',adj)
# adj.save('test.poo') # deprecated, has issues with file size 3k complete = 150mb where new = 18mb
# with open('test.poo', 'rb') as file:
#     adj1 = pickle.load(file) # new save and load procedure
# adj.randomPersonalBuild(1000)
# deg = degList.degreeList(adj)
# deg.printList()
# print(smallestLastVertOrder(adj, deg))
# adj.serialize('test.poo')
# adj1 = adjList.AdjacencyList.deserialize('test.poo')
# adj.printList()
# print(id(adj.vertices[deg.degrees[0].id]))
# print(id(deg.degrees[0]))
# orderingTemp = ordering.smallestLastVertOrdser(adj, deg)
# orderingTemp1 = ordering.smallestOriginalVertOrder(deg)
# orderingTemp2 = ordering.uniformRandomVertOrder(adj)
# print(orderingTemp2)
# coloring.greedyColoring(adj, orderingTemp2)
# temp = []
# for i in adj.vertices:
#     temp.append(i.id)
# print(temp)
# adj.printList()
# adj.printList()
# print(ordering.smallestLastVertOrder(adj, deg))
# deg.printList()
# adj1.printList()
# adj1.printList()
# deg.printList()
# V = sys.argv[1]
# E = sys.argv[2]
# G = sys.argv[3]
# DIST = sys.argv[4]