def even_odd_filter(**kwargs):

    for key in kwargs.keys():
        if key == "even":
            kwargs[key] = [int(x) for x in kwargs[key] if int(x) % 2 == 0]
        elif key == "odd":
            kwargs[key] = [int(x) for x in kwargs[key] if int(x) % 2 != 0]

    return kwargs


# #######################################
# Test_Code_1:
# print(even_odd_filter(
#     odd=[1, 2, 3, 4, 10, 5],
#     even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
# ))
# ----------------------------------------
# Output_1:
# {'even': [4, 10, 2, 2],
#  'odd': [1, 3, 5]}
# #######################################
# Test_Code_2:
# print(even_odd_filter(
#     odd=[2, 2, 30, 44, 10, 5],
# ))
# ----------------------------------------
# Output_2:
# {'odd': [5]}
# #######################################
