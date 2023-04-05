def genrange(start: int, end: int):
    for numbers in range(start, end + 1):
        yield numbers

# ##################################
# Test_Code_1:
print(list(genrange(1, 10)))
# ---------------------------------
# Output_1:
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# ##################################

