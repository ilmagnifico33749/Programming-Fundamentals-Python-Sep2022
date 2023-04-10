def logged(function):
    def wrapper(*parameters):
        return f"you called {function.__name__}{parameters}\n" \
               f"it returned {function(*parameters)}"
    return wrapper

# ###################################################
# Test_Code_1:
@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
# ---------------------------------------------------
# Output_1:
# you called func(4, 4, 4)
# it returned 6
# ###################################################
# Test_Code_2:
@logged
def sum_func(a, b):
    return a + b
print(sum_func(1, 4))
# ---------------------------------------------------
# Output_2:
# you called sum_func(1, 4)
# it returned 5
# ###################################################