# --------
# GYO algorithm (Graham's algorithm) is an algorithm that finds if a hypergraph is alpha-acyclic or not
# --------

import copy

def GYO(hypergraph):
    ORIGINAL = copy.deepcopy(hypergraph)

    # Run elimination and then reduction with hypergraph from elimination function
    elimination(hypergraph)

    # print('ORG: ', ORIGINAL)
    # print('New: ', hypergraph)

    # Keep repeating until you get the empty hypergraph or the hypergraph remains unchanged
    if bool(hypergraph) == False:
        # print("Alpha Acyclic")
        return True
    elif ORIGINAL == hypergraph:
        # print("Not Alpha Acyclic")
        return False
    else:
        return GYO(hypergraph)

def elimination(hypergraph):
    # Elimination of vertices that are only in one hyperedge
    count = 0

    hyperedges = []
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)

    listVertices = [] 
    for i in range(0, len(hyperedges)):
        listVertices = list(set(hyperedges[i] + listVertices))
    
    #print("listVertices: ", listVertices)

    # Start elimination of vertices that appear only in one edge
    for i in range(0, len(listVertices)):
        vertex = listVertices[i]
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

    # print("Elimination:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

    hyperedges = []
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)

    return reduction(hypergraph, hyperedges)

def reduction(hypergraph, hyperedges):
    # Reduce hypergraph by removing nested hyperedges
    for i in range(len(hyperedges)):
        for j in range(len(hyperedges)):
            # Check if hyperedges are nested
            if i!= j and set(hyperedges[i]) <= set(hyperedges[j]):
                deleteHyperedge(hypergraph, hyperedges[i])
            elif not hyperedges[i]:
                deleteHyperedge(hypergraph, hyperedges[i])

    # # Print new hypergraph
    # print("Reduction:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

    return hypergraph

def deleteHyperedge(hypergraph, hyperedge):
    for edge, vertices in dict(hypergraph).items():
        if vertices == hyperedge:
            del hypergraph[edge]

    return hypergraph

print(GYO({"e0": [1, 3, 4, 5], "e1": [3, 5], "e2": [1, 2], "e3": [4, 5]}))