sentence = list(input())

stack_indexes_beginning = []
stack_indexes_end = []

for symbol in range(len(sentence)):
    if sentence[symbol] == "(":
        stack_indexes_beginning.append(symbol)
    elif sentence[symbol] == ")":
        stack_indexes_end.append(symbol)

        starting_index = stack_indexes_beginning.pop()
        final_index = stack_indexes_end.pop()
        print(''.join(sentence[starting_index:final_index+1]))

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