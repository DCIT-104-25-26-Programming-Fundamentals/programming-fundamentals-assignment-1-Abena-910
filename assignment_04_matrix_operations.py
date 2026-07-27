def read_matrix(rows, cols, label=""):
    print(f"Enter {label} matrix:")
    matrix = []
    for i in range(rows):
        row_values = input(f"Enter row {i + 1}: ").split()
        row = [int(value) for value in row_values]
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    for row in matrix:
        print("  ".join(str(value) for value in row))
    print()


def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        result.append(new_row)
    return result


def add_matrices(matrix_a, matrix_b):
    rows = len(matrix_a)
    cols = len(matrix_a[0])
    result = []
    for i in range(rows):
        new_row = []
        for j in range(cols):
            new_row.append(matrix_a[i][j] + matrix_b[i][j])
        result.append(new_row)
    return result


def multiply_matrices(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            total = 0
            for k in range(cols_a):
                total += matrix_a[i][k] * matrix_b[k][j]
            new_row.append(total)
        result.append(new_row)
    return result


if __name__ == "__main__":
    
    print("PART A: Transpose a Matrix")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))
    matrix = read_matrix(rows, cols)

    print("\nOriginal Matrix:")
    print_matrix(matrix)

    print("Transposed Matrix:")
    transposed = transpose_matrix(matrix)
    print_matrix(transposed)

    print("PART B: Add Two Matrices")
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    matrix_a = read_matrix(rows, cols, label="first")
    matrix_b = read_matrix(rows, cols, label="second")

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("Matrix B:")
    print_matrix(matrix_b)

    print("Sum (A + B):")
    sum_result = add_matrices(matrix_a, matrix_b)
    print_matrix(sum_result)

    print("PART C: Multiply Two Matrices")
    rows_a = int(input("Enter number of rows for Matrix A: "))
    cols_a = int(input("Enter number of columns for Matrix A (= rows for Matrix B): "))
    cols_b = int(input("Enter number of columns for Matrix B: "))

    matrix_a = read_matrix(rows_a, cols_a, label="A")
    matrix_b = read_matrix(cols_a, cols_b, label="B")

    print("\nMatrix A:")
    print_matrix(matrix_a)
    print("Matrix B:")
    print_matrix(matrix_b)

    print("Product (A x B):")
    product_result = multiply_matrices(matrix_a, matrix_b)
    print_matrix(product_result)