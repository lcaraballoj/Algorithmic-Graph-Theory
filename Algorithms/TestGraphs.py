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
   
    # # Print the hypergraph
    # print("Original Hypergraph:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

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
   
    # # Print the hypergraph
    # print("Original Hypergraph:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

    return hypergraph

# # Hypergaph with one edge, alpha acyclic
# def test():
#     hypergraph = {
#         "e1": [1, 2, 3]
#     }

#     # # Print the hypergraph
#     # print("Original Hypergraph:")
#     # for edge, vertices in hypergraph.items():
#     #     print(f"{edge}: {vertices}")

#     return hypergraph

# Square conformal graph, not alpha acyclic
def square_conformal():
    hypergraph = {
        "e1": [1, 2],
        "e2": [1, 3],
        "e3": [2, 4],
        "e4": [3, 4]
    }

    # # Print the hypergraph
    # print("Original Hypergraph:")
    # for edge, vertices in hypergraph.items():
    #     print(f"{edge}: {vertices}")

    return hypergraph

# Gamma Triangle
def gammaTriangle():
    hypergraph = {
        "e1": [1, 2, 3],
        "e2": [1, 2],
        "e3": [1, 3]
    }

    return hypergraph

# Triangle Graph
def triangle():
    hypergraph = {
        "e1": [1, 2],
        "e2": [1, 3],
        "e3": [2, 3]
    }

    return hypergraph

# Tetraedron Graph
def tetraedron():
    hypergraph = {
        "e1": [1, 2, 3],
        "e2": [1, 3, 4],
        "e3": [1, 4],
        "e4": [2, 3]
    }

    return hypergraph

# Alpha Acyclic
def alphaAcyclic():
    hypergraph = {
        "e1": [1, 2, 3, 4],
        "e2": [5, 6, 3, 7],
        "e3": [7, 8, 9, 10],
        "e4": [3, 4, 7]
    }

    return hypergraph

# Beta Acyclic
def betaAcyclic():
    hypergraph = {
        "e1": [1, 2, 3],
        "e2": [3, 4, 5],
        "e3": [2, 3, 5, 6, 7]
    }
    
    return hypergraph

def betaTraingle():
    hypergraph = {
        'e1': [1,2,3],
        'e2': [1,2],
        'e3': [1,3],
        'e4': [2,3]
    }

    return hypergraph