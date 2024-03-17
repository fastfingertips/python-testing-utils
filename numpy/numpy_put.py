import numpy as np

# Define the target array
a = np.arange(5)

# Replace elements at specified indices with given values
np.put(a, [0, 2], [-44, -55])
print("Modified Array 1:", a)

# Define the target array again
a = np.arange(5)

# Replace elements at specified out-of-bounds index with given value using clip mode
np.put(a, 22, -5, mode='clip')
print("Modified Array 2:", a)
