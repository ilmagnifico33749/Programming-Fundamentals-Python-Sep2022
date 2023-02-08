def func_executor(*functions_data):
    return '\n'.join([f"{func.__name__} - {func(*args)}" for func, args in functions_data])

# def func_executor(*functions_data):
#     result = []
#
#     for func, args in functions_data:
#         result.append(f"{func.__name__} - {func(*args)}")
#
#     return '\n'.join(result)


# --------------------------------------------------------------------------------------
# Output_1:
# sum_numbers - 3
# multiply_numbers - 8
# ######################################################################################
# Test_Code_2:
# def make_upper(*strings):
#     result = tuple(s.upper() for s in strings)
#     return result
#
# def make_lower(*strings):
#     result = tuple(s.lower() for s in strings)
#     return result
#
# print(func_executor((make_upper, ("Python", "softUni")), (make_lower, ("PyThOn",)),))
# --------------------------------------------------------------------------------------
# Output_2:
# make_upper - ('PYTHON', 'SOFTUNI')
# make_lower - ('python', )
# ######################################################################################