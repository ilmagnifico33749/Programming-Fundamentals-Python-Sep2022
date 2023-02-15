text = input()
times_to_repeat = input()

try:
    print(text * times_to_repeat)
except TypeError:
    print("Variable times must be an integer")

# #################################
# Input_1:
# Hello
# Bye
# ---------------------------------
# Output_1:
# Variable times must be an integer
# #################################
# Input_2:
# Hello
# 2
# ---------------------------------
# Output_2:
# HelloHello
# #################################
