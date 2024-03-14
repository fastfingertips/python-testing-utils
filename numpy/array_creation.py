import numpy as np

def main():
    # Example 1: Creating an array from a list
    arr1 = np.array([1, 2, 3])
    print("Example 1 - Creating an array from a list:")
    print(arr1)
    print()

    # Example 2: Upcasting
    arr2 = np.array([1, 2, 3.0])
    print("Example 2 - Upcasting:")
    print(arr2)
    print()

    # Example 3: Creating a multi-dimensional array
    arr3 = np.array([[1, 2], [3, 4]])
    print("Example 3 - Creating a multi-dimensional array:")
    print(arr3)
    print()

    # Example 4: Specifying minimum dimensions
    arr4 = np.array([1, 2, 3], ndmin=2)
    print("Example 4 - Specifying minimum dimensions:")
    print(arr4)
    print()

    # Example 5: Specifying data type
    arr5 = np.array([1, 2, 3], dtype=complex)
    print("Example 5 - Specifying data type:")
    print(arr5)
    print()

    # Example 6: Creating an array from structured data type
    x = np.array([(1,2),(3,4)], dtype=[('a','<i4'),('b','<i4')])
    print("Example 6 - Creating an array from structured data type:")
    print(x)
    print("Accessing 'a' field:")
    print(x['a'])
    print()

    # Example 7: Creating an array from a sub-class
    arr7 = np.array(np.asmatrix('1 2; 3 4'))
    print("Example 7 - Creating an array from a sub-class:")
    print(arr7)
    print()

if __name__ == "__main__":
    main()
