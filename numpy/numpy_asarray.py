import numpy as np

# Convert a list into an array
a = [1, 2]
arr = np.asarray(a)
print("Array created from a list:")
print(arr)

# Existing arrays are not copied
a = np.array([1, 2])
print("Existing arrays are not copied:")
print(np.asarray(a) is a)

# If dtype is set, array is copied only if dtype does not match
a = np.array([1, 2], dtype=np.float32)
print("If dtype is set, array is copied only if dtype does not match:")
print(np.asarray(a, dtype=np.float32) is a)
print(np.asarray(a, dtype=np.float64) is a)

# Contrary to asanyarray, ndarray subclasses are not passed through
print("Contrary to asanyarray, ndarray subclasses are not passed through:")
print(issubclass(np.recarray, np.ndarray))
a = np.array([(1.0, 2), (3.0, 4)], dtype='f4,i4').view(np.recarray)
print(np.asarray(a) is a)
print(np.asanyarray(a) is a)