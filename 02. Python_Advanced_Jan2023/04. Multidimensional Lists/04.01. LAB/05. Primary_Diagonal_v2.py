rows_num = int(input())

matrix = [[int(x) for x in input().split(" ")] for _ in range(rows_num)]

print(sum([int(matrix[rows][rows]) for rows in range(rows_num)]))

# #########
# Input_1:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# ---------
# Output_1:
# 4
# #########
# Input_2:
# 3
# 1 2 3
# 4 5 6
# 7 8 9
# ---------
# Output_2:
# 15
# #########
