def number_increment(numbers):
    def increase():
        return [x+1 for x in numbers]
    return increase()


# ###################################################
# Test_Code_1:
print(number_increment([1, 2, 3]))
# ---------------------------------------------------
# Output_1:
# [2, 3, 4]
# ###################################################
