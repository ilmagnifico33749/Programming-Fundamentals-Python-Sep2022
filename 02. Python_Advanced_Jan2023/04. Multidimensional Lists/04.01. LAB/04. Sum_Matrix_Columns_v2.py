rows_num, columns_num = [int(x) for x in input().split(", ")]

matrix = [[int(x) for x in input().split(" ")] for _ in range(rows_num)]

[print(sum([matrix[rows][number_symbols] for rows in range(rows_num)])) for number_symbols in range(columns_num)]

# ############
# Input_1:
# 3, 6
# 7 1 3 3 2 1
# 1 3 9 8 5 6
# 4 6 7 9 1 0
# ------------
# Output_1:
# 12
# 10
# 19
# 20
# 8
# 7
# ############
# Input_2:
# 3, 3
# 1 2 3
# 4 5 6
# 7 8 9
# ------------
# Output_2:
# 12
# 15
# 18
# ############
