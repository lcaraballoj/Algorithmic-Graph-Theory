# --------
# Algorithm to determine if a graph is beta-acyclic
# 1. Remove vertices that exist in one hyperedge
# 2. Find nest points and remove them
# 3. Remove empty edges
# 4. Repeat until hypergraph is empty or is unchanged
# --------

import copy

from testGraphs import *

# Check if beta acyclic
def checkBetaAcyclic(hypergraph):
    ORIGINAL = copy.deepcopy(hypergraph)

    elimination(hypergraph)

    findNestPoint(hypergraph)

    if bool(hypergraph) == False:
        return True
    elif ORIGINAL == hypergraph:
        return False 
    else:
        return checkBetaAcyclic(hypergraph)

def elimination(hypergraph):
    # Delete vertices that exist only in one edge
    count = 0

    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)

    # List of vertices
    nodes = [] 
    for i in range(0, len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))
    
    for i in range(0, len(nodes)):
        # Start elimination of vertices that appear only in one edge
        vertex = nodes[i]
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                count += 1

        if count == 1:
            for edges, vertices in hypergraph.items():
                if vertex in vertices:
                    vertices.remove(vertex)

        count = 0

    return hypergraph

def findNestPoint(hypergraph):
    # Find the nest points
    hyperedges = []
    
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)
        
    nodes = [] 
    for i in range(len(hyperedges)):
        nodes = list(set(hyperedges[i] + nodes))

    for i in range(len(nodes)):
        edgeLength = {}
        for j in range(len(hyperedges)):
            if nodes[i] in hyperedges[j]:
                edgeLength[j] = len(hyperedges[j])

        sort = dict(sorted(edgeLength.items(), key=lambda item: item[1]))

        if checkNested(sort, hyperedges) == True:
            # If node is a nest point then remove it from H
            for edges, vertices in hypergraph.items():
                # Remove node (vertex)
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])
            break

    return deleteEmptyEdge(hypergraph)

def checkNested(dict, listEdges):
    # Check if a list of lists is nested
    count = 0

    dictKeys = list(dict.keys())
    edgeIndex = []
    for i in range(0, len(dictKeys)):
        edgeIndex.append(dictKeys[i])
        
    for i in range(len(dictKeys)-1):
        # Check if one edge is in another
        if set(listEdges[edgeIndex[i]]) <= set(listEdges[edgeIndex[i+1]]) or set(listEdges[edgeIndex[i]]) >= set(listEdges[edgeIndex[i+1]]):
            count += 1
    if count == (len(edgeIndex) - 1):
        return True
    else: 
        return False

def deleteEmptyEdge(hypergraph):
    # Check if edge is empty
    for edges, vertices in dict(hypergraph).items():
        if len(vertices) == 0:
            del hypergraph[edges]

    return hypergraph