# --------
# Find Isomorphic Hypergraphs
# Using the fact that the incidence graphs of hypergraphs are isomorphic iff the hypergraphs themselves are isomorphic
# --------
import networkx as nx
import hypernetx as hnx

import hypernetx as hnx

# ---------
# Check Isomorphism
def are_isomorphic(hypergraph1, hypergraph2):
    # Convert hypergraphs to graphs for comparison
    G1 = hnx.Hypergraph(hypergraph1).bipartite()
    G2 = hnx.Hypergraph(hypergraph2).bipartite()

    isomorphic = nx.is_isomorphic(G1, G2)

    return isomorphic

# --------
# Loop through all hypergraphs removing isomorphic ones
def checkList(hypergraphs):
    representatives = []
    seen_classes = set()

    for hg in hypergraphs:
        isomorphic_class = None

        for rep in representatives:
            if are_isomorphic(hg, rep):
                isomorphic_class = rep
                break

        if isomorphic_class is None:
            representatives.append(hg)
            seen_classes.add(tuple(hg))

    return representatives