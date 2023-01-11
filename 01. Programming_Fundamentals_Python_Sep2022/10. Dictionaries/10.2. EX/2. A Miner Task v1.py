
my_dict = {}
resourse_name = input()
while resourse_name != "stop":
    resourse_quantity = int(input())
    if resourse_name not in my_dict:
        my_dict[resourse_name] = resourse_quantity
    else:
        my_dict[resourse_name] += resourse_quantity
    resourse_name = input()
for resourse in my_dict.keys():
    print(f"{resourse} -> {my_dict[resourse]}")

# ------------#
# Input_1:
# Gold
# 155
# Silver
# 10
# Copper
# 17
# stop
# --
# Output_1:
# Gold -> 155
# Silver -> 10
# Copper -> 1
# -------------#
# input_2:
# gold
# 155
# silver
# 10
# copper
# 17
# gold
# 15
# stop
# Output_2:
# gold -> 170
# silver -> 10
# copper -> 17
# -------------#
