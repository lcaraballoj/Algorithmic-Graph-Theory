# Algorithmic-Graph-Theory
This repository is a collection of Jupyter Notebooks and Python code created throughout my masters degree. It highlights topics in graph theory and database theory, and their intersection. The main focus is on hypergraphs, specifically hypergraphs that are alpha-acyclic and beta-acyclic. The main question of my thesis is, how can we further evaluate and understand nest-set width which is a novel generalization of beta-acyclicity.

# Table of Contents
1. [Algorithms](#algorithms)
2. [Jupyter Notebooks](#jupyter-notebooks)

# Algorithms
## check_isomorphism.py
This code is used to check if two hypergraphs are isomorphic. It utilizes the Hypernetx library to get the bipartite graph of the hypergraphs and then uses the Networkx library to see if the bipartite graphs are isomorphic.

## find_nest_sets.py
This algorithm finds any nest-sets in a hypergraph of a specified size. A nest-set is a generalization of nest-points, but we want the reduced set of incident hyperedges, the set of incident hyperedges with vertices in the set removed, to be linearly ordered.

## generate_hypergraphs.py
This code is used to generate a certain number of hypergraphs with certain conditions. It requires specification of the number of vertices, number of hyperedges, and the size of each hyperedge. These hypergraphs will be unique and will not have repeated hyperedges.

## gyo_algorithm.py
This algorithm is the GYO algorithm (Mark Graham, Yu and Ozsoyoglu 1979). This algorithm is used to determine if a hypergraph is alpha-acyclic and depends on two operations: reduction and elimination.

## hypergraph_analysis.py

## hypergraph_database.py
This code is used to populate a database. The database schema is shown below.

![Database](https://github.com/lcaraballoj/Algorithmic-Graph-Theory/assets/71469786/e5dc55df-dbde-4a11-aead-475fa8b39a09)

## neo.py
This code is used to find if there is a $k$-nest-set elimination (NEO) ordering where $k$ is any natural number. It follows the definition of a NEO which is a sequence of nest-sets that when deleted will result in the empty hypergraph. It will return true if there is a $k$-NEO and false if there is not one. It works independently of find_nest_sets.py because it does not list the nest-sets.

## nest_point_elim.py 
This algorithm follows nest-point elimination orderings which is used to determine if a hypergraph is beta-acyclic. This algorithm depends on nest-points which are vertices whose set of incident hyperedges are linearly ordered.

## test_graphs_*.py
This code has hypergraphs that can be used for testing.

# Jupyter Notebooks
