import itertools, copy

from betaAcyclic import deleteEmptyEdge, checkBetaAcyclic
from findNestPoints import *

# Find all possible nest sets
def getSet(hypergraph, size):
    print(findNestPoint(copy.deepcopy(hypergraph)))
    # List of hyperedges
    verticesEdges = []
    
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)
        
    nodes = [] 
    for i in range(len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    # Get set
    listSets = [list(x) for x in itertools.combinations(nodes, size)]

    return isNestSet(listSets, verticesEdges)
    
# Determine if a set is a nest set
def isNestSet(listSets, verticesEdges):
    nestSets = []

    for i in range(len(listSets)):
        set = listSets[i]
        I = [] # Set of incident edges
        # print(set)
        for edge in verticesEdges:
            if any(i in edge for i in set) and edge not in I:
                I.append(edge)
        # print(I)
        for vertex in set:
            IReduced = [[node for node in edge if node != vertex] for edge in I]
            I = IReduced
            # print(I)
        if linearlyOrdered(I):
            nestSets.append(set)

    # print(nestSets)
    return nestSets

def linearlyOrdered(listSets):
    listSets.sort(key = len)
    # print(listSets)
    count = 0
    for i in range(len(listSets)-1):
        if set(listSets[i]) <= set(listSets[i+1]) or set(listSets[i]) >= set(listSets[i+1]):
            count += 1
            # print('Count: ', count)
        
    if count == (len(listSets)-1):
        return True
    else: 
        return False
        
def removeVertices(hypergraph, setVertices):
    for vertex in setVertices:
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                vertices.remove(vertex)
                
    return deleteEmptyEdge(hypergraph)

# def NEO(ORIGINAL, history, nestSet):
#     ORIGINAL = copy.deepcopy(ORIGINAL)
#     hypergraph = history[-1]['hypergraph']
#     nestSets = history[-1]['nestSets']

#     hypergraph = removeVertices(hypergraph, nestSet)

#     if not bool(hypergraph):
#         return True
#     elif ORIGINAL == hypergraph:
#         return False
#     else:
#         history.append({'hypergraph': hypergraph, 'nestSets': getSet(hypergraph, 2)})
#         return easy(ORIGINAL, history)

# def easy(ORIGINAL, history):
#     print(history[-1]['hypergraph'])
#     nestSets = history[-1]['nestSets']
#     print('NEST SETS: ', nestSets)

#     for i in range(len(nestSets)):
#         current_nest_set = nestSets[i]
#         print(current_nest_set)

#         if history[-1]['hypergraph'] == ORIGINAL:
#             print("NEW: ", ORIGINAL)
#             print(NEO(ORIGINAL, history, current_nest_set))
#         else:
#             print(NEO(ORIGINAL, history, current_nest_set))

hypergraph = {"e0": [2, 3, 4, 5], "e1": [1, 2, 3], "e2": [2, 3, 5], "e3": [1, 4, 5]}
hypergraph1 = removeVertices(copy.deepcopy(hypergraph), [2,3])
hypergraph2 = removeVertices(copy.deepcopy(hypergraph1), [1,4])
hypergraph3 = removeVertices(copy.deepcopy(hypergraph2), [])
# hypergraph4 = removeVertices(copy.deepcopy(hypergraph3), [1,3])
# hypergraph5 = removeVertices(copy.deepcopy(hypergraph4), [2,7])
print('H0 Nest Set: ', getSet(hypergraph, 2))
# print('H1 Nest Set: ', getSet(hypergraph1, 2)) 
# print('H2 Nest Set: ', getSet(hypergraph2, 2))  
# print('H3 Nest Set: ', getSet(hypergraph3, 2)) 
# print('H4 Nest Set: ', getSet(hypergraph4, 2))
# print('H5 Nest Set: ', getSet(hypergraph5, 2))
# print(checkBetaAcyclic(hypergraph))
