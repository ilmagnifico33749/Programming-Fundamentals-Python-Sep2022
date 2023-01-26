rows, columns = [int(x) for x in input().split(" ")]

def matrix_creator(rows_number, columns_number, letters_starting_index):
    rows_number = rows_number
    columns_number = columns_number
    letters_starting_index = letters_starting_index
    matrix = [list() for x in range(rows_number)]

    [[matrix[rows].append(
        str((''.join([
            chr(letters_starting_index + rows),
            chr(letters_starting_index + rows + columns),
            chr(letters_starting_index + rows)
        ]))))
      for columns in range(columns_number)]
     for rows in range(rows_number)]

    [print(' '.join(matrix[row])) for row in range(len(matrix))]


matrix_creator(rows, columns, 97)

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
