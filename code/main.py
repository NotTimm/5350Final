import pickle, sys, time
import adjList, degList, coloring, ordering

def distGraph(path, adj):
    # with open(path) as file:
    print("vertID, degree")
    for vert in adj.vertices:
        print(str(vert.id) + ', ' + str(vert.degree))
        # file.write(vert.id,',',vert.degree,'\n')

startTime = time.time()
sys.setrecursionlimit(10000)
# adj = adjList.AdjacencyList(10000)
V = int(sys.argv[1])
adj = adjList.AdjacencyList.deserialize('graphDumps/squared.adj')
# adj.completeBuild()
# adj.cycleBuild()
# adj.randomUniformBuild(100000)
# adj.randomPersonalBuild(200000)
# adj.randomSkewedBuild(40000)
deg = degList.degreeList(adj)
# adj.printList()
if V == 1:
    coloring.UROColoring(adj)
elif V == 2:
    coloring.SOVOFColoring(adj,deg)
elif V == 3:
    coloring.SLVOColoing(adj,deg)
else:
    coloring.SOVOColoring(adj,deg)
temp = []
for i in adj.vertices:
    temp.append(i.color)
print(max(temp)+1)
# adj.printList()
# adj1.printList()
# deg.printList()