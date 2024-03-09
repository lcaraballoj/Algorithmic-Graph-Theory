# --------
# Enter in first nest points and 2-nest sets into database
# --------
import mysql.connector, copy, json
import pandas as pd

from getHypergraphs import getHypergraphs
from findNestSets import *
from nestSetElimination import neo
from sqlalchemy import create_engine, text

# Create dataframe
df = pd.DataFrame()


# Database connection information
DB_USERNAME = 'root'
DB_PASSWORD = 'passwords'
DB_HOST = 'localhost'
DB_NAME = 'hypergraphs'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_NAME
)

# query = "SELECT H.hypergraph FROM hypergraphReduced as H WHERE NOT EXISTS (SELECT 1 FROM nestSets as N WHERE H.hypergraph = N.hypergraph);"
# query = "SELECT H.hypergraph FROM hypergraphReduced as H WHERE numVertices = 12;"
query = "SELECT hypergraph FROM hypergraphReduced WHERE numVertices = 6"
hypergraphList = getHypergraphs(DB_USERNAME, DB_PASSWORD,DB_HOST, DB_NAME, query)

def nestSets(hypergraphList):
    hypergraphs = []
    nestPoint = []
    twoNestSet = []
    threeNestSet = []

    for i in range(len(hypergraphList)):
        hypergraphs.append(hypergraphList[i])
        nestPoint.append(get_set(copy.deepcopy(hypergraphList[i]), 1))
        twoNestSet.append(get_set(copy.deepcopy(hypergraphList[i]),2))
        threeNestSet.append(get_set(copy.deepcopy(hypergraphList[i]),3))

    df['hypergraph'] = hypergraphs
    df['nestPoint'] = nestPoint
    df['twoNestSet'] = twoNestSet
    df['threeNestSet'] = threeNestSet

    df['hypergraph'] = df['hypergraph'].apply(json.dumps)
    df['nestPoint'] = df['nestPoint'].apply(json.dumps)
    df['twoNestSet'] = df['twoNestSet'].apply(json.dumps)
    df['threeNestSet'] = df['threeNestSet'].apply(json.dumps)

    # Create SQLAlchemy engine
    engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

    df.to_sql('temp_table', engine, if_exists='replace')

    sql = "UPDATE nestSets AS N INNER JOIN temp_table AS T ON N.hypergraph = T.hypergraph SET N.nestPoint = T.nestPoint, N.twoNestSet = T.twoNestSet, N.threeNestSet = T.threeNestSet;"

    with engine.begin() as conn:
        conn.execute(text(sql))

    # Close the MySQL connection
    conn.close()

def nestSetElimination(hypergraphList):
    hypergraphs = []
    two = []

    for i in range(len(hypergraphList)):
        hypergraphs.append(hypergraphList[i])
        two.append(neo(copy.deepcopy(hypergraphList[i]), 3))

    df['hypergraph'] = hypergraphs
    df['three'] = two

    df['hypergraph'] = df['hypergraph'].apply(json.dumps)

    # Create SQLAlchemy engine
    engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

    df.to_sql('temp_table', engine, if_exists='replace')

    # Close the MySQL connection
    conn.close()   

nestSetElimination(hypergraphList)


