rows_num, columns_num = [int(x) for x in input().split(' ')]
square_matrix_size = 3

def matrix_creator(rows_number):
    rows_number = rows_number
    created_matrix = [[int(x) for x in input().split(' ')] for rows in range(rows_number)]

    return created_matrix


matrix = matrix_creator(rows_num)

def iterator_sqmatrix_within_matrix(primary_matrix, square_size):
    primary_matrix = primary_matrix
    square_size = square_size
    highest_sum_matrix = []
    highest_sum = 0
    for rows in range(len(primary_matrix)-(square_size-1)):
        for columns in range(len(primary_matrix[rows])-(square_size-1)):
            current_matrix = [(primary_matrix[rows][columns:(columns + square_size)]) for rows in
                                     range(rows, (rows + square_size))]
            flattened_square_matrix = [num for row in current_matrix for num in row]
            sum_current_flattenned_sq_matrix = sum(flattened_square_matrix)
            if highest_sum < sum_current_flattenned_sq_matrix:
                highest_sum = sum_current_flattenned_sq_matrix
                highest_sum_matrix = current_matrix

    print(f"Sum = {highest_sum}")
    ([print(' '.join(list(map(str, highest_sum_matrix[row])))) for row in range(len(highest_sum_matrix))])

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
