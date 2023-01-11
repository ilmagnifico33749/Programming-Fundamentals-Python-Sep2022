user_input = input()
indexes = []

for i in range(len(user_input)):
    if user_input[i] == "(":
        indexes.append(i)
    elif user_input[i] == ")":
        starting_index = indexes.pop()
        print(user_input[starting_index:(i + 1)])

# ######################################
# Input_1:
# 1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5
# Output_1:
# (2 + 3)
# (3 + 1)
# (2 - (2 + 3) * 4 / (3 + 1))
# ######################################
# Input_2:
# (2 + 3) - (2 + 3
# Output_2:
# (2 + 3)
# (2 + 3)
# ######################################
