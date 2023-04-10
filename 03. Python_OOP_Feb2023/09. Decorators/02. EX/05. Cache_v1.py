def cache(function):
    def wrapper(number):
        if number not in wrapper.log:
            wrapper.log[number] = function(number)
        return wrapper.log[number]
    wrapper.log = {}
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# ###################################################
# Test_Code_1:
fibonacci(3)
print(fibonacci.log)
# ---------------------------------------------------
# Output_1:
# {1: 1, 0: 0, 2: 1, 3: 2}
# ###################################################
# Test_Code_2:
# fibonacci(4)
# print(fibonacci.log)
# ---------------------------------------------------
# Output_2:
# {1: 1, 0: 0, 2: 1, 3: 2, 4: 3}
# ###################################################
