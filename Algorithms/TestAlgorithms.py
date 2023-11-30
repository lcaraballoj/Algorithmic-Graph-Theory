# Import GYO algorithm
from GrahamsAlgorithm import GYO

# Import test graphs
from TestGraphs import *

# Testing the GYO algorithm 
# The GYO algorithm detects whether or not a graph is aplpha-acyclic
graphs = [hyper_graph, alphaCyclic, square_conformal, gammaTriangle, triangle, tetraedron, alphaAcyclic, betaAcyclic] # List of hypergraphs
ans = [] # Array for the answer 
# Should be ans = [True, True, False, False, True]

# # Loop through all test hypergraphs
# for i in range (0, len(graphs)):
#     print(graphs[i]()) # Print hypergraph
#     # Check if graphs is alpha-acyclic, False means that it is empty which correleates to alpha acyclicity
#     if bool(GYO(graphs[i](), graphs[i]())) == False:
#         print("Alpha acyclic")
#         ans.append(True)
#     else:
#         print("Not alpha acyclic")
#         ans.append(False)


i=3

print(graphs[i]()) # Print hypergraph
# Check if graphs is alpha-acyclic, False means that it is empty which correleates to alpha acyclicity
if bool(GYO(graphs[i](), graphs[i]())) == False:
    print("Alpha acyclic")
    ans.append(True)
else:
    print("Not alpha acyclic")
    ans.append(False)

print("Result: ", ans) # Print answer