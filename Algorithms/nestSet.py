# --------
# Checks if a hypergraph has a nest-set of a specified size (Thus it also check for beta acyclicity)
# --------

import itertools, copy

from betaAcyclic import deleteEmptyEdge
from findNestPoints import *

def neo(hypergraph, size):
    ORIGINAL = copy.deepcopy(hypergraph)

    getSet(hypergraph, size)

    print('new: ', hypergraph)
    print('ORIGINAL: ', ORIGINAL)

    if bool(hypergraph) == False:
        return True
    elif ORIGINAL == hypergraph:
        return False 
    else:
        return neo(hypergraph, size)

def getSet(hypergraph, size):
    # Find all possible nest sets
    hyperedges = []
    
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)
        
    nodes = [] 
    for i in range(len(hyperedges)):
        nodes = list(set(hyperedges[i] + nodes))

    listSets = []
    for i in range(1, size + 1):
        subListSets = [list(x) for x in itertools.combinations(nodes, i)]
        listSets.extend(subListSets)

    if not listSets:
        return deleteEmptyEdge(hypergraph)
    else:
        return removeVertices(hypergraph, isNestSet(listSets, hyperedges))
    
def isNestSet(listSets, hyperedges):
    # Determine if a set is a nest set
    nestSets = []

    for i in range(len(listSets)):
        set = listSets[i]
        I = [] # Set of incident edges
        for edge in hyperedges:
            if any(i in edge for i in set) and edge not in I:
                I.append(edge)
        # print(I)
        for vertex in set:
            IReduced = [[node for node in edge if node != vertex] for edge in I]
            I = IReduced
        if linearlyOrdered(I):
            nestSets.append(set)

    if not nestSets:
        return nestSets
    else:
        return nestSets[0]

def linearlyOrdered(listSets):
    # Checks if a list of sets is linearly ordered
    listSets.sort(key = len)
    count = 0
    for i in range(len(listSets)-1):
        if set(listSets[i]) <= set(listSets[i+1]) or set(listSets[i]) >= set(listSets[i+1]):
            count += 1
        
    if count == (len(listSets)-1):
        return True
    else: 
        return False
        
def removeVertices(hypergraph, setVertices):
    for vertex in setVertices:
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                vertices.remove(vertex)

    return hypergraph