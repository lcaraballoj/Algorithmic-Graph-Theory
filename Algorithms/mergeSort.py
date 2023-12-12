# --------
# Merge Sort Algorithms
# --------

# Merge sort algorithm for a dictionary
def mergeSortDict(dictionary):
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
 
    left_half = mergeSortDict(left_half)            # recursive call for the left half
    right_half = mergeSortDict(right_half)          # recursive call for the right half
 
    return mergeDict(left_half, right_half)          # merging the two sorted halves

def mergeDict(left_half, right_half):
    result = {}
    left_keys = list(left_half.keys())
    right_keys = list(right_half.keys())
    i = 0
    j = 0
    while i < len(left_keys) and j < len(right_keys):
        if left_keys[i] < right_keys[j]:         # executed if the left half has the lower element
            result[left_keys[i]] = left_half[left_keys[i]]
            i += 1
        else:                                    # executed if the right half has the lower element
            result[right_keys[j]] = right_half[right_keys[j]]
            j += 1
    while i < len(left_keys):                    # adding remaining elements of left half
        result[left_keys[i]] = left_half[left_keys[i]]
        i += 1
    while j < len(right_keys):                   # adding remaining elements of right half
        result[right_keys[j]] = right_half[right_keys[j]]
        j += 1
    return result

# Merge Sort Algorithm for a list
def mergeSort(list: [int]):
    list_length = len(list)
    
    if list_length == 1:
        return list
    
    mid_point = list_length // 2
    
    left_half = mergeSort(list[:mid_point])
    right_half = mergeSort(list[mid_point:])
    
    return merge(left_half, right_half)

def merge(left, right):
    output = []
    i = j = 0
    
    if (left != right):
        while (i < len(left) and j < len(right)):
            if left[i] < right[j]:
                output.append(left[i])
                i +=1
            else:
                output.append(right[j])
                j +=1
        output.extend(left[i:])
        output.extend(right[j:])
    
    return output

print(mergeSortDict({'e1': ['1', '2'], 'e2':['1', '3'], 'e3':['1', '2', '3']}))