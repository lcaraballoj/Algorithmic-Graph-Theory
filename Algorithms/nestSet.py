import itertools, copy

from betaAcyclic import deleteEmptyEdge

# Find all possible nest sets
def getSet(hypergraph, size):
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
    count = 0
    for i in range(len(listSets)-1):
        if set(listSets[i]) <= set(listSets[i+1]) or set(listSets[i]) >= set(listSets[i+1]):
            count += 1
        
    if count == (len(listSets) - 1):
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

# hypergraph = {"e0": [1, 2, 3, 4, 5, 6, 7, 8], "e1": [1, 2, 3, 4, 5, 6], "e2": [2, 7, 8], "e3": [5, 8]}
# initial_history = [{'hypergraph': hypergraph, 'nestSets': getSet(hypergraph, 2)}]

# easy(hypergraph, initial_history)
