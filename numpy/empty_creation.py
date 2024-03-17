import numpy as np

# Create an empty array of size 3
empty_array = np.empty(3)
print("Empty array of size 3:")
print(empty_array)

# Create an empty array of size 4
empty_array = np.empty(4)
print("\nEmpty array of size 4:")
print(empty_array)

# Create an empty 2D array of size (3, 3)
empty_array = np.empty([3, 3])
print("\nEmpty 2D array of size (3, 3):")
print(empty_array)

# Create an empty 2D array of size (3, 4)
empty_array = np.empty([3, 4])
print("\nEmpty 2D array of size (3, 4):")
print(empty_array)

# Create an empty 2D array of size (2, 2) with dtype=int
empty_array = np.empty([2, 2], dtype=int)
print("\nEmpty 2D array of size (2, 2) with dtype=int:")
print(empty_array)

# Create an empty 2D array of size (2, 2) with dtype=float
empty_array = np.empty([2, 2], dtype=float)
print("\nEmpty 2D array of size (2, 2) with dtype=float:")
print(empty_array)

# Create an empty array with a custom data type
dt = np.dtype([('Name', np.str_, 16), ('Age', np.int32), ('Salary', np.float64)])
custom_empty_array = np.empty((2, 3), dtype=dt)
print("\nEmpty array with a custom data type:")
print(custom_empty_array)
