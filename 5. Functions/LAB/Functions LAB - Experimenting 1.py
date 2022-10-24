#def function_name(parameter: type):
#    statement(s)


def print_logo(name):
    print(f"Hello {name}!")
    print("Python Fundamentals")
    #return
    return f"Retuning: Hello {name}!\n Python Fundamentals"

while True:
    name = input()
    if name == "end":
        break
    print_logo(name)
    #return
    print(print_logo(name))
