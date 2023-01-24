### !!! Getting 80/100 in Judge because Judge is being Judge ...

number_rows_columns = int(input())
matrix = [[x for x in input()] for rows in range(number_rows_columns)]
symbol_to_find = input()
found = False

for rows in range(number_rows_columns):
    for indexes in range(len(matrix[rows])):
        current_symbol = matrix[rows][indexes]
        if current_symbol == symbol_to_find:
            found = True
            print(f"({rows}, {indexes})")
            break

if found is False:
    print(f"{symbol_to_find} does not occur in the matrix")

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
