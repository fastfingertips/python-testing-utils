import numpy as np

def main():
    # Example: Finding the minimum value of an array
    arr = np.array([[0, 1], [2, 3]])
    print("Example - Finding the minimum value of an array:")
    print("Array:")
    print(arr)
    print("Minimum value of the array (flattened):", np.min(arr))
    print()

    # Example: Finding the minimum value along the first axis
    print("Example - Finding the minimum value along the first axis:")
    print("Minima along the first axis:", np.min(arr, axis=0))
    print()

    # Example: Finding the minimum value along the second axis
    print("Example - Finding the minimum value along the second axis:")
    print("Minima along the second axis:", np.min(arr, axis=1))
    print()

    # Example: Finding the minimum value with conditions and initial value
    print("Example - Finding the minimum value with conditions and initial value:")
    b = np.arange(5, dtype=float)
    b[2] = np.nan
    print("Array with NaN value:")
    print(b)
    print("Minimum value ignoring NaNs:", np.min(b, where=~np.isnan(b), initial=10))
    print()

if __name__ == "__main__":
    main()