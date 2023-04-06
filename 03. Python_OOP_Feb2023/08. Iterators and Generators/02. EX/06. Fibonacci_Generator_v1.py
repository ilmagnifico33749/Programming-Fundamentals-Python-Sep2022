def fibonacci():
    x = 0
    y = 1
    while True:
        sum_x_y = x + y
        yield x
        x = y
        y = sum_x_y


# ##################################
# Test_Code_1:
generator = fibonacci()
for i in range(5):
    print(next(generator))

# ---------------------------------
# Output_1:
# 0
# 1
# 1
# 2
# 3
# ##################################
# Test_Code_2:
generator = fibonacci()
for i in range(1):
    print(next(generator))
# ---------------------------------
# Output_2:
# 0
# ##################################
