from collections import deque
import math

def math_operations(*args, **kwargs):
    queue_floats = deque(args)
    my_dict = kwargs

    def math_actions(command, num1, num2):
        result = float()
        if command == "a":
            result = num1 + num2
        elif command == "s":
            result = num1 - num2
        elif command == "d":
            if num1 != 0 and num2 != 0:
                result = num1 / num2
            else:
                result = float(num1)
        elif command == "m":
            result = num1 * num2
        return result


    for keys, values in my_dict.items():
        if len(queue_floats) > 0:
            my_dict[keys] = math_actions(keys, my_dict[keys], queue_floats.popleft())

    for keys, values in my_dict.items():
        my_dict[keys] = round(float(my_dict[keys]), 1)

    return '\n'.join(
        [(': '.join([str(x) for x in y])) for y in sorted(my_dict.items(), key=lambda x: (-x[1], x[0]))])


# ####################################################################################
# Test_Code_1:
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(50 * '-')
# ------------------------------------------------------------------------------------
# Output_1:
# d: 33.0
# s: 15.1
# a: 9.1
# m: -58.5
# ####################################################################################
# Test_Code_2:
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(50 * '-')
# ------------------------------------------------------------------------------------
# a: 5.1
# d: 0.0
# m: 0.0
# s: 0.0
# ####################################################################################
# Test_Code_3:
print(math_operations(6.0, a=0, s=0, d=5, m=0))
print(50 * '-')
# ------------------------------------------------------------------------------------
# Output_1:
# a: 6.0
# d: 5.0
# m: 0.0
# s: 0.0
# ####################################################################################
