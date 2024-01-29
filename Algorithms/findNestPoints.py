from mergeSort import mergeSortDict
from betaAcyclic import checkNested

# Find the nest points
def findNestPoint(hypergraph):
    #print("\nFINDING NEST POINTS")
    nestPoints = []
    verticesEdges = []
    
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)
        
    # print("Vertices Edges: ", verticesEdges)
        
    # List of vertices
    nodes = [] 
    for i in range(len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    # print("NODES: ", nodes)

    # Check nest point
    for i in range(len(nodes)):
        edgeLength = {}
        # print("NODE: ", nodes[i])
        for j in range(len(verticesEdges)):
            if nodes[i] in verticesEdges[j]:
                #listOfEdges.append(verticesEdges[j])
                # print("Node in: ", verticesEdges[j])
                edgeLength[j] = len(verticesEdges[j])
        # print("Edge Dict: ", edgeLength)
        # print("Sorted: ", merge_sort(edgeLength))

        sort = dict(sorted(edgeLength.items(), key=lambda item: item[1]))

        # print("Unsrt: ", edgeLength)
        # print("Srt:", sort)

        # If node is a nest point then remove it from H
        if checkNested(sort, verticesEdges) == True:
            #print("REMOVE: ", nodes[i])
            nestPoints.append(nodes[i])
            # Remove vertex
            for edges, vertices in hypergraph.items():
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])

    # print("Nest Points: ", nestPoints)
    return nestPoints