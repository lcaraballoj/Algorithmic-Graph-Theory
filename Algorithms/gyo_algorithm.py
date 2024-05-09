# --------
# GYO algorithm (Graham's algorithm) is an algorithm that finds if a hypergraph is alpha-acyclic or not
# --------

import copy

def gyo(hypergraph):
    # Run elimination and then reduction with hypergraph from elimination function
    ORIGINAL = copy.deepcopy(hypergraph)

    hyperedges = []
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)

    reduction(hypergraph, hyperedges)

    # Keep repeating until you get the empty hypergraph or the hypergraph remains unchanged
    if bool(hypergraph) == False:
        return True
    elif ORIGINAL == hypergraph:
        return False
    else:
        return gyo(hypergraph)

def elimination(hypergraph):
    # Elimination of vertices that exist in one hyperedge
    count = 0

    hyperedges = []
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)

    list_vertices = [] 
    for i in range(0, len(hyperedges)):
        list_vertices = list(set(hyperedges[i] + list_vertices))

    
    for i in range(0, len(list_vertices)):
        # Elimination of vertices that appear in one edge
        vertex = list_vertices[i]
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                count += 1

        if count == 1:
            for edges, vertices in hypergraph.items():
                if vertex in vertices:
                    vertices.remove(vertex)
                    
        count = 0

    return hypergraph

def delete_hyperedge(hypergraph, hyperedge):
    edges = []
    for edge, vertices in dict(hypergraph).items():
        if vertices == hyperedge:
            edges.append(edge)

    del hypergraph[edges[0]]

    return hypergraph

def reduction(hypergraph, hyperedges):
    # Reduce hypergraph by removing nested hyperedges
    nested = []
    for i in range(len(hyperedges)):
        for j in range(len(hyperedges)):
            # Check if hyperedges are nested
            if i!= j and set(hyperedges[i]) <= set(hyperedges[j]):
                nested.append(hyperedges[i])
            elif not hyperedges[i]:
                delete_hyperedge(hypergraph, hyperedges[i])

    if len(nested) != 0:
        delete_hyperedge(hypergraph, nested[0])

    return elimination(hypergraph)