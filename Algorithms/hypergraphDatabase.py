# --------
# This code generates randome hypergraphs given specific parameters and then inputs them into a mysql database table
# --------

import copy, json
import hypernetx as hnx
import networkx as nx
import pandas as pd
import mysql.connector

from testGraphs import *
from sqlalchemy import create_engine
from betaAcyclic import checkBetaAcyclic
from generateHypergraph import *
from grahamsAlgorithm import GYO

# Dataframe to hold hypergraph info
df = pd.DataFrame()

# Dataframe for k-NEOs
kDf = pd.DataFrame()

# Specify parameters to generate hypergraphs
num_vertices = 6
min_vertices = 2
num_hyperedges = 4
max_vertices_per_edge = num_vertices

# Hypergraphs that have already been tested
hypergraphs = [
    # [[2, 5, 6, 4, 1],[1, 5],[3, 2, 4, 5],[6, 2, 4, 3],[5, 2, 1]],
    # [[1, 3, 5, 6], [1, 2, 3, 5], [2, 4], [4, 3, 6], [3, 4]],
    # [[2, 3, 4, 5, 6],[1, 3, 6],[2, 4, 5],[1, 2, 5],[1, 2, 4, 6]],
    # [[1, 2, 4], [2, 5], [1, 3, 5, 6],[2, 4, 5],[1, 3, 4]],
    # [[5, 6], [2, 5, 4, 3], [6, 2, 5, 1, 4], [6, 1, 4, 2],[3, 6]],
    # [[3, 6, 5], [5, 4],  [6, 3, 4],[5, 1],  [2, 1, 5, 4]],
    # [[3, 1, 4, 6, 5],[5, 6],[2, 5, 6, 3],[2, 5],[4, 6, 2]],
    # [ [1, 5, 3, 2, 4], [3, 2, 6], [4, 2, 5], [4, 3], [6, 5, 1, 4, 2]],
    # [ [4, 2, 6], [3, 1, 4, 6], [6, 5], [2, 3, 1], [4, 6, 1]],
    # [[6, 5, 3],  [6, 3, 1, 4], [5, 1, 4, 2, 3], [1, 5, 4], [2, 1, 5]],
    # [[1, 3, 4, 5], [3, 6, 2, 1], [3, 5, 4, 6, 1], [3, 4], [3, 5, 2, 4, 6]],
    # [[1, 2, 6, 3, 5, 4], [5, 2, 4], [3, 1, 2, 5], [2, 4, 1, 6, 3], [3, 2, 1]],
    # [[3, 6, 2],[3, 6, 2, 5],[2, 3, 5, 1, 4],[3, 6, 5, 4, 1], [2, 3, 1, 4]],
    # [[5, 2, 4, 1, 3], [6, 5, 1, 2], [4, 1, 2], [1, 3, 4, 6, 2], [5, 4]],
    # [[5, 1], [3, 4], [5, 3, 1, 2, 6], [6, 4, 1],[4, 2, 3, 5]],
    # [[6, 5, 4, 1],  [5, 2, 4, 3, 1, 6], [3, 2], [5, 3, 1, 6, 4], [2, 5, 3]],
    # [[3, 2], [2, 4, 1, 5, 3],[4, 6],[5, 1, 2],[3, 2, 1, 5, 4, 6]],
    # [[1, 5, 4, 2, 6, 3], [5, 1], [6, 3, 2], [4, 1],[3, 6, 4, 2]],
    # [[5, 1], [4, 6, 5], [2, 3], [4, 3, 2, 1], [5, 1, 3, 2, 4]],
    # [[2, 4, 6], [2, 5], [1, 3, 2], [6, 1], [6, 2, 4, 1, 3]],
    # [[5, 4, 3, 1],[4, 2, 3], [1, 5, 6], [2, 5, 3, 1, 6, 4], [5, 4, 2, 3, 6]],
    # [[5, 4, 3, 1], [4, 2, 3], [1, 5, 6], [2, 5, 3, 1, 6, 4], [5, 4, 2, 3, 6]]
]

# Generate random hypergraphs
for i in range(100):
    random_hypergraph = generate_random_hypergraph(num_vertices, num_hyperedges, min_vertices, max_vertices_per_edge)
    hypergraphs.append(random_hypergraph)

# Get rid of any duplicate hypergraphs
noDup = remove_outer_duplicates(hypergraphs)

# Get rid of hypergraphs that do not have the number of hyperedges specified
cleanList = [x for x in noDup if len(x)==num_hyperedges]

# Short the vertices in each hyperedge of each hypergraph
sortedList = [
    [sorted(inner, key=lambda x: str(x)) for inner in sublist]
    for sublist in cleanList
]

# print(*sortedList, sep='\n')

listDict = []

# Create dictionary from sortedList
for i in range(len(sortedList)):
    hypergraphDict = {}
    for j in range(len(sortedList[i])):
        hypergraphDict['e{}'.format(j)] = sortedList[i][j]

    listDict.append(hypergraphDict)


# Initialize arrays for data
checkHypergraphs = copy.deepcopy(listDict) # Copy to retain original dictionary
vertices = []
hyperedges = []
numHyperedges6 = []
numHyperedges5 = []
numHyperedges4 = []
numHyperedges3 = []
numHyperedges2 = []
hyperedgeAllVertices = []
alpha = []
beta = []
chordal = []
regular = []
complete = []
dual = []
dualAlpha = []
dualBeta = []
dualChordal = []
dualRegular = []
dualComplete = []

# Go through every hypergraph to get the information needed
for i in range(len(listDict)):
    H = hnx.Hypergraph(listDict[i]) # Convert hypergraph to hypergraph type

    # Get number of vertices and edge
    vertices.append(H.number_of_nodes())
    hyperedges.append(H.number_of_edges())

    # See if there is a hyperedge with all vertices
    count = 0
    for hyperedge in H.edges:
        if set(H.edges[hyperedge]) == set(H.nodes()):
            count += 1
    if count >= 1:
        hyperedgeAllVertices.append(True)
    else:
        hyperedgeAllVertices.append(False)

    # Get line graph
    G = H.get_linegraph()
    # Check line graph
    chordal.append(nx.is_chordal(G))
    reg = nx.is_regular(G)
    regular.append(nx.is_regular(G))
    # Check if line graph is a complete graph (every vertex should have degree of the # vertices - 1)
    if reg == True and G.degree['e0'] == (num_hyperedges - 1):
        complete.append(True)
    else:
        complete.append(False)

    # Check acyclicity of hypergraph
    hypergraph = copy.deepcopy(checkHypergraphs[i])
    alpha.append(GYO(checkHypergraphs[i]))
    beta.append(checkBetaAcyclic(hypergraph))

    # Get dual
    D = H.dual()
    dual.append(D.incidence_dict) # Convert dual to dictionary
    # Get line graph of the dual and check it
    dualG = D.get_linegraph()
    dualChordal.append(nx.is_chordal(dualG))
    dualReg = nx.is_regular(dualG)
    dualRegular.append(dualReg)
    # Check if line graph of the dual is complete (every vertex should have degree of the # vertices - 1)
    node = random.choice(list(dualG.nodes())) # Get a random node from the line graph
    if dualReg == True and dualG.degree[node] == (D.number_of_edges() - 1):
        dualComplete.append(True)
    else:
        dualComplete.append(False)

    # Check acyclicity of the dual
    dualHypergraph = copy.deepcopy(D.incidence_dict)
    dualAlpha.append(GYO(D.incidence_dict))
    dualBeta.append(checkBetaAcyclic(dualHypergraph))

# Add to dataframe
df['hypergraph'] = listDict
df['numVertices'] = vertices
df['numEdges'] = hyperedges
df['hyperedgeAllVertices'] = hyperedgeAllVertices
df['alpha'] = alpha
df['beta'] = beta
df['lineGraphChordal'] = chordal
df['lineGraphRegular'] = regular
df['lineGraphComplete'] = complete
df['dualGraph'] = dual
df['dualAlpha'] = dualAlpha
df['dualBeta'] = dualBeta
df['dualLineChordal'] = dualChordal
df['dualLineRegular'] = dualRegular
df['dualLineComplete'] = dualComplete

print(df)

# Convert Dictionary to string
df['hypergraph'] = df['hypergraph'].apply(json.dumps)
df['dualGraph'] = df['dualGraph'].apply(json.dumps)

# Dataframe for the table that holds the k-NEOs
kDf['hypergraph'] = listDict
kDf['hypergraph'] = kDf['hypergraph'].apply(json.dumps)

# --------
# Add dataframes to mysql database

# Database connection information
DB_USERNAME = 'root'
DB_PASSWORD = 'Acd2023='
DB_HOST = 'localhost'
DB_NAME = 'hypergraphs'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_NAME
)

# Create a SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# Insert DataFrame into hypergraph table
df.to_sql('hypergraph', con=engine, if_exists='append', index=False)

kDf.to_sql('kNEO', con=engine, if_exists='append', index=False)

# Close the MySQL connection
conn.close()