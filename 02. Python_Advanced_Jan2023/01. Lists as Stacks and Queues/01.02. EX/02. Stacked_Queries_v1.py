my_stack_1 = []
my_stack_1_reversed = []
num_queries = int(input())

for queries in range(num_queries):
    command = input()
    command_details = command.split(" ")
    query_command = command_details[0]
    if query_command == "1":
        my_stack_1.append(int(command_details[1]))
    elif query_command == "2":
        if len(my_stack_1) > 0:
            my_stack_1.pop()
    elif query_command == "3":
        if len(my_stack_1) > 0:
            print(max(my_stack_1))
    elif query_command == "4":
        if len(my_stack_1) > 0:
            print(min(my_stack_1))

while my_stack_1:
    my_stack_1_reversed.append(str(my_stack_1.pop()))

print(', '.join(my_stack_1_reversed))

# #######################
# #######################
# Input_1:
# 9
# 1 97
# 2
# 1 20
# 2
# 1 26
# 1 20
# 3
# 1 91
# 4
# -----------------------
# Output_1:
# 26
# 20
# 91, 20, 26
# #######################
# Input_2:
# 10
# 2
# 1 47
# 1 66
# 1 32
# 4
# 3
# 1 25
# 1 16
# 1 8
# 4
# -----------------------
# Output_2:
# 32
# 66
# 8
# 8, 16, 25, 32, 66, 47
# #######################
# #######################
