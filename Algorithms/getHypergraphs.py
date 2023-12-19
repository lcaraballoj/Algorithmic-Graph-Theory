# --------
# Pull data from mysql database or hypergraphs and then output the hypergraph pictures
# --------

from torchvision.io import read_image, ImageReadMode
from torchvision.utils import make_grid, save_image
from torchvision.transforms import transforms
from torchvision import torch

import os
import mysql.connector, json
import hypernetx as hnx
import matplotlib.pyplot as plt

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
query = "SELECT hypergraph FROM kNEO WHERE two = 'None'"

# Execute the query
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

list_of_dicts = [json.loads(row[0]) for row in rows]

print(list_of_dicts)

i = 0

# Print or process the fetched rows
for item in list_of_dicts:
    plt.title(item)
    H = hnx.Hypergraph(item)  # Or do something else with the data

    kwargs = {'layout_kwargs': {'seed': 8}, 'with_node_counts': False}
    hnx.drawing.draw(H,
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

    plt.savefig("no2NEO/hypergraph" + str(i) + ".png")
    plt.clf()

    i += 1


# Close the cursor and connection
cursor.close()
connection.close()

tensors = []

FOLDER = "/Users/linneacaraballo/Documents/Algorithmic-Graph-Theory/Algorithms/no2NEO"

transform = transforms.Compose([
    transforms.CenterCrop(800),
    transforms.ConvertImageDtype(dtype=torch.float),
])

for file in os.listdir(FOLDER):
    image = os.path.join(FOLDER, file)
    transformed_tensor = transform(read_image(image, mode=ImageReadMode.RGB))
    tensors.append(transformed_tensor)

grid = make_grid(tensors, nrow=4, padding=2)

save_image(grid, FOLDER+"/grid.jpg")
