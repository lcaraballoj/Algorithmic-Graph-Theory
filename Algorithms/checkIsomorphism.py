# --------
# Find Isomorphic Hypergraphs
# Using the fact that the incidence graphs of hypergraphs are isomorphic iff the hypergraphs themselves are isomorphic
# --------
import networkx as nx
import hypernetx as hnx

import copy
import mysql.connector, json
import hypernetx as hnx
import matplotlib.pyplot as plt

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

    # copyDict = copy.deepcopy(dict)

    # for i in range(len(copyDict)):
    #     target_hypergraph = copyDict[i]

    #     # Iterate through other hypergraphs
    #     isomorphic_hypergraphs = []
    #     nonIsomorphic = []

    #     for idx, hg in enumerate(dict):
    #         if are_isomorphic(target_hypergraph, hg):
    #             isomorphic_hypergraphs.append(idx)
    #             dict.pop(idx)
        
    #     print(isomorphic_hypergraphs)

    # print(dict)

# # --------
# # Get hypergraphs

# # Establish a connection to your MySQL database
# # Database connection information
# DB_USERNAME = 'root'
# DB_PASSWORD = 'password'
# DB_HOST = 'localhost'
# DB_NAME = 'hypergraphs'

# # Create a cursor object to execute queries
# cursor = connection.cursor()

# # Example query to select data
# query = "SELECT * FROM hypergraphSpecificEdges WHERE  sizeOfEdges = '[6, 4, 4, 3]' AND beta = False;"

# # Execute the query
# cursor.execute(query)

# # Fetch all the rows
# rows = cursor.fetchall()

# # List of all hypergraphs
# list_of_dicts = [json.loads(row[0]) for row in rows]

# # Find representatives of isomorphic hypergraphs
# representatives = checkList(list_of_dicts)

# # Create a cursor object to execute queries
# cursor = connection.cursor()

# # Create a new table similar to the original table
# cursor.execute("SHOW CREATE TABLE hypergraphSpecificEdges")
# create_table_query = cursor.fetchone()[1]
# create_table_query = create_table_query.replace("hypergraphSpecificEdges", "representative_hypergraphs")
# cursor.execute(create_table_query)

# # Insert representative hypergraphs into the new table
# insert_query = "INSERT INTO representative_hypergraphs SELECT * FROM hypergraphSpecificEdges WHERE JSON_CONTAINS(%s, json_column, '$')"
# for hg in representatives:
#     hg_json = json.dumps(hg)
#     cursor.execute(insert_query, (hg_json,))

# # Commit changes and close the cursor and connection
# connection.commit()
# cursor.close()
# connection.close()