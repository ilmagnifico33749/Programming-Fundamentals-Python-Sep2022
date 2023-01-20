list_usernames = [input() for x in range(int(input()))]
print('\n'.join(set(list_usernames)))

# #############
# Input_1:
# 6
# George
# George
# George
# Peter
# George
# NiceGuy1234
# -------------
# George
# Peter
# NiceGuy1234
# #############
# Input_2:
# 10
# Peter
# Maria
# Peter
# George
# Steve
# Maria
# Alex
# Peter
# Steve
# George
# -------------
# Output_2:
# Peter
# Maria
# George
# Steve
# Alex
# #############
