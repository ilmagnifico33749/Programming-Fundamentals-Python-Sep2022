list_one = input().split("|")
sub_list = []
sub_list.extend([x.split() for x in list_one[::-1]])
flattened = [num for row in sub_list for num in row]
print(' '.join(flattened))

# print(' '.join([(' '.join(sublist)) for sublist in matrix_one]))

# ####################
# Input_1:
# 1 2 3 |4 5 6 | 7 88
# --------------------
# Output_1:
# 7 88 4 5 6 1 2 3
# ####################
# Input_2:
# 7 | 4 5|1 0| 2 5 |3
# --------------------
# Output_2:
# 3 2 5 1 0 4 5 7
# ###
# Input_3:
# 1| 4 5 6 7 | 8 9
# --------------------
# Output_3:
# 8 9 4 5 6 7 1
# ####################
