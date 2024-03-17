import numpy as np

# Append values to the end of a 1D array
original_array = np.array([10, 20, 30])
values_to_append = np.array([40, 50, 60])
appended_array_1d = np.append(original_array, values_to_append)
print("1D Appended Array:", appended_array_1d)

# Append values to the end of a 2D array along axis 0
original_2d_array = np.array([[1, 2, 3], [4, 5, 6]])
values_2d_to_append = np.array([[7, 8, 9]])
appended_array_2d = np.append(original_2d_array, values_2d_to_append, axis=0)
print("2D Appended Array (axis=0):")
print(appended_array_2d)