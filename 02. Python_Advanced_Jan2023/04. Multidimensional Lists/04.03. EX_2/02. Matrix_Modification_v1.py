def matrix_creator(rows_number):
    rows_number = rows_number
    matrix_created = [[int(x) for x in input().split()] for rows in range(rows_number)]
    return matrix_created


matrix = matrix_creator(int(input()))


def matrix_modification(primary_matrix):
    primary_matrix = primary_matrix
    command = input()
    while command != "END":
        command_instruction, command_row, command_column, command_value = command.split()
        coordinates_validity = True
        if 0 <= int(command_row) <= (len(primary_matrix)-1) and 0 <= int(command_column) <= (len(primary_matrix[int(command_row)]) - 1):
            coordinates_validity = True
        else:
            coordinates_validity = False

        if coordinates_validity is False:
            print(f"Invalid coordinates")
            # break
        else:
            if command_instruction == "Add":
                primary_matrix[int(command_row)][int(command_column)] += int(command_value)
            elif command_instruction == "Subtract":
                primary_matrix[int(command_row)][int(command_column)] -= int(command_value)
        command = input()

    else:
        [print(' '.join(map(str, row))) for row in matrix]


matrix_modification(matrix)


# ################
# Input_1:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# Add 0 0 5
# Subtract 1 1 2
# END
# ---------------
# Output_1:
# 6 2 3
# 4 3 6
# 7 8 9
# ################
# Input_2:
# 4
# 1 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 1
# Add 4 4 100
# Add 3 3 100
# Subtract -1 -1 42
# Subtract 0 0 42
# END
# ---------------
# Output_2:
# Invalid coordinates
# Invalid coordinates
# -41 2 3 4
# 5 6 7 8
# 8 7 6 5
# 4 3 2 101
# ################
