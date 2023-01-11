user_input = list(input())
stack = []

for i in range(len(user_input)):
    stack.append(user_input.pop())

print(''.join(stack))


##############################
# Input_1: I Love Python
# Output_1: nohtyP evoL I
##############################
# Input_2: Stacks and Queues
# Output_2: seueuQ dna skcatS
##############################
