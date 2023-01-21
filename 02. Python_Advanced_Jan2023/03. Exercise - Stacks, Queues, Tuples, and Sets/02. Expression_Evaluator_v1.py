from _collections import deque
import math

single_line_expression = input()
queue_whole_expression = single_line_expression.split(" ")
previous_operator_index = -1
current_operator_index = 0
current_operator = ""
current_numbers = []
current_sum = 0
final_sum = 0
first_time = True

def math_expr_calc(operator, numbers, ongoing_sum, first_time_status):
    operator = operator
    numbers_queue = numbers
    ongoing_sum = ongoing_sum
    current_result = 0
    final_result = 0
    if first_time_status == True:
        number_first_pos = int(numbers.pop(0))
        current_result = number_first_pos
    elif first_time_status == False:
        current_result = ongoing_sum

    for number in range(len(numbers_queue)):
        if operator == "+":
            current_result += int(numbers_queue[number])
        elif operator == "-":
            current_result -= int(numbers_queue[number])
        elif operator == "*":
            current_result *= int(numbers_queue[number])
        elif operator == "/":
            current_result /= int(numbers_queue[number])

    if operator == "/":
        final_result = math.floor(current_result)
    else:
        final_result = current_result

    return final_result

for symbols in range(len(queue_whole_expression)):
    symbol = queue_whole_expression[symbols]

    if len(symbol) == 1 and symbol.isnumeric() == False:
        current_operator_index = symbols
        current_operator = symbol
        current_numbers = [x for x in queue_whole_expression[(previous_operator_index + 1):current_operator_index]]
        previous_operator_index = current_operator_index
        final_sum = math_expr_calc(current_operator, current_numbers, current_sum, first_time)
        current_sum = final_sum
        first_time = False

print(final_sum)
# ###
# Input_1:
# 6 3 - 2 1 * 5 /
# ---
# Output_1:
# 1
# ###
# Input_2:
# 2 2 - 1 *
# ---
# Output_2:
# 0
# ###
# Input_3:
# 10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *
# ---
# Output_3:
# 164
# ###
