### !!! Getting only 50/100 from Judge.

from _collections import deque

chocolates_stack = list(map(int, (input().split(", "))))
cups_milk_queue = deque(list(map(int, (input().split(", ")))))
count_milkshakes = 0

for chocolate in range((len(chocolates_stack)-1), -1, -1):
    if len(chocolates_stack) == 0 or cups_milk_queue == 0:
        break

    else:
        current_chocolate = chocolates_stack[-1]
        current_milk = cups_milk_queue[0]

        if current_chocolate <= 0:
            chocolates_stack.pop(-1)
            if len(chocolates_stack) > 0:
                current_chocolate = int(chocolates_stack[-1])
            else:
                break
        if current_milk <= 0:
            cups_milk_queue.popleft()
            if len(cups_milk_queue) > 0:
                current_milk = int(cups_milk_queue[0])
            else:
                break

        if current_chocolate == current_milk:
            count_milkshakes += 1
            current_milk = cups_milk_queue.popleft()
            current_chocolate = chocolates_stack.pop()
        else:
            if len(chocolates_stack) > 0 and len(cups_milk_queue) > 0:
                current_milk = cups_milk_queue.popleft()
                cups_milk_queue.append(current_milk)
                chocolates_stack[-1] = int(chocolates_stack[-1]) - 5
            else:
                break
        if count_milkshakes == 5:
            break

if count_milkshakes >= 5:
    print(f"Great! You made all the chocolate milkshakes needed!")
else:
    print(f"Not enough milkshakes.")

if len(chocolates_stack) > 0:
    print(f"Chocolate: {', '.join(list(map(str, chocolates_stack)))}")
else:
    print(f"Chocolate: empty")

if len(cups_milk_queue) > 0:
    print(f"Milk: {', '.join(list(map(str, cups_milk_queue)))}")
else:
    print(f"Milk: empty")

# ######################################################
# Input_1:
# 20, 24, -5, 17, 22, 60, 26
# 26, 60, 22, 17, 24, 10, 55
# ------------------------------------------------------
# Output_1:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: 20
# Milk: 10, 55
# ######################################################
# Input_2:
# -10, -2, -30, 10
# -5
# ------------------------------------------------------
# Output_2
# Not enough milkshakes.
# Chocolate: -10, -2, -30, 10
# Milk: empty
# ######################################################
# Input_3:
# 2, 3, 3, 7, 2
# 2, 7, 3, 3, 2, 14, 6
# ------------------------------------------------------
# Output_3:
# Great! You made all the chocolate milkshakes needed!
# Chocolate: empty
# Milk: 14, 6
# ######################################################
