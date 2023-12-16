# --------
# GYO algorithm (Graham's algorithm) is an algorithm that finds if a hypergraph is alpha-acyclic or not
# --------

import copy # Used to ensure a deep copy where inner lists are also copied

def GYO(hypergraph):
    ORIGINAL = copy.deepcopy(hypergraph)

    # Run elimination and then reduction with hypergraph from elimination function
    elimination(hypergraph)
    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)

    reduction(hypergraph, verticesEdges)

    # List of vertices
    nodes = [] 
    for i in range(0, len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    # print('ORG: ', ORIGINAL)
    # print('New: ', hypergraph)

    # Recursion
    if bool(hypergraph) == False:
        # print("Alpha Acyclic")
        return True
    elif ORIGINAL == hypergraph:
        # print("Not Alpha Acyclic")
        return False
    else:
        return GYO(hypergraph)


# Elimination
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

    # print("Elimination:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)

    return hypergraph


# Reduction
def reduction(hypergraph, verticesEdges):
    for i in range(len(verticesEdges)):
        for j in range(len(verticesEdges)):
            if i!= j and set(verticesEdges[i]) <= set(verticesEdges[j]):
                deleteEdge(hypergraph, verticesEdges[i])
            elif not verticesEdges[i]:
                deleteEdge(hypergraph, verticesEdges[i])

    # Print new hypergraph
    # print("Reduction:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

    return hypergraph

# Delete Edge
def deleteEdge(hypergraph, vertexEdge):
    for edge, vertices in dict(hypergraph).items():
        if vertices == vertexEdge:
            del hypergraph[edge]

    return hypergraph