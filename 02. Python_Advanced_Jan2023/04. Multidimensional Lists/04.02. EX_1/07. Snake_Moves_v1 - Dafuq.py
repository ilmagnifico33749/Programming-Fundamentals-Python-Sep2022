### Some weird observations are being made here.
### In the def sname_matrix, in the cycle, each time the var used to creating the first row is taken
### or if the first row itself is taken as value all the rows, incl the first one are being changed
### according to the last change make as per the ... thing I wrote here just for experiment with
### different things. To look in the internet what might be the reason for this.
### DAFUQ


# rows_num, columns_num = (int(x) for x in input().split(" "))
#snake = input()

#
rows_num = 5
columns_num = 6
snake = "SoftUni"

matrix_row = [x for x in snake]
print(matrix_row)
#

def empty_matrix_creator(rows_number, columns_number):
    rows_number = rows_number
    columns_number = columns_number
    return [[] for rows in range(rows_number)]

matrix = empty_matrix_creator(rows_num, columns_num)
print(matrix)

def snake_matrix(primary_matrix, rows_number, columns_number, snake):
    primary_matrix = primary_matrix
    rows_number = rows_number
    columns_number = columns_number
    snake = snake
    transitional_row = snake
    for rows in range(len(primary_matrix)):
        if rows == 0:
            primary_matrix[rows] = snake
            print(primary_matrix)
        else:
            for times in range(rows):
                transitional_row = snake
                print(f"Current Row: {rows}")
                print(f"Previous Row: {primary_matrix[rows-1]}")
                print(f"Current Row: {primary_matrix[rows]}")
                print(50 * '*')
                transitional_row = primary_matrix[rows-1]
                print(f"Transitional Row: {transitional_row}")
                last_symbol_prev_row = transitional_row.pop(-1)
                print(f"Symbol Preview: {last_symbol_prev_row}")
                print(f"Again Previous Row: {primary_matrix[rows-1]}")
                transitional_row.reverse()
                transitional_row.insert((len(transitional_row)), last_symbol_prev_row)
                print(f"New Row 2: {transitional_row}")
                print(f"New Row 3: {transitional_row}")
                print(f"Again Previous Row: {primary_matrix[rows-1]}")
                # primary_matrix[rows].append([x for x in transitional_row])

            primary_matrix[rows] = transitional_row
            transitional_row.clear()
            print(f"Matrix: {primary_matrix}")
        print(50 * "-")
    print(primary_matrix)


snake_matrix(matrix, rows_num, columns_num, matrix_row)

# def snake_matrix(rows_number, columns_number):
#     rows_number = rows_number
#     columns_number = columns_number
#
#     SoftUn i
#     --
#     inUtfoS
#     --
#     UtfoSi n
#     niSoft U
#     foSinU t
#     tUniSo f
#
#
# matrix = snake_matrix(rows_num, columns_num)


# #########
# Input_1:
# 5 6
# SoftUni
# ---------
# Output_1:
# SoftUn
# UtfoSi
# niSoft
# foSinU
# tUniSo
# #########
# Input_2:
# 1 4
# Python
# ---------
# Output_2:
# Pyth
# #########
