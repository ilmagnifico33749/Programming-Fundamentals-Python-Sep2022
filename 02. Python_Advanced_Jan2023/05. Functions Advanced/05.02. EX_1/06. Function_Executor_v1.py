def func_executor(*args):

    # for function_name, function_parameters in args:
        # print(f"F: {function_name.__name__}")
        # print(f"P: {function_parameters}")
        # print(f"R: {function_name(*function_parameters)}")
        # print(50 * "-")
    return '\n'.join([f"{function_name.__name__} - {function_name(*function_parameters)}"
                      for function_name, function_parameters in args])


# ######################################################################################
# Test_Code_1:
def sum_numbers(num1, num2):
    return num1 + num2

def multiply_numbers(num1, num2):
    return num1 * num2

print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4))))
# --------------------------------------------------------------------------------------
# Output_1:
# sum_numbers - 3
# multiply_numbers - 8
# ######################################################################################
# Test_Code_2:
def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor((make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)),))
# --------------------------------------------------------------------------------------
# Output_2:
# make_upper - ('PYTHON', 'SOFTUNI')
# make_lower - ('python', )
# ######################################################################################