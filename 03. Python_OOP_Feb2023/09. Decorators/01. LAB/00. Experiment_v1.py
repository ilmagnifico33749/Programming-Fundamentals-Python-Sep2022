from functools import wraps

def uppercase(function):
    @wraps(function)
    def wrapper():
        result = function()
        uppercase_result = result.upper()
        return uppercase_result

    return wrapper

#
# def say_hi():
#     return 'hello there'
#
# decorate = uppercase(say_hi())
#
# # decorate()
#
# print(decorate)

@uppercase
def say_hi():
    return 'hello there'
print(str(say_hi()))

print(say_hi.__name__)
print(say_hi.__doc__)
