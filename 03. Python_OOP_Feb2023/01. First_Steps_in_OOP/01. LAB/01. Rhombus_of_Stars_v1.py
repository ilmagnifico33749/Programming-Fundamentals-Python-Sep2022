import math
n = int(input())

def rombus_drawing(size, symbol_to_print):
    matrix_size = size
    rombus_matrix = []
    symbol_to_print = symbol_to_print

    def upper_part():
        for times in range(1, matrix_size, 1):
            free_space = (math.ceil(size)-times)
            current_row_matrix = free_space * ' ' + times * symbol_to_print
            rombus_matrix.append(current_row_matrix)

    def mid_part():
        rombus_matrix.append(matrix_size * "* ")

    def lower_part():
        for times in range(matrix_size-1, 0, -1):
            free_space = (math.ceil(size)-times)
            current_row_matrix = free_space * ' ' + times * symbol_to_print
            rombus_matrix.append(current_row_matrix)

    upper_part(), mid_part(), lower_part()

    matrix_printing = [print(''.join(row)) for row in rombus_matrix]
    return matrix_printing


rombus_drawing(n, "* ")
