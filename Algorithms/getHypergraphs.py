# --------
# Pull data from mysql database or hypergraphs and then output various results
# --------

from PIL import Image
from collections import defaultdict
from betaAcyclic import findNestPoint
import numpy as np
import pandas as pd
import os
import mysql.connector, json
import hypernetx as hnx
import matplotlib.pyplot as plt

# Get hypergraphs from database based on a specific query
def getHypergraphs(DB_USERNAME, DB_PASSWORD, DB_HOST, DB_NAME, query):
    # Connect to the MySQL database
    connection = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USERNAME,
        passwd=DB_PASSWORD,
        database=DB_NAME
    )

    # Create a cursor object to execute queries
    cursor = connection.cursor()

    # Execute the query
    cursor.execute(query)

    # Fetch all the rows
    rows = cursor.fetchall()

    list_of_dicts = [json.loads(row[0]) for row in rows]

     # Close the cursor and connection
    cursor.close()
    connection.close()

    return list_of_dicts

# Get pictures for hypergraphs
def getPictures(list_of_dicts):
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

        plt.savefig("Temp/hypergraph" + str(i) + ".png")
        plt.clf()

        i += 1

# Put pictures from a folder into a grid
def createGrid(folder_path):
    # List to hold the images
    images = []

    # Loop through the folder to open images
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):  # Add more extensions if needed
            image_path = os.path.join(folder_path, filename)
            img = Image.open(image_path)
            images.append(img)

    # Calculate the size of the grid based on the number of images
    num_images = len(images)
    columns = 6  # Number of columns in the grid, change this as needed
    rows = -(-num_images // columns)  # Ceil division to determine number of rows

    # Create a blank canvas to arrange images in a grid
    canvas_width = max(img.width for img in images) * columns
    canvas_height = max(img.height for img in images) * rows
    canvas = Image.new('RGB', (canvas_width, canvas_height), color='white')

    # Paste images onto the canvas in a grid pattern
    for i, img in enumerate(images):
        x = (i % columns) * img.width
        y = (i // columns) * img.height
        canvas.paste(img, (x, y))

    # Save the grid image
    grid_image_path = folder_path + '/grid.jpg'
    canvas.save(grid_image_path)

    # Display the grid image
    canvas.show()

# Get the incidence matrices for a list of hypergraphs
def incidenceMatrices(hypergraph):
    incidenceMatrix = []
    for i in range(len(hypergraph)):
        print(hypergraph[i])

        H = hnx.Hypergraph(hypergraph[i])
        result = H.incidence_matrix().toarray()
        incidenceMatrix.append(result)

        cols = ["e0", "e1", "e2", "e3", "e4"]
        df = pd.DataFrame(result, columns=cols, index=[1,2,3,4,5,6])
        print(df)

    return incidenceMatrix

# Get the adjacency matrices for a list of hypergraphs
def adjacencyMatrices(hypergraph):
    adjacencyMatrix = []

    for i in range(len(hypergraph)):
        H = hnx.Hypergraph(hypergraph[i])
        matrix = H.adjacency_matrix().toarray()
        adjacencyMatrix.append(matrix)
    
    return adjacencyMatrix

# Get the submatrices for a matrix
def submatrices(matrix):
    m = len(matrix)
    n = len(matrix[0])
    submatrices_list = []
    
    for i in range(m):
        for j in range(n):
            for k in range(i, m):
                for l in range(j, n):
                    submatrix = []
                    for p in range(i, k+1):
                        row = []
                        for q in range(j, l+1):
                            row.append(matrix[p][q])
                        submatrix.append(row)
                    submatrices_list.append(submatrix)
                    
    return submatrices_list


# Establish a connection to your MySQL database
# Database connection information
DB_USERNAME = 'root'
DB_PASSWORD = 'Acd2023='
DB_HOST = 'localhost'
DB_NAME = 'hypergraphs'

query = "SELECT hypergraph FROM hypergraphReduced WHERE sizeOfEdges = '[5, 2, 2, 2]';"

# Folder containing your images
folder_path = '/Users/linneacaraballo/Documents/Algorithmic-Graph-Theory/Algorithms/Temp'

# matrices = incidenceMatrices(getHypergraphs(DB_USERNAME, DB_PASSWORD,DB_HOST, DB_NAME, query))

# for i in range(len(matrices)):
#     print(submatrices(matrices[i]), '\n')

hypergraphs = getHypergraphs(DB_USERNAME, DB_PASSWORD,DB_HOST, DB_NAME, query)

# for i in range(len(hypergraphs)):
#     print(hypergraphs[i])

# print(hypergraphs)

# incidenceMatrices(hypergraphs)

# getPictures(hypergraphs)

# createGrid(folder_path)

# triangle = {
#         'e2': [2,3],
#         'e3': [2,4],
#         'e4': [3,4]
#     }

# T = hnx.Hypergraph(triangle)

# print(T.is_connected())

# print(T.incidence_matrix().toarray())
             
