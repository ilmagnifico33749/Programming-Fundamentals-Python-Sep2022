def recursive_power (num_1, num_2):
    result = 1
    if num_2 == 0:
        return result
    # result = num_1 * recursive_power(num_1, num_2 - 1)
    # return result
    return num_1 * recursive_power(num_1, num_2 - 1)

# ###
# Test_Code_1:
print(recursive_power(2, 10))
# ---
# Output_1:
# 1024
# ###
# ###
# Test_Code_2:
print(recursive_power(10, 100))
# ---
# Output_2:
# 10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
# ###
