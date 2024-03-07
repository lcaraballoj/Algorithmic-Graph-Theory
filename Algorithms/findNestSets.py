import itertools, copy

from mergeSort import mergeSortDict
from betaAcyclic import check_nested
from nestSetElimination import linearly_ordered

# Find the nest points
def find_nest_point(hypergraph):
    nestPoints = []
    verticesEdges = []
    
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)
        
    # List of vertices
    nodes = [] 
    for i in range(len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    # Check nest point
    for i in range(len(nodes)):
        edgeLength = {}
        for j in range(len(verticesEdges)):
            if nodes[i] in verticesEdges[j]:
                edgeLength[j] = len(verticesEdges[j])

        sort = dict(sorted(edgeLength.items(), key=lambda item: item[1]))

        # If node is a nest point then remove it from H
        if check_nested(sort, verticesEdges) == True:
            nestPoints.append(nodes[i])
            # Remove vertex
            for edges, vertices in hypergraph.items():
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])

    return nestPoints

def get_set(hypergraph, size):
    # Find all possible nest sets
    hyperedges = []
    
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)
        
    nodes = [] 
    for i in range(len(hyperedges)):
        nodes = list(set(hyperedges[i] + nodes))

    list_sets = []
    sub_list_sets = [list(x) for x in itertools.combinations(nodes, size)]
    list_sets.extend(sub_list_sets)

    return is_nest_set(list_sets, hyperedges)
    
def is_nest_set(list_sets, hyperedges):
    # Determine if a set is a nest set
    nestSets = []

    for i in range(len(list_sets)):
        set = list_sets[i]
        I = [] # Set of incident edges
        for edge in hyperedges:
            if any(i in edge for i in set) and edge not in I:
                I.append(edge)
        # print(I)
        for vertex in set:
            IReduced = [[node for node in edge if node != vertex] for edge in I]
            I = IReduced
        if linearly_ordered(I):
            nestSets.append(set)

    # print(nestSets)

    return nestSets