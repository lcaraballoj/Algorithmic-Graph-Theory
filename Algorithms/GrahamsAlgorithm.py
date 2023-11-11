# GYO algorithm (Graham's algorithm) is an algorithm that finds if a hypergraph is alpha-acyclic or not
def GYO(hypergraph):
    # Vertices in Edges
    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)

    # Run elimination and then reduction with hypergraph from elimination function
    newHypergraph = reduction(elimination(hypergraph, verticesEdges), verticesEdges)

    # Recursion
    if bool(hypergraph) == False: 
        print("Empty!")
    # elif original == newHypergraph:
    #     print("DONE!")
    else:
        GYO(newHypergraph)


# Elimination
def elimination(hypergraph, verticesEdges):
    # Set count
    count = 0

    # List of vertices
    nodes = [] 
    for i in range(0, len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    # Start elimination of vertices that appear only in one edge
    for i in range(0, len(nodes)):
        vertex = nodes[i]
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                count += 1

        if count == 1:
            for edges, vertices in hypergraph.items():
                if vertex in vertices:
                    vertices.remove(vertex)

        count = 0

    print("Elimination:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph


# Reduction
def reduction(hypergraph, verticesEdges):
    for i in range(len(verticesEdges)):
        for j in range(len(verticesEdges)):
            print("Hypergraph: ", hypergraph)
            if i!= j and set(verticesEdges[i]) <= set(verticesEdges[j]):
                deleteEdge(hypergraph, verticesEdges[i])
            elif not verticesEdges[i]:
                deleteEdge(hypergraph, verticesEdges[i])

    # Print new hypergraph
    print("Reduction:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

# Delete Edge
def deleteEdge(hypergraph, vertexEdge):
    for edge, vertices in dict(hypergraph).items():
        if vertices == vertexEdge:
            print("Deleting: ", hypergraph[edge])
            del hypergraph[edge]

# Test hypergraph
def hyper_graph():
    # Define a hypergraph
    hypergraph = {
        "e1": [1, 2, 3, 4, 5],
        "e2": [4, 5, 6, 7, 8, 9, 10],
        "e3": [4, 5, 6, 11, 12, 13, 17],
        "e4": [9, 10, 14, 15, 16, 18],
        "e5": [15, 16, 18]
    }
   
    # Print the hypergraph
    print("Original Hypergraph:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

# Example of an alpha acyclic hypergraph
def alphaCyclic():
    # Define a hypergraph
    hypergraph = {
        "e1": [1, 2, 3],
        "e2": [1, 2],
        "e3": [1, 3],
        "e4": [2, 3]
    }
   
    # Print the hypergraph
    print("Original Hypergraph:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

# Hypergaph with one edge, alpha acyclic
def test():
    hypergraph = {
        "e1": [1, 2, 3]
    }

    # Print the hypergraph
    print("Original Hypergraph:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

# Square conformal graph, not alpha acyclic
def square_conformal():
    hypergraph = {
        "e1": [1, 2],
        "e2": [1, 3],
        "e3": [2, 4],
        "e4": [3, 4]
    }

    # Print the hypergraph
    print("Original Hypergraph:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

GYO(alphaCyclic())

