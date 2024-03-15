import numpy as np

# Create a 1D array filled with ones
ones_1d = np.ones(5)
print("1D array of ones:")
print(ones_1d)

# Create a 1D array filled with ones of integer type
ones_int_1d = np.ones((5,), dtype=int)
print("\n1D array of ones with integer type:")
print(ones_int_1d)

# Create a 2D array filled with ones
ones_2d = np.ones((2, 1))
print("\n2D array of ones:")
print(ones_2d)

# Create a 2D array filled with ones with a specific shape
s = (2,2)
ones_custom_shape = np.ones(s)
print("\n2D array of ones with a custom shape:")
print(ones_custom_shape)