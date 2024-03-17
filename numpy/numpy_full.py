import numpy as np

# Create a new array filled with np.inf (infinity)
arr = np.full((3, 3), np.inf)
print("Array filled with np.inf (infinity):")
print(arr)

# Create a new array filled with a float value 10.1
arr = np.full((3, 3), 10.1)
print("Array filled with float value 10.1:")
print(arr)

# Create a new array filled with integer value 55, with dtype=int explicitly specified
arr = np.full((3, 3), 55, dtype=int)
print("Array filled with integer value 55, dtype=int:")
print(arr)

# Create a new array of the specified shape and type, filled with fill_value
arr = np.full((2, 2), np.inf)
print("Array with infinity values:")
print(arr)

# Create a new array of the specified shape and type, filled with fill_value
arr = np.full((2, 2), 10)
print("Array filled with 10s:")
print(arr)

# Create a new array of the specified shape and type, filled with fill_value
arr = np.full((2, 2), [1, 2])
print("Array filled with [1, 2]:")
print(arr)