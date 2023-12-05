# --------
# Algorithm to determine if a graph is beta-acyclic
# --------

# Find nest-points
def nestPoints(H):
    verticesEdges = []
    for edges, vertices in H.items():
        verticesEdges.append(vertices)
    print(verticesEdges)
        
    # List of vertices
    nodes = [] 
    for i in range(0, len(verticesEdges)):
        nodes = list(set(verticesEdges[i] + nodes))

    print(nodes)

    listOfEdges = []
    edgeLength = {}

    # Check nest point
    for i in range(0, len(nodes)):
        print(nodes[i])
        for j in range(0, len(verticesEdges)):
            if nodes[i] in verticesEdges[j]:
                listOfEdges.append(verticesEdges[j])
                edgeLength[j] = len(verticesEdges[j])
        print("List of Edges: ", listOfEdges)
        print("Edge Dict: ", edgeLength)
        print("Sorted: ", merge_sort(edgeLength))

        # sort = mergeSort(edgeLength)
        # print("Unsrt: ", edgeLength)
        # print("Srt:", sort)
        # if len(edgeLength) == len(sort):
        #     print("Same length!")
        listOfEdges = []
        edgeLength = {}

def merge_sort(dictionary):
                     # base case
    if len(dictionary) <= 1:                     # checking if the dictionary needs sorting
        return dictionary
 
    mid = len(dictionary) // 2
    left_half = {}
    right_half = {}
    for index, key in enumerate(dictionary):     # keys are given index numbers and split in two groups
        if index < mid:
            left_half[key] = dictionary[key]     # forming the left half dictionary
        else:
            right_half[key] = dictionary[key]    # forming the right half dictionary
    # print("Left: ", left_half)
    # print("Right: ", right_half)
 
    left_half = merge_sort(left_half)            # recursive call for the left half
    right_half = merge_sort(right_half)          # recursive call for the right half
 
    return merge(left_half, right_half)          # merging the two sorted halves\

def merge(left_half, right_half):
    result = {}
    left_keys = list(left_half.keys())
    left_values = list(left_half.values())
    right_keys = list(right_half.keys())
    right_values = list(right_half.values())

    i = 0
    j = 0

    while i < len(left_values) and j < len(right_values):
        if left_values[i] < right_values[j]:         # executed if the left half has the lower element
            result[left_keys[left_values.index(left_values[i])]] = left_values[i]
            i += 1
        else:                                    # executed if the right half has the lower element
            result[right_keys[right_values.index(right_values[j])]] = right_values[j]
            j += 1
    while i < len(left_values):                    # adding remaining elements of left half
        result[left_keys[left_values.index(left_values[i])]] = left_values[i]
        i += 1
    while j < len(right_values):                   # adding remaining elements of right half
        result[right_keys[right_values.index(right_values[j])]] = right_values[j]
        j += 1
    return result

# # Merge Sort Algorithm
# def mergeSort(list: [int]):
#     list_length = len(list)
    
#     if list_length == 1:
#         return list
    
#     mid_point = list_length // 2
    
#     left_half = mergeSort(list[:mid_point])
#     right_half = mergeSort(list[mid_point:])
    
#     return merge(left_half, right_half)

# def merge(left, right):
#     output = []
#     i = j = 0
    
#     if (left != right):
#         while (i < len(left) and j < len(right)):
#             if left[i] < right[j]:
#                 output.append(left[i])
#                 i +=1
#             else:
#                 output.append(right[j])
#                 j +=1
#         output.extend(left[i:])
#         output.extend(right[j:])
    
#     return output

# def checkNested(arr):


def gammaTriangle():
    hypergraph = {
        "e1": [1, 2, 3],
        "e2": [1, 2],
        "e3": [1, 3]
    }
    return hypergraph

nestPoints(gammaTriangle())

#sample_dictionary = {'b': 2, 'c': 3, 'a': 1, 'e': 5, 'd': 4}
#print(merge_sort(sample_dictionary))



# # creating a new dictionary
# my_dict ={"Java":100, "Python":112, "C":11}
 
# # one-liner
# print("One line Code Key value: ", list(sample_dictionary.keys())
#       [list(sample_dictionary.values()).index(2)])

