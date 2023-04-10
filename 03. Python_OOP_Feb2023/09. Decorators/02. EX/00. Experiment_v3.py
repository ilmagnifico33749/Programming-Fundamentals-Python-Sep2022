def store_results(function):
    def wrapper(*parameters):
        # return f"Function {function.__name__} was called. Result: {function(*parameters)}"
        print(f"Function {function.__name__} was called. Result: {function(*parameters)}")
        log_string = f"Function {function.__name__} was called. Result: {function(*parameters)}"
        with open()
    return wrapper


# ###################################################
# Test_Code_1:
@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)
# ---------------------------------------------------
# Output_1:
# Function 'add' was called. Result: 4
# Function 'mult' was called. Result: 24
# ###################################################
