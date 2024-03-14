import numpy as np

def main():
    # Example 1: Creating an array of zeros with shape (5,)
    arr1 = np.zeros(5)
    print("Example 1 - Creating an array of zeros with shape (5,):")
    print(arr1)
    print()

    # Example 2: Creating an array of zeros with shape (5,) and dtype=int
    arr2 = np.zeros((5,), dtype=int)
    print("Example 2 - Creating an array of zeros with shape (5,) and dtype=int:")
    print(arr2)
    print()

    # Example 3: Creating an array of zeros with shape (2, 1)
    arr3 = np.zeros((2, 1))
    print("Example 3 - Creating an array of zeros with shape (2, 1):")
    print(arr3)
    print()

    # Example 4: Creating an array of zeros with custom dtype
    arr4 = np.zeros((2,), dtype=[('x', 'i4'), ('y', 'i4')])
    print("Example 4 - Creating an array of zeros with custom dtype:")
    print(arr4)
    print()

if __name__ == "__main__":
    main()