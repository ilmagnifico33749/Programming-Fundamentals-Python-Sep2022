def tags(tag):
    def decorator(function):
        def wrapper(*parameters):
            return f"<{tag}>{function(*parameters)}</{tag}>"
        return wrapper
    return decorator


# ###################################################
# Test_Code_1:
@tags('p')
def join_strings(*args):
    return "".join(args)
print(join_strings("Hello", " you!"))

# ---------------------------------------------------
# Output_1:
# <p>Hello you!</p>
# ###################################################
# Test_Code_2:
@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))
# ---------------------------------------------------
# Output_2:
# <h1>HELLO</h1>
# ###################################################
