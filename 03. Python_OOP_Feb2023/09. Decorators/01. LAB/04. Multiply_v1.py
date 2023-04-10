def multiply(times):
    def decorator(function):
        def wrapper(parameters):
            return times * function(parameters)
        return wrapper
    return decorator

# ###################################################
# Test_Code_1:
@multiply(3)
def add_ten(number):
    return number + 10
print(add_ten(3))
# ---------------------------------------------------
# Output_1:
# 39
# ###################################################
# Test_Code_2:
@multiply(5)
def add_ten(number):
    return number + 10
print(add_ten(6))
# ---------------------------------------------------
# Output_2:
# 80
# ###################################################
