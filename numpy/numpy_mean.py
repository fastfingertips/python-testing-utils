import numpy as np

# Example data
a = np.array([[1, 2], [3, 4]])

# Compute mean of the entire array
mean_all = np.mean(a)
print("Mean of the entire array:", mean_all)

# Compute mean along the first axis (columns)
mean_axis_0 = np.mean(a, axis=0)
print("Mean along the first axis (columns):", mean_axis_0)

# Compute mean along the second axis (rows)
mean_axis_1 = np.mean(a, axis=1)
print("Mean along the second axis (rows):", mean_axis_1)

# Example with float32 data
b = np.zeros((2, 512*512), dtype=np.float32)
b[0, :] = 1.0
b[1, :] = 0.1
mean_float32 = np.mean(b)
print("Mean with float32 data:", mean_float32)

# Example with specifying dtype=float64 for more accurate computation
mean_float64 = np.mean(b, dtype=np.float64)
print("Mean with float64 data for more accurate computation:", mean_float64)

# Example with where argument
c = np.array([[5, 9, 13], [14, 10, 12], [11, 15, 19]])
mean_with_where = np.mean(c, where=[[True], [False], [False]])
print("Mean with where argument:", mean_with_where)