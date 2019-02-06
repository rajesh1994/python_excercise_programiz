# How To Insert And Delete Array Elements

# Import numpy as 'np'
import numpy as np

# Initialize array 'x1'
x1 = np.array([[1, 5, 9, 3], [2, 6, 10, 4]])
print("Array 'x1' is:")
print(x1)

# Insert 7 at index 1
print("\nInserting element 7 in index 1:")
print(np.insert(x1, [1], 22))

# Initialize array 'y1'
y1 = np.array([[3, 4], [11, 22]])
print("\nArray 'y1' is:")
print(y1)

# Delete the value at index 0
print("Delete the value at index 0 in array 'y1':")
print(np.delete(y1,0))
