### !!! 72/100 (3 errors) in Judge, to verify why.

sequence_one = set(input().split(" "))
sequence_two = set(input().split(" "))

commands_number = int(input())
for commands in range(commands_number):
    command = input()
    command_details = command.split(" ")
    if command_details[0] == "Add":
        if command_details[1] == "First":
            [sequence_one.add(x) for x in command_details[2:]]
        elif command_details[1] == "Second":
            [sequence_two.add(x) for x in command_details[2:]]
    elif command_details[0] == "Remove":
        if command_details[1] == "First":
            [sequence_one.remove(x) for x in command_details[2:] if x in sequence_one]
        elif command_details[1] == "Second":
            [sequence_two.remove(x) for x in command_details[2:] if x in sequence_two]
    elif command_details[0] == "Check":
        if sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one):
            print(True)
        else:
            print(False)

print(', '.join(sorted(sequence_one)))
print(', '.join(sorted(sequence_two)))

# ######################
# Input_1:
# 1 2 3 4 5
# 1 2 3
# 3
# Add First 5 6
# Remove Second 8 9 11
# Check Subset
# ----------------------
# Output_1:
# True
# 1, 2, 3, 4, 5, 6
# 1, 2, 3
# ######################
# Input_2:
# 5 4 2 9 9 5 4
# 1 1 1 5 6 5
# 4
# Add First 5 6 9 3
# Add Second 1 2 3 3 3
# Check Subset
# Remove Second 1 2 3 4 5
# ----------------------
# Output_2:
# False
# 2, 3, 4, 5, 6, 9
# 6
# ######################
