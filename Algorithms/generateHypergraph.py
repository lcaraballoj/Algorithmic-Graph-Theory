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

# Check if hypergraph is connected
def is_connected(hyperedges, numVertices):
    # Create a set containing all vertices
    all_vertices = set(range(1, numVertices + 1))

    # Traverse hyperedges and merge vertices to find connected components
    connected_vertices = set()
    for edge in hyperedges:
        connected_vertices.update(edge)

    return connected_vertices == all_vertices

# Remove duplicate hypergraph
def remove_outer_duplicates(list_of_lists_of_lists):
    seen = set()
    uniqueHypergraphs = []

    for element in list_of_lists_of_lists:
        # Convert inner lists to sets to disregard the order of elements
        element_sets = {frozenset(sublist) for sublist in element}

        # Check if the set representation of the element is already seen
        if tuple(element_sets) not in seen:
            uniqueHypergraphs.append(element)
            seen.add(tuple(element_sets))

    return remove_duplicate_edge(uniqueHypergraphs)

# Remove hypergraphs where there is an edge repeated
def remove_duplicate_edge(listHypergraphs):
    unique = []

    for sublist in listHypergraphs:
        # Convert each sublist to a set to remove duplicate elements
        unique_sublist = [list(set(inner_list)) for inner_list in sublist]

        # Check if there are any duplicates in the sublist
        if len(unique_sublist) == len(set(tuple(sub) for sub in unique_sublist)):
            # Add the unique sublist to the result
            unique.append(sublist)

    return unique