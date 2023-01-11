parameter_one = str(input())
parameter_two = int(input())
parameter_three = int(input())

def calculations(action, number_one, number_two):
    result = int()
    if action == "multiply":
        result = number_one * number_two
    elif action == "divide":
        result = number_one / number_two
    elif action == "add":
        result = number_one + number_two
    elif action == "subtract":
        result = number_one - number_two
    return int(result)

print(calculations(parameter_one, parameter_two, parameter_three))