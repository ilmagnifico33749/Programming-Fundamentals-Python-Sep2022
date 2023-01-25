rows, columns = [int(x) for x in input().split(' ')]
squares_matrix_size = 2


def primary_matrix(rows_number):
    rows_number = rows_number
    matrix = [[str(x) for x in input().split(' ')] for row in range(rows_number)]

    return matrix


matrix = primary_matrix(rows)


def square_matrix(primary_matrix, squares_size):
    primary_matrix = primary_matrix
    squares_size = squares_size
    starting_index = 0
    square_matrix = [(primary_matrix[row][starting_index:(starting_index + 2)]) for row in range(squares_size)]

    return square_matrix

# def flattenned_matrix(not_flat_matrix):
#     not_flat_matrix = not_flat_matrix
#     flattened_square_matrix = [num for row in not_flat_matrix for num in row]

def finding(matrix):
    #Suitable for regular matrix, not flattened
    matrix = matrix
    count_identical = 0
    identical = True
    first_symbol = matrix[0][0]
    for rows in range(len(matrix)):
        for elements in range(len(matrix[rows])):
            current_element = matrix[rows][elements]
            if first_symbol != current_element:
                identical = False
                break
    if identical == True:
        count_identical += 1

    return count_identical


def iterating_sqmatrix_within_Matrix(primary_matrix, square_matrix_size):
    total_count = 0
    primary_matrix = primary_matrix
    square_matrix_size = squares_matrix_size
    count_identical = 0
    for rows in range(len(primary_matrix) - 1):
        for columns in range(len(matrix[rows]) - 1):
            # print(f"Current Symbol: {matrix[rows][columns]}")
            current_matrix = [(primary_matrix[rows][columns:(columns + 2)]) for rows in
                              range(rows, (rows + squares_matrix_size))]
            # flat_matrix = flattenned_matrix(current_matrix)
            # identicity_result = finding(flat_matrix)
            identicity_result = finding(current_matrix)
            total_count += identicity_result

    return total_count


print(iterating_sqmatrix_within_Matrix(matrix, squares_matrix_size))

# #########
# Input_1:
# 3 4
# A B B D
# E B B B
# I J B B
# ---------
# Output_1:
# 2
# #########
# Input_2:
# 2 2
# a b
# c d
# ---------
# Output_2:
# 0
# #########
# Input_3:
# 5 4
# A A B D
# A A B B
# I J B B
# C C C G
# C C K P
# ---------
# Output_3:
# 3
# #########
