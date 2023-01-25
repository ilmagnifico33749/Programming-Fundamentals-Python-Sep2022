num_rows, num_columns =[int(x) for x in input().split(", ")]


def matrix_reader(number_rows):
    number_rows = number_rows
    matrix = [[int(x) for x in input().split(", ")] for rows in range(number_rows)]
    return matrix


matrix = matrix_reader(num_rows)


def finding_biggest_sq_submatrix(number_columns, original_matrix):
    original_matrix = original_matrix
    number_columns = number_columns
    square_submatrix_size = 2
    highest_sum_square_submatrix = 0
    submatrix_with_highest_sum = []

    for rows in range(len(original_matrix)-1):
        for columns in range(number_columns - 1):
            submatrix = [original_matrix[current_row][columns:columns+square_submatrix_size] for current_row in range(rows, rows + square_submatrix_size)]
            flattened_submatrix = [num for row in submatrix for num in row]
            sum_flattened_submatrix = sum(flattened_submatrix)
            if sum_flattened_submatrix > highest_sum_square_submatrix:
                highest_sum_square_submatrix = sum_flattened_submatrix
                submatrix_with_highest_sum.clear()
                submatrix_with_highest_sum = submatrix

    [print(' '.join([str(x) for x in submatrix_with_highest_sum[element]])) for element in range(len(submatrix_with_highest_sum))]
    print(highest_sum_square_submatrix)


finding_biggest_sq_submatrix(num_columns, matrix)

# ################
# Input_1:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# ----------------
# Output_1:
# 9 8
# 7 9
# 33
# ################
# Input_2:
# 2, 4
# 10, 11, 12, 13
# 14, 15, 16, 17
# ----------------
# Output_2:
# 12 13
# 16 17
# 58
# ################
