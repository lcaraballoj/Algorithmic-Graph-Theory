# --------
# Algorithm to determine if a graph is beta-acyclic
# 1. Remove vertices that exist in one hyperedge
# 2. Find nest points and remove them
# 3. Remove empty edges
# 4. Repeat until hypergraph is empty or is unchanged
# --------

import copy

def check_beta_acyclic(hypergraph):
    ORIGINAL = copy.deepcopy(hypergraph)

    find_nest_point(hypergraph)

    # Keep repeating until you get the empty hypergraph or hypergraph remains unchanged
    if bool(hypergraph) == False:
        return True
    elif ORIGINAL == hypergraph:
        return False 
    else:
        return check_beta_acyclic(hypergraph)

def find_nest_point(hypergraph):
    # Find the nest points
    hyperedges = []
    
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)
        
    nodes = [] 
    for i in range(len(hyperedges)):
        nodes = list(set(hyperedges[i] + nodes))

    for i in range(len(nodes)):
        edge_length = {}
        for j in range(len(hyperedges)):
            if nodes[i] in hyperedges[j]:
                edge_length[j] = len(hyperedges[j])

        sort = dict(sorted(edge_length.items(), key=lambda item: item[1]))

        if check_nested(sort, hyperedges) == True:
            # If node is a nest point then remove it from H
            for edges, vertices in hypergraph.items():
                # Remove node (vertex)
                if nodes[i] in vertices:
                    vertices.remove(nodes[i])
            break

    return delete_empty_edge(hypergraph)

def check_nested(dict, list_edges):
    # Check if a list of lists is nested
    count = 0

    dictKeys = list(dict.keys())
    edgeIndex = []
    for i in range(0, len(dictKeys)):
        edgeIndex.append(dictKeys[i])
        
    for i in range(len(dictKeys)-1):
        # Check if one edge is in another
        if set(list_edges[edgeIndex[i]]) <= set(list_edges[edgeIndex[i+1]]) or set(list_edges[edgeIndex[i]]) >= set(list_edges[edgeIndex[i+1]]):
            count += 1
    if count == (len(edgeIndex) - 1):
        return True
    else: 
        return False

def delete_empty_edge(hypergraph):
    # Check if edge is empty
    for edges, vertices in dict(hypergraph).items():
        if len(vertices) == 0:
            del hypergraph[edges]

    return hypergraph