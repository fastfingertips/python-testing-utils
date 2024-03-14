import numpy as np

def create_zeros_matrix():
    """
    Creates a zeros matrix based on user input for dimensions.
    """
    try:
        rows = int(input("Enter the number of rows: "))
        cols = int(input("Enter the number of columns: "))
        zeros_matrix = np.zeros((rows, cols))
        return zeros_matrix
    except ValueError:
        print("Please enter valid integer values for rows and columns.")
        return None

def main():
    zeros_matrix = create_zeros_matrix()
    if zeros_matrix is not None:
        print("Zeros Matrix:")
        print(zeros_matrix)

if __name__ == "__main__":
    main()
