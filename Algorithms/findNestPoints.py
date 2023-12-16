from mergeSort import mergeSortDict
from betaAcyclic import checkNested

# Find the nest points
def findNestPoint(hypergraph):
    #print("\nFINDING NEST POINTS")
    nestPoints = []
    verticesEdges = []
    
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)
        
    #print("Vertices Edges: ", verticesEdges)
        
    # List of vertices
    nodes = [] 
    for i in range(len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    #print("NODES: ", nodes)

    # Check nest point
    for i in range(len(nodes)):
        edgeLength = {}
        #print("NODE: ", nodes[i])
        for j in range(len(verticesEdges)):
            if nodes[i] in verticesEdges[j]:
                #listOfEdges.append(verticesEdges[j])
                #print("Node in: ", verticesEdges[j])
                edgeLength[j] = len(verticesEdges[j])
        #print("Edge Dict: ", edgeLength)
        # print("Sorted: ", merge_sort(edgeLength))

        sort = mergeSortDict(edgeLength)

        #print("Unsrt: ", edgeLength)
        #print("Srt:", sort)

        # If node is a nest point then remove it from H
        if checkNested(sort, verticesEdges) == True:
            #print("REMOVE: ", nodes[i])
            nestPoints.append(nodes[i])
            # Remove vertex
            for edges, vertices in hypergraph.items():
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])

    print("Nest Points: ", nestPoints)

findNestPoint({'e0': [3, 2, 6, 1, 4], 'e1': [2, 3], 'e2': [5, 4, 6, 2, 1], 'e3': [4, 6, 1, 5], 'e4': [4, 5]})
findNestPoint({'e0': [1, 6, 2, 4, 3], 'e1': [6, 5], 'e2': [2, 1, 5, 6, 4], 'e3': [3, 4], 'e4': [5, 4, 6]})
findNestPoint({
    'e1': ['a','b','c','d'],
    'e2': ['a','d','e'],
    'e3': ['d','c','f'],
    'e4': ['b','e'],
    'e5': ['c','f']
})
findNestPoint({
    'e1': ['a', 'b', 'c', 'd', 'e', 'f'],
    'e2': ['d', 'g', 'h'],
    'e3': ['h', 'l', 'm', 'n'],
    'e4': ['f', 'j', 'l'],
    'e5': ['d', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l']
})
