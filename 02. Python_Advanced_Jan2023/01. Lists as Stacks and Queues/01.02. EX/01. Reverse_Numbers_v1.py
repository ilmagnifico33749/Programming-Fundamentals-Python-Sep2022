original_stack = list(input().split(" "))
new_stack = []

while original_stack:
    new_stack.append(original_stack.pop())

print(' '.join(new_stack))

# ###########
# ###########
# Input_1:
# 1 2 3 4 5
# ---------
# Output_1:
# 5 4 3 2 1
# ###########
# Input_2:
# 1
# Output_2:
# 1
# ###########
# ###########
