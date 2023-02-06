def operate(operator, *numbers):

    def addition():
        result = numbers[0]
        for x in range(1, len(numbers)):
            result += numbers[x]
        return result

    def subtraction():
        result = numbers[0]
        for x in range(1, len(numbers)):
            result -= numbers[x]
        return result

    def multiplication():
        result = numbers[0]
        for x in range(1, len(numbers)):
            result *= numbers[x]
        return result

    def division():
        result = numbers[0]
        for x in range(1, len(numbers)):
            result /= numbers[x]
        return result


    if operator == "+":
        return addition()
    elif operator == "-":
        return subtraction()
    elif operator == "*":
        return multiplication()
    elif operator == "/":
        return division()


# #############################
# Test_Code_1:
# print(operate("+", 1, 2, 3))
# ---
# Output_1:
# 6
# ###
# Test_Code_2:
# print(operate("*", 3, 4))
# ---
# Output_2
# 12
# #############################