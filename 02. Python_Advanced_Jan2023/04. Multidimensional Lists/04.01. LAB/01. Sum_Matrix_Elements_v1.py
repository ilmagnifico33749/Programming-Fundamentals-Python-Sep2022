rows, columns = [int(x) for x in input().split(", ")]

matrix = []

for row in range(rows):
    matrix.append([int(x) for x in input().split(", ")])

print(sum([sum(matrix[index]) for index in range(len(matrix))]))
# or
# print(sum([sum(element) for element in matrix]))

print(matrix)

# ###
# Input_1:
# 3, 6
# 7, 1, 3, 3, 2, 1
# 1, 3, 9, 8, 5, 6
# 4, 6, 7, 9, 1, 0
# ---
# Output:
# 76
# [[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
# ###

