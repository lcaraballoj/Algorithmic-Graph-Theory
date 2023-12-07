# --------
# Algorithm to determine if a graph is beta-acyclic
# --------

# Import merge sort and graphs
from mergeSort import mergeSortDict
from testGraphs import *

# Check if beta acyclic
def checkBetaAcyclic(hypergraph):
    ORIGINAL = hypergraph.copy()
    print("\nMODIFYING: ", ORIGINAL)

    deleteEmptyEdge(findNestPoint(hypergraph))
    
    print("ORG: ", ORIGINAL)
    print("NEW: ", hypergraph)
    

    if ORIGINAL == hypergraph:
        if bool(hypergraph) ==  False:
            print("Beta Acyclic")
        else: 
            print("Not Beta Acyclic")
    else:
        checkBetaAcyclic(hypergraph)

# Find the nest points
def findNestPoint(hypergraph):
    edgeLength = {}
    nestPoints = []

    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)
    print("Vertices Edges: ", verticesEdges)
        
    # List of vertices
    nodes = [] 
    for i in range(0, len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    # Check nest point
    for i in range(0, len(nodes)):
        print("NODE: ", nodes[i])
        for j in range(0, len(verticesEdges)):
            if nodes[i] in verticesEdges[j]:
                #listOfEdges.append(verticesEdges[j])
                edgeLength[j] = len(verticesEdges[j])
        print("Edge Dict: ", edgeLength)
        # print("Sorted: ", merge_sort(edgeLength))

        sort = mergeSortDict(edgeLength)
        print("Unsrt: ", edgeLength)
        print("Srt:", sort)

        # If node is a nest point then remove it from H
        if checkNested(sort, verticesEdges) == True:
            print("REMOVE: ", nodes[i])
            nestPoints.append(nodes[i])
            # Remove vertex
            for edges, vertices in hypergraph.items():
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])

    print("Nest Points: ", nestPoints)

    return hypergraph

# Check if a list of lists is nested
def checkNested(dict, listEdges):
    #print("List of Edges:", listEdges)
    dictKeys = list(dict.keys())
    edgeIndex = []

    # Get list of indexes
    for i in range(0, len(dictKeys)):
        edgeIndex.append(dictKeys[i])

    for i in range(len(dictKeys)-1):
        print("Current: ", listEdges[edgeIndex[i]])
        print("Next: ", listEdges[edgeIndex[i+1]])
        if set(listEdges[edgeIndex[i]]) <= set(listEdges[edgeIndex[i+1]]):
            return True
        else:
            return False

# Check if edge is empty
def deleteEmptyEdge(hypergraph):
    print("Remove empty edges")
    for edges, vertices in dict(hypergraph).items():
        if len(vertices) == 0:
            del hypergraph[edges]

    return hypergraph

# checkBetaAcyclic(square_conformal())

# def emptyHypergraph():
#     hypergraph = {
#         "e1": [1,2,3],
#         "e2": [2,4,5],
#         "e3": [5,6],
#         "e4": []
#     }

#     return hypergraph

#print(deleteEmptyEdge(emptyHypergraph()))