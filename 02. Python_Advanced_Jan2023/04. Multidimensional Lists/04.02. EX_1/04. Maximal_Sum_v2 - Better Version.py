rows_num, columns_num = [int(x) for x in input().split(' ')]
square_matrix_size = 3

def matrix_creator(rows_number):
    rows_number = rows_number
    created_matrix = [[int(x) for x in input().split(' ')] for rows in range(rows_number)]
    return created_matrix


matrix = matrix_creator(rows_num)


def square_matrix_creator(primary_matrix, square_size, starting_row, starting_column):
    primary_matrix = primary_matrix
    square_size = square_size
    starting_row = starting_row
    starting_column = starting_column
    square_matrix_created = [(primary_matrix[rows][starting_column:(starting_column+square_size)]) for rows in range(starting_row, (starting_row+square_size))]
    return square_matrix_created


def flattening_matrix(primary_matrix):
    primary_matrix = primary_matrix
    flattened_matrix = [num for row in primary_matrix for num in row]
    return flattened_matrix


def iterator_sqmatrix_within_matrix(primary_matrix, square_size):
    primary_matrix = primary_matrix
    square_size = square_size
    matrix_with_highest_sum = []
    highest_sum_matrix = 0
    for rows in range(len(primary_matrix)-(square_size-1)):
        starting_row = rows
        for columns in range(len(primary_matrix[rows])-(square_size-1)):
            starting_column = columns
            current_matrix = square_matrix_creator(primary_matrix, square_size, starting_row, starting_column)
            sum_current_matrix = sum(flattening_matrix(current_matrix))
            if highest_sum_matrix < sum_current_matrix:
                highest_sum_matrix = sum_current_matrix
                matrix_with_highest_sum.clear()
                matrix_with_highest_sum = current_matrix

    print(f"Sum = {highest_sum_matrix}")
    [print(' '.join(list(map(str, matrix_with_highest_sum[row])))) for row in range(len(matrix_with_highest_sum))]


iterator_sqmatrix_within_matrix(matrix,square_matrix_size)

# ############
# Input_1:
# 4 5
# 1 5 5 2 4
# 2 1 4 14 3
# 3 7 11 2 8
# 4 8 12 16 4
# ------------
# Output_1:
# Sum = 75
# 1 4 14
# 7 11 2
# 8 12 16
# ############
# Input_2:
# 5 6
# 1 0 4 3 1 1
# 1 3 1 3 0 4
# 6 4 1 2 5 6
# 2 2 1 5 4 1
# 3 3 3 6 0 5
# ------------
# Output_2:
# Sum = 34
# 2 5 6
# 5 4 1
# 6 0 5
# ############
