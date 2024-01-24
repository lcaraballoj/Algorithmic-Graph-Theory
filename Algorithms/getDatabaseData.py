# --------
# Get data from a hypergraph database to convert into new form
# --------

import os
import pandas as pd
import mysql.connector, json


# Establish a connection to your MySQL database
# Database connection information
DB_USERNAME = 'root'
DB_PASSWORD = 'Acd2023='
DB_HOST = 'localhost'
DB_NAME = 'hypergraphs'

# Connect to the MySQL database
connection = mysql.connector.connect(
    host=DB_HOST,
    user=DB_USERNAME,
    passwd=DB_PASSWORD,
    database=DB_NAME
)

# Create a cursor object to execute queries
cursor = connection.cursor()

# Example query to select data
query = "SELECT * FROM kNEOReduced INNER JOIN hypergraphReduced USING (hypergraph) WHERE kNEOReduced.one IS NOT False"

# Execute the query
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

list_of_dicts = [json.loads(row[0]).values() for row in rows] # Get the hyperedge vertex data

sorted_data = [sorted(sublist, key=len, reverse=True) for sublist in list_of_dicts] # Sort hyperedges by size

print(sorted_data)

df = pd.read_sql(query,connection)

dict = {'hypergraph': sorted_data, 'one': df['one']}

df = pd.DataFrame(dict)

df.to_csv('2NEO.csv')

# Close the cursor and connection
cursor.close()
connection.close()

