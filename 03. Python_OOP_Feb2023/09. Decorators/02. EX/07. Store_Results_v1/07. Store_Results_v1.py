class store_results:
    _logfile = 'results.txt'
    def __init__(self, function):
        self.function = function

    def __call__(self, *parameters):
        # return f"Function {function.__name__} was called. Result: {function(*parameters)}"
        # print(f"Function {self.function.__name__} was called. Result: {self.function(*parameters)}")
        log_string = f"Function {self.function.__name__} was called. Result: {self.function(*parameters)}"
        with open(self._logfile, 'a') as opened_file:
            opened_file.write(log_string + '\n')
        return self.function(*parameters)


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
