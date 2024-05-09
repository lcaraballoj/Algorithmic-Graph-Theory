# --------
# Check if a hypergraph has a nest-set elimination ordering of a specified size (So it can also be used to check for beta acyclicity)
# --------

import itertools, copy

from nest_point_elim import delete_empty_edge

def neo(hypergraph, size):
    ORIGINAL = copy.deepcopy(hypergraph)

    get_set(hypergraph, size)

    # Keep repeating until you get the empty hypergraph or the hypergraph remains unchanged
    if bool(hypergraph) == False:
        return True
    elif ORIGINAL == hypergraph:
        return False 
    else:
        return neo(hypergraph, size)

def get_set(hypergraph, size):
    # Find all possible nest sets
    hyperedges = []
    
    for edges, vertices in hypergraph.items():
        hyperedges.append(vertices)
        
    nodes = [] 
    for i in range(len(hyperedges)):
        nodes = list(set(hyperedges[i] + nodes))

    list_sets = []
    for i in range(size, 0, -1):
        sub_list_sets = [list(x) for x in itertools.combinations(nodes, i)]
        list_sets.extend(sub_list_sets)

    if not list_sets:
        return delete_empty_edge(hypergraph)
    else:
        return remove_vertices(hypergraph, is_nest_set(list_sets, hyperedges))
    
def is_nest_set(list_sets, hyperedges):
    # Determine if a set is a nest set
    nestSets = []

    for i in range(len(list_sets)):
        set = list_sets[i]
        I = [] # Set of incident edges
        for edge in hyperedges:
            if any(i in edge for i in set) and edge not in I:
                I.append(edge)
                
        for vertex in set:
            IReduced = [[node for node in edge if node != vertex] for edge in I]
            I = IReduced
        if linearly_ordered(I):
            nestSets.append(set)

    if not nestSets:
        return nestSets
    else:
        return nestSets[0]

def linearly_ordered(list_sets):
    # Check a list of sets to see if it is linearly ordered
    list_sets.sort(key = len)
    count = 0
    for i in range(len(list_sets)-1):
        if set(list_sets[i]) <= set(list_sets[i+1]) or set(list_sets[i]) >= set(list_sets[i+1]):
            count += 1
        
    if count == (len(list_sets)-1):
        return True
    else: 
        return False
        
def remove_vertices(hypergraph, set_vertices):
	# Remove vertices that are in a certain nest-set
    for vertex in set_vertices:
        for edges, vertices in hypergraph.items():
            if vertex in vertices:
                vertices.remove(vertex)

    return hypergraph