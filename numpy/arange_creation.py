import numpy as np

def main():
    # Example 1: arange(stop)
    arr1 = np.arange(3)
    print("Example 1 - arange(stop):")
    print(arr1)
    print()

    # Example 2: arange(stop) with floating point argument
    arr2 = np.arange(3.0)
    print("Example 2 - arange(stop) with floating point argument:")
    print(arr2)
    print()

    # Example 3: arange(start, stop)
    arr3 = np.arange(3, 7)
    print("Example 3 - arange(start, stop):")
    print(arr3)
    print()

    # Example 4: arange(start, stop, step)
    arr4 = np.arange(3, 7, 2)
    print("Example 4 - arange(start, stop, step):")
    print(arr4)
    print()

if __name__ == "__main__":
    main()
