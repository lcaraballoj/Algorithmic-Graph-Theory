# --------
# Algorithm to determine if a graph is beta-acyclic
# 1. Remove vertices that exist in one hyperedge
# 2. Find nest points and remove them
# 3. Remove empty edges
# 4. Repeat until hypergraph is empty or is unchanged
# --------

import copy

# Import merge sort and graphs
from mergeSort import mergeSortDict
from testGraphs import *

# Check if beta acyclic
def checkBetaAcyclic(hypergraph):
    #print("\nHYPERGRAPH: ", hypergraph)
    ORIGINAL = copy.deepcopy(hypergraph)
    # print("\nMODIFYING: ", ORIGINAL)

    elimination(hypergraph)

    findNestPoint(hypergraph)
    
    # print("ORG: ", ORIGINAL)
    # print("NEW: ", hypergraph)

    if bool(hypergraph) == False:
        # print("Beta Acyclic")
        return True
    elif ORIGINAL == hypergraph:
        # print("Not Beta Acyclic")
        return False 
    else:
        return checkBetaAcyclic(hypergraph)

# Delete vertices that exist only in one edge
def elimination(hypergraph):
    # Set count
    count = 0

    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)

    # List of vertices
    nodes = [] 
    for i in range(0, len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))
    
    #print("Nodes: ", nodes)

    # Start elimination of vertices that appear only in one edge
    for i in range(0, len(nodes)):
        vertex = nodes[i]
        # print("Vertex: ", vertex)
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                count += 1
        
        #print("Count: ", count)

        if count == 1:
            for edges, vertices in hypergraph.items():
                if vertex in vertices:
                    vertices.remove(vertex)

        count = 0

    return hypergraph

# Find the nest points
def findNestPoint(hypergraph):
    # print("\nFINDING NEST POINTS")
    #nestPoints = []
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
                # listOfEdges.append(verticesEdges[j])
                # print("Node in: ", verticesEdges[j])
                edgeLength[j] = len(verticesEdges[j])

        sort = mergeSortDict(edgeLength)

        # print("Unsrt: ", edgeLength)
        # print("Srt:", sort)

        # If node is a nest point then remove it from H
        if checkNested(sort, verticesEdges) == True:
            # print("REMOVE: ", nodes[i])

            # Remove vertex
            for edges, vertices in hypergraph.items():
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])
            break

    # print("Nest Points: ", nodes[i])

    deleteEmptyEdge(hypergraph)

# Check if a list of lists is nested
def checkNested(dict, listEdges):
    count = 0 # Keept track of nested

    # print("List of Edges:", listEdges)
    dictKeys = list(dict.keys())
    # print("Dictionary Keys: ", dictKeys)
    edgeIndex = []

    # Get list of indexes
    for i in range(0, len(dictKeys)):
        edgeIndex.append(dictKeys[i])

    #print("EDGE INDEX: ", edgeIndex)

    for i in range(len(dictKeys)-1):
        # print("Current: ", listEdges[edgeIndex[i]])
        # print("Next: ", listEdges[edgeIndex[i+1]])
        if set(listEdges[edgeIndex[i]]) <= set(listEdges[edgeIndex[i+1]]) or set(listEdges[edgeIndex[i]]) >= set(listEdges[edgeIndex[i+1]]):
        #if edgeIndex[i].issubset(edgeIndex[i+1]):
            count += 1
            # print("COUNT: ", count)
    if count == (len(edgeIndex) - 1):
        return True
    else: 
        return False

# Check if edge is empty
def deleteEmptyEdge(hypergraph):
    # print("Remove empty edges")
    for edges, vertices in dict(hypergraph).items():
        if len(vertices) == 0:
            del hypergraph[edges]

    return hypergraph