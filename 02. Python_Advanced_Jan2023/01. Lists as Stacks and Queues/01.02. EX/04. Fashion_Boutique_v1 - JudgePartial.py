# !!!!!! Getting  60 / 100 on Judge, to verify why

box_with_clothes = list(map(int, input().split(" ")))
single_rack_capacity = int(input())
rack_count = 1

while box_with_clothes:
    current_rack_capacity = single_rack_capacity
    for cloth in range(len(box_with_clothes)):
        cloth_size = box_with_clothes.pop()
        if cloth_size < current_rack_capacity:
            current_rack_capacity -= cloth_size
        else:
            rack_count += 1
            current_rack_capacity = single_rack_capacity
            current_rack_capacity -= cloth_size

print(rack_count)

# ##############################
# ##############################
# Input_1:
# 5 4 8 6 3 8 7 7 9
# 16
# ------------------------------
# Output_1:
# 5
# ##############################
# Input_2:
# 1 7 8 2 5 4 7 8 9 6 3 2 5 4 6
# 20
# ------------------------------
# Output_2:
# 5
# ##############################
# ##############################
