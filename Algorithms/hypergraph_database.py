import ast, copy, json, mysql.connector, os, random, time
import hypernetx as hnx
import networkx as nx
import pandas as pd

from sqlalchemy import create_engine, text

from nest_point_elim import check_beta_acyclic
from check_isomorphism import checkList
from find_nest_sets import get_set
from generate_hypergraphs import *
from gyo_algorithm import gyo
from neo import neo


# Create dicitonary of hypergraphs
def create_hypergaphs(hypergraphs):
    # Convert dictionaries to list of lists
    hypergraphs_list = []

    for i in range(len(hypergraphs)):
        hypergraphs_list.append(list(hypergraphs[i].values()))

    # Create dataframe
    df = pd.DataFrame()

    # Get size of hyperedges
    hyperedge_sizes = []
    for i in range (len(hypergraphs_list)):
        hyperedge_sizes.append([len(x) for x in hypergraphs_list[i]])

    # Get number of hyperedges and number of vertices
    num_hyperedges = []
    num_vertices = []
    for i in range (len(hypergraphs)):
        num_hyperedges.append(len(hypergraphs_list[i]))
        max_values = [max(sublist) for sublist in hypergraphs_list[i]]
        num_vertices.append(max(max_values))

    df['hypergraph'] = hypergraphs
    df['hyperedge_sizes'] = hyperedge_sizes
    df['num_hyperedges'] = num_hyperedges
    df['num_vertices'] = num_vertices

    df['hypergraph'] = df['hypergraph'].apply(json.dumps)
    df['hyperedge_sizes'] = df['hyperedge_sizes'].apply(json.dumps)

    print(df)

    df.to_sql('hypergraphs', con=engine, if_exists='append', index=False)

# Create acyclicity of hypergaphs
def create_acyclicity(hypergraphs):
    df = pd.DataFrame()

    alpha = []
    beta = []

    for i in range(len(hypergraphs)):
        alpha.append(gyo(copy.deepcopy(hypergraphs[i])))
        beta.append(check_beta_acyclic(copy.deepcopy(hypergraphs[i])))

    df['hypergraph'] = hypergraphs
    df['alpha'] = alpha
    df['beta'] = beta

    df['hypergraph'] = df['hypergraph'].apply(json.dumps)

    # print(df)

    df.to_sql('acyclicity', con=engine, if_exists='append', index=False)

# Create hypergraph properties
def create_properties(hypergraphs):
    df = pd.DataFrame()
    
    chordal = []
    regular = []
    complete = []
    dual_hypergraph = []
    dual_alpha = []
    dual_beta= []
    dual_line_chordal = []
    dual_line_regular = []
    dual_line_complete = []

    for i in range(len(hypergraphs)):
        # Convert dictionaries to list of lists
         hypergraphs_list = []

    for i in range(len(hypergraphs)):
        H = hnx.Hypergraph(hypergraphs[i]) # Convert hypergraph to hypergraph type
        hypergraphs_list.append(list(hypergraphs[i].values()))
        num_hyperedges = len(hypergraphs_list[i])

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

        # Get dual
        D = H.dual()
        dual_hypergraph.append(D.incidence_dict) # Convert dual to dictionary
        # Get line graph of the dual and check it
        dualG = D.get_linegraph()
        dual_line_chordal.append(nx.is_chordal(dualG))
        dual_reg = nx.is_regular(dualG)
        dual_line_regular.append(dual_reg)
        # Check if line graph of the dual is complete (every vertex should have degree of the # vertices - 1)
        node = random.choice(list(dualG.nodes())) # Get a random node from the line graph
        if dual_reg == True and dualG.degree[node] == (D.number_of_edges() - 1):
            dual_line_complete.append(True)
        else:
            dual_line_complete.append(False)

        # Check acyclicity of the dual
        dual_alpha.append(gyo(copy.deepcopy(D.incidence_dict)))
        dual_beta.append(check_beta_acyclic(copy.deepcopy(D.incidence_dict)))

    df['hypergraph'] = hypergraphs
    df['line_chordal'] = chordal
    df['line_regular'] = regular
    df['line_complete'] = complete
    df['dual_hypergraph'] = dual_hypergraph
    df['dual_alpha'] = dual_alpha
    df['dual_beta'] = dual_beta
    df['dual_line_chordal'] = dual_line_chordal
    df['dual_line_regular'] = dual_line_regular
    df['dual_line_complete'] = dual_line_complete

    df['hypergraph'] = df['hypergraph'].apply(json.dumps)
    df['dual_hypergraph'] = df['dual_hypergraph'].apply(json.dumps)

    # print(df)

    df.to_sql('properties', con=engine, if_exists='append', index=False)
        
# Create list of nest-sets
def create_nest_sets(hypergraphs):
    df = pd.DataFrame()

    nest_point = []
    two_nest_set = []
    three_nest_set = []

    for i in range(len(hypergraphs)):
        nest_point.append(get_set(copy.deepcopy(hypergraphs[i]),1))
        two_nest_set.append(get_set(copy.deepcopy(hypergraphs[i]),2))
        three_nest_set.append(get_set(copy.deepcopy(hypergraphs[i]),2))

    df['hypergraph'] = hypergraphs
    df['two_nest_set'] = two_nest_set
    df['three_nest_set'] = three_nest_set

    df['hypergraph'] = df['hypergraph'].apply(json.dumps)
    df['two_nest_set'] = df['two_nest_set'].apply(json.dumps)
    df['three_nest_set'] = df['three_nest_set'].apply(json.dumps)

    # print(df)

    df.to_sql('nest_sets', con=engine, if_exists='append', index=False)

# Create list of nest-set eliminations
def create_nest_set_elimination(hypergraphs):
    df = pd.DataFrame()

    two_neo = []
    three_neo = []

    for i in range(len(hypergraphs)):
        two_neo.append(neo(copy.deepcopy(hypergraphs[i]),2))
        three_neo.append(neo(copy.deepcopy(hypergraphs[i]),3))

    df['hypergraph'] = hypergraphs
    df['two_neo'] = two_neo
    df['three_neo'] = three_neo
    
    df['hypergraph'] = df['hypergraph'].apply(json.dumps)

    # print(df)

    df.to_sql('nest_set_elimination', con=engine, if_exists='append', index=False)

# Check connected
def connected(hypergraph):
    connectedHypergraph = []
    for i in range(len(hypergraph)):
        H = hnx.Hypergraph(hypergraph[i])
        if H.is_connected() == True:
            connectedHypergraph.append(hypergraph[i])

    return connectedHypergraph

# Create databse rows from CSV file
def hypergraphs_csv(file):
    # Import Data
    data = pd.read_csv(file)

    # Get Hypergraphs 
    data['hypergraphs']
    print(data['hypergraphs'])
    string_hypergraphs = data['hypergraphs'].values 

    # Convert string representation of dictionaries to dictionaries
    hypergraphs = []

    for i in range (len(string_hypergraphs)):
        hypergraphs.append(ast.literal_eval(string_hypergraphs[i]))
    
    return hypergraphs

def hypergraphs_random(num_hypergraphs, num_vertices, num_hyperedges, hyperedge_size):
    hypergraphs = []

    numbers = set(range(1,num_vertices + 1))

    # Generate random hypergraphs
    for i in range(num_hypergraphs):
        random_hypergraph = generate_random_hypergraph(num_vertices, num_hyperedges, hyperedge_size)
        unique_items = set(item for sublist in random_hypergraph for item in sublist) # Get all unique vertices in the hypergraph

        # Make sure that all vertices are in the hypergraph
        if unique_items == numbers:
            hypergraphs.append(random_hypergraph)

    # Get rid of any duplicate hypergraphs
    noDup = remove_outer_duplicates(hypergraphs)

    # Get rid of hypergraphs that do not have the number of hyperedges specified
    cleanList = [x for x in noDup if len(x)== num_hyperedges]

    # Sort the vertices in each hyperedge of each hypergraph
    sortedList = [
        [sorted(inner, key=lambda x: str(x)) for inner in sublist]
        for sublist in cleanList
    ]

    sorted_data = [sorted(sublist, key=len, reverse=True) for sublist in sortedList]

    fullList = []

    # Create dictionary from sortedList
    for i in range(len(sorted_data)):
        hypergraphDict = {}
        for j in range(len(sorted_data[i])):
            hypergraphDict['e{}'.format(j)] = sorted_data[i][j]

        fullList.append(hypergraphDict)

    connectedList = connected(fullList)

    # Account for isomorphic graphs
    listDict = checkList(connectedList)

    return listDict

# Database connection information
# Replace with your database information
DB_USERNAME = 'user'
DB_PASSWORD = 'password'
DB_HOST = 'host'
DB_PORT = 3309
DB_NAME = 'hypergraphs'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_NAME,
    port=DB_PORT
)

# Create a SQLAlchemy engine
engine = create_engine(f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

hyperedge_sizes = [
    [2,2,2],
    [3,2,2],
    [3,3,2],
    [3,3,3],
    [4,2,2],
    [4,3,2],
    [4,3,3],
    [4,4,3],
    [4,4,4],
    [5,2,2],
    [5,3,2],
    [5,3,3],
    [5,4,2],
    [5,4,3],
    [5,4,4],
    [5,5,2],
    [5,5,3],
    [5,5,4],
    [5,5,5],
    [6,2,2],
    [6,3,2],
    [6,4,2],
    [5,4,3],
    [6,4,4],
    [6,5,2],
    [6,5,3],
    [6,5,4],
    [6,5,5]
]

for i in range(len(hyperedge_sizes)):

    start_time = time.time()

    hypergraphs = hypergraphs_random(800, 6, 3, hyperedge_sizes[i])

    create_hypergaphs(copy.deepcopy(hypergraphs))
    create_acyclicity(copy.deepcopy(hypergraphs))
    create_properties(copy.deepcopy(hypergraphs))
    create_nest_sets(copy.deepcopy(hypergraphs))
    create_nest_set_elimination(copy.deepcopy(hypergraphs))

    # Close the MySQL connection
    conn.close()

    end_time = time.time()

    print(end_time - start_time)

os.system('say "your program has finished"')