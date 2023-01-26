rows_num, columns_num = (int(x) for x in input().split(" "))


def matrix_creator(rows_number):
    rows_number = rows_number
    matrix = [[str(x) for x in input().split(" ")] for rows in range(rows_number)]
    return matrix


matrix = matrix_creator(rows_num)


def matrix_shuffler(primary_matrix):
    primary_matrix = primary_matrix
    command = input()

    while command != "END":
        command_details = command.split(" ")
        command_instruction = command_details[0]
        command_validity = True

        if command_instruction == "swap" and len(command_details) == 5:
            el_1_row = int(command_details[1])
            el_1_col = int(command_details[2])
            el_2_row = int(command_details[3])
            el_2_col = int(command_details[4])
            if el_1_row < 0 or el_1_col < 0 or el_2_row < 0 or el_2_col < 0:
                command_validity = False
            if el_1_row > rows_num or el_1_col > columns_num or el_2_row > rows_num or el_2_col > columns_num:
                command_validity = False
        else:
            command_validity = False

        if command_validity == True:
            primary_matrix[el_1_row][el_1_col], primary_matrix[el_2_row][el_2_col] = \
                primary_matrix[el_2_row][el_2_col], primary_matrix[el_1_row][el_1_col]
            [print(' '.join(map(str, primary_matrix[row]))) for row in range(len(primary_matrix))]
        else:
            print(f"Invalid input!")

        command = input()


matrix_shuffler(matrix)

# ##############
# Input_1:
# 2 3
# 1 2 3
# 4 5 6
# swap 0 0 1 1
# swap 10 9 8 7
# swap 0 1 1 0
# END
# --------------
# Output_1:
# 5 2 3
# 4 1 6
# Invalid input!
# 5 4 3
# 2 1 6
# ##############
# Input_2:
# 1 2
# Hello World
# 0 0 0 1
# swap 0 0 0 1
# swap 0 1 0 0
# END
# --------------
# Output_2:
# Invalid input!
# World Hello
# Hello World
# ##############
