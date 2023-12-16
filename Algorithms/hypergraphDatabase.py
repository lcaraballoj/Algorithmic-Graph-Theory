import pandas as pd
from sqlalchemy import create_engine

# Replace these values with your database connection details
DB_USERNAME = 'root'
DB_PASSWORD = 'Acd2023='
DB_HOST = 'localhost'  # Usually 'localhost' if the database is on the same machine
DB_NAME = 'hypergraphs'

# Create a DataFrame (this is just an example, replace it with your DataFrame)
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
}


df = pd.DataFrame(data)

# MySQL database connection string
conn_str = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

# Create SQLAlchemy engine to connect to the database
engine = create_engine(conn_str)

# Replace 'table_name' with the name you want for your table in the database
table_name = 'example_table'

# Insert the DataFrame into the MySQL database table
df.to_sql(table_name, con=engine, if_exists='replace', index=False)

# Close the database connection
engine.dispose()
