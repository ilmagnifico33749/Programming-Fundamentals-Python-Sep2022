from _collections import deque

rows_num, columns_num = [int(x) for x in input().split()]
word = list(input())

word_copy = deque(word)

for row in range(rows_num):
    while len(word_copy) < columns_num:
        word_copy.extend(word)

    if row % 2 == 0:
        print(*[word_copy.popleft() for _ in range(columns_num)], sep="")
    else:
        print(*[word_copy.popleft() for _ in range(columns_num)][::-1], sep="")

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


