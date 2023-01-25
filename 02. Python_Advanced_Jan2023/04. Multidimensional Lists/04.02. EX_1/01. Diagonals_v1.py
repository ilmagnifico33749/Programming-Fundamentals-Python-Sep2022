matrix = [[int(x) for x in input().split(', ')] for x in range(int(input()))]

first_diagonal = [str(matrix[row][row]) for row in range(len(matrix))]
second_diagonal = [str(matrix[row][(-1) - int(row)]) for row in range(len(matrix))]
print(f"Primary diagonal: {', '.join(first_diagonal)}. Sum: {sum([int(x) for x in first_diagonal])}")
print(f"Secondary diagonal: {', '.join(second_diagonal)}. Sum: {sum([int(x) for x in second_diagonal])}")

# #####################################
# Input_1:
# 3
# 1, 2, 3
# 4, 5, 6
# 7, 8, 9
# -------------------------------------
# Output_1:
# Primary diagonal: 1, 5, 9. Sum: 15
# Secondary diagonal: 3, 5, 7. Sum: 15
# #####################################
