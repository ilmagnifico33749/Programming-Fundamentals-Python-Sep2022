def matrix_reader():
    number_rows = int(input())
    matrix = [[x for x in input()] for rows in range(number_rows)]

    return matrix

matrix = matrix_reader()

def check_matrix_special_symbol(matrix_to_check):
    matrix_to_check = matrix_to_check
    special_symbol = input()
    symbol_found = False

    for row in range(len(matrix_to_check)):
        for column in range(len(matrix_to_check[row])):
            current_element = matrix_to_check[row][column]
            if current_element == special_symbol:
                symbol_found = False
                return row, column

    if symbol_found is False:
        return f"{special_symbol} does not occur in the matrix"

print(check_matrix_special_symbol(matrix))

# ##############################
# Input_1:
# 3
# ABC
# DEF
# X!@
# !
# ------------------------------
# Output_1:
# (2, 1)
# ##############################
# Input_2:
# 4
# asdd
# xczc
# qwee
# qefw
# 4
# ------------------------------
# Output_2:
# 4 does not occur in the matrix
# ##############################
