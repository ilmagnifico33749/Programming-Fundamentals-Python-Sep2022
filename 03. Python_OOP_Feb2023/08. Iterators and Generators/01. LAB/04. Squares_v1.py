def squares(n):
    for times in range(1, n+1):
        yield times ** 2


# ##################################
# Test_Code_1:
print(list(squares(5)))
# ---------------------------------
# Output_1:
# [1, 4, 9, 16, 25]
# ##################################
