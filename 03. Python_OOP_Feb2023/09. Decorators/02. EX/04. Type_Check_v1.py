def type_check(data_type):
    def decorator(function):
        def wrapper(parameter):
            if type(parameter) == data_type:
                return function(parameter)
            else:
                return f"Bad Type"
        return wrapper
    return decorator


# ###################################################
# Test_Code_1:
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
# ---------------------------------------------------
# Output_1:
# 4
# Bad Type
# ###################################################
# Test_Code_2:
@type_check(str)
def first_letter(word):
    return word[0]

print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
# ---------------------------------------------------
# Output_2:
# H
# Bad Type
# ###################################################
