# GYO algorithm (Graham's algorithm) is an algorithm that finds if a hypergraph is alpha-acyclic or not
def GYO(hypergraph):
    original = hypergraph 

    # Vertices in Edges
    verticesEdges = []
    for edges, vertices in hypergraph.items():
        verticesEdges.append(vertices)

    # Run elimination and then reduction with hypergraph from elimination function
    newHypergraph = reduction(elimination(hypergraph, verticesEdges), verticesEdges)

    # Recursion
    if bool(hypergraph) == False: 
        print("Empty!")
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
            if i == j: 
                print("Equal!")

            elif not verticesEdges[i]:
                for edge, vertices in dict(hypergraph).items():
                    if vertices == verticesEdges[i]:
                        print("Deleting: ", hypergraph[edge])
                        del hypergraph[edge]
            elif set(verticesEdges[i]) <= set(verticesEdges[j]):
                for edge, vertices in dict(hypergraph).items():
                    if vertices == verticesEdges[i]:
                        print("Deleting: ", hypergraph[edge])
                        del hypergraph[edge]

    # Print new hypergraph
    print("Reduction:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

# Function to create Hypergraph
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

def test():
    hypergraph = {
        "e1": [1, 2, 3]
    }

    # Print the hypergraph
    print("Original Hypergraph:")
    for edge, vertices in hypergraph.items():
        print(f"{edge}: {vertices}")

    return hypergraph

GYO(hyper_graph())

