def age_assignment(*args, **kwargs):
    new_dict = {}

    for name in args:
        for letter, age in kwargs.items():
            if letter in name:
                new_dict[name] = age

    new_dict = sorted(new_dict.items(), key=lambda x: x[0])

    return '\n'.join([f"{pers_name} is {pers_age} years old." for pers_name, pers_age in new_dict])



# ################################################################
# Test_Code_1:
print(age_assignment("Peter", "George", G=26, P=19))
# ----------------------------------------------------------------
# Output_1:
# George is 26 years old.
# Peter is 19 years old.
# ################################################################
# Test_Code_2:
# print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
# ----------------------------------------------------------------
# Output_2:
# Amy is 22 years old.
# Bill is 61 years old.
# Willy is 36 years old.
# ################################################################
