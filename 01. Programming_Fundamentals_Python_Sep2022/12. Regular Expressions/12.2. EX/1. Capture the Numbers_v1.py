import re

sequence = input()

regex = "\d+"

while sequence:
    matches = re.findall(regex, sequence)
    if matches:
        print(' '.join(matches), end=" ")
    sequence = input()

##########################################
# Input 1:
#   The300
#   What is that?
#   I think it's the 3rd movie
#   Let's watch it at 22:45
# Output 1: 300 3 22 45
##########################################
# Input 2:
#   123a456
#   789b987
#   654c321
#   0
# Output 2: 123 456 789 987 654 321 0
##########################################
# Input 3:
# Let's go11!!!11!
# Okey!1!
# Output 3: 11 11 1
##########################################
