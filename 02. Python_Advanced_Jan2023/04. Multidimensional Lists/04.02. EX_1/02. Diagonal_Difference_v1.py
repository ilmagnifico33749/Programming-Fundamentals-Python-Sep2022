matrix = [[int(x) for x in input().split()] for rows in range(int(input()))]

sum_diagonal_1 = sum([matrix[row][row] for row in range(len(matrix))])
sum_diagonal_2 = sum([matrix[row][(-1) - row] for row in range(len(matrix))])
difference_sums_rows = abs(sum_diagonal_1 - sum_diagonal_2)
print(difference_sums_rows)

# #############
# Input_1:
# 3
# 11 2 4
# 4 5 6
# 10 8 -12
# -------------
# Output_1:
# 15
# #############
# Input_2:
# 4
# -7 14 9 -20
# 3 4 9 21
# -14 6 8 44
# 30 9 7 -14
# -------------
# Output_2:
# 34
# #############
