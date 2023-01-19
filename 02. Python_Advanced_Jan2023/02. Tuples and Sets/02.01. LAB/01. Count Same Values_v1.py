numbers = tuple(map(float, input().split(" ")))
numbers_count = {}

for number in numbers:
    if number not in numbers_count:
        numbers_count[number] = 0
    numbers_count[number] += 1

[print(f"{key} - {value} times") for key,value in numbers_count.items()]

# #########################################
# Input_1:
# -2.5 4 3 -2.5 -5.5 4 3 3 -2.5 3
# Output_1:
# -2.5 - 3 times
# 4.0 - 2 times
# 3.0 - 4 times
# -5.5 - 1 times
# -----------------------------------------
# Input_2:
# 2 4 4 5 5 2 3 3 4 4 3 3 4 3 5 3 2 5 4 3
# Output_2:
# 2.0 - 3 times
# 4.0 - 6 times
# 5.0 - 4 times
# 3.0 - 7 times
# ###########################################