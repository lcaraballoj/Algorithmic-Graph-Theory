# -------
# Testing the GYO algorithm 
# The GYO algorithm detects whether or not a graph is aplpha-acyclic
# -------

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import hypernetx as hnx
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
from cycler import cycler

# Import GYO algorithm
from GrahamsAlgorithm import GYO
# Import test graphs
from TestGraphs import *

# Get number of hyperedges
print("How many hyperedges?")
numHyperedges = int(input())

H = {}

for i in range (1, numHyperedges+1):
    print("List the vertices in hyperedge, e{} \n \
    i.e. 1, 2, 3, 4, etc.".format(i))
    vertices = input().replace(" ", "")
    H['e{}'.format(i)] = vertices.split(',')

scenes = H

hypergraph = hnx.Hypergraph(scenes)

kwargs = {'layout_kwargs': {'seed': 0}, 'with_node_counts': False, 'with_edge_labels': True}

hnx.drawing.draw(hypergraph,
    node_labels_kwargs={
        'fontsize': 24
    },
    edge_labels_kwargs={
        'fontsize': 36
    },
    edges_kwargs={
        'linewidths': 4
    },
    **kwargs
)

print(H)

# Check if graph is alpha-acyclic, False means that it is empty which correleates to alpha acyclicity
if bool(GYO(H)) == False:
    print("Alpha acyclic")
else:
    print("Not alpha acyclic")

plt.show()