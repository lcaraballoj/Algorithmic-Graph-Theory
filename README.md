# Algorithmic-Graph-Theory
This repository is a collection of Jupyter Notebooks and Python code created throughout my masters degree. It highlights topics in graph theory and database theory, and their intersection. The main focus is on hypergraphs, specifically hypergraphs that are alpha-acyclic and beta-acyclic. The main question of my thesis is, how can we further evaluate and understand nest-set width which is a novel generalization of beta-acyclicity.

# Table of Contents
1. [Algorithms](#algorithms)
2. [Jupyter Notebooks](#jupyter-notebooks)

# Algorithms
## gyo_algorithm.py
This algorithm is the GYO algorithm (Mark Graham, Yu and Ozsoyoglu 1979). This algorithm is used to determine if a hypergraph is alpha-acyclic and depends on two operations: reduction and elimination.

## nest_point_elim.py 
This algorithm follows nest-point elimination orderings which is used to determine if a hypergraph is beta-acyclic. This algorithm depends on nest-points which are vertices whose set of incident hyperedges are linearly ordered.

## find_nest_points.py
This algorithm finds any nest-points in a hypergraph. 

## find_nest_sets.py
This algorithm finds any nest-sets in a hypergraph of a specified size. A nest-set is a generalization of nest-points, but we want the reduced set of incident hyperedges, the set of incident hyperedges with vertices in the set removed, to be linearly ordered.

## generate_hypergraphs.py
This code is used to generate a certain number of hypergraphs with certain conditions. It requires specification of the number of vertices, number of hyperedges, and the size of each hyperedge. These hypergraphs will be unique and will not have repeated hyperedges.

## check_isomorphism.py
THis code is used to check if two hypergraphs are isomorphic. It utilizes the Hypernetx library to get the bipartite graph of the hypergraphs and then uses the Networkx library to see if the bipartite graphs are isomorphic.


# Jupyter Notebooks
