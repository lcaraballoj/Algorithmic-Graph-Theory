# --------
# Enter in first nest points and 2-nest sets into database
# --------
import mysql.connector, copy, json
import pandas as pd

from getHypergraphs import getHypergraphs
from nestSet import getSet
from findNestPoints import *
from sqlalchemy import create_engine

# Create dataframe
df = pd.DataFrame()


# Database connection information
DB_USERNAME = 'root'
DB_PASSWORD = 'password'
DB_HOST = 'localhost'
DB_NAME = 'hypergraphs'

# Connect to the MySQL database
conn = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_NAME
)

query = "SELECT hypergraph FROM hypergraphReduced WHERE numVertices = 8 AND sizeOfEdges = '[4, 4, 3]';"
hypergraphList = getHypergraphs(DB_USERNAME, DB_PASSWORD,DB_HOST, DB_NAME, query)

hypergraphs = []
nestPoint = []
twoNestSet = []
threeNestSet = []

for i in range(len(hypergraphList)):
    hypergraphs.append(hypergraphList[i])
    nestPoint.append(findNestPoint(copy.deepcopy(hypergraphList[i])))
    twoNestSet.append(getSet(copy.deepcopy(hypergraphList[i]),2))
    threeNestSet.append(getSet(copy.deepcopy(hypergraphList[i]),3))

df['hypergraph'] = hypergraphs
df['nestPoint'] = nestPoint
df['twoNestSet'] = twoNestSet
df['threeNestSet'] = threeNestSet

df['hypergraph'] = df['hypergraph'].apply(json.dumps)
df['nestPoint'] = df['nestPoint'].apply(json.dumps)
df['twoNestSet'] = df['twoNestSet'].apply(json.dumps)
df['threeNestSet'] = df['threeNestSet'].apply(json.dumps)

print(df)


df.to_csv('testNest.csv')

# Create a SQLAlchemy engine
engine = create_engine(f"mysql+mysqlconnector://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}")

# Insert DataFrame into hypergraph table
df.to_sql('nestSets', con=engine, if_exists='append', index=False)

# Close the MySQL connection
conn.close()