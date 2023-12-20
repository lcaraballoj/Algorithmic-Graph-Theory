# --------
# Generate random hypergraphs
# --------

import random, copy
from testGraphs import *
from betaAcyclic import checkBetaAcyclic
from grahamsAlgorithm import GYO

def generate_random_hypergraph(numVertices, numHyperedges, edgeSize):
    if numVertices <= 0 or numHyperedges <= 0 or len(edgeSize) != numHyperedges:
        raise ValueError("Inputs must be positive integers")

    vertices = set(range(1, numVertices + 1))
    hyperedges = []

    for size in edgeSize:
        verticesInEdge = random.sample(vertices, size)
        hyperedges.append(verticesInEdge)

    return hyperedges

import random

def generate_specific_hypergraph(numVertices, numHyperedges, edgeSizes):
    if numVertices <= 0 or numHyperedges <= 0 or sum(edgeSizes) != numVertices:
        raise ValueError("Invalid inputs")

    vertices = set(range(1, numVertices + 1))
    hyperedges = []

    for size in edgeSizes:
        if size > len(vertices):
            raise ValueError("Edge size exceeds available vertices")

        verticesInEdge = random.sample(vertices, size)
        hyperedges.append(verticesInEdge)
        vertices.difference_update(verticesInEdge)

    # Check if the hypergraph has the desired number of hyperedges
    if len(hyperedges) != numHyperedges:
        raise ValueError("Could not generate specified number of hyperedges")

    return hyperedges

# Remove duplicate hypergraph
def remove_outer_duplicates(list_of_lists_of_lists):
    seen = set()
    unique_elements = []

    for element in list_of_lists_of_lists:
        # Convert inner lists to sets to disregard the order of elements
        element_sets = {frozenset(sublist) for sublist in element}

        # Check if the set representation of the element is already seen
        if tuple(element_sets) not in seen:
            unique_elements.append(element)
            seen.add(tuple(element_sets))

    return unique_elements

# # Example usage:
# num_vertices = 6
# min_vertices = 2
# num_hyperedges = 5
# max_vertices_per_edge = 5

# hypergraphs = []

# for i in range(30):
#     random_hypergraph = generate_random_hypergraph(num_vertices, num_hyperedges, min_vertices, max_vertices_per_edge)
#     hypergraphs.append(random_hypergraph)

# # print('Hypergraph: ', *hypergraphs, sep='\n')

# noDup = remove_outer_duplicates(hypergraphs)

# cleanList = [x for x in noDup if len(x)==num_hyperedges]

# listDict = []

# for i in range(len(cleanList)):
#     hypergraphDict = {}
#     for j in range(len(cleanList[i])):
#         hypergraphDict['e{}'.format(j)] = cleanList[i][j]

#     listDict.append(hypergraphDict)

# # Check Acyclicity 
    
# alpha = []
# beta = []
# for i in range(len(listDict)):
#     hypergraph = copy.deepcopy(listDict[i])
#     alpha.append(GYO(listDict[i]))
#     beta.append(checkBetaAcyclic(hypergraph))


# print(alpha)
# print(beta)