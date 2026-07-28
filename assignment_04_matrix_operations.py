# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.
#
# -----------------------------------------------------------------------------
# PART A — Transpose a Matrix
# -----------------------------------------------------------------------------
# - Read an M x N matrix from the user.
# - Compute and display its transpose (rows become columns, columns become rows).
#
# Example (2 x 3 input):
#
#   Original Matrix:      Transposed Matrix:
#   1  2  3               1  4
#   4  5  6               2  5
#                         3  6
#
# -----------------------------------------------------------------------------
# PART B — Add Two Matrices
# -----------------------------------------------------------------------------
# - Read two matrices of exactly the same size (M x N).
# - Compute their element-wise sum and display the result.
#   (Each position in the result = the sum of the values at that position
#    in both matrices.)
#
# -----------------------------------------------------------------------------
# PART C — Multiply Two Matrices
# -----------------------------------------------------------------------------
# - Read matrix A of size M x N and matrix B of size N x P.
#   (The number of COLUMNS in A must equal the number of ROWS in B.)
# - Compute and display the matrix product A × B (result is M x P).
#
# -----------------------------------------------------------------------------
# EXPECTED INPUT FORMAT
# -----------------------------------------------------------------------------
# When entering a row, the user types all values on one line separated by spaces:
#
#   Enter number of rows: 2
#   Enter number of columns: 3
#   Enter row 1: 1 2 3
#   Enter row 2: 4 5 6
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Use nested loops for all operations (no NumPy or other libraries).
# - Each operation must be in its own function (see scaffold below).
# - Display each matrix in a neat, aligned grid format.
# - Tip: Complete Part A first, then Parts B and C.
#

#
# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================
# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
# =============================================================================


def read_matrix(name, rows=None, cols=None):
    """Reads an M x N matrix from the user, row by row."""
    if rows is None:
        rows = int(input(f"Enter number of rows for {name}: "))
    if cols is None:
        cols = int(input(f"Enter number of columns for {name}: "))

    matrix = []
    for r in range(rows):
        while True:
            values = input(f"Enter row {r + 1}: ").split()
            if len(values) != cols:
                print(f"Error: expected {cols} values, got {len(values)}. Try again.")
                continue
            matrix.append([int(v) for v in values])
            break
    return matrix


def display_matrix(matrix, title="Matrix"):
    """Displays a matrix in a neat, aligned grid format."""
    print(f"\n{title}:")
    if not matrix:
        print("(empty)")
        return

    # find the widest number so every column lines up
    width = max(len(str(value)) for row in matrix for value in row)

    for row in matrix:
        line = "  ".join(str(value).rjust(width) for value in row)
        print(line)


def transpose(matrix):
    """Part A: Returns the transpose of a matrix using nested loops."""
    rows = len(matrix)
    cols = len(matrix[0])

    result = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            result[j][i] = matrix[i][j]

    return result


def add_matrices(matrix_a, matrix_b):
    """Part B: Returns the element-wise sum of two same-sized matrices."""
    rows = len(matrix_a)
    cols = len(matrix_a[0])

    result = [[0 for _ in range(cols)] for _ in range(rows)]

    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix_a[i][j] + matrix_b[i][j]

    return result


def multiply_matrices(matrix_a, matrix_b):
    """Part C: Returns the matrix product A x B using nested loops.

    A is M x N, B is N x P, result is M x P.
    """
    m = len(matrix_a)
    n = len(matrix_a[0])
    p = len(matrix_b[0])

    result = [[0 for _ in range(p)] for _ in range(m)]

    for i in range(m):
        for j in range(p):
            total = 0
            for k in range(n):
                total += matrix_a[i][k] * matrix_b[k][j]
            result[i][j] = total

    return result


def run_transpose():
    print("\n--- PART A: TRANSPOSE ---")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix("matrix", rows, cols)

    display_matrix(matrix, "Original Matrix")
    display_matrix(transpose(matrix), "Transposed Matrix")


def run_addition():
    print("\n--- PART B: MATRIX ADDITION ---")
    rows = int(input("Enter number of rows (both matrices): "))
    cols = int(input("Enter number of columns (both matrices): "))

    print("\nEnter values for Matrix A:")
    matrix_a = read_matrix("Matrix A", rows, cols)

    print("\nEnter values for Matrix B:")
    matrix_b = read_matrix("Matrix B", rows, cols)

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(add_matrices(matrix_a, matrix_b), "Sum (A + B)")


def run_multiplication():
    print("\n--- PART C: MATRIX MULTIPLICATION ---")
    m = int(input("Enter rows for Matrix A: "))
    n = int(input("Enter columns for Matrix A (= rows for Matrix B): "))
    p = int(input("Enter columns for Matrix B: "))

    print("\nEnter values for Matrix A:")
    matrix_a = read_matrix("Matrix A", m, n)

    print("\nEnter values for Matrix B:")
    matrix_b = read_matrix("Matrix B", n, p)

    display_matrix(matrix_a, "Matrix A")
    display_matrix(matrix_b, "Matrix B")
    display_matrix(multiply_matrices(matrix_a, matrix_b), "Product (A x B)")


def main():
    run_transpose()
    run_addition()
    run_multiplication()


if __name__ == "__main__":
    main()
