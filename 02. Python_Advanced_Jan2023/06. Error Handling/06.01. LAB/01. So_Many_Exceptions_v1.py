### Initial_Code_with_Errors_To_Redact
# numbers_list = int(input()).split(", ")
# result = 1
#
# for i in range(numbers_list):
#     number = numbers_list[i+1]
#     if number <= 5 result *= number
#     elif 5 < number <= 10:
#
# result /= number
#
# print(total)
### --------------------------------------
### Redacted_Code:
numbers_list = list(map(int, (input().split(", "))))
result = 1

for i in range(len(numbers_list)):
    number = numbers_list[i]
    if number <= 5:
        result *= number
    elif 5 < number <= 10:
        result /= number

print(result)


# #################################
# Test_Code_1:
# 2, 5, 10
# ---------------------------------
# Output_1:
# 1.0
# #################################
# Test_Code_2:
# 4, 5, 6, 1, 3
# ---------------------------------
# Output_2:
# 10.0
# #################################
# Test_Code_3:
# 1, 4, 5
# ---------------------------------
# Output_3:
# 20.0
# #################################
# Test_Code_4:
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
# ---------------------------------
# Output_4:
# 0.003968253968253968
# #################################
