from itertools import permutations

def possible_permutations(sequence):
    for el in list(permutations(sequence)):
        yield list(el)


# ##################################
# Test_Code_1:
[print(n) for n in possible_permutations([1, 2, 3])]
# ---------------------------------
# Output_1:
# [1, 2, 3]
# [1, 3, 2]
# [2, 1, 3]
# [2, 3, 1]
# [3, 1, 2]
# [3, 2, 1]
# ##################################
# Test_Code_2:
[print(n) for n in possible_permutations([1])]
# ---------------------------------
# Output_2:
# [1]
# ##################################
