def even_parameters(function):
    def wrapper(*parameters):
        for par in parameters:
            if not isinstance(par, int):
                return f"Please use only even numbers!"
            else:
                if par % 2 != 0:
                    return f"Please use only even numbers!"
        return function(*parameters)
    return wrapper

# ###################################################
# Test_Code_1:
@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add("Peter", 1))

# ---------------------------------------------------
# Output_1:
# 6
# Please use only even numbers!
# ###################################################
# Test_Code_2:
@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))
# ---------------------------------------------------
# Output_2:
# 384
# Please use only even numbers!
# ###################################################
