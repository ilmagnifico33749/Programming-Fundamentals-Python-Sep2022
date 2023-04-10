def make_bold(function):
    def wrapper(*parameters):
        return f"<b>{function(*parameters)}</b>"
    return wrapper

def make_italic(function):
    def wrapper(*parameters):
        return f"<i>{function(*parameters)}</i>"
    return wrapper

def make_underline(function):
    def wrapper(*parameters):
        return f"<u>{function(*parameters)}</u>"
    return wrapper


# ###################################################
# Test_Code_1:
@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"

print(greet("Peter"))
# ---------------------------------------------------
# Output_1:
# <b><i><u>Hello, Peter</u></i></b>
# ###################################################
# Test_Code_2:
@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
# ---------------------------------------------------
# Output_2:
# <b><i><u>Hello, Peter, George</u></i></b>
# ###################################################
