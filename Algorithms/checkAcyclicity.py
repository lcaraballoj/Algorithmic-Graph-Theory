# -------
# Choose which type of acyclciity to use and check it
# -------

import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx
import hypernetx as hnx
from networkx.drawing.nx_pydot import graphviz_layout

# Import GYO algorithm
from grahamsAlgorithm import GYO
# Import betaAcyclic algorithm
from betaAcyclic import checkBetaAcyclic
# Import test graphs
from testGraphs import *

# Choose type of acyclicity
print("What type of acyclicity: \n 1: Alpha \n 2: Beta")
acyclicity = int(input())

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
if acyclicity == 1:
    GYO(H)
else: 
    checkBetaAcyclic(H)

plt.show()