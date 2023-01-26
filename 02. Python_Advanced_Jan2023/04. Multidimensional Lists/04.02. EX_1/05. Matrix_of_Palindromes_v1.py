rows, columns = [int(x) for x in input().split(" ")]
element_size = 3

def matrix_creator(rows_number, columns_number, letters_starting_index):
    rows_number = rows_number
    columns_number = columns_number
    letters_starting_index = letters_starting_index
    matrix = [list() for x in range(rows_number)]
    for rows in range(rows_number):
        for columns in range(columns_number):
            first_letter = chr(letters_starting_index+rows)
            middle_letter = chr(letters_starting_index+rows+columns)
            last_letter = chr(letters_starting_index+rows)
            current_row = str((''.join([first_letter, middle_letter, last_letter])))
            matrix[rows].append(current_row)

    [print(' '.join(matrix[row])) for row in range(len(matrix))]


matrix_creator(rows, columns, 97)

# print(matrix_creator(rows, columns, 97))

#######################
# Input_1:
# 4 6
# -----------------------
# Output_1:
# aaa aba aca ada aea afa
# bbb bcb bdb beb bfb bgb
# ccc cdc cec cfc cgc chc
# ddd ded dfd dgd dhd did
# #######################
# Input_2:
# 3 2
# -----------------------
# Output_2:
# aaa aba
# bbb bcb
# ccc cdc
#######################
