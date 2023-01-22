# This is the code for the v2 solution of the problem, not the final version but the draft
# with the comments.
# To write  a different, desirably more optimized solution

from _collections import deque
import math

single_line_expression = input()
# single_line_expression = "6 3 - 2 1 * 5 /"
# single_line_expression = "10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *"
queue_whole_expression = single_line_expression.split(" ")
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

print(queue_whole_expression)
print(50 * "#")
print(50 * "#")

while queue_whole_expression:
    for symbols in range(len(queue_whole_expression)):
        symbol = queue_whole_expression[symbols]
        print(f"Current_symbol: {symbol}")
        print(f"Len Current Symbol = {len(symbol)}")
        print(50 * "-")
        if len(symbol) == 1 and symbol.isnumeric() == False:
            print(50 * "-")
            current_operator_index = symbols
            current_operator = queue_whole_expression.pop(symbols)
            print(f"Current Operator: {current_operator} with index {symbols}")
            print(f"Current Queue: {queue_whole_expression}")
            current_numbers = [queue_whole_expression.pop(0) for x in queue_whole_expression[0:current_operator_index]]
            print(f"Current Numbers: {current_numbers}")
            if first_time == False:
                print(f"Previous current_ongoing_sum: {current_sum}")
            final_sum = math_expr_calc(current_operator, current_numbers, current_sum, first_time)
            print(f"New Current_ongoing_sum: {final_sum}")
            current_sum = final_sum
            first_time = False
            print(50 * "#")
            break

print(f"Final Sum: {final_sum}")
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
