### !!! Getting 52/100 from Judge ...

from _collections import deque

queue_bees = deque(int(x) for x in input().split())
queue_nectar = deque(int(x) for x in input().split())
queue_math_actions = deque(input().split(" "))
honey = 0

def math_ops(num_1, operator, num_2):
    num_1 = num_1
    operator = operator
    num_2 = num_2
    final_result = int()
    if operator == "+":
        final_result = num_1 + num_2
    elif operator == "-":
        final_result = num_1 - num_2
    elif operator == "*":
        final_result = num_1 * num_2
    elif operator == "/":
        final_result = num_1 / num_2

    return abs(final_result)

while queue_nectar and queue_bees:
    current_bees = queue_bees.popleft()
    current_nectar = queue_nectar.pop()
    current_operator = queue_math_actions.popleft()
    while current_nectar < current_bees:
        current_nectar = queue_nectar.pop()

    honey += math_ops(current_nectar, current_operator, current_bees)

print(f"Total honey made: {honey}")
if len(queue_bees) > 0:
    print(f"Bees left: {', '.join(list(map(str, queue_bees)))}")
if len(queue_nectar) > 0:
    print(f"Nectar left: {', '.join(list(map(str, queue_nectar)))}")

# ###
# Input_1:
# 20 62 99 35 0 150
# 120 60 10 1 70 10
# + - + + / * - - /
# ---
# Output_1:
# Total honey made: 148 Bees left: 99, 35, 0, 150
# ###
# Input_2:
# 30
# 15 9 5 150 8
# * + + * -
# ---
# Output_2:
# Total honey made: 4500
# Nectar left: 15, 9, 5
# ###
