# --------
# Pull data from mysql database or hypergraphs and then output the hypergraph pictures
# --------

# from torchvision.io import read_image, ImageReadMode
# from torchvision.utils import make_grid, save_image
# from torchvision.transforms import transforms
# from torchvision import torch

from PIL import Image
import os
import mysql.connector, json
import hypernetx as hnx
import matplotlib.pyplot as plt

# Establish a connection to your MySQL database
# Database connection information
DB_USERNAME = 'root'
DB_PASSWORD = 'passwords'
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
query = "SELECT hypergraph FROM kNEOReduced WHERE one = True;"

# Execute the query
cursor.execute(query)

# Fetch all the rows
rows = cursor.fetchall()

list_of_dicts = [json.loads(row[0]) for row in rows]

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

    plt.savefig("Graphs/hypergraph" + str(i) + ".png")
    plt.clf()

    i += 1


# Close the cursor and connection
cursor.close()
connection.close()

# tensors = []

# FOLDER = "/Users/linneacaraballo/Documents/Algorithmic-Graph-Theory/Algorithms/2NEO"

# transform = transforms.Compose([
#     transforms.CenterCrop(800),
#     transforms.ConvertImageDtype(dtype=torch.float),
# ])

# for file in os.listdir(FOLDER):
#     image = os.path.join(FOLDER, file)
#     transformed_tensor = transform(read_image(image, mode=ImageReadMode.RGB))
#     tensors.append(transformed_tensor)

# grid = make_grid(tensors, nrow=4, padding=2)

# save_image(grid, FOLDER+"/grid.jpg")

# Folder containing your images
folder_path = '/Users/linneacaraballo/Documents/Algorithmic-Graph-Theory/Algorithms/Graphs'

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