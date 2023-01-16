user_input = list(input())
reversed_sentence = []

while user_input:
    reversed_sentence.append(user_input.pop())

print(''.join(reversed_sentence))

##############################
# Input_1: I Love Python
# Output_1: nohtyP evoL I
##############################
# Input_2: Stacks and Queues
# Output_2: seueuQ dna skcatS
##############################
