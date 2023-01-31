### !!! 75/100 (3 of 4 checks) points from Judge !!!

def matrix_creator(user_input):
    user_input = user_input
    created_matrix = [sublist.split() for sublist in user_input.split("|")]
    return created_matrix[::-1]


matrix = matrix_creator(input())


def matrix_to_string(primary_matrix):
    primary_matrix = primary_matrix
    return ' '.join([' '.join(sublist) for sublist in matrix])


print(matrix_to_string(matrix))


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
