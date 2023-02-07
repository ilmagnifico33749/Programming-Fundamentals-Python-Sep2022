def concatenate(*args, **kwargs):
    word = ''.join(args)
    for keys, values in kwargs.items():
        if keys in word:
            word = word.replace(keys, (kwargs[keys]))
    return word


# ###############################################################################
# Test_Code_1:
# print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
# print(50 * "#")
# -------------------------------------------------------------------------------
# Output_1
# SoftUniIsGreat!
# ###############################################################################
# Test_Code_2:
# print(concatenate("I", " ", "Love", " ", "Cythons", C="P", s="", java='Java'))
# -------------------------------------------------------------------------------
# I Love Python
# ###############################################################################
