import numpy as np

def main():
    # Example: Finding the maximum value of an array
    arr = np.array([[0, 1], [2, 3]])
    print("Example - Finding the maximum value of an array:")
    print("Array:")
    print(arr)
    print("Maximum value of the array (flattened):", np.max(arr))
    print()

    # Example: Finding the maximum value along the first axis
    print("Example - Finding the maximum value along the first axis:")
    print("Maxima along the first axis:", np.max(arr, axis=0))
    print()

    # Example: Finding the maximum value along the second axis
    print("Example - Finding the maximum value along the second axis:")
    print("Maxima along the second axis:", np.max(arr, axis=1))
    print()

    # Example: Finding the maximum value with conditions and initial value
    print("Example - Finding the maximum value with conditions and initial value:")
    b = np.arange(5, dtype=float)
    b[2] = np.nan
    print("Array with NaN value:")
    print(b)
    print("Maximum value ignoring NaNs:", np.max(b, where=~np.isnan(b), initial=-1))
    print()

if __name__ == "__main__":
    main()