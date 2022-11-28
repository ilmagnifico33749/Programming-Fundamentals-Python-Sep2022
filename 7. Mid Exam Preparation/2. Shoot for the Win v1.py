targets_sequence = list(map(int, input().split(" ")))
count_targets_shot = 0

command = int(input())
while command != "End":
    target_to_shoot = int(command)
    for target_one in range(len(targets_sequence)):
        if target_one == target_to_shoot and targets_sequence[target_one] != "NOT":
            count_targets_shot += 1
            current_target_value = targets_sequence[target_to_shoot]
            targets_sequence[target_to_shoot] = "NOT"
            for target_two in range(len(targets_sequence)):
                if targets_sequence[target_two] != "NOT":
                    if targets_sequence[target_two] <= current_target_value:
                        targets_sequence[target_two] += current_target_value
                    elif targets_sequence[target_two] > current_target_value:
                        targets_sequence[target_two] -= current_target_value
        else:
            pass
    command = input()
else:
    for target in range(len(targets_sequence)):
        if targets_sequence[target] == "NOT":
            targets_sequence[target] = -1
    print(f"Shot targets: {count_targets_shot} -> {' '.join(list(map(str, targets_sequence)))}")

# ---------------------------------------#
# Input_1:
# 24 50 36 70
# 0
# 4
# 3
# 1
# End
# Output_1:
# Shot targets 3 -> -1 -1 130 -1
# ---------------------------------------#
# Input_2:
# 30 30 12 60 54 66
# 5
# 2
# 4
# 0
# End
# Output_2:
# Shot targets: 4 -> -1 120 -1 66 -1 -1
# ---------------------------------------#
