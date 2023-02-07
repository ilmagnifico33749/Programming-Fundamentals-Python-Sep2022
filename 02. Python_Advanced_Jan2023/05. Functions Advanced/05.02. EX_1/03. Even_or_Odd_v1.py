def even_odd(*user_input):
    list_user_input = list(user_input)
    command = list_user_input.pop()

    def user_output(list_numbers, user_command):
        if command == "even":
            return ([int(x) for x in list_numbers if int(x) % 2 == 0])
        elif command == "odd":
            return ([int(x) for x in list_numbers if int(x) % 2 != 0])

    return user_output(list_user_input, command)


# ######################################################
# Test_Code_1:
# print(even_odd(1, 2, 3, 4, 5, 6, "even"))
# ------------------------------------------------------
# Output_1:
# [2, 4, 6]
# ######################################################
# Test_Code_2:
# print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))
# ------------------------------------------------------
# Output_2:
# [1, 3, 5, 7, 9]
# ######################################################
